#!/usr/bin/env bash
set -euo pipefail

# Regenerates:
# - AI_PRODUCTIVITY_ANALYSIS.md
# - FEATURE_SIZE_COMPARISON.md
#
# Usage:
#   ./scripts/generate_productivity_reports.sh
#
# Notes:
# - Expects git history to be available for each compared repo path.
# - If /tmp mirror repos are missing, this script will attempt to clone them.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="${TMPDIR:-/tmp}/productivity-analysis"
mkdir -p "$TMP_DIR"

WINDOWS_FILE="$TMP_DIR/windows.tsv"
METRICS_FILE="$TMP_DIR/metrics.tsv"
INDEX_FILE="$TMP_DIR/index.tsv"
INDEX_NOWF_FILE="$TMP_DIR/index_nowf.tsv"
INITIATIVES_FILE="$TMP_DIR/initiatives.tsv"
INITIATIVE_SCORES_FILE="$TMP_DIR/initiative_scores.tsv"
INITIATIVE_TOTALS_FILE="$TMP_DIR/initiative_totals.tsv"

cat > "$WINDOWS_FILE" <<EOF
repo	repo_path	clone_url	start	end
blog	$ROOT_DIR	-	2026-02-08	2026-03-07 23:59:59
simple-excel	/tmp/toby-repo-metrics/simple-excel	https://github.com/tobyweston/simple-excel.git	2012-08-25	2012-09-21 23:59:59
tempus-fugit	/tmp/toby-repo-metrics/tempus-fugit	https://github.com/tobyweston/tempus-fugit.git	2009-11-30	2009-12-27 23:59:59
temperature-machine	/tmp/toby-repo-metrics/temperature-machine	https://github.com/tobyweston/temperature-machine.git	2018-04-12	2018-05-09 23:59:59
radiate	/tmp/toby-repo-metrics/radiate	https://github.com/tobyweston/radiate.git	2013-07-24	2013-08-20 23:59:59
EOF

ensure_repo() {
  local repo_path="$1"
  local clone_url="$2"

  if [[ -d "$repo_path" ]]; then
    return
  fi

  if [[ -z "$clone_url" || "$clone_url" == "-" ]]; then
    echo "Missing repo path and clone url for local repo: $repo_path" >&2
    exit 1
  fi

  mkdir -p "$(dirname "$repo_path")"
  git clone --quiet --mirror "$clone_url" "$repo_path"
}

collect_metrics() {
  {
    echo -e "repo\tcommits\tnew_files\tnew_code_files\tnew_test_files\tunique_files\tfeature_like\tfix_like\trelease_ci_test_like\tworkflow_files_touched"

    tail -n +2 "$WINDOWS_FILE" | while IFS=$'\t' read -r repo repo_path clone_url start end; do
      ensure_repo "$repo_path" "$clone_url"

      local commits new_files new_code_files new_test_files unique_files msgs
      local feature_like fix_like rel_like workflows

      commits=$(git -C "$repo_path" rev-list --count --all --since="$start" --until="$end" --author='[Tt]oby')
      new_files=$(git -C "$repo_path" log --since="$start" --until="$end" --diff-filter=A --name-only --pretty=format: --author='[Tt]oby' | rg -v '^$' | sort -u | wc -l | tr -d ' ' || true)
      new_code_files=$(git -C "$repo_path" log --since="$start" --until="$end" --diff-filter=A --name-only --pretty=format: --author='[Tt]oby' | rg '\.(py|js|ts|astro|java|scala|c|cpp|h)$' | sort -u | wc -l | tr -d ' ' || true)
      new_test_files=$(git -C "$repo_path" log --since="$start" --until="$end" --diff-filter=A --name-only --pretty=format: --author='[Tt]oby' | rg -i '(test|spec|cypress|pytest|workflow)' | sort -u | wc -l | tr -d ' ' || true)
      unique_files=$(git -C "$repo_path" log --since="$start" --until="$end" --name-only --pretty=format: --author='[Tt]oby' | rg -v '^$' | sort -u | wc -l | tr -d ' ' || true)

      msgs=$(git -C "$repo_path" log --since="$start" --until="$end" --pretty=format:'%s' --author='[Tt]oby')
      feature_like=$(printf '%s\n' "$msgs" | rg -i '(add|initial|implement|enhance|support|migrate|introduce|configure|dedicate|include|semantic|rag|cli|evaluate|plan stage|refactor|feature|new)' | wc -l | tr -d ' ' || true)
      fix_like=$(printf '%s\n' "$msgs" | rg -i '(fix|bug|tweak|warning|typo|remove|cleanup|clean up|rollback|revert|rename|downgrade)' | wc -l | tr -d ' ' || true)
      rel_like=$(printf '%s\n' "$msgs" | rg -i '(release|deploy|publish|ci|workflow|action|upgrade|version|snapshot|test|build|maven-release)' | wc -l | tr -d ' ' || true)
      workflows=$(git -C "$repo_path" log --since="$start" --until="$end" --name-only --pretty=format: --author='[Tt]oby' | rg '^\.github/workflows/|^astro/\.github/workflows/' | sort -u | wc -l | tr -d ' ' || true)

      echo -e "$repo\t$commits\t$new_files\t$new_code_files\t$new_test_files\t$unique_files\t$feature_like\t$fix_like\t$rel_like\t$workflows"
    done
  } > "$METRICS_FILE"
}

build_indexes() {
  awk -F'\t' '
    NR==1{next}
    {
      if($7>maxf)maxf=$7
      if($4>maxc)maxc=$4
      if($5>maxt)maxt=$5
      if($9>maxr)maxr=$9
      if($10>maxw)maxw=$10
      rows[NR]=$0
    }
    END{
      print "repo\tcapability_index"
      for(i=2;i<=NR;i++){
        split(rows[i],a,"\t")
        f=a[7]/maxf
        c=a[4]/maxc
        t=a[5]/maxt
        r=a[9]/maxr
        w=(maxw>0?a[10]/maxw:0)
        idx=100*(0.40*f + 0.20*c + 0.20*t + 0.10*r + 0.10*w)
        printf "%s\t%.1f\n", a[1], idx
      }
    }
  ' "$METRICS_FILE" > "$INDEX_FILE"

  awk -F'\t' '
    NR==1{next}
    {
      if($7>maxf)maxf=$7
      if($4>maxc)maxc=$4
      if($5>maxt)maxt=$5
      if($9>maxr)maxr=$9
      rows[NR]=$0
    }
    END{
      print "repo\tfeature_value_index"
      for(i=2;i<=NR;i++){
        split(rows[i],a,"\t")
        f=a[7]/maxf
        c=a[4]/maxc
        t=a[5]/maxt
        r=a[9]/maxr
        idx=100*(0.45*f + 0.25*c + 0.20*t + 0.10*r)
        printf "%s\t%.1f\n", a[1], idx
      }
    }
  ' "$METRICS_FILE" > "$INDEX_NOWF_FILE"
}

calc_index_multipliers() {
  awk -F'\t' '
    NR>1 && $1=="blog" {blog=$2}
    NR>1 && $1!="blog" {
      vals[++n]=$2
      sum+=$2
      if($2>max)max=$2
    }
    END{
      for(i=1;i<=n;i++) for(j=i+1;j<=n;j++) if(vals[i]>vals[j]){t=vals[i];vals[i]=vals[j];vals[j]=t}
      if(n%2==0) med=(vals[n/2]+vals[n/2+1])/2
      else med=vals[(n+1)/2]
      mean=sum/n
      printf "%.2f\t%.2f\t%.2f\n", blog/mean, blog/med, blog/max
    }
  ' "$INDEX_NOWF_FILE"
}

write_ai_report() {
  local multipliers
  multipliers="$(calc_index_multipliers)"
  local ratio_mean ratio_median ratio_best
  ratio_mean="$(echo "$multipliers" | awk -F'\t' '{print $1}')"
  ratio_median="$(echo "$multipliers" | awk -F'\t' '{print $2}')"
  ratio_best="$(echo "$multipliers" | awk -F'\t' '{print $3}')"

  {
    cat <<'EOF'
# AI Productivity Analysis (Feature-Level, Cross-Repo)

Date: 2026-03-07
Author scope: commits by `Toby`/`toby`
Window size: 28 days per repo (peak busy windows for historical repos)

## Goal

Quantify whether recent AI-assisted work produced more **feature/value throughput** than prior busy periods in other open-source projects, using coarse-grained delivery signals rather than lines of code alone.

## Compared Windows

| Repo | Window |
|---|---|
| `blog` | 2026-02-08 to 2026-03-07 |
| `simple-excel` | 2012-08-25 to 2012-09-21 |
| `tempus-fugit` | 2009-11-30 to 2009-12-27 |
| `temperature-machine` | 2018-04-12 to 2018-05-09 |
| `radiate` | 2013-07-24 to 2013-08-20 |

## Raw Delivery Signals

| Repo | Commits | New Files | New Code Files | New Test Files | Feature-like Commits | Fix-like Commits | Reliability/CI/Test-like Commits |
|---|---:|---:|---:|---:|---:|---:|---:|
EOF

    awk -F'\t' 'NR>1 {printf "| `%s` | %s | %s | %s | %s | %s | %s | %s |\n",$1,$2,$3,$4,$5,$7,$8,$9}' "$METRICS_FILE"

    cat <<EOF

## Feature-Value Index

\`FeatureValueIndex = 100 * (0.45*feature + 0.25*new_code + 0.20*new_tests + 0.10*reliability)\`

| Repo | FeatureValueIndex |
|---|---:|
$(awk -F'\t' 'NR>1{printf "| `%s` | %.1f |\n",$1,$2}' "$INDEX_NOWF_FILE")

### Relative Multipliers (Recent \`blog\` vs historical)

- vs historical mean: **${ratio_mean}x**
- vs historical median: **${ratio_median}x**
- vs best historical window: **${ratio_best}x**

## Charts

\`\`\`mermaid
xychart-beta
    title "Feature-Value Index by Repo (28-day windows)"
    x-axis ["blog","radiate","simple-excel","tempus-fugit","temperature-machine"]
    y-axis "Index" 0 --> 100
    bar [$(awk -F'\t' 'NR>1{v[$1]=$2} END{printf "%.1f,%.1f,%.1f,%.1f,%.1f", v["blog"],v["radiate"],v["simple-excel"],v["tempus-fugit"],v["temperature-machine"]}' "$INDEX_NOWF_FILE")]
\`\`\`

\`\`\`mermaid
xychart-beta
    title "Feature-like Commit Count by Repo"
    x-axis ["blog","radiate","simple-excel","tempus-fugit","temperature-machine"]
    y-axis "Count" 0 --> 70
    bar [$(awk -F'\t' 'NR>1{v[$1]=$7} END{printf "%s,%s,%s,%s,%s", v["blog"],v["radiate"],v["simple-excel"],v["tempus-fugit"],v["temperature-machine"]}' "$METRICS_FILE")]
\`\`\`

## Caveats

1. Commit-message classification is heuristic.
2. Repo age/tooling norms differ by era.
3. This is a relative productivity model, not a universal absolute measure.

---

Companion initiative-sizing report:

- [FEATURE_SIZE_COMPARISON.md](/Users/toby/dev/code/blog/FEATURE_SIZE_COMPARISON.md)
EOF
  } > "$ROOT_DIR/AI_PRODUCTIVITY_ANALYSIS.md"
}

write_initiatives_config() {
  cat > "$INITIATIVES_FILE" <<'EOF'
repo	initiative	novelty	depth	breadth	ops	impact
blog	Ghostwriter core from scratch (plan/draft/revise/evaluate/CLI)	5	5	5	4	4
blog	Semantic RAG + chunking + index + retrieval integration	5	5	4	3	4
blog	Testing+CI hardening (Ghostwriter + visual test stabilization)	3	3	4	5	3
blog	Site IA/UX/routing improvements (archive/search/redirect/infinite scroll)	3	3	4	3	4
blog	SEO/community/observability additions (JSON-LD/robots/llms/Giscus/GA)	3	2	3	3	3
simple-excel	API abstraction reshaping (Workbook/Cell interfaces)	4	4	3	3	4
simple-excel	Styling and cell-update behavior expansion	3	3	2	3	3
simple-excel	Release/packaging hardening around 1.0	2	2	3	4	3
simple-excel	Docs clarification	1	1	1	2	2
tempus-fugit	Concurrency/deadlock/intermittent-test capabilities	4	4	3	3	4
tempus-fugit	Site/docs/deploy skin and publishing pipeline	2	2	3	3	2
tempus-fugit	Supportive testing and cleanup around those capabilities	2	2	2	3	2
temperature-machine	Packaging/install/runtime scripts hardening	3	3	3	4	4
temperature-machine	Documentation restructuring for install/onboarding	1	1	2	2	2
temperature-machine	Small operational bug fixes	1	1	1	2	2
radiate	Exception/info display subsystem (HUD/dialog behaviors)	4	4	4	3	4
radiate	Logging/event observability refactor	3	4	3	3	3
radiate	UI controls + thread-safety improvements	3	3	3	3	3
radiate	Example mode enhancements and supporting UX	2	2	2	2	3
EOF
}

score_initiatives() {
  awk -F'\t' '
    NR==1{print "repo\tinitiative\tN\tD\tB\tO\tU\tfss\tsize\tfp"; next}
    {
      N=$3; D=$4; B=$5; O=$6; U=$7
      fss=20*(0.30*N + 0.25*D + 0.20*B + 0.15*O + 0.10*U)
      if (fss>=85){size="XXL"; fp=13}
      else if (fss>=70){size="XL"; fp=8}
      else if (fss>=55){size="L"; fp=5}
      else if (fss>=40){size="M"; fp=3}
      else if (fss>=25){size="S"; fp=2}
      else {size="XS"; fp=1}
      printf "%s\t%s\t%d\t%d\t%d\t%d\t%d\t%.0f\t%s\t%d\n",$1,$2,N,D,B,O,U,fss,size,fp
    }
  ' "$INITIATIVES_FILE" > "$INITIATIVE_SCORES_FILE"

  awk -F'\t' '
    NR==1{next}
    {sum[$1]+=$10; count[$1]++}
    END{
      print "repo\ttotal_fp\tinitiative_count\tavg_fp"
      for (r in sum) printf "%s\t%d\t%d\t%.1f\n", r, sum[r], count[r], sum[r]/count[r]
    }
  ' "$INITIATIVE_SCORES_FILE" | sort > "$INITIATIVE_TOTALS_FILE"
}

write_feature_size_report() {
  local hist_avg best_fp ratio_avg ratio_best
  hist_avg=$(awk -F'\t' '$1!="repo" && $1!="blog"{sum+=$2; n++} END{printf "%.1f", sum/n}' "$INITIATIVE_TOTALS_FILE")
  best_fp=$(awk -F'\t' '$1!="repo" && $1!="blog" && $2>max{max=$2} END{printf "%d", max}' "$INITIATIVE_TOTALS_FILE")
  ratio_avg=$(awk -F'\t' -v avg="$hist_avg" '$1=="blog"{printf "%.2f",$2/avg}' "$INITIATIVE_TOTALS_FILE")
  ratio_best=$(awk -F'\t' -v best="$best_fp" '$1=="blog"{printf "%.2f",$2/best}' "$INITIATIVE_TOTALS_FILE")

  {
    cat <<'EOF'
# Feature Size Comparison (Coarse-Grained Productivity)

Date: 2026-03-07
Scope: Compare 28-day peak windows across repos by **initiative size**, not LOC.

## Sizing Rubric

Each initiative is scored on 1-5:

1. Novel capability (30%)
2. Technical depth (25%)
3. Surface breadth (20%)
4. Operational hardening (15%)
5. User/product impact (10%)

Formula:

`FSS = 20 * (0.30*N + 0.25*D + 0.20*B + 0.15*O + 0.10*U)`

Mapped to Feature Points (FP):

- `XXL`=13, `XL`=8, `L`=5, `M`=3, `S`=2, `XS`=1

## Initiative Scores
EOF

    for repo in blog simple-excel tempus-fugit temperature-machine radiate; do
      echo
      echo "### \`$repo\`"
      echo
      echo "| Initiative | N | D | B | O | U | FSS | Size | FP |"
      echo "|---|---:|---:|---:|---:|---:|---:|---|---:|"
      awk -F'\t' -v r="$repo" '$1==r{printf "| %s | %s | %s | %s | %s | %s | %s | %s | %s |\n",$2,$3,$4,$5,$6,$7,$8,$9,$10}' "$INITIATIVE_SCORES_FILE"
      echo
      awk -F'\t' -v r="$repo" '$1==r{sum+=$10; c++} END{if(c>0) printf "**Total FP: %d**\n", sum}'
      echo
    done

    cat <<EOF
## Comparative Results

| Repo | Total FP | # Initiatives | Avg FP/Initiative |
|---|---:|---:|---:|
$(awk -F'\t' '$1!="repo"{printf "| `%s` | %s | %s | %s |\n",$1,$2,$3,$4}' "$INITIATIVE_TOTALS_FILE")

Historical baseline (non-\`blog\`) average Total FP = **${hist_avg}**.

Relative multipliers for recent \`blog\`:
- vs historical average: **${ratio_avg}x**
- vs best historical: **${ratio_best}x**

## Charts

\`\`\`mermaid
xychart-beta
    title "Total Feature Points by Repo Window"
    x-axis ["blog","radiate","simple-excel","tempus-fugit","temperature-machine"]
    y-axis "Feature Points" 0 --> 50
    bar [$(awk -F'\t' '$1!="repo"{v[$1]=$2} END{printf "%s,%s,%s,%s,%s",v["blog"],v["radiate"],v["simple-excel"],v["tempus-fugit"],v["temperature-machine"]}' "$INITIATIVE_TOTALS_FILE")]
\`\`\`

\`\`\`mermaid
xychart-beta
    title "Average Initiative Size (FP per Initiative)"
    x-axis ["blog","radiate","tempus-fugit","simple-excel","temperature-machine"]
    y-axis "Avg FP" 0 --> 10
    bar [$(awk -F'\t' '$1!="repo"{v[$1]=$4} END{printf "%.1f,%.1f,%.1f,%.1f,%.1f",v["blog"],v["radiate"],v["tempus-fugit"],v["simple-excel"],v["temperature-machine"]}' "$INITIATIVE_TOTALS_FILE")]
\`\`\`

## Caveat

This report is intentionally a structured judgment model. It is best used for **relative trend tracking** over time, not for absolute precision.

---

Companion metric-first report:

- [AI_PRODUCTIVITY_ANALYSIS.md](/Users/toby/dev/code/blog/AI_PRODUCTIVITY_ANALYSIS.md)
EOF
  } > "$ROOT_DIR/FEATURE_SIZE_COMPARISON.md"
}

main() {
  collect_metrics
  build_indexes
  write_ai_report

  write_initiatives_config
  score_initiatives
  write_feature_size_report

  echo "Generated:"
  echo "  - $ROOT_DIR/AI_PRODUCTIVITY_ANALYSIS.md"
  echo "  - $ROOT_DIR/FEATURE_SIZE_COMPARISON.md"
}

main "$@"

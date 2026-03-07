from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASTRO_CONTENT = (BASE_DIR / "../astro/src/content").resolve()

BLOG_DIR = ASTRO_CONTENT / "blog"
UNPUBLISHED_DIR = ASTRO_CONTENT / "unpublished"
OUTPUT_DIR = BLOG_DIR

CACHE_DIR = BASE_DIR / "cache"
CACHE_DIR.mkdir(exist_ok=True)

CORPUS_CACHE = CACHE_DIR / "corpus.json"
STYLE_PROFILE_JSON = CACHE_DIR / "style_profile.json"
STYLE_PROFILE_MD = CACHE_DIR / "style_profile.md"

INCLUDE_UNPUBLISHED = True

MAX_STYLE_SAMPLES = 6
MAX_SAMPLE_CHARS = 4000

DEFAULT_AUDIENCE = "Senior engineers and engineering leaders"
DEFAULT_DRAFT = True

DEFAULT_MAX_AGE_YEARS = 12
DEFAULT_STRICT_MAX_AGE = False
RECENCY_HALF_LIFE_YEARS = 6

DEFAULT_MODEL = "gpt-5"

MODEL_PRICING = {
    "gpt-5": {
        "input_per_million": 1.25,
        "output_per_million": 10.00,
    },
    "gpt-5-mini": {
        "input_per_million": 0.25,
        "output_per_million": 2.00,
    },
}
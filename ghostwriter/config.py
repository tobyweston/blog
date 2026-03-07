from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASTRO_CONTENT = (BASE_DIR / "../astro/src/content").resolve()

BLOG_DIR = ASTRO_CONTENT / "blog"
UNPUBLISHED_DIR = ASTRO_CONTENT / "unpublished"
OUTPUT_DIR = BLOG_DIR

CACHE_DIR = BASE_DIR / "cache"
CACHE_DIR.mkdir(exist_ok=True)

CORPUS_CACHE = CACHE_DIR / "corpus.json"

INCLUDE_UNPUBLISHED = True

MAX_STYLE_SAMPLES = 6
MAX_SAMPLE_CHARS = 4000

DEFAULT_AUDIENCE = "Senior engineers and engineering leaders"
DEFAULT_DRAFT = True

# Retrieval behaviour
DEFAULT_MAX_AGE_YEARS = 12      # soft default for style selection
DEFAULT_STRICT_MAX_AGE = False  # if true, hard-cut old posts
RECENCY_HALF_LIFE_YEARS = 6     # score decays with age
i# Ghostwriter

AI-powered blog post generator for Toby Weston's blog. Analyzes existing posts to match writing style and tone.

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Dependencies:
   - `openai` - for AI blog post generation
   - `pyyaml` - for parsing markdown frontmatter

3. **Set your OpenAI API key:**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

```bash
python generate_post.py
```

You'll be prompted to enter a topic. The script will:
- Analyze your existing blog posts for writing style
- Generate a draft post in your voice
- Save it to `../astro/src/content/blog/ai-draft.mdx`

## Deactivate

When done, deactivate the virtual environment:
```bash
deactivate
```


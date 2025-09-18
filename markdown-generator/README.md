# Markdown Generator

This project generates Markdown reports from a Jinja2 template.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python generate.py \
  --title "My Report" \
  --author "Author Name" \
  --date "2025-05-16" \
  --summary "Project update summary" \
  --notes "Point 1" "Point 2" "Point 3"
```

The generated file will appear in `output/report.md`.

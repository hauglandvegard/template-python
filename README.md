# template-python

Python project template.

## Setup

```bash
uv sync --group dev
cp .env.example .env
```

## Run

```bash
uv run python -m src.main
```

## Dev

```bash
uv run ruff check .
uv run mypy src
uv run pytest
```

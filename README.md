# Soma AI

A Python-based AI assistant project.

## Project Structure

```
soma-ai/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── ai_engine.py
│   │   └── config.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   └── logger.py
│   └── models/
│       ├── __init__.py
│       └── schemas.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py
│   └── test_utils.py
├── docs/
│   ├── README.md
│   ├── ARCHITECTURE.md
│   └── API.md
├── requirements.txt
├── .gitignore
├── .env.example
├── setup.py
└── conftest.py
```

## Setup

1. Create virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   # Unix
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create .env file from .env.example:
   ```bash
   cp .env.example .env
   ```

## Running

```bash
python src/main.py
```

## Testing

```bash
pytest
```
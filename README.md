# create-fastapi-app

![logo](./img/logo.png)

CLI to scaffold clean, production-ready FastAPI projects with modern tooling.

![python](https://img.shields.io/badge/python-3.10%2B-blue) ![fastapi](https://img.shields.io/badge/fastapi-%23009688) ![ruff](https://img.shields.io/badge/ruff-linting-red) ![mypy](https://img.shields.io/badge/mypy-typing-blue) ![license](https://img.shields.io/badge/license-MIT-green)

---

## Overview

create-fastapi-app is a CLI tool to quickly bootstrap a clean and structured FastAPI project.

It provides a minimal, opinionated setup with modern tooling, allowing you to focus on building your application instead of configuring your environment.

---

## Features

- Project scaffolding for FastAPI with structured architecture
- Multiple project architectures (minimal, modular, clean architecture)
- Database support (SQLite, PostgreSQL) with optional advanced configurations
- ORM integration (SQLAlchemy or Prisma)
- Optional async task systems (FastAPI background tasks, Celery, Arq)
- Built-in rate limiting support
- Environment configuration with pydantic-settings
- Static typing with mypy
- Linting and formatting with Ruff
- Opinionated project structure for maintainability and scalability

---

## Installation

```bash
pip install create-fastapi-app
```

## Usage

```bash
create-fastapi-app my_project
cd my_project
uv run uvicorn main:app --reload
```

## Generated Structure

```
my_project/
├── main.py
├── app/
│   ├── routes/
│   ├── services/
│   └── schemas/
├── pyproject.toml
```

## Philosophy

This tool follows an opinionated approach.

The goal is to provide a clean, consistent and maintainable starting point without unnecessary configuration complexity.

## Contributing

Contributions are welcome. Before opening a pull request, please ensure that your changes follow the project conventions.

## Development setup

```bash
uv sync
```

### Code quality

Run linting and type checking before committing:

```bash
uv run ruff check .
uv run mypy .
```

### Commit convention

This project uses [git-z￼](https://github.com/ejpcmac/git-z) for commit standardization.

Please follow the commit structure below:

Types

- WIP — Work in progress
- ADD — New feature or file
- FIX — Bug fix
- UPDATE — Improvement or modification
- DELETE — Removal of code or files
- CONFIG — Configuration or dependencies
- DOCS — Documentation only
- REFACTOR — Refactoring without behavior change
- STYLE — Formatting or minor cleanup

Scopes

- route
- controllers
- security
- storage
- external-api
- data-schema
- auth
- config

Format :

```
TYPE description (scope)
```

### Guidelines

- Keep changes focused and minimal
- Follow the existing project structure
- Write clear and explicit commit messages
- Ensure code is typed and linted

## License

MIT

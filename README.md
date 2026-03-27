# create-fastapi-app

![logo](./img/logo.png)

A CLI to generate production-ready FastAPI backends with a clean, opinionated architecture.

![python](https://img.shields.io/badge/python-3.12%2B-blue)
![cli](https://img.shields.io/badge/interface-CLI-black)
![ruff](https://img.shields.io/badge/ruff-linting-red)
![mypy](https://img.shields.io/badge/mypy-typing-blue)
![pydantic](https://img.shields.io/badge/pydantic-validation-blue)
![status](https://img.shields.io/badge/status-active--development-orange)
![license](https://img.shields.io/badge/license-MIT-green)

---

## Overview

create-fastapi-app is an opinionated CLI designed to generate production-ready FastAPI backends with modern Python tooling and clear architecture conventions.

It generates a structured backend ready to scale, not just a starting point.

The goal is not just to scaffold code — it's to enforce a consistent, scalable foundation from day one, whether you're building web backends, microservices, or data/ML APIs.

---

## Key Features

- Interactive CLI to generate FastAPI backends
- Opinionated architecture templates (minimal, modular)
- Modern Python tooling out of the box (Ruff, Mypy, strict typing)
- Configurable stack (database, ORM, package manager)
- Progressive versioning — v0.5 → v1 → v2, each expanding the ecosystem

## Project Status

> **Work in progress**

The CLI foundations and interactive configuration flow are implemented.  
FastAPI project generation is currently under development.

---

## Current Scope

What is currently available:

- Interactive CLI entrypoint (`create-fastapi-app`)
- Project configuration wizard (project name, stack options, etc.)
- Typed configuration models
- Restart / validation flow before generation
- Linting with Ruff
- Static typing with Mypy

---

## What it does today

Run the CLI to configure your backend interactively. The tool captures your full stack setup (architecture, database, ORM, tooling) and prepares a ready-to-generate FastAPI project.

The scaffolding engine is currently in progress.

```bash
create-fastapi-app
```

## Development Setup

### Clone the repository and install dependencies:

```bash
git clone https://github.com/initd-fr/create-fastapi-app.git
cd create-fastapi-app
uv sync
```

### Install locally in editable mode:

```bash
uv pip install -e .
```

### Run the CLI:

```bash
create-fastapi-app
```

## Code Quality

Before committing, ensure code quality:

```bash
uv run ruff check .
uv run mypy .
```

## Contributing

We are open to suggestions for future versions (v1.5, v2+).

If you have ideas for features, tooling integrations, or improvements, feel free to open an issue or discussion.

Before opening a pull request:

- keep changes focused and minimal
- respect the existing project structure
- ensure code is typed and linted
- follow commit conventions

### Commit Convention

This project uses a structured commit format:

```
TYPE description (scope)
```

**Types:**

| Type       | Description                              |
| ---------- | ---------------------------------------- |
| `INIT`     | Initial setup                            |
| `FEAT`     | New feature                              |
| `FIX`      | Bug fix                                  |
| `CHORE`    | Maintenance / tooling                    |
| `REFACTOR` | Code improvement without behavior change |
| `STYLE`    | Formatting / lint fixes                  |
| `BUILD`    | Packaging / release                      |

**Scopes:** `cli`, `generator`, `template`, `config`, `dependencies`, `typing`, `lint`, `docs`

Example:

```
FEAT add CLI question flow (cli)
```

## Vision

create-fastapi-app aims to become the reference scaffolding tool for FastAPI projects in Python — the equivalent of `create-t3-app` for the backend ecosystem.

The focus is on clarity, strong defaults, and progressive complexity: simple setups work out of the box, advanced architectures are unlocked as the project matures.

Each version expands the ecosystem while preserving the same opinionated, low-friction developer experience.

---

## Roadmap

### v0.5 — Core CLI (FastAPI Starter)

- [x] CLI initialization
- [x] Interactive configuration flow
- [x] Typed configuration models
- [x] Linting and typing (Ruff + Mypy)

- [ ] FastAPI project generation
- [ ] Project structures:
  - minimal
  - modular
- [ ] Package managers:
  - pip
  - uv
- [ ] Database support:
  - none
  - SQLite
  - PostgreSQL
- [ ] ORM:
  - SQLAlchemy
  - SQLModel
- [ ] Basic rate limiting
- [ ] `.env` configuration
- [ ] Optional typing setup
- [ ] Optional Ruff integration
- [ ] Virtual environment creation
- [ ] Dependency installation
- [ ] Run server after setup

---

### v1 — Advanced Backend Generator (Data / ML / DL Ready)

- [ ] Extended package manager support:
  - poetry
  - pipenv

- [ ] Extended database support:
  - MySQL / MariaDB
  - MongoDB

- [ ] ORM / ODM:
  - SQLAlchemy
  - SQLModel
  - Beanie (MongoDB async)

- [ ] Data processing stack (optional):
  - pandas
  - numpy
  - scikit-learn

- [ ] Deep learning support (optional):
  - PyTorch
  - TensorFlow

- [ ] ML/DL project structure:
  - `ml/`
  - `pipelines/`
  - `models/`

- [ ] Improved configuration system
- [ ] Advanced rate limiting
- [ ] Production-ready project templates

---

### v2 — Industrialization & Scaling

- [ ] Redis integration
- [ ] Task queues:
  - Celery
  - ARQ

- [ ] Event streaming:
  - Kafka

- [ ] Distributed computing:
  - Ray

- [ ] Microservices patterns
- [ ] Event-driven architecture
- [ ] Advanced security hardening
- [ ] Observability (logging / metrics)

---

## Why this project

Starting a FastAPI project correctly takes time — structure, tooling, database setup, typing, linting.

This CLI removes that friction by generating a clean, consistent, and production-ready foundation in minutes.

It ensures every project starts with the same high standards, reducing technical debt from day one.

## License

MIT

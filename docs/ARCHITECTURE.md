# Architecture

## Overview

Soma AI follows a layered architecture pattern with the following structure:

```
┌─────────────────────────────────────┐
│         Application Layer           │
│         (CLI/API endpoints)         │
└──────────────────┬──────────────────┘
                   │
┌──────────────────┴──────────────────┐
│         Business Logic Layer        │
│     (AIEngine, Processors, etc)     │
└──────────────────┬──────────────────┘
                   │
┌──────────────────┴──────────────────┐
│         Data Layer                  │
│     (Models, Schemas, DB Access)    │
└──────────────────┬──────────────────┘
                   │
┌──────────────────┴──────────────────┐
│         Infrastructure Layer        │
│   (Config, Logging, Utils)          │
└─────────────────────────────────────┘
```

## Modules

### Core (`src/core/`)
- **config.py** - Configuration management from environment
- **ai_engine.py** - Main AI processing engine

### Utils (`src/utils/`)
- **logger.py** - Logging configuration
- **helpers.py** - Utility helper functions

### Models (`src/models/`)
- **schemas.py** - Pydantic data validation schemas

## Design Patterns

1. **Singleton Pattern** - Config and Logger instances
2. **Factory Pattern** - AI Engine creation
3. **Dependency Injection** - Config passed to components

## Data Flow

1. Input → Validation (schemas)
2. Processing → AI Engine
3. Response → Formatting & Output

# Siomi — Multi-Agent AI System

Siomi is a multi-agent system designed to answer data queries, perform analysis, generate charts, documents, and reports through a conversational interface. It is built on Clean Architecture principles with AI agent patterns for extensibility, reliability, and testability.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [AI Agent Patterns](#ai-agent-patterns)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Configuration](#configuration)
- [Running](#running)
- [Testing](#testing)
- [Roadmap](#roadmap)

---

## Overview

Siomi exposes a conversational interface where users can ask questions in natural language. Behind the scenes, a multi-agent orchestrator routes each request to the most appropriate specialized agent:

| Capability | Description |
|---|---|
| **Data Query** | Query structured databases or APIs using natural language |
| **Data Analysis** | Statistical and exploratory analysis over datasets |
| **Chart Generation** | Produce bar, line, pie, and other visualizations |
| **Document Generation** | Create Word, PDF, or Markdown documents from data |
| **Report Generation** | Combine analysis + charts into formatted business reports |

---

## Architecture

Siomi follows **Clean Architecture** (also known as Hexagonal/Ports & Adapters). Each layer has a single responsibility and depends only inward.

```
┌────────────────────────────────────────────────────┐
│                   Infrastructure                    │  ← Frameworks, DBs, APIs, LLMs
│  - HTTP Controllers (FastAPI)                       │
│  - LLM Adapters (Azure OpenAI, OpenAI)              │
│  - Chart Renderers (matplotlib, plotly)             │
│  - Document Exporters (PDF, DOCX)                   │
│  - Settings / Configuration                         │
└───────────────────┬────────────────────────────────┘
                    │ implements
┌───────────────────▼────────────────────────────────┐
│                   Application                       │  ← Use Cases, Orchestration
│  - Use Cases (LLMUseCase, AnalysisUseCase, …)       │
│  - DTOs (UserMessageDto, ResponseMessageDto, …)     │
│  - Mappers (MessageMapper, …)                       │
│  - Validators                                       │
└───────────────────┬────────────────────────────────┘
                    │ uses
┌───────────────────▼────────────────────────────────┐
│                     Domain                          │  ← Business Logic (pure Python)
│  - Models (Message, Report, Chart, Document, …)     │
│  - Interfaces / Ports (LLM, ChartRenderer, …)       │
│  - Domain Exceptions (BusinessException, …)         │
│  - Enums (TechnicalMessage, AgentType, …)           │
└────────────────────────────────────────────────────┘
```

### Layer Rules

- **Domain** knows nothing about the layers above it.
- **Application** depends only on Domain interfaces, never on concrete infrastructure classes.
- **Infrastructure** implements Domain interfaces and wires everything together via dependency injection.

---

## AI Agent Patterns

Siomi implements the following AI agent design patterns:

### 1. Tool Discovery

Each agent advertises a set of tools with typed schemas. The orchestrator queries available tools at runtime and selects the appropriate tool for the user's intent — no hardcoded routing.

```
User Request
    │
    ▼
Orchestrator Agent
    │── discovers tools from registered agents
    │── selects best tool via LLM reasoning
    ▼
Specialized Agent (QueryAgent | AnalysisAgent | ChartAgent | ReportAgent)
    │── executes tool
    ▼
Response
```

### 2. Dynamic Prompts

Prompts are not static strings. They are constructed at runtime based on:
- User intent extracted from the conversation
- Available schema (table names, column types)
- Current context (previous messages, active report, etc.)

This allows the same agent to adapt to different data sources without redeployment.

### 3. Multithreading / Async Concurrency

Long-running tasks (chart rendering, PDF export, LLM calls) run concurrently using Python's `asyncio`. When a report requires multiple charts and a summary, all subtasks are dispatched in parallel and merged before responding.

```
Report Request
    │
    ├── asyncio.gather(
    │     ChartAgent.run("sales_by_month"),
    │     ChartAgent.run("top_products"),
    │     AnalysisAgent.run("summary_statistics")
    │   )
    ▼
ReportAgent.assemble(charts, analysis) → PDF
```

### 4. Conversation Memory

Each agent session maintains conversation context. Previous messages are summarized and injected into subsequent prompts to preserve continuity.

### 5. Agent Supervisor

A supervisor monitors agent execution. If a specialized agent fails or produces an uncertain result, the supervisor can retry with a different strategy, escalate to a more powerful model, or return a graceful error.

---

## Features

- Natural language data queries (SQL generation via LLM)
- Exploratory data analysis with statistical summaries
- Chart generation (bar, line, pie, scatter, heatmap)
- Document export (Markdown, PDF, DOCX)
- Report generation combining charts and analysis
- Multi-turn conversation with memory
- Clean Architecture for testability and maintainability
- Async-first execution for performance
- SonarQube integration for code quality

---

## Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.13+ |
| Web Framework | FastAPI |
| LLM Integration | LangChain, Azure OpenAI |
| Data Validation | Pydantic v2 |
| Async Runtime | asyncio |
| Charts | matplotlib / plotly _(planned)_ |
| PDF Export | reportlab / weasyprint _(planned)_ |
| Testing | pytest |
| Code Quality | SonarQube |
| Dependency Manager | uv |

---

## Project Structure

```
siomi/
├── main.py                          # Entry point
├── pyproject.toml                   # Project metadata and dependencies
├── .env                             # Environment variables (not committed)
└── src/
    ├── app/
    │   ├── application/             # Use cases, DTOs, mappers, validators
    │   │   ├── dto/
    │   │   │   ├── user_message_dto.py
    │   │   │   └── response_message_dto.py
    │   │   ├── mapper/
    │   │   │   └── message_mapper.py
    │   │   ├── use_case/
    │   │   │   └── llm_use_case.py
    │   │   └── validator/
    │   ├── domain/                  # Pure business logic
    │   │   ├── enum/
    │   │   │   └── technical_message.py
    │   │   ├── exception/
    │   │   │   ├── business_exception.py
    │   │   │   └── processor_exception.py
    │   │   ├── interface/
    │   │   │   └── llm.py           # LLM port (abstract)
    │   │   └── model/
    │   │       └── message.py
    │   └── infrastructure/          # Adapters and framework code
    │       ├── adapter/
    │       │   └── ai/
    │       │       └── AzureOpenAILLM.py
    │       ├── configuration/
    │       │   └── settings.py
    │       └── controller/          # FastAPI routers (planned)
    └── tests/
        └── unit/
            └── domain/
                └── model/
                    └── test_message.py
```

---

## Setup

**Prerequisites:** Python 3.13+, [uv](https://docs.astral.sh/uv/)

```bash
# Clone the repository
git clone <repository-url>
cd siomi

# Install dependencies
uv sync
```

---

## Configuration

Create a `.env` file at the project root:

```env
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_URL=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-01
```

---

## Running

```bash
# Run the main entry point
uv run python main.py

# Start the FastAPI server (once controllers are implemented)
uv run uvicorn src.app.infrastructure.controller.main:app --reload
```

---

## Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=xml
```

Test structure mirrors the source tree:

```
tests/
└── unit/          # Fast, isolated unit tests (no I/O, no LLM calls)
    └── domain/
└── integration/   # Tests against real adapters (planned)
└── e2e/           # Full pipeline tests (planned)
```

---

## Roadmap

### Phase 1 — Core Infrastructure ✅
- [x] Clean Architecture skeleton
- [x] Azure OpenAI adapter
- [x] Domain models and exceptions
- [x] Unit test setup with pytest

### Phase 2 — Agent Orchestration
- [ ] Orchestrator agent with tool discovery
- [ ] Dynamic prompt builder
- [ ] Conversation memory (in-memory + persistent)
- [ ] FastAPI HTTP controllers
- [ ] Agent supervisor with retry logic
- [ ] Advance RAG

### Phase 3 — Specialized Agents
- []  DataAgent - Query data to api
- [ ] ChartAgent — visualization generation
- [ ] DocumentAgent — Markdown / DOCX export
- [ ] ReportAgent — combined report assembly
### Phase 4 — Async & Performance
- [ ] Parallel agent execution with `asyncio.gather`
- [ ] Streaming responses via Server-Sent Events
- [ ] Task queue for long-running jobs (Celery / ARQ)

### Phase 5 — Quality & Observability
- [ ] Integration and E2E test suites
- [ ] SonarQube quality gates in CI
- [ ] Structured logging and tracing (OpenTelemetry)
- [ ] API documentation (auto-generated from FastAPI)

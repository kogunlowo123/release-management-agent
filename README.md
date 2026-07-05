# Release Management Agent

[![CI](https://github.com/kogunlowo123/release-management-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/release-management-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Release orchestration agent that manages semantic versioning, generates changelogs, coordinates release trains, automates release notes, manages feature flags, and tracks release health metrics post-deployment.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `create_release` | Create a new release with version bump and changelog |
| `generate_changelog` | Generate changelog from conventional commits |
| `manage_feature_flag` | Toggle or configure a feature flag for a release |
| `check_release_health` | Monitor post-release health metrics (errors, latency, rollback signals) |
| `rollback_release` | Rollback to a previous release version |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/release/create` | Create new release |
| `POST` | `/api/v1/release/changelog` | Generate changelog |
| `POST` | `/api/v1/release/flags` | Manage feature flags |
| `GET` | `/api/v1/release/{version}/health` | Check release health |
| `POST` | `/api/v1/release/rollback` | Rollback release |

## Features

- Semantic Versioning
- Changelog Generation
- Release Coordination
- Feature Flags
- Release Health

## Integrations

- Github Connector
- Npm Registry
- Pypi Registry
- Launchdarkly
- Datadog

## Architecture

```
release-management-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── release_management_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Git + Package Registries + Feature Flag Platforms**

---

Built as part of the Enterprise AI Agent Platform.

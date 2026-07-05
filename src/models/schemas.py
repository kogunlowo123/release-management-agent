"""Release Management Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class ReleaseRequest(BaseModel):
    """ReleaseRequest for Release Management Agent."""
    bump_type: str
    prerelease: str | None = None
    deploy_environments: list[str] = ['staging']


class ReleaseHealth(BaseModel):
    """ReleaseHealth for Release Management Agent."""
    version: str
    status: str
    error_rate: float
    p99_latency_ms: float
    rollback_recommended: bool


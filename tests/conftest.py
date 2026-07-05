"""Test configuration for Release Management Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "release-management-agent", "category": "DevOps & Platform Engineering"}

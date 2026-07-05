"""Release Management Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_create_release():
    """Test Create a new release with version bump and changelog."""
    tools = AgentTools()
    result = await tools.create_release(bump_type="test", prerelease="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_changelog():
    """Test Generate changelog from conventional commits."""
    tools = AgentTools()
    result = await tools.generate_changelog(from_tag="test", to_ref="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_feature_flag():
    """Test Toggle or configure a feature flag for a release."""
    tools = AgentTools()
    result = await tools.manage_feature_flag(flag_name="test", action="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_check_release_health():
    """Test Monitor post-release health metrics (errors, latency, rollback signals)."""
    tools = AgentTools()
    result = await tools.check_release_health(release_version="test", metrics="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.release_management_agent_agent import ReleaseManagementAgentAgent
    agent = ReleaseManagementAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0

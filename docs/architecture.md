# Release Management Agent Architecture

Release orchestration agent that manages semantic versioning, generates changelogs, coordinates release trains, automates release notes, manages feature flags, and tracks release health metrics post-deployment.

## Domain Tools

- **create_release**: Create a new release with version bump and changelog
- **generate_changelog**: Generate changelog from conventional commits
- **manage_feature_flag**: Toggle or configure a feature flag for a release
- **check_release_health**: Monitor post-release health metrics (errors, latency, rollback signals)
- **rollback_release**: Rollback to a previous release version
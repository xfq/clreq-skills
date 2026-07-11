# Platform Adapters

Platform Adapters map the Universal Rule Package into specific coding-agent environments.

First-version priority:

- `reference.md`: Reference Adapter for general agent instruction files
- `codex/`: Codex Platform Adapter
- `claude-code/`: Claude Code Platform Adapter

Later adapters may cover Cursor, OpenClaude, OpenCode, and other agents. Adapters should stay thin: they handle installation, Coarse Triggers, Project Overrides, and output conventions, but the Universal Rule Package remains the source of truth.

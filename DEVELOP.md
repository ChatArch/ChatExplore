# Development Guide

## Shared CLI Runtime

- Keep the public root explicit as `chatexplore`.
- Keep `chatstyle>=0.2.0,<0.3.0` and use `add_tree_option()` for the registered
  `--tree` and `--tree-brief` views. Do not add a package-local tree renderer.
- Keep the CLI adapter thin. Add importable typed Python functions before
  exposing business commands.
- Missing required inputs may use ChatStyle interaction only when recovery is
  unambiguous. Non-interactive use must fail cleanly instead of blocking.
- Keep sensitive values out of prompts, summaries, trees, and logs.
- ChatExplore currently has no env, profile, or config behavior. If that
  changes, register a typed ChatEnv provider and use
  `chatenv>=0.2.10,<0.3.0` with ChatEnv storage paths.

## Docs and Tests

- Use doc-first CLI testing with `click.testing.CliRunner`.
- Assert that full and brief trees come from the real command registry.
- Keep `README.md`, `docs/`, and `CHANGELOG.md` in sync with user-facing changes.

## Automation

Run the complete local gate before proposing a release:

```bash
python -m pytest -q
python -m build
python -m twine check dist/*
chatexplore --version
chatexplore --tree
chatexplore --tree-brief
git diff --check
```

CI must exercise the installed console script. Releases use the tag-driven
trusted-publishing workflow: merge a green PR, tag the merged `main` commit
with the package version, verify the publish workflow, then clean-install the
exact PyPI version and repeat all three CLI readbacks without `PYTHONPATH`.

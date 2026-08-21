# Changelog

## 0.0.2 - 2026-08-21

### Added

- Added the missing `chatexplore` Click entrypoint with top-level `--version`,
  `--tree`, and `--tree-brief`.
- Added installed-console-script, command-tree, package metadata, CI, and
  release workflow contract tests.

### Changed

- Bounded the shared runtime at `chatstyle>=0.2.0,<0.3.0` and made the public
  root command name explicit.
- Replaced the non-publishing workflow scaffold with guarded tag-driven PyPI
  trusted publishing.
- Updated package metadata, README, long-lived docs, and development gates to
  describe the truthful root-only command surface.

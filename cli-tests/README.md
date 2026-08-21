# CLI Tests

Executable CLI contract coverage lives in `tests/test_cli.py`. It exercises
the real Click registry through `CliRunner`; installed console-script readbacks
are enforced by CI and the release checklist.

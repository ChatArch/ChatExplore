# Mock CLI Tests

No mock CLI surface is currently needed. Prefer direct `CliRunner` coverage of
the registered command tree, and add mocks only around real external
boundaries introduced by future business commands.

# ChatExplore

`ChatExplore` is the ChatArch exploration CLI package shell. Its current public
surface is intentionally root-only: it provides package and registered-command
introspection without claiming unfinished exploration features.

## Quick Start

```bash
python -m pip install chatexplore
chatexplore --help
chatexplore --version
chatexplore --tree
chatexplore --tree-brief
```

## CLI Tree

```text
chatexplore
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

The root is an explicit Click command named `chatexplore`. ChatStyle
`add_tree_option()` renders both tree views from the real Click registry.
`--tree` retains parameter signatures for future commands, while
`--tree-brief` omits them. The outputs are currently identical because no
business subcommands are registered.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m build
python -m twine check dist/*
chatexplore --version
chatexplore --tree
chatexplore --tree-brief
```

## Layout

- `src/chatexplore/`: package and Click CLI entrypoint
- `tests/`: version, CLI, dependency, CI, and release contract tests
- `docs/`: long-lived CLI contract documentation
- `.github/workflows/`: CI and tag-driven trusted publishing

## Development Notes

See `DEVELOP.md` and `setup.md` before expanding the scaffold.

## Project Links

- Repository: https://github.com/ChatArch/ChatExplore
- Package: https://pypi.org/project/chatexplore/

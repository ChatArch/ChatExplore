# Docs

Long-lived documentation for `chatexplore` lives here.

## Registered CLI Contract

```text
chatexplore
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

The root Click group uses `chatstyle.add_tree_option()` to render this actual
registered surface. `chatexplore --tree` includes parameter signatures when
business commands exist; `chatexplore --tree-brief` preserves the same nodes
and descriptions while omitting signatures. ChatExplore currently registers
no business subcommands, so the two outputs are identical.

New commands must first expose reusable typed Python functions, state their
inputs, outputs, side effects, and security boundary, and update this contract,
the README, tests, and changelog together.

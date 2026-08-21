# Setup

This scaffold was generated from the `cli-style` template.

The package now has an established root-only CLI baseline.

## Current Contract

- Distribution and import module: `chatexplore`
- Console script and explicit Click root: `chatexplore`
- Shared tree runtime: `chatstyle>=0.2.0,<0.3.0`
- Public root options: `--help`, `--version`, `--tree`, `--tree-brief`
- Business commands: none registered yet

## Expansion Rule

Do not add placeholder commands. Add an importable, typed Python operation
first, then a thin Click command whose inputs, outputs, side effects, and
security boundary are documented and tested. Keep the registered full/brief
trees, README, docs, changelog, CI, and release checks synchronized.

"""CLI entrypoint for ChatExplore."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatexplore import __version__


@click.group(
    name="chatexplore",
    invoke_without_command=True,
    no_args_is_help=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.version_option(version=__version__, prog_name="chatexplore")
@add_tree_option(renderer_options={"root_name": "chatexplore"})
def main() -> None:
    """ChatExplore exploration CLI package shell."""


if __name__ == "__main__":
    main()

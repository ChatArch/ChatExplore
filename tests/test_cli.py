import click
from click.testing import CliRunner

from chatexplore import __version__
from chatexplore.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0, result.output
    assert f"chatexplore, version {__version__}" in result.output


def test_help_lists_shared_tree_options():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0, result.output
    assert "--tree" in result.output
    assert "Print the registered CLI tree and exit." in result.output
    assert "--tree-brief" in result.output
    assert "without parameter signatures" in result.output


def test_tree_options_render_truthful_root_only_surface():
    full = CliRunner().invoke(main, ["--tree"])
    brief = CliRunner().invoke(main, ["--tree-brief"])

    assert full.exit_code == 0, full.output
    assert brief.exit_code == 0, brief.output
    assert full.output == brief.output
    assert full.output.splitlines() == [
        "chatexplore",
        "├── --help  # Show this message and exit.",
        "├── --version  # Show the version and exit.",
        "├── --tree  # Print the registered CLI tree and exit.",
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.",
    ]


def test_tree_defaults_to_signatures_and_brief_omits_them():
    @click.command(name="inspect", help="Inspect one exploration target without changing it.")
    @click.argument("target")
    @click.option("--format", "output_format")
    def inspect(target: str, output_format: str | None) -> None:
        del target, output_format

    main.add_command(inspect)
    try:
        full = CliRunner().invoke(main, ["--tree"])
        brief = CliRunner().invoke(main, ["--tree-brief"])
    finally:
        main.commands.pop("inspect", None)

    assert full.exit_code == 0, full.output
    assert brief.exit_code == 0, brief.output
    assert (
        "inspect <TARGET> [--format OUTPUT-FORMAT]"
        "  # Inspect one exploration target without changing it."
    ) in full.output
    assert "inspect  # Inspect one exploration target without changing it." in brief.output
    assert "<TARGET>" not in brief.output
    assert "[--format OUTPUT-FORMAT]" not in brief.output


def test_tree_root_uses_public_console_command_in_module_mode():
    result = CliRunner().invoke(
        main,
        ["--tree"],
        prog_name="python -m chatexplore.cli",
    )

    assert result.exit_code == 0, result.output
    assert result.output.splitlines()[0] == "chatexplore"
    assert "python -m chatexplore.cli" not in result.output

# Software Version Checker

A command-line agent that uses the Claude Agent SDK's web search and fetch tools
to look up the latest stable releases of programming languages and standards.
It returns the version, release date when verified, and source links.

## Setup

1. Install [uv](https://docs.astral.sh/uv/) and the Claude Code CLI.
2. Install the project dependencies:

   ```powershell
   uv sync
   ```

3. Create a `.env` file in the project root and add your Anthropic API key:

   ```text
   ANTHROPIC_API_KEY=your_api_key_here
   ```

   Keep `.env` private; do not commit your API key.

## Run

Check every language in the catalog:

```powershell
uv run software-version-checker
```

Check only selected languages:

```powershell
uv run software-version-checker Python Rust "C++"
```

You can also run the project entry script with `uv run python main.py Python`.
In the project checkout, the agent reads `Sheets/requiresoftwares.csv`; when
installed as a package, it uses the bundled catalog. The saved versions in the
CSV are not treated as current—the agent verifies current releases online each
time it runs.

from dotenv import load_dotenv
import asyncio
import csv
from pathlib import Path
from claude_agent_sdk import ClaudeAgentOptions, query

Sheets_dir = Path("Sheets/requiredsoftwares.csv")


async def main():
    

    with open(Sheets_dir, "r", encoding="utf-8-sig") as file:
        softwares = list(csv.DictReader(file))

    options = ClaudeAgentOptions(
        system_prompt="Find the latest stable software versions using official sources.",
        model="claude-haiku-4-5",
        max_turns=30,
        permission_mode="bypassPermissions"
    )

    for software in softwares:
        name = software["name"]
        version = software.get("version", "")
        url = software.get("url", "")

        prompt = f"""
        Find the latest stable version of {name}.
        Current version: {version or "Not provided"}
        URL: {url or "Not provided"}
        Use official sources and report the latest version and source URL.
        """

        async for message in query(prompt=prompt, options=options):
            if hasattr(message, "content"):
                for block in message.content:
                    if hasattr(block, "text"):
                        print(f"{name}: {block.text}")


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())

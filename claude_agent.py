from dotenv import load_dotenv 
import os
import asyncio 
from pathlib import Path
from claude_agent_sdk import ClaudeSDKClient,ClaudeAgentOptions,query
import csv 
import json

Sheets_dir = Path("Sheets/requiredsoftwares.csv")

with open(Sheets_dir, 'r') as csvfile:
    softwares = list(csv.DictReader(csvfile))
async def main():
    options = ClaudeAgentOptions(
        system_prompt = "You are a helpful assistant",
        model = 'claude-haiku-4-5',
        max_turns = 30,
        allowed_tools = ['WebSearch', 'WebFetch'],
        permission_mode = 'bypassPermissions'
    )

for software in softwares :
    name = software['name']
    version = software.get('version'," ")
    url = software.get('url'," ")

    for message in query(options = options):
        if version in message.get("content", ""):
            print(f"{name} is installed with version {version}")

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())

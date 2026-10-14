from dotenv import load_dotenv 
import os
import asyncio 
from pathlib import Path
from claude_agent_sdk import ClaudeSDKClient,ClaudeAgentOptions,query

Sheets_dir = Path("Sheets/requiredsoftwares.csv")

async def main():
    options = ClaudeAgentOptions(
        system_prompt = "You are a helpful assistant",
        model = 'claude-haiku-4-5',
        max_turns = 30,
        permission_mode = 'bypassPermissions'
    
    )

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())

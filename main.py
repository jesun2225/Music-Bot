import discord
from discord.ext import commands
from discord import app_commands
import wavelink
import asyncio
from config.config import *

class MusicBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.voice_states = True
        intents.members = True
        intents.guilds = True
        
        super().__init__(
            command_prefix=BOT_PREFIX,
            intents=intents,
            application_id=APPLICATION_ID
        )

    async def setup_hook(self):
        try:
            await self.load_extension('cogs.music')
            print("Music cog loaded successfully!")
        except Exception as e:
            print(f"Failed to load music cog: {e}")
        
        try:
            node: wavelink.Node = wavelink.Node(
                uri=f'{"https" if LAVALINK_SECURE else "http"}://{LAVALINK_HOST}:{LAVALINK_PORT}',
                password=LAVALINK_PASSWORD,
                identifier=LAVALINK_NAME
            )
            await wavelink.Pool.connect(nodes=[node], client=self)
            print("Connected to Lavalink node!")
        except Exception as e:
            print(f"Failed to connect to Lavalink: {e}")

        try:
            print("Syncing commands globally...")
            await self.tree.sync()
            print("Commands synced successfully!")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f'Node {node.identifier} is ready!')

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print(f'Bot is ready to play music!')
        print(f'Connected to {len(self.guilds)} guilds')
        
        await self.change_presence(
            status=discord.Status.dnd,
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="JEESAN2225"
            )
        )

async def main():
    async with MusicBot() as bot:
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
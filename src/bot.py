import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from commands.tasks import setup_tasks

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("🏓 Pong! Estoy vivo.")

setup_tasks(bot)

if __name__ == "__main__":
    bot.run(TOKEN)

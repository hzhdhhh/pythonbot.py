import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='is')

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	
@bot.command()
async def ping():
	await bot.say('Vladi e gay')

bot.run('NTQ5MjY5NjIyNjg0MjU0MjE5.D1Rk6Q.74m5pYhvRjp0DFYF-m_NJjXwU9c')

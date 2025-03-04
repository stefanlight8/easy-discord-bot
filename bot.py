import disnake
from disnake.ext import commands
from config import settings

class EasyDiscordBot(commands.Bot):
    def __init__(self):
        super().__init__(
	    command_prefix = settings['PREFIX'], 
	    intents = disnake.Intents.all()
        )

    async def on_ready(self):
        print("Запущен!")

bot = EasyDiscordBot()
bot.run(settings['TOKEN'])

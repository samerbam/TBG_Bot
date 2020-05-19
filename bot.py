import discord
from discord.ext.commands import Bot
import config


bot = Bot(command_prefix="/", description="The Beautiful Game Bot")
bot.remove_command('help')
#startup_extensions = ["playlist", "admin", "general", "meeting"]
startup_extensions = ["general", "managment", "commands"]

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))
	
#	t = Thread(target=app.run)
#	t.setDaemon(True)
#	t.start()
	bot.run(config.BOT_TOKEN)
#	sys.exit()
			
#@bot.event
#async def on_ready():
#	print('Logged in as: {0} (ID: {0.id})'.format(bot.user))


import discord
from discord.ext import commands
import utils
from utils import make_embed
#import config
import math
import config

class Commands(commands.Cog):
	def __init__(self, bot):
 		self.bot = bot

	async def on_ready(self):
		#self.channel = self.bot.get_channel(config.channel)
		await self.bot.say('''```css\n+ \N{WHITE HEAVY CHECK MARK} cogs.commands```''')

    #@commands.command(aliases=["p"])
    #async def ping(self, ctx):
    #    await self.channel.send('📢 Pong! {0}ms'.format(round(self.bot.latency*1000)))

	@commands.command(aliases=["nc", "netherc", "checkn"], pass_context=True)
	async def nethercheck(self, ctx, *qoords):
		try:
			x=int(qoords[0])
			z=int(qoords[1])
			xc=config.XC
			zc=config.ZC
			if (math.sqrt(((x*x)-(xc*xc))+((z*z)-(zc*zc))) < 8000):
				embed = make_embed(author_url=["Your location is safe!", "", config.SUCCESS], color=config.EMBED_SUCCESS)
				await ctx.author.send(embed=embed)
				await ctx.message.delete()
			else:
				embed = make_embed(author_url=["Your location is not safe!", "", config.WARN], color=config.EMBED_WARN, footer_text="The staff team has been notified.")
				await ctx.author.send(embed=embed)
				channel = self.bot.get_channel(config.MOD_CHANNEL_ID)
				await channel.send(f"@everyone {ctx.author} has a location outside of nether border! X: {x}, Z:{z}")
				await ctx.message.delete()
		except:
			embed = make_embed(author_url=["Invalid input.", "", config.WARN], color=config.EMBED_WARN, footer_text="Aliases for command: /nc /netherc /checkn", fields=[["Usage:", "**/nethercheck x z**", False], ["Examples:", "**/nethercheck 7836 1634**\n**/nethercheck 100 100**", False]])
			await ctx.author.send(embed=embed)
			await ctx.message.delete()
	
	
def setup(bot):
	bot.add_cog(Commands(bot))

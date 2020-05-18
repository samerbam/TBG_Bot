import discord
from discord.ext import commands

#import utils
#from os import environ
from utils import make_embed
import config
import time
import datetime


class Managment(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.time = time.time()
		
	#@commands.Cog.listener()
	#async def on_ready(self):
		#self.channel = self.bot.get_channel(config.channel)
	#	await self.bot.say('''```css\n+ \N{WHITE HEAVY CHECK MARK} Managment```''')
		
	@commands.command(aliases=["p"])
	async def ping(self, ctx):
		#await ctx.send('📢 Pong! {0}ms'.format(round(self.bot.latency*1000)))
		await ctx.send(f"📢 Pong! {self.bot.latency*1000}ms")
		
	@commands.command()
	async def uptime(self, ctx):
		await ctx.send(f"📢 Current Uptime: {datetime.timedelta(seconds=int(round(time.time()-self.time)))}")
  
	@commands.command(hidden=True)
	async def load(self, ctx, *, module):
		"""Loads a module."""
		try:
			self.bot.load_extension(module)
		except Exception as e:
			#await ctx.send(f'```py\n{e}\n```')
			await ctx.send(embed=make_embed(author_url=["Exception", "", config.WARN], fields=[[f"{e}", "\u200b"]], color=config.EMBED_WARN))
		else:
			#await ctx.send('\N{OK HAND SIGN}')
			await ctx.send(embed=make_embed(author_url=["Loaded Module", "", config.LOADED], fields=[[f"+ {module}", "\u200b"]], color=config.EMBED_SUCCESS))
			
	@commands.command(hidden=True)
	async def unload(self, ctx, *, module):
		"""Unloads a module."""
		try:
			self.bot.unload_extension(module)
		except Exception as e:
			#await ctx.send(f'```py\n{traceback.format_exc()}\n```')
			await ctx.send(embed=make_embed(author_url=["Exception", "", config.WARN], fields=[[f"{e}", "\u200b"]], color=config.EMBED_WARN))
		else:
			#await ctx.send('\N{OK HAND SIGN}')
			await ctx.send(embed=make_embed(author_url=["Unloaded Module", "", config.UNLOADED], fields=[[f"- {module}", "\u200b"]], color=config.EMBED_ERROR))
			
	#@commands.command(name='reload', hidden=True)
	#async def _reload(self, ctx, *, module):
	#    """Reloads a module."""
	#    try:
	#        self.bot.unload_extension(module)
	#        self.bot.load_extension(module)
	#    except Exception as e:
	#        await ctx.send(f'```py\n{traceback.format_exc()}\n```')
	#    else:
	#        await ctx.send('\N{OK HAND SIGN}')
	
	@commands.command(aliases=["r"])
	async def reload(self, ctx, *, extensions: str = "*"):
		"""Reload an extension.
		
		Use `reload *` to reload all extensions.
		
		This command is automatically run by `update`.
		"""
		await self.reload_(ctx, *extensions.split())
	
		
	#make_embed(*, author_url=None, fields=[], footer_text=None, thumbnail_url=None, **kwargs):	
	async def reload_(self, ctx, *extensions):
		if "*" in extensions:
			title = "Reloading all extensions"
		elif len(extensions) > 1:
			title = "Reloading extensions"
		else:
			title = f"Reloading {extensions[0]}"

		embed = make_embed(author_url=[title, "", config.THUMBNAIL], color=config.EMBED_INFO) #, title=title
		m = await ctx.send(embed=embed)
		color = config.EMBED_SUCCESS
		fields = [[f"", '\u200b']]
		if "*" in extensions:
			extensions = list(self.bot.extensions.keys())
		for extension in extensions:
			self.bot.unload_extension(extension)
			try:
				self.bot.load_extension(extension)
				#fields.append([f"+ {extension}", '\u200b'])
				fields[0][0] += f"+ {extension}\n"
			except:
				color = config.EMBED_ERROR
				#fields.append([f"- {extension}", '\u200b'])
				fields[0][0] += f"- {extension}\n"
		#description += "Done."
		await m.edit(embed=make_embed(author_url=[title.replace("ing", "ed"), "", config.THUMBNAIL], fields=fields, color=color)) #title=title.replace("ing", "ed")
		
	@commands.command()
	@commands.is_owner()
	async def shutdown(self, ctx):
		await ctx.bot.logout()
		await ctx.bot.close()
	
	@commands.command()
	async def restart_bot(self, ctx):
		m = await ctx.send(embed=make_embed(title="Restarting...", color=0xff00ff))
		
		msg_id = m.id
		msg_channel_id = m.channel.id
		msg_guild_id = m.guild.id
		print(m)
		print(m.id)
		print(m.channel.id)
		print(m.guild.id)
		#print(await self.bot.get_guild(msg_guild_id).get_channel(msg_channel_id).fetch_message(msg_id).edit("this"))
#		channel = self.bot.get_guild(msg_guild_id).get_channel(msg_channel_id)
		#channel = guild.get_channel(msg_channel_id)
#		msg = await channel.fetch_message(msg_id)
#		await msg.edit(embed=make_embed(title="Restarted.", color=0xff00ff))
		with open('restart.dat', 'w+') as f:
			f.write(f"True\n{m.guild.id}\n{m.channel.id}\n{m.id}")
			#f.write('\n')
			#f.write(str(m))
			#pickle.dump(m, f, -1)
		#await ctx.send("Hi!")
		await self.bot.logout()
		await self.bot.close()
		
def setup(bot):
	bot.add_cog(Managment(bot))


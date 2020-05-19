import discord
from discord.ext import commands
from utils import make_embed
import pickle
#bot = commands.Bot(command_prefix=".!")

from discord.ext.commands import has_permissions, MissingPermissions

class General(commands.Cog):
	"""General Commands"""

	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_ready(self):
		try:
			with open('restart.dat', 'r') as f:
				#did_restart = pickle.load(f)
				did_restart = f.read().split('\n')
				print(did_restart)
			if did_restart[0] == 'True':
				guild = self.bot.get_guild(int(did_restart[1]))
				channel = guild.get_channel(int(did_restart[2]))
				msg = await channel.fetch_message(int(did_restart[3]))
				await msg.edit(embed=make_embed(title="Restarted.", color=0x00ff00))
				print(did_restart)
				with open('restart.dat', 'w') as f:
					f.write('False')
		except FileNotFoundError:
			print('Did not restart.')
		print('Ready!')
		print('Logged in as ---->', self.bot.user)
		print('ID:', self.bot.user.id)
		print(self.bot.extensions)
		
#	@commands.Cog.listener()
#	async def on_message(self, message):
#		print(message)
#	
#	
#	@bot.command(name="kick", pass_context=True)
#	@has_permissions(manage_roles=True, ban_members=True, )
#	async def _kick(ctx, member: Member):
#		await bot.kick(member)
#
#	@_kick.error
#	async def kick_error(error, ctx):
#		if isinstance(error, MissingPermissions):
#			text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
#			await bot.send_message(ctx.message.channel, text)
#	
#	@commands.command()
#	async def hello(self, ctx):
#		"""Prints "Hello World!" """
#		#return await self.bot.say("Hello World!")
#		return await ctx.send("Hello World!")
#	
#	@commands.command(name='repeat', aliases=['copy', 'mimic'])
#	async def do_repeat(self, ctx, *, our_input: str):
#		await ctx.send(our_input)
#	

#
#	@commands.command(pass_context=True)
#	async def announce(self, ctx, text = None, servChan : discord.TextChannel = None):
#		text = "```" + text + "```"
#		if servChan == None:
#			server = ctx.message.guild
#			for i in server.channels:
#				if i.type==discord.ChannelType.text:
#					#print(i) #Debug
#					#await self.bot.send_message(i, text)
#					await i.send(text)
#		else:
#			if servChan.type==discord.ChannelType.text:
#				#await self.bot.send_message(servChan, text)
#				await servChan.send(text)

def setup(bot):
	bot.add_cog(General(bot))

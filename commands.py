import discord
from discord.ext import commands
import utils
from utils import make_embed
#import config


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        #self.channel = self.bot.get_channel(config.channel)
        await self.bot.say('''```css\n+ \N{WHITE HEAVY CHECK MARK} cogs.commands```''')

    #@commands.command(aliases=["p"])
    #async def ping(self, ctx):
    #    await self.channel.send('📢 Pong! {0}ms'.format(round(self.bot.latency*1000)))

    #@commands.command(hidden=True)
    #async def load(self, ctx, *, module):
    #    """Loads a module."""
    #    try:
    #        self.bot.load_extension(module)
    #    except Exception as e:
    #        await ctx.send('```py\n{traceback.format_exc()}\n```')
    #    else:
    #        await ctx.send('\N{OK HAND SIGN}')

    #@commands.command(hidden=True)
    #async def unload(self, ctx, *, module):
    #    """Unloads a module."""
    #    try:
    #        self.bot.unload_extension(module)
    #    except Exception as e:
    #        await ctx.send(f'```py\n{traceback.format_exc()}\n```')
    #    else:
    #        await ctx.send('\N{OK HAND SIGN}')

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
   
    """@commands.command(aliases=["r"])
    async def reload(self, ctx, *, extensions: str = "*"):
        Reload an extension.

        Use `reload *` to reload all extensions.

        This command is automatically run by `update`.
        
        await self.reload_(ctx, *extensions.split())

    async def reload_(self, ctx, *extensions):
        if "*" in extensions:
            title = "Reloading all extensions"
        elif len(extensions) > 1:
            title = "Reloading extensions"
        else:
            title = f"Reloading `{extensions[0]}`"
        embed = make_embed(color=utils.EMBED_INFO, title=title)
        m = await ctx.send(embed=embed)
        color = utils.EMBED_SUCCESS
        description = ""
        if "*" in extensions:
            #extensions = get_extensions()
            #extensions = startup_extensions
            extensions = list(self.bot.extensions.keys())
        for extension in extensions:
            self.bot.unload_extension(extension)
            try:
                self.bot.load_extension(extension)
                description += f"Successfully loaded `{extension}`.\n"
            except:
                color = utils.EMBED_ERROR
                description += f"Failed to load `{extension}`.\n"
                _, exc, _ = sys.exc_info()
                if not isinstance(exc, ImportError):
                    await report_error(ctx, exc, *extensions)
        description += "Done."
        await m.edit(
            embed=make_embed(
                color=color, title=title.replace("ing", "ed"), description=description
            )
        )
"""

def setup(bot):
	bot.add_cog(Commands(bot))

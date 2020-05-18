import discord




#import os
#print(os.environ['HOME'])
#from os import environ
#print(environ['HOME'])

def make_embed(*, author_url=None, fields=[], footer_text=None, thumbnail_url=None, **kwargs):
	# TODO Add docstring
	embed = discord.Embed(**kwargs)
	for field in fields:
		if len(field) > 2:
			embed.add_field(name=field[0], value=field[1], inline=field[2])
		else:
			embed.add_field(name=str(field[0]), value=str(field[1]), inline=False)
	if footer_text:
		embed.set_footer(text=footer_text)
	if thumbnail_url:
		embed.set_thumbnail(url=thumbnail_url)
	if author_url:
		embed.set_author(name=author_url[0], url=author_url[1], icon_url=author_url[2])
	return embed

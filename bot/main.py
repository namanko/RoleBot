import discord
from discord.ext import commands,tasks

bot = commands.Bot(command_prefix="%", case_insensitive=True)


role_ranks={
	'Reincarnation Slime':3,
	'Pikachu':5,
	'Cheesecake lover':10,
	'GME Stonk Millionaire':15
}


@bot.event
async def on_ready():
	global role_list
	print('Logged in as: '+"Rolebot")
	print('Bot ID: '+str(805657827392749569))
	await bot.change_presence(activity=discord.Game(name='?invites - list your invites'))
	print('------\n')
	for server in bot.guilds:
		role_list=dict((role.name,role) for role in server.roles)

@bot.event
async def on_member_join(ctx,*,new_member):
	invites= await message.guild.invites()
	for member in new_member.guild.members:
		if member.bot==False:
			uses=0
			prole=None
			for invite in invites:
				if invite.max_age==0 and invite.inviter==member:
					uses += invite.uses
			for role,used in role_ranks.items():
				if uses in used and role_list[role] not in member.roles:
					for mrole in member.roles:
						if mrole.name in role_ranks.keys():
							await bot.remove_roles(member,mrole)
					await ctx.send(member,"Congratulations  {}, you have been promoted to **{}**!".format(member.mention,role))
					await member.add_roles(role_list[role])

@bot.event
async def on_message(message):
	if message.content=='?invites':
		total_uses=0
		embed=discord.Embed(title='__Invites from {}__'.format(message.author.name))
		for invite in await message.guild.invites():
			if invite.inviter == message.author and invite.max_age==0:
				total_uses += invite.uses
				embed.add_field(name='Invite',value=invite.id)
				embed.add_field(name='Uses',value=invite.uses)
				embed.add_field(name='Expires',value='Never')
		embed.add_field(name='__Total Uses__',value=total_uses)
		await message.channel.send(message.channel,embed=embed)


bot.run('ODA1NjU3ODI3MzkyNzQ5NTY5.YBeFUg.u0BE5a606rp7gQugZk-IZ3-t82E')

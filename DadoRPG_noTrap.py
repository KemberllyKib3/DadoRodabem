import discord
from discord.ext import commands, tasks
import random

with open('token.txt') as file:
    token = file.readline()

client = commands.Bot(command_prefix='?')

channels = ['rolar-dados']
status = ['RPG', 'Dados', 'Paciência Spider', 'League of Legends', 'Destiny 2', 'Minecraft', 'Dungeons & Dragons','Campo Minado']
 
@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(random.choice(status)))
    await clear(client)

@client.event
async def on_ready():
    change_status.start()
    print(f"""\n>>> Tá Onn <<<\n""")

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"""Seja bem-vindo, {member.mention}, você está no servidor "{guild.name}".""")

@client.event
async def on_command_error(ctx, error):
    if (commands.CommandNotFound):
        await ctx.send("Este comando não existe.")

def rightChannel(message):
    if str(message.channel) in channels:
        return False
    else:
        return True

def exagero(num, lim=10):
    num = int(num)
    if ((num>lim) or (num<0)):
        return True
    else:
        return False

def rolardados(B, E, HM=1): # (Begin, End, HowMany)
    t = 1
    rolagem = []
    while t <= HM:
        t += 1
        rolagem.append(int(random.randint(B, E)))
    total = sum(rolagem)
    return rolagem, total

@client.command()
async def hello(ctx):
    await ctx.send(f"""Olá, {ctx.author.mention}.\nEstou a sua disposição.""")

@client.command()
async def d20(ctx, mod=0, times=1):
    t = int(times)

    if exagero(t):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    if (times == 1):
        chute, total = rolardados(1, 20, times)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 

    else:
        chute, total = rolardados(1, 20, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total)) 
            

@client.command()
async def d12(ctx, times=1):
    t = int(times)

    if exagero(t,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    if (times == 1):
        chute, total = rolardados(1, 12, times)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 

    else:
        chute, total = rolardados(1, 12, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total))

@client.command()
async def d10(ctx, times=1):
    t = int(times)

    if exagero(t,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    if (times == 1):
        chute, total = rolardados(1, 10, times)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 

    else:
        chute, total = rolardados(1, 10, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total))

@client.command()
async def d8(ctx, times=1):
    t = int(times)

    if exagero(t,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    if (times == 1):
        chute, total = rolardados(1, 8, times)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 

    else:
        chute, total = rolardados(1, 8, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total))

@client.command()
async def d6(ctx, times=1):
    t = int(times)

    if exagero(t,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    if (times == 1):
        chute, total = rolardados(1, 6, times)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 

    else:
        chute, total = rolardados(1, 6, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total))

@client.command()
async def d4(ctx, times=1):
    t = int(times)

    if exagero(t, 15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    if (times == 1):
        chute, total = rolardados(1, 4, times)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 

    else:
        chute, total = rolardados(1, 4, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total))
    
@client.command()
async def d100(ctx):

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    chute = rolardados(1, 100)
    await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute))

    
N = []

@client.command()
async def iniciativa(ctx, n1="",n2="",n3="",n4="",n5="",n6="",n7="",n8="",n9=""):
    global N
    nomes = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
    nomes.remove("")
    N = [x for x in nomes if x]
    
    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    await ctx.send(f"""Ordem de combate: {N}""")

@client.command()
async def ordem(ctx):
    global N
    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    await ctx.send(f"""Ordem de combate: {N}""")

@client.command()
async def clear(ctx):

    def isnt_me(m):
        return m.author != client.user
    def is_me(m):
        return m.author == client.user
    
    deleted = await ctx.channel.purge(check=isnt_me)
    deletedbot = await ctx.channel.purge(check=is_me)
    await ctx.channel.send('Deleted {} message(s)'.format(int(len(deletedbot))+int(len(deleted))))

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Dado Rodabem", description="Sou irmão do Dado Rodabella. Minha lista de comandos são:", color=0x0326899)
    
    embed.add_field(name="?d4 *vezes*", value="Rolar um d4 multiplicado." )
    embed.add_field(name="?d6 *vezes*", value="Rolar um d6 multiplicado." )
    embed.add_field(name="?d8 *vezes*", value="Rolar um d8 multiplicado." )
    embed.add_field(name="?d10 *vezes*", value="Rolar um d10 multiplicado." )
    embed.add_field(name="?d12 *vezes*", value="Rolar um d12 multiplicado." )
    embed.add_field(name="?d100 *sorte*", value="Rolar um d100." )
    embed.add_field(name="?d20 *mod* *vezes*", value="Rolar um d20 com mod(opcional) multiplicado." )
    embed.add_field(name="?iniciativa *nome nome*", value="Declarar ordem de combate." )
    embed.add_field(name="?ordem", value="Mostrar ordem de combate" )
    embed.add_field(name="?help", value="Gera isso aqui que você tá lendo.", inline=True)
    await ctx.send(content=None, embed=embed)


client.run(token)

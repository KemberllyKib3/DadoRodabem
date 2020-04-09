import discord
from discord.ext import commands, tasks
import random

with open('token.txt') as file:
    token = file.readline()

client = commands.Bot(command_prefix='?')

channels = ['rolar-dados']
permitido = ["KemberllyKib3#5922"]
<<<<<<< HEAD

adv = 0


async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="RPG de Mesa", type=discord.ActivityType.playing))
    

@client.event
async def on_ready():
    print(f"""\n>>> Tá Onn <<<\n""")
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="RPG de Mesa", type=discord.ActivityType.playing))
=======
status = ['RPG', 'Dados', 'Paciência Spider', 'League of Legends', 'Destiny 2', 'Minecraft', 'Dungeons & Dragons','Campo Minado']
adv = 0
 
@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(random.choice(status)))
    await clear(client)

@client.event
async def on_ready():
    change_status.start()
    print(f"""\n>>> Tá Onn <<<\n""")
    #await client.change_presence(status=discord.Status.idle, activity=discord.Game('Campo Minado'))
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"""Seja bem-vindo, {member.mention}, você está no servidor "{guild.name}".""")

@client.event
async def on_command_error(ctx, error):
    if (commands.CommandNotFound):
        await ctx.send("Este comando não existe.")
<<<<<<< HEAD
    if(commands.CommandError):
        await ctx.send("Você deve ter escrito algo.")

def formatar(texto):
    resp = []
    for text in texto:
        text = str(text)
        text = text.replace(", ", "+")
        resp.append(text)
        resp = list(resp)

    return ('+'.join(resp))

def rolagem(msg, adv=1):
    msg = str(msg)

    msg = msg.replace(" ", "")
    msg = msg.lower()

    sep = msg.split('+')
    resultado = []
    rolldices = []
    rollint = []

    for word in sep:
        if not (word.isdigit()):
            sep1 = word.split('d')
            rolag, tot = rolardados(1, int(sep1[1]), int(sep1[0]), adv)
            resultado.append(tot)
            rolldices.append(rolag)
        else:
            resultado.append(int(word))
            rollint.append(int(word))

    return formatar(rolldices+rollint), sum(resultado)
=======
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

def rightChannel(message):
    if str(message.channel) in channels:
        return False
    else:
        return True

<<<<<<< HEAD
def becomenotdiv3():
    global adv
    if div3(adv):
        adv += 1
    else:
        return True

def becomediv3():
    global adv
    if div3(adv):
        return True
    else:
        adv += 1
        becomediv3()

def div3(num):
    num = str(num)
    if (sum(map(int, num)))%3 == 0:
        return True
    else:
        return False

def rolardados(B, E, HM=1, advan=1): # (Begin, End, HowMany, Vantagem)
    t = 1
    rolagem = []

    if (E==100) and div3(advan):
        if advan == 999:
            rolagem.append(int(random.randint(85, 100)))
            B=E/2
            while t <= HM-1:
                t += 1
                rolagem.append(int(random.randint(B, E)))
            total = sum(rolagem)
            return rolagem, total
        if advan == 888:
            rolagem.append(int(random.randint(1, 30)))
            B=E/2
            while t <= HM-1:
                t += 1
                rolagem.append(int(random.randint(B, E)))
            total = sum(rolagem)
            return rolagem, total
        else:
            B=E/2
            while t <= HM:
                t += 1
                rolagem.append(int(random.randint(B, E)))
            total = sum(rolagem)
            return rolagem, total

    if (E==20) and div3(advan):
        if advan == 999:
            rolagem.append(20)
            B=E/2
            while t <= HM-1:
                t += 1
                rolagem.append(int(random.randint(B, E)))
            total = sum(rolagem)
            return rolagem, total
        if advan == 888:
            rolagem.append(1)
            B=E/2
            while t <= HM-1:
                t += 1
                rolagem.append(int(random.randint(B, E)))
            total = sum(rolagem)
            return rolagem, total
        else:
            B=E/2
            while t <= HM:
                t += 1
                rolagem.append(int(random.randint(B, E)))
            total = sum(rolagem)
            return rolagem, total

    
    else:
        while t <= HM:
            t += 1
            rolagem.append(int(random.randint(B, E)))
        total = sum(rolagem)
        return rolagem, total
=======
def becomeImpar():
    global adv
    if adv % 2 == 0:
        adv += 1
        return True
    else:
        return True

def becomePar():
    global adv
    if adv % 2 != 0:
        adv += 1
        return True
    else:
        return True

def rolardados(B, E, HM=1): # (Begin, End, HowMany)
    t = 1
    rolagem = []
    while t <= HM:
        t += 1
        rolagem.append(int(random.randint(B, E)))
    total = sum(rolagem)
    return rolagem, total

def exagero(num, lim=10):
    num = int(num)
    if ((num>lim) or (num<0)):
        return True
    else:
        return False
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

def allowed(msg):
    if str(msg.author) in permitido:
        return True
    else: 
        return False

@client.command()
async def hello(ctx):
    await ctx.send(f"""Olá, {ctx.author.mention}.\nEstou a sua disposição.""")

@client.command()
<<<<<<< HEAD
async def sorte(ctx, sorte=1):

    global adv
    
    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return
    
    dado = rolardados(1, 100, advan=adv)
    
    if sorte == 2:
        sorte = 1.07
    if sorte == 3:
        sorte = 1.15

    if sorte > 3 or sorte < 1:
        sorte = 1

    final = round((dado[1]*sorte), 2)

    if final > 100:
        final = 100

    adv += 1

    await ctx.send(f"A sorte de {ctx.author.mention} foi: {final}%")
    

@client.command()
async def d(ctx, msg):

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return
    
    global adv

    roll, total = rolagem(msg, adv=adv)

    await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, roll, total))
    adv+=1

#region Dados soltos

@client.command()
async def d20(ctx, times=1):
=======
async def d20(ctx, mod=0, times=1):

    if exagero(times):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    global adv

    if (times == 1):
<<<<<<< HEAD
        chute, total = rolardados(1, 20, advan=adv)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 
        adv+=1

    else:
        chute, total = rolardados(1, 20, times, advan=adv)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total))
        adv+=1
=======
   
        if (adv % 2 == 0):
            adv += 1
            chute, total = rolardados(10, 20, times)
            await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute))         
            
        elif(adv % 2 != 0):
            adv += 1
            chute, total = rolardados(1, 20, times)
            await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 

    else:
        chute, total = rolardados(1, 20, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total)) 
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

@client.command()
async def d12(ctx, times=1):

<<<<<<< HEAD
=======
    if exagero(times,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
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

<<<<<<< HEAD
=======
    if exagero(times,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
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

<<<<<<< HEAD
=======
    if exagero(times,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

    if (times == 1):
        chute, total = rolardados(1, 8, times)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute)) 
    else:
        chute, total = rolardados(1, 8, times)
        await ctx.send("{} sua rolagem resultou {} e o somatório: {}".format(ctx.author.mention, chute, total))

<<<<<<< HEAD
@client.command()
async def d6(ctx, times=1):

=======

@client.command()
async def d6(ctx, times=1):

    if exagero(times,15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
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

<<<<<<< HEAD
=======
    if exagero(times, 15):
        await ctx.send(f"""{ctx.author.mention}, peço que repense essa quantidade de repetições, obrigado!""")
        return

>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
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
<<<<<<< HEAD
async def d100(ctx):
=======
async def d100(ctx, sorte=1):
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal "{channels[0]}", obrigado!""")
        return

    global adv
<<<<<<< HEAD
    chute = rolardados(1, 100, advan=adv)
    await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute[0]))
    adv+=1
#endregion
    

@client.command()
async def ultratrap(ctx):
    if allowed(ctx):
        global adv
        adv = 999
        await ctx.send("Este comando não existe!")
    else:
        await ctx.send("Este comando não existe.")
    return

@client.command()
async def ultradetrap(ctx):
    if allowed(ctx):
        global adv
        adv = 888
        await ctx.send("Este comando nem existe!")
    else:
        await ctx.send("Este comando não existe.")
    return

@client.command()
async def trap(ctx):
    if allowed(ctx):
        becomediv3()
        await ctx.send("Este comando não existe!")
    else:
        await ctx.send("Este comando não existe.")
    return

@client.command()
async def detrap(ctx):
    if allowed(ctx):
        becomenotdiv3()
        await ctx.send("Este comando nem existe.")
    else:
        await ctx.send("Este comando não existe.")
    return
    
=======
    
    if (adv % 2 == 0):
        adv += 1
        chute = rolardados(50, 100)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute))         
        
    elif(adv % 2 != 0):
        adv += 1
        chute = rolardados(1, 100)
        await ctx.send("{} sua rolagem resultou {}".format(ctx.author.mention, chute))

@client.command()
async def trap(ctx):
    global adv
    if allowed(ctx):
        becomePar()
        await ctx.send("Tudo certo, boa sorte!")
    else:
        await ctx.send(f"""ERROR: 2458762xe53\nFunction Unavailable, try again later!""")
        return

@client.command()
async def detrap(ctx):
    global adv
    if allowed(ctx):
        becomeImpar()
        await ctx.send("Armadilha montada, boa sorte!")
    else:
        await ctx.send(f"""ERROR: 2458762xe53\nFunction Unavailable, try again later!""")
        return
    
N = []
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

@client.command()
async def valor(ctx):
    global adv
<<<<<<< HEAD
    await ctx.send(adv)

#region iniciativa e ordem

N = []
@client.command()
async def iniciativa(ctx, n1="",n2="",n3="",n4="",n5="",n6="",n7="",n8="",n9="",n10="",n11="",n12="",n13="",n14="",n15="",n16="",n17=""):
    global N
    nomes = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17]
=======
    await ctx.send(f"""{adv}""")

#import numpy as np

@client.command()
async def iniciativa(ctx, n1="",n2="",n3="",n4="",n5="",n6="",n7="",n8="",n9=""):
    global N
    nomes = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
    nomes.remove("")
    N = [x for x in nomes if x]

    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return
<<<<<<< HEAD
    
    with open("iniciativa.txt", "w+") as inic:
        #inic.writelines(N)
        inic.write("** ~ **".join(N))
        
    personagens = "** ~ **".join(N)

    await ctx.send(f"""Ordem de combate: **{personagens}** """)
=======

    await ctx.send(f"""Ordem de combate: {N}""")
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

@client.command()
async def ordem(ctx):
    global N
    if rightChannel(ctx):
        await ctx.send(f"""{ctx.author.mention}, peço que reenvie este comando no canal {channels[0]}, obrigado!""")
        return

<<<<<<< HEAD
    with open("iniciativa.txt", "r") as inic:
        personagens = inic.readline()
        personagensformatado = personagens.split("** ~ **")

    await ctx.send(f"""Ordem de combate: **{"** ~ **".join(personagensformatado)}** """)
#endregion iniciativa e ordem
=======
    await ctx.send(f"""Ordem de combate: {N}""")
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e

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
    embed = discord.Embed(title="Dado Rodabem", description="Sou um rolador de dados. Minha lista de comandos são:", color=0x0326899)
    
<<<<<<< HEAD
    embed.add_field(name="?d xd20+y", value="Rolar dados juntos e somar." )
=======
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
    embed.add_field(name="?d4 *vezes*", value="Rolar um d4 multiplicado." )
    embed.add_field(name="?d6 *vezes*", value="Rolar um d6 multiplicado." )
    embed.add_field(name="?d8 *vezes*", value="Rolar um d8 multiplicado." )
    embed.add_field(name="?d10 *vezes*", value="Rolar um d10 multiplicado." )
    embed.add_field(name="?d12 *vezes*", value="Rolar um d12 multiplicado." )
    embed.add_field(name="?d100 *sorte*", value="Rolar um d100." )
<<<<<<< HEAD
    embed.add_field(name="?d20 *vezes*", value="Rolar um d20 multiplicado." )
    embed.add_field(name="?iniciativa *nome nome ...*", value="Declarar ordem de combate." )
=======
    embed.add_field(name="?d20 *mod* *vezes*", value="Rolar um d20 com mod(opcional) multiplicado." )
    embed.add_field(name="?iniciativa *nome nome*", value="Declarar ordem de combate." )
>>>>>>> c2a4de05084f8c44c5edf1e99a32f0d902f4178e
    embed.add_field(name="?ordem", value="Mostrar ordem de combate" )
    embed.add_field(name="?help", value="Gera isso aqui que você tá lendo.", inline=True)
    await ctx.send(content=None, embed=embed)


client.run(token)

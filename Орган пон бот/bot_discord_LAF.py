import requests
import os
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot, has_permissions, MissingPermissions
#from discord_slash import SlashCommand
#from discord_slash.utils.manage_commands import create_option
from discord import Activity, ActivityType
import random
from datetime import datetime, date, time, timedelta
from Pon_db import db
import re
import time
import random
import asyncio
import psutil

prefix = ".", "!"
Bot = commands.Bot(command_prefix=prefix, intents = discord.Intents.all())
#slash = SlashCommand(Bot, sync_commands = True)


@Bot.command()
async def ping(ctx):
     CPU = psutil.cpu_percent()
     mem = psutil.virtual_memory()
     percentmem = int(mem.percent)
     idk = psutil.boot_time()
     embed=discord.Embed(title="загруженность бота", color=0x0400ff)
     embed.add_field(name="CPU", value=f"{CPU}%", inline=False)
     embed.add_field(name="memory", value=f"{percentmem}%", inline=False)
     embed.add_field(name="idk", value=f"<t:{round(idk)}:R>", inline=False)
     embed.add_field(name="ping", value=f"{round(Bot.latency * 1000)}ms", inline=False)
     await ctx.send(embed=embed)

@Bot.command()
async def v(ctx, *, Nagatoro:int):
    for i in range(Nagatoro):
        await ctx.send(i+1)

@Bot.command()
async def m(ctx, idk,* lolxd):
    idk = idk.lower().replace('https://discord.com/channels/', '')
    ls = []
    ls = idk.split('/')
    guild = await Bot.fetch_guild(ls[0])
    channel = await Bot.fetch_channel(ls[1])
    mes = int(ls[2])
    message = await channel.fetch_message(mes)
    author = ctx.message.author.id
    embed = discord.Embed(color = 233421, type='rich', description =f'{message.content}\n\n[сообщение]({message.jump_url})', timestamp=message.created_at)
    embed.set_author(name=f'Сообщение от {message.author} ({message.author.id})', icon_url=message.author.avatar)
    embed.set_footer(text=guild.name, icon_url=guild.icon)
    await ctx.send(f'<@{author}>', embed = embed)

@Bot.command()
@commands.has_any_role(1076124376879079475, 1022787786614509661, 1070233324909502484, 1022732409373990994, 1056598029710413884, 1067094092812660836, 1027112230082334722, 1068939649600458946, 1068939649600458945, 1068939649646604352, 1068939649571110939, 1068939649571110936)
async def say(ctx, *,arg):
    await ctx.message.channel.purge(limit=1)
    author = ctx.message.author
    embed = discord.Embed(color = 99999, type='rich', description =f'{arg}')
    embed.set_author(name=f'{author} ({author.id})', icon_url=author.avatar)
    await ctx.send(embed=embed)
    
@Bot.command()
@commands.has_permissions(administrator=True)
async def saybebra(ctx):
    await ctx.message.channel.purge(limit=1)
    await ctx.send(embed = discord.Embed(color = 112280, title = 'Правила HR', type='rich',  description =f'```md\nЗа нарушение ниже указанных правил вам будет сделан строгий выговор или даже увольнение.\n\n#HR1: Вы должны быть адекватным и грамотно излагать свои мысли\n#HR2: Быть инициативным\n#HR3: Не унижать никого из людей и админов из "ДРИРЛ"\n#HR4: Не абузить свои права\n#HR5: При принятии человека на роль админа или другую роль, вы должны заносить его в таблицу\n#HR6: Желательно не иметь конфликтов с  ГА\n#HR7: Оффтоп запрещён\n#HR8: Обман высшего звена администрации запрещён```\n[Таблица Администрации](https://docs.google.com/spreadsheets/d/172HU4cdrdKkiIgCssXl-JJ0MjyjupVBNpxoBZ-iTQyU/edit#gid=0)\n\n© ДГИРЛ 2023. Все права нихера не защищены.\n\n<@{author}> ({author}) ©'))
 
@Bot.command()
@commands.has_permissions(administrator=True)
async def delms(ctx, c:int):
    await ctx.message.channel.purge(limit=c)
    channel = await Bot.fetch_channel(1072880578879307786)
    author = ctx.message.author
    embed = discord.Embed(color = 321, type='rich', description =f'<@{author.id}> Очистил {c} сообщений в канале <#{ctx.message.channel.id}> ({ctx.message.channel.id})', timestamp=ctx.message.created_at)
    embed.set_author(name=f'{author} ({author.id})', icon_url=author.avatar)
    await channel.send(embed=embed)
 
@Bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, User:discord.Member):
    author = ctx.message.author.id
    userid = User.id
    await ctx.send(f'<@{author}>, <@{userid}> ({userid}) был забанен!')
 
 
@Bot.command()
@commands.has_permissions(administrator=True)
async def sayaboba(ctx):
    author = ctx.message.author.id
    await ctx.message.channel.purge(limit=1)
    await ctx.send(embed = discord.Embed(color = 0o00777723, title = 'Правила Администрации', type='rich',  description =f'```cs\n#Ниже показан список требований для должностей:\n\nСтажёр(сдать правила)---->Администратор(админ правила)--->Куратор(путем доверия) --->Human Resource(сдать правила HR) --->Главная Администрация(путем доверия)--->Глава "ДГИРЛ"(путем доверия)\n```\n```yaml\n#Правила:\nR1-Зпрещено распространять информацию из закрытых текстовых и голосовых каналов.\nR2-Запрещено крысить других администраторов.\nИсключение: если администратор сильно нарушал.\nR3-Запрещено оскорблять других участников серверов.\nR4-Запрещено невыполнение своих обязанностей.\nR5-Запрещено использование своих возможностей в корыстных целях.\nR6-Запрещён обман Администрации, и тех, кто выше в должности\n\n#Правила поведения в тикетах:\nL1-Вы обязаны вежливо поздороваться.\nПример: Доброго времени суток.\nL2-Если человек не отвечает на ваш вопрос (сутки) вы должны закрыть тикет попрощавшись.\nL3-Запрещено отвечать на тикет не по своей теме.\n\nP.s. За нарушение правила R2 вы будете забанены.```\nПравила будут дополнятся.\n\n[Таблица Администрации](https://docs.google.com/spreadsheets/d/172HU4cdrdKkiIgCssXl-JJ0MjyjupVBNpxoBZ-iTQyU/edit#gid=0)\n\n© ДГИРЛ 2023. Все права нихера не защищены.\n\n<@{author}> ({author}) ©'))
 

#@slash.slash(name = 'role', description = 'Я хз че писать', options = [{"name": "role", "description": "Роль", "type": 8, "required" : True}], guild_ids = [1068939649470435449])
@Bot.command()
async def r(ctx, *, role: discord.Role):
    arg = '\n'.join([f'<@{member.id}> ({member.id})\n' for member in role.members])
    await ctx.send(embed = discord.Embed(color = 0o77777777, title = f'Cписок тех, у кого есть роль {role}', type='rich', description = f'\n\n\n{arg}'))


@Bot.command()
async def report(ctx, User:discord.Member, *, arg):
    author = ctx.message.author.id
    user = User.id
    url = ctx.message.jump_url
    await ctx.message.channel.purge(limit=1)
    await ctx.send(f'<@{author}>, Жалоба отправлена!')
    channel = await Bot.fetch_channel(1075731632704716851)
    message = await channel.send('<@&1068939649571110939>', embed = discord.Embed(color = 199991, title = 'Жалоба', type='rich', description = f'<@{author}> ({author}) жалуется на <@{user}> ({user})\n\n**Причина:** {arg}\n\n[Сообщение]({url})'))
    await message.add_reaction('🟢')
    await message.add_reaction('⏰')
    await message.add_reaction('🔴')


#@slash.slash(name = 'vote', description = 'Создаёт голосование под указанным сообщением', options = [{"name": "arg", "description": "ID сообщения", "type": 3, "required" : False}], guild_ids = [1068939649470435449])
@Bot.command()
async def vote(ctx, *, arg=None):
    await ctx.message.channel.purge(limit=1)
    message = await ctx.fetch_message(arg)
    await message.add_reaction('🟢')
    await message.add_reaction('⏰')
    await message.add_reaction('🔴')

@Bot.command()
@commands.has_any_role(1076124376879079475, 1022732409373990994, 1070233324909502484, 1068939649600458946, 1068939649646604352)
async def rise(ctx, user:discord.Member, role: discord.Role, *, delrole: discord.Role=None):
    author = ctx.message.author.id
    await ctx.message.channel.purge(limit=1)
    await user.add_roles(role)
    if not delrole == None:
        await user.remove_roles(delrole)
    channel = await Bot.fetch_channel(1068939649646604357)
    await channel.send(f'<@{user.id}> Был повышен до `{role}` членом Главной Администрации <@{author}>')
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 123456, title = 'Повышение', type='rich', description = f'<@{author}> Повысил <@{user.id}>\n\n**Информация:**\n<@{user.id}> был повышен до: `{role}`\nРоль которую забрали: `{delrole}`'))
    
    
@Bot.command()
@commands.has_any_role(1076124376879079475, 1022732409373990994, 1070233324909502484, 1068939649600458946, 1068939649646604352)
async def lower(ctx, user:discord.Member, role: discord.Role, *, delrole: discord.Role=None):
    author = ctx.message.author.id
    await ctx.message.channel.purge(limit=1)
    await user.remove_roles(role)
    if not delrole == None:
        await user.add_roles(delrole)
    channel = await Bot.fetch_channel(1068939649646604357)
    userid = user.id
    await channel.send(f'<@{userid}> Был понижен с должности `{role}` до `{delrole}` членом Главной Администрации <@{author}>')
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 987654, title = 'Понижение', type='rich', description = f'<@{author}> Понизил <@{user.id}>\n\n**Информация:**\n<@{user.id}> был понижен \nс: `{role}`\nДо: `{delrole}`'))
    
@Bot.command()
@commands.has_any_role(1076124376879079475, 1022732409373990994, 1070233324909502484, 1068939649600458946, 1068939649646604352)
async def dismiss(ctx, user: discord.Member, role: discord.Role, *, reason=None):
    author = ctx.message.author.id
    role2 = discord.utils.get(user.guild.roles, name='Администрация🎁')
    role3 = discord.utils.get(user.guild.roles, name='Отдел кадров')
    role4 = discord.utils.get(user.guild.roles, name='Куратор')
    roleMemory = discord.utils.get(user.guild.roles, name='В отставке')
    await ctx.message.channel.purge(limit=1)
    await user.remove_roles(role, role2, role3, role4)
    await user.add_roles(roleMemory)
    channel = await Bot.fetch_channel(1068939649646604357)
    userid = user.id
    await channel.send(f'<@{userid}> Был уволен с должности `{role}` членом Главной Администрации <@{author}>. Причина: {reason}')
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 211993, title = 'Увольнение', type='rich', description = f'<@{author}> Уволил <@{userid}>\n\n**Информация:**\n<@{userid}> был Уволен с должности: `{role}`\nПричина: {reason}'))
    
@Bot.command()
@commands.has_any_role(1076124376879079475, 1067094092812660836, 1022732409373990994, 1070233324909502484, 1068939649600458946, 1068939649646604352, 1068939649600458945)
async def sobes(ctx, user:discord.Member):
    role = discord.utils.get(user.guild.roles, name="собеседование")
    if not role in user.roles:
        await user.add_roles(role)
        await ctx.channel.send(f'<@{user.id}> Была выдана роль `собеседование`')
    else:
        await user.remove_roles(role)
        await ctx.channel.send(f'Роль `собеседование` была снята с <@{user.id}>')
        
@Bot.command()
@commands.has_any_role(1076124376879079475, 1067094092812660836, 1022732409373990994, 1070233324909502484, 1068939649600458946, 1068939649600458945, 1068939649646604352)
async def hr(ctx, user:discord.Member):
    author = ctx.message.author
    rows = db.black.get_all()
    for row in rows:
        if row.user == user.id:
            await ctx.send(f'<@{author.id}>, <@{user.id}> ({user.id}) находится в ЧС, повнимательней!!!')
            return
    role = discord.utils.get(user.guild.roles, name='Стажёр')
    role2 = discord.utils.get(user.guild.roles, name="Администрация🎁")
    roleAdm = discord.utils.get(user.guild.roles, name="Отдел кадров")
    roleMemory = discord.utils.get(user.guild.roles, name='В отставке')
    authorid = author.id
    await ctx.message.channel.purge(limit=1)
    channel = await Bot.fetch_channel(1068939649646604357)
    userid = user.id
    await user.add_roles(role)
    await user.add_roles(role2)
    await user.remove_roles(roleMemory)
    if roleAdm in author.roles:
        await channel.send(f'<@{userid}> Был принят на должность `{role}` членом Отдела кадров <@{author.id}>')
    else:
        await channel.send(f'<@{userid}> Был принят на должность `{role}` членом Главной Администрации <@{author.id}>')
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 666666, title = 'Новый администратор', type='rich', description = f'<@{authorid}> Принял на стажировку <@{user.id}>'))

@Bot.command()
@commands.has_any_role(1076124376879079475, 1027112230082334722, 1056581187411390496, 1070233324909502484, 1022732409373990994, 1068939649600458946, 1068939649600458945, 1068939649646604352)
async def vacate(ctx, user:discord.Member, Duration:int=None, *, re=None):
    if Duration == None:
        Duration = 0
    author = ctx.message.author.id
    role = discord.utils.get(user.guild.roles, name="отпуск")
    delrole = discord.utils.get(user.guild.roles, name="Администрация🎁")
    dtnow = datetime.now()
    dt = datetime.now() + timedelta(days=Duration)
    stampdt = dt.timestamp()
    stampnow = dtnow.timestamp()
    await ctx.message.channel.purge(limit=1)
    if role in user.roles:
        await user.add_roles(delrole)
        await user.remove_roles(role)
        await ctx.channel.send(f'<@{author}>, Отпуск Администратора <@{user.id}> был прерван.')
        channel = await Bot.fetch_channel(1072880578879307786)
        await channel.send(embed = discord.Embed(color = 214365, title = 'Снял отпуск', type='rich', description = f'<@{author}> Снял отпуск администратору <@{user.id}>'))
    else:
        if Duration == 0:
            await ctx.channel.send(f'<@{author}> укажите срок отпуска!')
            return
        await user.add_roles(role)
        await user.remove_roles(delrole)
        await ctx.channel.send(f'<@{author}>, Администратор <@{user.id}> был отправлен в отпуск до <t:{round(stampdt)}:f>. По причине: {re}')
        channel = await Bot.fetch_channel(1072880578879307786)
        await channel.send(embed = discord.Embed(color = 896756, title = 'Выдал отпуск', type='rich', description = f'<@{author}> Выдал отпуск администратору <@{user.id}>\n\n**Информация:**\nПричина отпуска: {re}\nСрок окончания отпуска: <t:{round(stampdt)}:f>'))

@Bot.command()
@commands.has_permissions(administrator=True)
async def rolegv(ctx, user:discord.Member, *, role: discord.Role):
    if not role in user.roles:
        await user.add_roles(role)
        await ctx.channel.send(f'<@{user.id}> была выдана роль `{role}`')
    else:
        await user.remove_roles(role)
        await ctx.channel.send(f'`{role}` была снята с <@{user.id}>')
        
#Команда банов


'''
@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def ban(ctx, member: discord.Member, *, reason):
    channel = Bot.get_channel(789968921432031272)
    await member.ban(reason=reason)
    await ctx.channel.purge(limit=0)
    emb = discord.Embed(color=344462)
    emb.add_field(name='✅ Ban пользователя', value='Пользователь {} был забанен!'.format(member.mention))
    await channel.send(embed = emb)
'''

#@slash.slash(name = 'phelp', description = 'Выводит помощь по командам', guild_ids = [1068939649470435449])
@Bot.command()
async def phelp(ctx):
    await ctx.channel.send(embed = discord.Embed(color = 745232, title = 'Помощь по командам', type='rich', description = f'**Условные обозначения:**\n[] - обязательный аргумент.\n() - необязательный аргумент\n\n**Префиксы:**\nЕсть 2 префикса команд, 1 - это `!`, а 2 - `.`\n**Общие:**\n> .phelp - Выводит список всех команд\n> .vote [id сообщения] - добавляет рекции на сообщения для голосования\n**Варны:**\n> .mywarns - выводит все ваши активные варны\n> .allwarns - Выводит все активные варны\n> .warns [слап человека] - Выводит активные варны указанного человека\n**Команды <@&1068939649600458946>:**\n> .delwarn [id варна] - удаляет варн\n> .rise [id человека] [слап роли на которую нужно повысить] (слап роли которую нужно забрать) - Повышает человека и делает об этом объявление в <#1068939649646604357>\n> .lower [id человека] [слап роли которую нужно забрать] (слап роли которую нужно выдать) - Понижает человека и делает об этом объявление в <#1068939649646604357>\n> .dismiss [id человека] [слап роли которую нужно забрать] (причина) - Увольняет человека и делает об этом объявление в <#1068939649646604357>\n**Команды <@&1068939649600458945>:**\n> .vacate [слап человека] [продолжительно отпуска] (причина)\n> .warn [слап человека] [продолжительность] (причина) - Выдает варн человеку\n> .sobes [слап человека] - выдает/забирает человеку роль <@&1068939649571110934>\n> .hr [слап человека] - Принимает человека на <@&1068939649571110940>\n**Команды <@&1068939649571110939>:**\n> .say [сообщение] - Бот отправляет эмбед с вашим сообщением.'))

@tasks.loop(seconds=600)
async def warn_loop():
    rows = db.warns.get_all()
    dtnow = datetime.now()
    stampnow = dtnow.timestamp()
    stnow = round(stampnow)
    for row in rows:
        if row.Duration < stnow:
            channel = await Bot.fetch_channel(1072880578879307786)
            await channel.send(embed = discord.Embed(color = 983204, title = 'Окончание варна', type='rich', description = f'Варн #{row.id} окончился у администратора <@{row.User}>\n\n**Информация:**\nПричина варна: {row.Reason}\nКогда выдали: <t:{row.given}:f>\nКто выдал: <@{row.author}>'))
            db.warns.delete('id', row.id)
            
@tasks.loop(minutes=60)
async def black_loop():
    rows = db.black.get_all()
    dtnow = datetime.now()
    stampnow = dtnow.timestamp()
    stnow = round(stampnow)
    for row in rows:
        if not row.duration == 0:
            if row.duration < stnow:
                channel = await Bot.fetch_channel(1072880578879307786)
                await channel.send(embed = discord.Embed(color = 190000, title = 'Окончание ЧС', type='rich', description = f'ЧС <@{row.user}> ({row.user}) был окончен\n\n**Информация:**\nКто занёс: <@{row.author}>\nПричина: {row.reason}\nЗанесён: <t:{row.given}:F>'))
                db.black.delete('user', row.user)
                
@tasks.loop(seconds=30)
async def rainbow_role():
    guild = await Bot.fetch_guild(1068939649470435449)
    role = guild.get_role(1076123833511194744)
    b = random.randint(1,255)
    r = random.randint(1,255)
    g = random.randint(1,255)
    await role.edit(color=discord.Colour.from_rgb(r, g, b))

@tasks.loop(minutes=60)
async def black_chl():
    rows = db.black.get_all()
    arg = '\n'.join([f'<@{row.user}> ({row.user})\nЧС до: <t:{row.duration}:f>' for row in rows if not row.duration == 0])
    arg1 = '\n'.join([f'<@{row.user}> ({row.user})\nЧС: **бессрочно**' for row in rows if row.duration == 0])
    channel = await Bot.fetch_channel(1068939650095399141)
    await channel.purge(limit=150)
    await channel.send(embed = discord.Embed(color = 1999999, title = 'Чёрный Список', type='rich', description = f'{arg}'))
    await channel.send(embed = discord.Embed(color = 1999999, title = 'Бессрочный Чёрный Список', type='rich', description = f'{arg1}'))

@tasks.loop(minutes=30)
async def user_count():
    count = 0
    guild = await Bot.fetch_guild(1068939649470435449)
    async for member in guild.fetch_members():
        count += 1
    channel = await Bot.fetch_channel(1078631847296249926)
    await channel.edit(name=f'⟐🐱{guild.name}: {count}')

@tasks.loop(minutes=15)
async def tick_upd():
    guild = await Bot.fetch_guild(1068939649470435449)
    channel = await Bot.fetch_channel(1084367942365478913)
    await channel.purge(limit=1)
    #mes = await channel.fetch_message(1087713941825785916)
    embed = discord.Embed(color = discord.Colour(1203908), type='rich', title = 'Открыть тикет', description ='> С помощью кнопоки ниже вы сможете открыть премиум тикет')
    embed.set_footer(text=guild.name, icon_url=guild.icon)
    #await mes.edit(embed=embed, view=Buttons())
    await channel.send(embed=embed, view=Buttons())

@Bot.command()
@commands.has_any_role(1076124376879079475, 1027112230082334722, 1022732409373990994, 1068939649600458946, 1068939649600458945, 1068939649646604352)
async def badd(ctx, user:discord.Member, duration:int, *, reason=None):
    author = ctx.message.author.id
    await ctx.message.channel.purge(limit=1)
    dtnow = datetime.now()
    stampnow = dtnow.timestamp()
    stnow = round(stampnow)
    if not duration == 0:
        dt = datetime.now() + timedelta(days=duration)
        stampdt = dt.timestamp()
        duration = round(stampdt)
    blist = {'user': user.id,
             'duration': duration,
             'reason': reason,
             'given': stnow,
             'author': author}
    data = dict(blist)
    db.black.put(data=data)
    if duration == 0:
        await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 100009, title = 'Занос в ЧС', type='rich', description = f'<@{user.id}> ({user.id}) был занесён в ЧС.\n\n**Информация:**\nКто занёс:  <@{author}>\nПричина: {reason}\nЗанесён: <t:{stnow}:F>\nСрок истекает: **Бессрочно**'))
    else: 
        await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 100009, title = 'Занос в ЧС', type='rich', description = f'<@{user.id}> ({user.id}) был занесён в ЧС.\n\n**Информация:**\nКто занёс:  <@{author}>\nПричина: {reason}\nЗанесён: <t:{stnow}:F>\nСрок истекает: <t:{duration}:R>'))
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 100009, title = 'Занос в ЧС', type='rich', description = f'<@{user.id}> был занесён в ЧС.\n\n**Информация:**\nКто занёс:  <@{author}>\nПричина: {reason}\nЗанесён: <t:{stnow}:F>\nСрок истекает: <t:{duration}:R>'))

@Bot.command()
@commands.has_any_role(1076124376879079475, 1027112230082334722, 1022732409373990994, 1068939649600458946, 1068939649600458945, 1068939649646604352)
async def bdel(ctx, user:discord.Member):
    author = ctx.message.author.id
    user = user.id
    row = db.black.get('user', user)
    db.black.delete('user', user)
    await ctx.message.channel.purge(limit=1)
    await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 100900, title = 'Вынос из ЧС', type='rich', description = f'<@{user}> ({user}) был удалён из ЧС <@{author}>'))
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 100900, title = 'Вынос из ЧС', type='rich', description = f'<@{user}> ({user}) был удалён из ЧС <@{author}>'))
    
@Bot.command()
@commands.has_any_role(1076124376879079475, 1027112230082334722, 1022732409373990994, 1068939649600458946, 1068939649600458945, 1068939649646604352)
async def blist(ctx, *, user:discord.Member=None):
    count = 0
    author = ctx.message.author.id
    if user == None:
        author = ctx.message.author.id
        rows = db.black.get_all()
        for row in rows:
            count += 1
            if row.duration == 0:
                await ctx.channel.send(embed = discord.Embed(color = 100090, title = f'ЧС', type='rich', description = f'<@{row.user}> был занес в ЧС: <@{row.author}>\n\n**Информация:**\nПричина: {row.reason}\nВыдан: <t:{row.given}:F>\nСрок истекает: **Бессрочно**'))
            else:
                await ctx.channel.send(embed = discord.Embed(color = 100090, title = f'ЧС', type='rich', description = f'<@{row.user}> был занес в ЧС: <@{row.author}>\n\n**Информация:**\nПричина: {row.reason}\nВыдан: <t:{row.given}:F>\nСрок истекает: <t:{row.duration}:R>'))
        if count == 0:
            await ctx.channel.send(f'В базе данных нет никого в ЧС!')
    else:
        rows = db.black.get_all()
        for row in rows:
            if row.user == user.id:
                count += 1
                if row.duration == 0:
                    await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 100090, title = f'ЧС', type='rich', description = f'<@{row.user}> был занес в ЧС: <@{row.author}>\n\n**Информация:**\nПричина: {row.reason}\nВыдан: <t:{row.given}:F>\nСрок истекает: **Бессрочно**'))
                else:
                    await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 109000, title = f'ЧС', type='rich', description = f'<@{row.user}> был занес в ЧС: <@{row.author}>\n\n**Информация:**\nПричина: {row.reason}\nВыдан: <t:{row.given}:F>\nСрок истекает: <t:{row.duration}:R>'))
        if count == 0:
            await ctx.channel.send(f'<@{author}>, <@{user.id}> не находится в ЧС!')


@Bot.command()
@commands.has_any_role(1076124376879079475, 1027112230082334722, 1022732409373990994, 1068939649600458946, 1068939649600458945, 1068939649646604352)
async def warn(ctx, User:discord.Member, Duration:int, *, Reason=None):
    author = ctx.message.author.id
    dtnow = datetime.now()
    dt = datetime.now() + timedelta(days=Duration)
    stampnow = dtnow.timestamp()
    stampdt = dt.timestamp()
    stnow = round(stampnow)
    stdt = round(stampdt)
    await ctx.message.channel.purge(limit=1)
    await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 58324, title = 'Новый варн!!!!', type='rich', description = f'<@{User.id}> получил варн от: <@{author}>\n\n**Информация:**\nПричина: {Reason}\nВыдан: <t:{stnow}:F>\nСрок истекает: <t:{stdt}:R>'))
    bebra = {'User': User.id,
             'Duration': stdt,
             'Reason': Reason,
             'given': stnow,
             'author': author}
    data = dict(bebra)
    db.warns.put(data=data)
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 900704, title = 'Выдан новый варн', type='rich', url='https://memepedia.ru/wp-content/uploads/2021/05/amogus.png', description = f'<@{User.id}> получил варн от: <@{author}>\n\n**Информация:**\nПричина: {Reason}\nВыдан: <t:{stnow}:F>\nСрок истекает: <t:{stdt}:R>'))
    await User.send(embed = discord.Embed(color = 58324, title = 'Новый варн!!!!', type='rich', description = f'<@{User.id}> получил варн от: <@{author}>\n\n**Информация:**\nПричина: {Reason}\nВыдан: <t:{stnow}:F>\nСрок истекает: <t:{stdt}:R>'))


@Bot.command()
async def mywarns(ctx):
    count = 0
    author = ctx.message.author.id
    rows = db.warns.get_all()
    for row in rows:
        if row.User == author:
            count += 1
            await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 58324, title = f'Варн #{row.id}', type='rich', description = f'<@{row.User}> получил варн от: <@{row.author}>\n\n**Информация:**\nПричина: {row.Reason}\nВыдан: <t:{row.given}:F>\nСрок истекает: <t:{row.Duration}:R>'))
    if count == 0:
        await ctx.channel.send(f'<@{author}>, У вас нет активных варнов!')

@Bot.command()
async def warns(ctx, *, User:discord.Member):
    count = 0
    author = ctx.message.author.id
    rows = db.warns.get_all()
    for row in rows:
        if row.User == User.id:
            count += 1
            await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 58324, title = f'Варн #{row.id}', type='rich', description = f'<@{row.User}> получил варн от: <@{row.author}>\n\n**Информация:**\nПричина: {row.Reason}\nВыдан: <t:{row.given}:F>\nСрок истекает: <t:{row.Duration}:R>'))
    if count == 0:
        await ctx.channel.send(f'<@{author}>, у `{User}` нет активных варнов!')
           
@Bot.command()
async def allwarns(ctx):
    count = 0
    author = ctx.message.author.id
    rows = db.warns.get_all()
    for row in rows:
        count += 1
        await ctx.channel.send(embed = discord.Embed(color = 58324, title = f'Варн #{row.id}', type='rich', description = f'<@{row.User}> получил варн от: <@{row.author}>\n\n**Информация:**\nПричина: {row.Reason}\nВыдан: <t:{row.given}:F>\nСрок истекает: <t:{row.Duration}:R>'))
    if count == 0:
        await ctx.channel.send(f'В базе данных нет активных варнов!')
        
@Bot.command()
@commands.has_any_role(1076124376879079475, 1022732409373990994, 1070233324909502484, 1068939649600458946, 1068939649646604352)
async def delallwarns(ctx, *, user:discord.Member=None):
    count = 0
    author = ctx.message.author.id
    if user == None:
        rows = db.warns.get_all()
        for row in rows:
            count += 1
            Userid = row.User
            userd = await Bot.fetch_user(Userid)
            db.warns.delete('id', row.id)
            await ctx.channel.send(embed = discord.Embed(color = 469832, type='rich', description = f'Варн #{row.id} был аннулирован <@{author}>'))
            try:
                await userd.send(embed = discord.Embed(color = 469832, type='rich', description = f'Варн #{row.id} был аннулирован <@{author}>'))
            except:
                print("JoJo")
        if count == 0:
            await ctx.channel.send(f'В базе данных нет активных варнов!')
        channel = await Bot.fetch_channel(1072880578879307786)
        await channel.send(embed = discord.Embed(color = 999999, type='rich', description = f'<@{author}> аннулировал все варны'))
    else:
        rows = db.warns.get_all()
        for row in rows:
            if row.User == user.id:
                count += 1
                Userid = row.User
                userd = await Bot.fetch_user(Userid)
                db.warns.delete('id', row.id)
                await ctx.channel.send(embed = discord.Embed(color = 469832, type='rich', description = f'Варн #{row.id} был аннулирован <@{author}>'))
                try:
                    await userd.send(embed = discord.Embed(color = 469832, type='rich', description = f'Варн #{row.id} был аннулирован <@{author}>'))
                except:
                    print("Соня")
        if count == 0:
            await ctx.channel.send(f'В базе данных у пользователя <@{user.id}>нет активных варнов!')
        channel = await Bot.fetch_channel(1072880578879307786)
        await channel.send(embed = discord.Embed(color = 999999, type='rich', description = f'<@{author}> аннулировал все варны пользователя <@{user.id}>'))
                
@Bot.command()
@commands.has_any_role(1076124376879079475, 1022732409373990994, 1070233324909502484, 1068939649600458946, 1068939649646604352)
async def delwarn(ctx, *, wid:int):
    author = ctx.message.author.id
    row = db.warns.get('id', wid)
    Userid = row.User
    user = await Bot.fetch_user(Userid)
    db.warns.delete('id', wid)
    await ctx.message.channel.purge(limit=1)
    await ctx.channel.send(f'<@{author}>', embed = discord.Embed(color = 469832, type='rich', description = f'Варн #{wid} был аннулирован <@{author}>'))
    channel = await Bot.fetch_channel(1072880578879307786)
    await channel.send(embed = discord.Embed(color = 111111, title = 'Аннуляция варна', type='rich', description = f'Варн #{wid} был аннулирован <@{author}>\n\n**Информация:**\nПричина варна: {row.Reason}\nКогда выдали: <t:{row.given}:f>\nКто выдал: <@{row.author}>\nКому выдали: <@{row.User}>'))
    await user.send(embed = discord.Embed(color = 469832, type='rich', description = f'Варн #{wid} был аннулирован <@{author}>'))

@Bot.command()
async def leav(ctx):
    await ctx.guild.leave()

class Button_close(discord.ui.View):
    def __init__(self):
        super().__init__()
    @discord.ui.button(label="🧔🏿Закрыть тикет",style=discord.ButtonStyle.green)
    async def green_button(self, interaction:discord.ui.Button, button:discord.Interaction):
        channel = interaction.channel
        rows = db.ticket.get_all()
        rows_rep = db.ticket_rep.get_all()
        rows_bug = db.ticket_bug.get_all()
        role = discord.utils.get(interaction.user.guild.roles, name="Администрация🎁")
        if role in interaction.user.roles:
            for row in rows:
                if row.channel == interaction.channel.id:
                    embed = discord.Embed(color = 0x0000, type='rich', description =f'Тикет был разобран: <@{interaction.user.id}> ({interaction.user.id})', timestamp=datetime.now())
                    await channel.send('Тикет закроется в течении нескольких секунд!', embed=embed)
                    user = await Bot.fetch_user(row.user)
                    embed = discord.Embed(color = 0x000453ff, type='rich', title=f'Вопрос-{row.id} был закрыт', description =f'Тикет пользователя <@{user.id}> ({user.id}) в категории `Вопросы` был закрыт администратором <@{interaction.user.id}> ({interaction.user.id})', timestamp=datetime.now())
                    embed.set_author(name=f'{user} ({user.id})', icon_url=user.avatar)
                    with open(f'log{row.id}.txt', 'a') as f:
                            f.write(f'Ticket closing {datetime.now()}')
                    channel = await Bot.fetch_channel(1083706837473431572)
                    await asyncio.sleep(3) 
                    log = f'log{row.id}.txt'
                    await channel.send(file=discord.File(log))
                    await channel.send(embed = embed)
                    location = "/root/bot"
                    db.ticket.delete('id', row.id)
                    channel = interaction.channel
                    await channel.delete()
                    try:
                        await user.send(file=discord.File(log))
                        print('Лог тикета был отправлен пользователю!')
                    except:
                        print('Не удалось отправить лог пользователю(')
                    path = os.path.join(location, log)
                    os.remove(path)
            for row in rows_rep:
                if row.channel == interaction.channel.id:
                    embed = discord.Embed(color = 0x0000, type='rich', description =f'Тикет был разобран: <@{interaction.user.id}> ({interaction.user.id})', timestamp=datetime.now())
                    await channel.send('Тикет закроется в течении нескольких секунд!', embed=embed)
                    user = await Bot.fetch_user(row.user)
                    embed = discord.Embed(color = 0x000453ff, type='rich', title=f'Жалоба-{row.id} была закрыта', description =f'Тикет пользователя <@{user.id}> ({user.id}) в категории `Жалобы` был закрыт администратором <@{interaction.user.id}> ({interaction.user.id})', timestamp=datetime.now())
                    embed.set_author(name=f'{user} ({user.id})', icon_url=user.avatar)
                    with open(f'log_rep{row.id}.txt', 'a') as f:
                            f.write(f'Ticket closing {datetime.now()}')
                    channel = await Bot.fetch_channel(1083706837473431572)
                    await asyncio.sleep(3) 
                    log = f'log_rep{row.id}.txt'
                    await channel.send(file=discord.File(log))
                    await channel.send(embed = embed)
                    location = "/root/bot"
                    db.ticket.delete('id', row.id)
                    channel = interaction.channel
                    await channel.delete()
                    try:
                        await user.send(file=discord.File(log))
                        print('Лог тикета был отправлен пользователю!')
                    except:
                        print('Не удалось отправить лог пользователю(')
                    path = os.path.join(location, log)
                    os.remove(path)
            for row in rows_bug:
                if row.channel == interaction.channel.id:
                    embed = discord.Embed(color = 0x0000, type='rich', description =f'Тикет был разобран: <@{interaction.user.id}> ({interaction.user.id})', timestamp=datetime.now())
                    await channel.send('Тикет закроется в течении нескольких секунд!', embed=embed)
                    user = await Bot.fetch_user(row.user)
                    embed = discord.Embed(color = 0x000453ff, type='rich', title=f'Баг-{row.id} был закрыт', description =f'Тикет пользователя <@{user.id}> ({user.id}) в категории `Баги` был закрыт администратором <@{interaction.user.id}> ({interaction.user.id})', timestamp=datetime.now())
                    embed.set_author(name=f'{user} ({user.id})', icon_url=user.avatar)
                    with open(f'log_bug{row.id}.txt', 'a') as f:
                            f.write(f'Ticket closing {datetime.now()}')
                    channel = await Bot.fetch_channel(1083706837473431572)
                    await asyncio.sleep(3) 
                    log = f'log_bug{row.id}.txt'
                    await channel.send(file=discord.File(log))
                    await channel.send(embed = embed)
                    location = "/root/bot"
                    db.ticket_bug.delete('id', row.id)
                    channel = interaction.channel
                    await channel.delete()
                    try:
                        await user.send(file=discord.File(log))
                        print('Лог тикета был отправлен пользователю!')
                    except:
                        print('Не удалось отправить лог пользователю(')
                    path = os.path.join(location, log)
                    os.remove(path)
        else:
            return


class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__()
    @discord.ui.button(label="Вопрос",style=discord.ButtonStyle.blurple)
    async def red_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        dtnow = datetime.now()
        stampnow = dtnow.timestamp()
        stnow = round(stampnow)
        tick = {'date': stnow,
                'channel': 1000-7,
                'user': button.user.id}
        db.ticket.put(tick)
        guild = await Bot.fetch_guild(1068939649470435449)
        category = Bot.get_channel(1078236857986469968)
        for row in db.ticket.get_all():
            if stnow == row.date:
                channel = await guild.create_text_channel(name=f'Вопрос-{row.id}', topic = None, category=category)
                await channel.set_permissions(button.user, read_messages=True, send_messages=True)
                for row in db.ticket.get_all():
                    if row.date == stnow:
                        with open(f'log{row.id}.txt', 'w+') as f:
                            f.write('Hello world!\nStarting logging\n\n')
                Sempai = await Bot.fetch_user(506417814102343693)
                embed = discord.Embed(color = 0x21893, type='rich', description =f'Создателем данного бота и функции является: <@{Sempai.id}>', timestamp=datetime.now())
                embed.set_author(name=f'{Sempai}', icon_url=Sempai.avatar)
                await channel.send(f'Приветствую, <@{button.user.id}>! Ты открыл премиум версию тикета категории `Вопросы`. Пожалуйста, опиши свой вопрос и дождись ответа нашей доблесной администрации (обычно время ответа не превышает 30 минут)\n\nЗакрыть тикет может только <@&1068939649571110939>!', embed=embed, view=Button_close())
                db.ticket.update('channel', 1000-7, channel.id)
                channel2 = await Bot.fetch_channel(1083706837473431572)
                embed = discord.Embed(color = 0x083212, type='rich', title=f'Новый вопрос-{row.id}', description =f'<@{button.user.id}> ({button.user.id}) открыл тикет', timestamp=datetime.now())
                embed.set_author(name=f'{button.user} ({button.user.id})', icon_url=button.user.avatar)
                embed.set_footer(text=guild.name, icon_url=guild.icon)
                await channel2.send(embed=embed)
        @Bot.event
        async def on_message(message):
            for row in db.ticket.get_all():
                if message.channel.id == row.channel:                    
                    with open(f'log{row.id}.txt', 'a') as f:
                        f.write(f'Time: {datetime.now()}\nMessage id: {message.id}\nUser id: {message.author.id}\nUser: {message.author}\nMessage: {message.content}\t\n\n\n')
            await Bot.process_commands(message)
    @discord.ui.button(label="Жалоба",style=discord.ButtonStyle.blurple)
    async def gray_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        dtnow = datetime.now()
        stampnow = dtnow.timestamp()
        stnow = round(stampnow)
        tick = {'date': stnow,
                'channel': 1000-7,
                'user': button.user.id}
        db.ticket_rep.put(tick)
        guild = await Bot.fetch_guild(1068939649470435449)
        category = Bot.get_channel(1078236857986469968)
        for row in db.ticket_rep.get_all():
            if stnow == row.date:
                channel = await guild.create_text_channel(name=f'Жалоба-{row.id}', topic = None, category=category)
                await channel.set_permissions(button.user, read_messages=True, send_messages=True)
                for row in db.ticket_rep.get_all():
                    if row.date == stnow:
                        with open(f'log_rep{row.id}.txt', 'w+') as f:
                            f.write('Hello world!\nStarting logging\n\n')
                Sempai = await Bot.fetch_user(506417814102343693)
                embed = discord.Embed(color = 0x21893, type='rich', description =f'Создателем данного бота и функции является: <@{Sempai.id}>', timestamp=datetime.now())
                embed.set_author(name=f'{Sempai}', icon_url=Sempai.avatar)
                await channel.send(f'Приветствую, <@{button.user.id}>! Ты открыл премиум версию тикета категории `Жалобы`. Пожалуйста, расскажите на кого жалоба и детально опишите её, а после дождись ответа нашей доблесной администрации (обычно время ответа не превышает 30 минут)\n\nЗакрыть тикет может только <@&1068939649571110939>!', embed=embed, view=Button_close())
                db.ticket_rep.update('channel', 1000-7, channel.id)
                channel2 = await Bot.fetch_channel(1083706837473431572)
                embed = discord.Embed(color = 0x083212, type='rich', title=f'Новая жалоба-{row.id}', description =f'<@{button.user.id}> ({button.user.id}) открыл тикет', timestamp=datetime.now())
                embed.set_author(name=f'{button.user} ({button.user.id})', icon_url=button.user.avatar)
                embed.set_footer(text=guild.name, icon_url=guild.icon)
                await channel2.send(embed=embed)
        @Bot.event
        async def on_message(message):
            for row in db.ticket_rep.get_all():
                if message.channel.id == row.channel:                    
                    with open(f'log_rep{row.id}.txt', 'a') as f:
                        f.write(f'Time: {datetime.now()}\nMessage id: {message.id}\nUser id: {message.author.id}\nUser: {message.author}\nMessage: {message.content}\t\n\n\n')
            await Bot.process_commands(message)
    @discord.ui.button(label="Баг",style=discord.ButtonStyle.blurple)
    async def grey_button(self, button:discord.ui.Button, interaction:discord.Interaction):
        dtnow = datetime.now()
        stampnow = dtnow.timestamp()
        stnow = round(stampnow)
        tick = {'date': stnow,
                'channel': 1000-7,
                'user': button.user.id}
        db.ticket_bug.put(tick)
        guild = await Bot.fetch_guild(1068939649470435449)
        category = Bot.get_channel(1085551767460261918)
        for row in db.ticket_bug.get_all():
            if stnow == row.date:
                channel = await guild.create_text_channel(name=f'Баг-{row.id}', topic = None, category=category)
                await channel.set_permissions(button.user, read_messages=True, send_messages=True)
                for row in db.ticket_bug.get_all():
                    if row.date == stnow:
                        with open(f'log_bug{row.id}.txt', 'w+') as f:
                            f.write('Hello world!\nStarting logging\n\n')
                Sempai = await Bot.fetch_user(506417814102343693)
                embed = discord.Embed(color = 0x21893, type='rich', description =f'Создателем данного бота и функции является: <@{Sempai.id}>', timestamp=datetime.now())
                embed.set_author(name=f'{Sempai}', icon_url=Sempai.avatar)
                await channel.send(f'Приветствую, <@{button.user.id}>! Ты открыл премиум версию тикета категории `Баги`. Пожалуйста, опишите баг и дождись ответа нашего IT отдела (обычно время ответа не превышает часа)\n\nЗакрыть тикет может только <@&1076124376879079475>!', embed=embed, view=Button_close())
                db.ticket_bug.update('channel', 1000-7, channel.id)
                channel2 = await Bot.fetch_channel(1083706837473431572)
                embed = discord.Embed(color = 0x083212, type='rich', title=f'Новый баг-{row.id}', description =f'<@{button.user.id}> ({button.user.id}) открыл тикет', timestamp=datetime.now())
                embed.set_author(name=f'{button.user} ({button.user.id})', icon_url=button.user.avatar)
                embed.set_footer(text=guild.name, icon_url=guild.icon)
                await channel2.send(embed=embed)
        @Bot.event
        async def on_message(message):
            for row in db.ticket_bug.get_all():
                if message.channel.id == row.channel:                    
                    with open(f'log_bug{row.id}.txt', 'a') as f:
                        f.write(f'Time: {datetime.now()}\nMessage id: {message.id}\nUser id: {message.author.id}\nUser: {message.author}\nMessage: {message.content}\t\n\n\n')
            await Bot.process_commands(message)
    
@Bot.command()
@commands.has_permissions(administrator=True)
async def button(ctx):
    await ctx.channel.purge(limit=1)
    guild = await Bot.fetch_guild(1068939649470435449)
    embed = discord.Embed(color = discord.Colour(1203908), type='rich', title = 'Открыть тикет', description ='> С помощью кнопоки ниже вы сможете открыть премиум тикет')
    embed.set_footer(text=guild.name, icon_url=guild.icon)
    await ctx.send(embed=embed, view=Buttons())
    
@Bot.command()
@commands.has_permissions(administrator=True)
async def reserve(ctx):
    author = ctx.message.author
    await ctx.channel.purge(limit=1)
    await ctx.send(f'<@{author.id}> Нажмите кнопку ниже, чтобы закрыть тикет!', view=Button_close())
    
def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 506417814102343693
    return commands.check(predicate)

@Bot.event
async def on_message(message):
    await Bot.process_commands(message)

@Bot.command()
@is_me()
async def don(ctx, user: discord.Member, price:int, *, price_name):
    await ctx.message.channel.purge(limit=1)
    guild = await Bot.fetch_guild(1068939649470435449)
    channel = await Bot.fetch_channel(1084111610651615394)
    dtnow = datetime.now()
    stampnow = dtnow.timestamp()
    stnow = round(stampnow)
    nagatoro = {'user': user.id,
                'price': price,
                'price_text': price_name,
                'date': stnow}
    data = dict(nagatoro)
    db.donat.put(data=data)
    price_sum = 0
    for row in db.donat.get_all():
        price_sum += row.price
    embed = discord.Embed(color = 233421, type='rich', description =f'<@{user.id}> задонатил {price} {price_name}\n> Всего уже собрано: {price_sum} рублей', timestamp=datetime.now())
    embed.set_author(name=f'{user}', icon_url=user.avatar)
    embed.set_footer(text='Огромное спасибо!❤️‍🔥')
    role = discord.utils.get(user.guild.roles, name='Премиум')
    await user.add_roles(role)
    await channel.send(embed = embed)
    try:
        await user.send(f'{user.name}, Огромное тебе спасибо за твой вклад в развитие сервера и бота!')
    except:
        return

@Bot.command()
@is_me()
async def gv(ctx, user:discord.Member, *, role: discord.Role):
    if not role in user.roles:
        await user.add_roles(role)
        await ctx.channel.send(f'<@{user.id}> была выдана роль `{role}`')
    else:
        await user.remove_roles(role)
        await ctx.channel.send(f'`{role}` была снята с <@{user.id}>')

@Bot.command()
@is_me()
async def mom(ctx, user:discord.Member, ls, time:int, *, mes):
    if ls == 'da':
        for i in range(time):
            await ctx.channel.send(mes)
            await user.send(mes)
    else:
        for i in range(time):
            await ctx.channel.send(mes)
    
''' 
Bot.command()
@commands.has_any_role(1093015829622308884, 1068939649600458946, 1068939649646604352, 1093015600357445652)
async def kloun(ctx, user: discord.Member, duration:int, *, reason=None):
    role = discord.utils.get(user.guild.roles, name='Клоун')
    await member.add_roles(role)
'''
    
@Bot.command()
@commands.has_any_role(1068939649571110937, 1068939649571110937, 1068939649646604352)
async def event(ctx, serv, duration:int, name, *, reason=None):
    author = ctx.message.author
    #name = name.lower().replace('.', '')
    dt = datetime.now() + timedelta(minutes=duration)
    stampdt = dt.timestamp()
    dtime = round(stampdt)
    if serv == "PRP":
        serv = "Pineapple RP"
    channel = await Bot.fetch_channel(1068939651081060439)
    embed = discord.Embed(color = 0xe100ff, type='rich', description =f'**Проводит:** \n<@{author.id}>\n**Сервер:** \n{serv}')
    if not reason == None:
        embed.add_field(name="Комментарий организатора:", value=f"{reason}", inline=False)
    await channel.send(f'<@&1068939649541746727>\n**Ивент:** {name}\n<t:{dtime}:R>', embed = embed)
    
@Bot.event
async def on_member_join(member: discord.Member):
    user = member
    role = discord.utils.get(user.guild.roles, name='проверка')
    await member.add_roles(role)
    guild = await Bot.fetch_guild(1068939649470435449)
    channel = await Bot.fetch_channel(1091981901562126428)
    embed = discord.Embed(color = 233421, type='rich', description =f'Приветствую, <@{member.id}>! Добро пожаловать на {guild.name}, ознакомься с правилами в канале <#1068939650288324768>, это важно!\nХорошего тебе время провождения на нашем сервере!', timestamp=datetime.now())
    embed.set_author(name=f'{member.name}', icon_url=member.avatar)
    embed.set_footer(text=guild.name, icon_url=guild.icon)
    await channel.send(embed = embed)
    
@Bot.command()
async def t(ctx, *, user: discord.Member):
    idk = await Bot.create_dm(user)
    await idk.send('Bebra')
    
@Bot.event
async def on_ready():
    warn_loop.start()
    black_loop.start()
    black_chl.start()
    user_count.start()
    rainbow_role.start()
    #tick_upd.start()
    await Bot.change_presence(status=discord.Status.online, activity=discord.Game(".phelp | Author: Lifaster#1699"))
    print("ready")

#xUUtV7c2zDj16UrHdASY7JURG2Xx1fVll0L1b1Ga
Bot.run('MTAyMzQzOTUxMzg2MDcwMjI3OA.GWG9lP.7HxlBJQXA9ewwGaQe4cWHgOVudH3_jj2797UpE')
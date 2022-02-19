import json
from os import stat
from this import s
import hikari
import lightbulb
import random
from twitchAPI.twitch import Twitch
from lightbulb.ext import tasks
from tokens import twitch_id, twitch_secret, discord_token, default_guild, default_channel
twitch = Twitch(twitch_id, twitch_secret)
status = 'notlive'

bot = lightbulb.BotApp(
    token = 'OTM5MTk3MDQzMTU3NjMwOTg3.Yf1VaA.sdMJhFo6oNIYnL6TjJgwL0-dswg',
    default_enabled_guilds = (default_guild)
)
tasks.load(bot)

@tasks.task(s=30, pass_app=True)
async def ce30secs(bot):
    global status
    user_info = twitch.get_streams(user_login=['asmongold'])
    json_data = json.dumps(user_info)
    tuser = 'asmongold'
    if 'id' in json_data:
        if status != 'live':
            print(status)
            await bot.rest.create_message(channel=default_channel, mentions_everyone=True,content=f'Hey, {tuser} is now live at https://twitch.tv/{tuser}')
            status = 'live'
    else:
        status = 'notlive'
        print(status)

@bot.command
@lightbulb.command('quote', 'Says a McPoyle quote.')
@lightbulb.implements(lightbulb.SlashCommand)
async def quote(ctx):
    list_of_quotes = [
        'My name\'s Artemis. I have a bleached asshole.',
        'It\'s time to take off my bra and blast my nips',
        'Frank: Deandra, you got any bacon bits? We like to put em in Artemis\' hair and they rain down on me when we bang.\nI feel like a Cobb salad. It\'s amazing.',
        'Frank: We\'re trying to piece a night together and we need your help.\nArtemis: I don\'t remember that night.\nFrank: I didn\'t tell you which night yet.\nArtemis: I don\'t remember most evenings.',
        'Let\'s talk about payment. I\'ll accept the following things...Coins, cash, checks, food, vape pens, pens in general, SCISSORS...',
        'Frank needed someone to replicate Charlie\'s small and malnourished turd. And that\'s where he came across his old friend, Rickety Cricket. Known the world over for his ability to replicate any man\'s stool. Cricket came back and committed fecal forgery.',
        'Hey, did he send you any dick pics? \'Cause it could be a mess down there.',


    ]
    quote_count = len(list_of_quotes) - 1
    randquote = random.randint(0, quote_count)
    await ctx.respond(list_of_quotes[randquote])

usernameDict = {

}

@bot.command
@lightbulb.option('saying', 'What do you want to say?', type=str)
@lightbulb.command('say', 'Says whatever you want it to say.')
@lightbulb.implements(lightbulb.SlashCommand)
async def say(ctx):
    await ctx.respond(ctx.options.said)

@bot.command
@lightbulb.option('username', 'Twitch username:', type=str)
@lightbulb.command('subscribe', 'Test')
@lightbulb.implements(lightbulb.SlashCommand)
async def usernameDictionary(ctx):
    await ctx.respond('test')
    author = ctx.author
    
    usernameDict.append[author] = ctx.options.username
    ctx.respond


@bot.command
@lightbulb.command('print_twitch_list', 'Prints the list of streams\
 you are going to be notified for')
@lightbulb.implements(lightbulb.SlashCommand)
async def twitchList(ctx):
    await ctx.respond(usernameDict)

ce30secs.start()
bot.run()

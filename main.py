import discord
from discord.ext import commands
import requests
import aiofiles
import aiohttp
import re
from datetime import datetime

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
shortenurl = config.get('shortenurl')
serverurl = config.get('serverurl')
textpasteurl = config.get('textpasteurl')

bot = commands.Bot(command_prefix="{prefix}")




bot.remove_command('help')
body = {
     "token": "SIKE LMAO"
    }
fileform = "file" # file as example

@bot.event
async def on_ready():
    print("Connected to API")
  
@bot.command(name='upload')
@commands.has_any_role(ROLE ID THAT YOU WANT PEOPLE TO NEED TO UPLOAD IMAGES GOES HERE)
async def upload(ctx, file=""):
    channel = bot.get_channel(LOG CHANNEL TO SEE WHAT PEOPLE UPDATE )
    if file:

        url = file
    else:
        try:
            url = ctx.message.attachments[0].url
        except IndexError as e:
            return await ctx.send("No attachment found")
    if not url.endswith(".png") and not url.endswith(".gif") and not url.endswith(".jpg") and not url.endswith(".jpeg"):
        return await ctx.send("File type not supported.")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                search = re.search("([^.]+$)", url)
                ext = search.group(1)
                s = await aiofiles.open('cache/x.{}'.format(ext), mode="wb")
                await s.write(await resp.read())
                await s.close()
    # upload part

    files = {
        '{}'.format(fileform): open('cache/x.{}'.format(ext), 'rb')
    }
    r = requests.request('POST', serverurl, data=body, files=dict(files))
    
    data = r.json()

    image = data['url']
    s = (r)
  
    a = (r.text)

    #data = r.json()
    #image = data['url']
  
    print (a)      # parse json
    #decode = r.content.decode("utf-8") # convert bytes to string
    embed=discord.Embed(title=f'Here Is Your Link',  color=0x36393F, description=f'Status code = {s}```{image}```Was uploaded by {ctx.author.name}#{ctx.author.discriminator}')
    embead=discord.Embed(title=f'LOGS',  color=0x36393F, description=f'```{image}```Was uploaded by {ctx.author.name}#{ctx.author.discriminator} With {s} Status Code')

    await ctx.send(embed=embed)
    await channel.send(embed=embead)


@bot.command()
async def codes(ctx):
        await ctx.message.delete()
        embeded = discord.Embed(title='Status Codes', description='Sharex Discord Bot', color=0x36393F)
        embeded.set_thumbnail(url='https://cdn.discordapp.com/emojis/393945218799501312.gif?v=1',)
        embeded.add_field(name="412", value=f'The request did not contain a User-Agent header.', inline=False)
        embeded.add_field(name="410", value='The collection you tried to upload to is set to private and requires a collection token in order to upload to it.', inline=False)
        embeded.add_field(name="403", value=f'The specified upload token does not match the domains upload token',inline=False)
        embeded.add_field(name="416", value=f'The specified collection token does not match the collections token', inline=False)
        embeded.add_field(name="404", value=f'The specified collection was not found.', inline=False)
        embeded.add_field(name="405", value=f'The request method must be POST.', inline=False)
        embeded.add_field(name="406", value=f'An error occurred while handling the uploaded file.', inline=False)
        embeded.add_field(name="409", value=f'No binary file was sent in the image field.', inline=False)
        embeded.add_field(name="413", value=f'Uploaded file is larger than 95 MB.', inline=False)
        embeded.add_field(name="413", value=f'Uploaded file is smaller than 12 B.', inline=False)
        embeded.add_field(name="415", value=f'The type of the uploaded file is not supported', inline=False)
        embeded.add_field(name="422", value=f'The OpenGraph properties JSON array could not be properly parsed, and is most likely malformed.', inline=False)
        embeded.add_field(name="429", value=f'The request exceeded the rate limit.', inline=False)
        embeded.add_field(name="500", value=f'An unknown error has occurred while processing the file, try again later.', inline=False)
        await ctx.send(embed=embeded)

@bot.command()
async def help(ctx):
        await ctx.message.delete()
        embeded = discord.Embed(title=f'***Help***', description='Sharex Bot', color=0x36393F)
        embeded.set_thumbnail(url='https://cdn.discordapp.com/emojis/393945218799501312.gif?v=1',)
        embeded.add_field(name="Upload", value=f'Uploads An Image To pays.host.', inline=False)
        embeded.add_field(name="Codes", value='Shows all the Status codes you may recive when uploading an image and what they mean', inline=False)
        embeded.add_field(name="shorten", value='Shortens a url', inline=False)
        embeded.add_field(name="paste", value='uploads text to a text hoster like pastebin', inline=False)

        embeded.add_field(name="Help", value='Shows This Menu', inline=False)
        await ctx.send(embed=embeded)

@bot.command()          
async def paste(self, *, text):
        fart = textpasteurl
        a = {
           "text": f"{text}"
           }
        r = requests.post(fart, data=a)
        b = (r.text)
        c = (r)
        data = r.json()

        aya = data['url']
        embed=discord.Embed(title='text uploader', color=0x36393F)
        embed.add_field(name='URL:',value=f"{aya}, {c}")
        embed.set_footer(text="Sharex Bot", icon_url="https://cdn.discordapp.com/emojis/393945218799501312.gif?v=1")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/393945218799501312.gif?v=1")
        embed.timestamp = datetime.now()
        await self.send(embed=embed)

          
@bot.command()
async def shorten(self,website):
  sex = shortenurl
  sexo = {
     "link": f"{website}"
      }
  r = requests.post(sex, data=sexo)
  data = r.json()
  shortlink = data['url']
  embed=discord.Embed(title='URL', color=0x36393F)
  embed.add_field(name='URL:',value=f"{shortlink}")
  embed.set_footer(text="Sharex Bot", icon_url="https://cdn.discordapp.com/emojis/393945218799501312.gif?v=1")
  embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/393945218799501312.gif?v=1")
  embed.timestamp = datetime.now()
  await self.send(embed=embed) 
          
bot.run(token)

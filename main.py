
import discord
from discord.ext import commands
import requests
import aiofiles
import aiohttp
import re
token = "token"
bot = commands.Bot(command_prefix=">")


bot.remove_command('help')
serverurl = "Image Server"
body = {
     "password": "image password",
    }
fileform = "file" # file as example

@bot.event
async def on_ready():
    print("Connected to API")
  
@bot.command(name='upload')
@commands.has_any_role(role id)
async def upload(ctx, file=""):
    channel = bot.get_channel(log channel id)
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
    
    #image = data['url']
    s = (r)
  
    a = (r.text)
    #data = r.json()
    #image = data['url']
  
    print (a)      # parse json
    #decode = r.content.decode("utf-8") # convert bytes to string
    embed=discord.Embed(title=f'Here Is Your Link',  color=0xff08e8, description=f'Status code = {s}```{a}```Was uploaded by {ctx.author.name}#{ctx.author.discriminator}')
    embead=discord.Embed(title=f'LOGS',  color=0xff08e8, description=f'```{a}```Was uploaded by {ctx.author.name}#{ctx.author.discriminator} With {s} Status Code')

    await ctx.send(embed=embed)
    await channel.send(embed=embead)


@bot.command()
async def codes(ctx):
        await ctx.message.delete()
        embeded = discord.Embed(title='Status Codes', description='Sharex Discord Bot', color=0xff08e8)
        embeded.set_thumbnail(url='https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_98e000fe6f47f2143f404d71bbd8c4d8/sharex.png',)
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
        embeded = discord.Embed(title=f'***Help***', description='Sharex Bot', color=0xff08e8)
        embeded.set_thumbnail(url='https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_98e000fe6f47f2143f404d71bbd8c4d8/sharex.png',)
        embeded.add_field(name="Upload", value=f'Uploads An Image To pays.host.', inline=False)
        embeded.add_field(name="Codes", value='Shows all the Status codes you may recive when uploading an image and what they mean', inline=False)
        embeded.add_field(name="Help", value='Shows This Menu', inline=False)
        await ctx.send(embed=embeded)

@bot.command()          
async def text(self, *, text):
        fart = ("https://cancer-co.de/upload")
        a = {
           "text": f"{text}"
           }
        r = requests.post(fart, data=a)
        b = (r.text)
        c = (r)
        embed=discord.Embed(title=main.EMBEDTITLE, color=main.EMBEDCOLOUR)
        embed.add_field(name='URL:',value=f"{b}, {c}")
        embed.set_footer(text=Here Is Your Code, icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSIJUoUGnHsedhJ7kr_5aikSz3tLRibYpEy2Kx82FLzvABc6GY:https://bs-uploads.toptal.io/blackfish-uploads/blog/post/seo/og_image_file/og_image/21026/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSIJUoUGnHsedhJ7kr_5aikSz3tLRibYpEy2Kx82FLzvABc6GY:https://bs-uploads.toptal.io/blackfish-uploads/blog/post/seo/og_image_file/og_image/21026/how-to-make-a-discord-bot-7c0fe302b98b05b145682344b3a4ec59.png&usqp=CAU")
        embed.timestamp = datetime.now()
        await self.send(embed=embed)

bot.run(token)

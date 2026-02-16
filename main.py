import discord
from discord.ext import commands, tasks
from discord.ui import Button, View
import json
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.members = True 
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "MTQ1NjQ1NDk3MjA4OTgyNzMzOA.GmkWv6.q4ig3fQAXwi3Cd1U9TMxunbmdny17njcLMzhd0"


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1446239188965130324)  # ID قناة الترحيب
    if not channel:
        return

    embed = discord.Embed(
        title="<a:velvet:1471960605236920350> Welcome to Velvet Hearts <a:velvet:1471960605236920350>",
        description=(
            f"<:NAME:1471991230555488568> Welcome, {member.mention}, to **{member.guild.name}**\n\n"
            "Step into a realm of grace, charm, and velvet delights.\n\n"
            "━━━━━━━━━━━━━━━\n\n"
            f"<:NAME:1471991226856243441> مرحبًا بك، {member.mention}، في **{member.guild.name}**\n\n"
            "ادخل عالمًا من الرقي، والسحر، ومتعة المخمل 💖"
        ),
        color=0x800020
    )

    if member.avatar:
        embed.set_thumbnail(url=member.avatar.url)

    embed.set_image(url="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4CDQW5-P7L-bMjfp0Cv_reqUqn8DltEuIRikzjRVoUMs0ovf-s3tIowHck919PXL7Fe1eZom-yx5AeYREsgirVttq4gmB0WmUTeyQs3L-ydXj0xhLD9yhsL_Mvx34Y9_DNgRtl2_L__E/s1600/29.gif")
    embed.set_footer(text="نتمنى لك وقتًا ممتعًا معنا ✨")
    await channel.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

bot.run(TOKEN)







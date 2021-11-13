import discord, asyncio, datetime, pytz
import os

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} 봇을 연결했습니다'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith ("~공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(892410210449248256)
            embed = discord.Embed(title="*공지*",description="\n와!\n\n{}샌즈\n\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. ddoiy #7903 | 담당 관리자 : {}".format(message.author), icon_url="https://mblogthumb-phinf.pstatic.net/MjAxOTExMjlfMjk3/MDAxNTc1MDExNTQxMTI0.xeXU-B-yei3gz_Lg7UBeQ8Qg6ze8y_GDqcDEYg9v_OAg.bqWxqpZVi4h0U9uSPUvgiaFCWhn1JIch8uoZoIVxMWAg.PNG.elproy93/%EC%9E%89_%EC%95%97%EC%82%B4%EB%9D%BC%EB%A7%90%EB%9D%BC%EC%9D%B4%EC%BF%B0_%EB%9C%BB__01.PNG?type=w800")
            embed.set_thumbnail(url="https://mblogthumb-phinf.pstatic.net/MjAxOTExMjlfMjk3/MDAxNTc1MDExNTQxMTI0.xeXU-B-yei3gz_Lg7UBeQ8Qg6ze8y_GDqcDEYg9v_OAg.bqWxqpZVi4h0U9uSPUvgiaFCWhn1JIch8uoZoIVxMWAg.PNG.elproy93/%EC%9E%89_%EC%95%97%EC%82%B4%EB%9D%BC%EB%A7%90%EB%9D%BC%EC%9D%B4%EC%BF%B0_%EB%9C%BB__01.PNG?type=w800")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료됨 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 아 몰라 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
            
@client.event
async def on_message(message):
    if message.content.startswith ("!인증 "):
            if message.author.guild_permissions.administrator:
                await message.delete()
                user = message.mentions[0]

                embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
                embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
                embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
                embed.set_footer(text="Bot Made by. ddoiy #7903")
                await message.author.send (embed=embed)
                role = discord.utils.get(message.guild.roles, name = '사원')
                await user.add_roles(role)

            else:
                await message.delete()
                await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

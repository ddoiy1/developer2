import discord, asyncio, datetime, pytz
import os

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} 봇을 연결했습니다'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith ("~청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))
            embed = discord.Embed(title="메시지 삭제 알림", description="디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 삭제 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. ddoiy #7903", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)

        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다.".format(message.author.mention))

    if message.content.startswith ("~공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(886558700779765840)
            embed = discord.Embed(title="*공지*",description="\n와!\n\n{}샌즈\n\n".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. ddoiy #7903 | 담당 관리자 : {}".format(message.author), icon_url="https://mblogthumb-phinf.pstatic.net/MjAxOTExMjlfMjk3/MDAxNTc1MDExNTQxMTI0.xeXU-B-yei3gz_Lg7UBeQ8Qg6ze8y_GDqcDEYg9v_OAg.bqWxqpZVi4h0U9uSPUvgiaFCWhn1JIch8uoZoIVxMWAg.PNG.elproy93/%EC%9E%89_%EC%95%97%EC%82%B4%EB%9D%BC%EB%A7%90%EB%9D%BC%EC%9D%B4%EC%BF%B0_%EB%9C%BB__01.PNG?type=w800")
            embed.set_thumbnail(url="https://mblogthumb-phinf.pstatic.net/MjAxOTExMjlfMjk3/MDAxNTc1MDExNTQxMTI0.xeXU-B-yei3gz_Lg7UBeQ8Qg6ze8y_GDqcDEYg9v_OAg.bqWxqpZVi4h0U9uSPUvgiaFCWhn1JIch8uoZoIVxMWAg.PNG.elproy93/%EC%9E%89_%EC%95%97%EC%82%B4%EB%9D%BC%EB%A7%90%EB%9D%BC%EC%9D%B4%EC%BF%B0_%EB%9C%BB__01.PNG?type=w800")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료됨 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 아 몰라 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

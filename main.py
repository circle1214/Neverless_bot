# from typing import Final
# import os
# from dotenv import load_dotenv
# from discord import Intents, Client, Message
# from responses import get_response

# # Load our token
# load_dotenv()
# TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# # Bot setup
# intents: Intents = Intents.default()
# intents.message_content = True
# client: Client = Client(intents=intents)

# # Message functionality
# async def send_message(message: Message, user_message: str) -> None:
#     if not user_message:
#         print('(Message was empty because intents were not enabled probably)')
#         return
#     if is_private := user_message[0] =='?':
#         user_message = user_message[1:]

#         try:
#             response: str = get_response(user_message)
#             await message.author.send(response) if is_private else await message.channel.send(response)
#         except Exception as e:
#             print(e)

# # Handling the starup of neverless bot
# @client.event
# async def on_ready() -> None:
#     print(f'{client.user} is now running!')

# # Handling incoming message
# @client.event
# async def on_message(message: Message) -> None:
#     if message.author == client.user:
#         return
    
#     username: str = str(message.author)
#     user_message: str = message.content
#     channel: str = str(message.channel)

#     print(f'[{channel}] {username}: "{user_message}"')
#     await send_message(message, user_message)

# # Main enter point
# def main() -> None:
#     client.run(token=TOKEN)

# if __name__ == '__main__':
#     main()







# from typing import Final
# import os
# from dotenv import load_dotenv

# # ✅ 强制加载 .env 文件（重点！）
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# load_dotenv(dotenv_path=dotenv_path)

# from discord import Intents, Client, Message
# from responses import get_response


# # Load environment variables
# load_dotenv()
# TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
# CHANNEL_ID: Final[int] = int(os.getenv("CHANNEL_ID"))  # 确保是整数

# # Print token for debugging (可删除)
# print(f"Loaded TOKEN: {TOKEN}")
# print(f"Using CHANNEL ID: {CHANNEL_ID}")

# # Set up bot intents
# intents: Intents = Intents.default()
# intents.message_content = True
# client: Client = Client(intents=intents)

# # Send a message to channel
# async def send_message(message: Message, user_message: str) -> None:
#     if not user_message:
#         print("(Message was empty — maybe message_content intent not enabled)")
#         return

#     is_private: bool = user_message.startswith('?')
#     if is_private:
#         user_message = user_message[1:]

#     try:
#         response: str = get_response(user_message)
#         if is_private:
#             await message.author.send(response)
#         else:
#             await message.channel.send(response)
#     except Exception as e:
#         print("Error while sending message:", e)

# # On bot ready
# @client.event
# async def on_ready() -> None:
#     print(f'{client.user} is now running!')
#     channel = client.get_channel(CHANNEL_ID)
#     if channel:
#         try:
#             await channel.send("@everyone 📢 **Bot 已上线！欢迎大家使用～**\n你可以发送 `hello`、`roll dice` 等消息测试我喔~")
#         except Exception as e:
#             print("Failed to send startup announcement:", e)
#     else:
#         print("❌ 无法找到频道，请检查 CHANNEL_ID 是否正确。")

# # On message event
# @client.event
# async def on_message(message: Message) -> None:
#     if message.author == client.user:
#         return

#     username = str(message.author)
#     user_message = message.content
#     channel = str(message.channel)

#     print(f'[{channel}] {username}: "{user_message}"')
#     await send_message(message, user_message)

# # Entry point
# def main() -> None:
#     client.run(TOKEN)

# if __name__ == '__main__':
#     main()





# from dotenv import load_dotenv
# import os
# import discord
# from discord import app_commands

# # 加载环境变量
# load_dotenv()
# TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD_ID = int(os.getenv("GUILD_ID"))  # 确保转换为整数

# # 调试输出
# print("DISCORD_TOKEN:", TOKEN)
# print("GUILD_ID:", GUILD_ID)

# intents = discord.Intents.default()
# client = discord.Client(intents=intents)
# tree = app_commands.CommandTree(client)

# @client.event
# async def on_ready():
#     print(f'{client.user} 已上线')
#     try:
#         await tree.sync(guild=discord.Object(id=GUILD_ID))
#         print("✅ Slash 指令已同步")
#     except Exception as e:
#         print("❌ 同步失败：", e)

# @tree.command(name="faq", description="显示服务器频道导航指南", guild=discord.Object(id=GUILD_ID))
# async def faq_command(interaction: discord.Interaction):
#     embed = discord.Embed(
#         title="📚 Server FAQ",
#         description="Below, you'll find guidelines for navigating our channels:",
#         color=discord.Color.green()
#     )

#     embed.add_field(
#         name="**📖 Knowledge Centre**",
#         value=(
#             "<:icon:1234> <#频道ID1> - Stay informed about Extended announcements and updates.\n"
#             "🔗 <#频道ID2> - Access official Extended links and answers to popular questions.\n"
#             "🚀 <#频道ID3> - Discover Extended community opportunities.\n"
#             "🛠️ <#频道ID4> - Get the latest updates on the platform status.\n"
#             "📅 <#频道ID5> - Propose new features or report bugs to help us improve."
#         ),
#         inline=False
#     )

#     embed.add_field(
#         name="**💬 Community Channels**",
#         value=(
#             "💭 <#频道ID6> - Engage in discussions related to Extended.\n"
#             "📈 <#频道ID7> - Share views on the market and your trades.\n"
#             "💻 <#频道ID8> - Discuss anything related to API trading on Extended."
#         ),
#         inline=False
#     )

#     embed.add_field(
#         name="**📨 Contact Us**",
#         value="🤝 <#频道ID9> - Create a ticket to suggest a partnership or ask for help.",
#         inline=False
#     )

#     await interaction.response.send_message(embed=embed)

# # 启动 Bot
# client.run(TOKEN)





from dotenv import load_dotenv
import os
import discord
from discord import Intents, Client, Message

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

# Setup bot intents
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

# Event: on bot ready
@client.event
async def on_ready():
    print(f"{client.user} is now online ✅")

# Event: on message received
@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    if message.content.startswith("!announce"):
        announce_content = message.content[len("!announce"):].strip()
        if not announce_content:
            await message.channel.send("⚠️ Please provide content for the announcement. Usage: `!announce Your message here...`")
            return

        channel = client.get_channel(GUILD_ID)
        if channel:
            try:
                await channel.send(f"📢 {announce_content}")
                await message.channel.send("✅ Announcement has been posted to the designated channel.")
            except Exception as e:
                await message.channel.send("❌ Failed to send the announcement.")
                print("❌ Error:", e)
        else:
            await message.channel.send("❌ Announcement channel not found. Check ANNOUNCE_CHANNEL_ID.")

# Run the bot
client.run(TOKEN)






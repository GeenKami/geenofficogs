import discord
from redbot.core import commands
import requests

class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = "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"
        self.api_url = "https://api.chatgpt.com/v1/conversations"
        self.conversation_id = None
    
    @commands.command()
    async def newchat(self, ctx):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {}
        response = requests.post(self.api_url, headers=headers, json=data)
        response_json = response.json()
        self.conversation_id = response_json['conversation_id']
        await ctx.send("New ChatGPT conversation started!")
    
    @commands.command()
    async def chatgpt(self, ctx, *, message: str):
        if not self.conversation_id:
            await ctx.send("No ChatGPT conversation has been started. Use the `newchat` command to start a new conversation.")
            return
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": message,
            "conversation_id": self.conversation_id
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        response_text = response.json()['response']
        await ctx.send(response_text)

def setup(bot):
    bot.add_cog(ChatGPT(bot))

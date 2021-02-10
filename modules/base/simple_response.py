from wallace.modules.base.basemodule import BaseModule

class SimpleResponseModule(BaseModule):
	def __init__(self, client, priority=0):
		super().__init__(client, priority)

	async def on_message(self, message):
		if message.author == self.client.user:
			return
		if self.can_respond(message):
			await message.channel.send(self.respond(message))
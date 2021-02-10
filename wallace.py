import discord
from wallace.modules.core import CoreModule
from blist import sortedset

class Wallace(discord.Client):
	def __init__(self):
		super().__init__()
		self.modules = sortedset(key=lambda x: x.priority)
		# Load the core module
		self.load_module(CoreModule)
		
	def load_module(self, module, *args, **kwargs):
		m = module(self, *args, **kwargs)
		self.modules.add(m)

	async def on_event(self, event, *args, **kwargs):
		for module in reversed(self.modules):
			handler = getattr(module, f'on_{event}', None)
			if handler is not None:
				if await handler(*args, **kwargs) is True:
					return

	async def on_connect(self):
		await self.on_event("connect")
		
	async def on_disconnect(self):
		await self.on_event("disconnect")
		
	async def on_ready(self):
		await self.on_event("ready")
		
	async def on_resume(self):
		await self.on_event("resumed")
	
	async def on_typing(self, channel, user, when):
		await self.on_event("typing", channel, user, when)
		
	async def on_message(self, message):
		await self.on_event("message", message)

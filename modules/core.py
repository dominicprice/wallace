from wallace.modules.base.basemodule import BaseModule

class CoreModule(BaseModule):
	def __init__(self, client):
		super().__init__(client, -1000)
		
	async def on_ready(self):
		print("Wallace is ready to rumble")
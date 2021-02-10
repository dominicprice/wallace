import nabg
from wallace.modules.base.simple_response import SimpleResponseModule

class BullshitModule(SimpleResponseModule):
	def __init__(self, client):
		super().__init__(client)
		self.triggers = [
			"inspir",
			"inspirational",
			"wise",
			"wisdom",
		]
		
	def can_respond(self, message):
		msg = message.content.lower()
		return any(trigger in msg for trigger in self.triggers)
		
	def respond(self, message):
		return nabg.ionize()

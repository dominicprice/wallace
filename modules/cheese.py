import os, json, random
from wallace.modules.base.simple_response import SimpleResponseModule
from wallace.config import res_dir

class CheeseModule(SimpleResponseModule):
	def __init__(self, client):
		super().__init__(client)
		# Load cheeses as trigger words
		with open(os.path.join(res_dir, "cheeses.json"), "r") as f:
			self.triggers = json.load(f)
		# Load responses
		self.responses = [
			"Did someone say cheese?",
			"Let me get the crackers!",
			"I think a nice bit of double gloucester!",
			"Never too early for a bit of cheese eh boy",
			"I'll just finish off my contraption first"
		]
				
	def can_respond(self, message):
		msg = message.content.lower()
		return any(trigger in msg for trigger in self.triggers)
		
	def respond(self, message):
		return random.choice(self.responses)
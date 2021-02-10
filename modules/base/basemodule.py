class BaseModule:
	def __init__(self, client, priority=0):
		self.client = client
		self.priority = priority

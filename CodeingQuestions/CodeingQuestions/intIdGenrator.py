class IntIdGenrator(object):
	def __init__(self):
		self.top = 0
		self.freeIds = []
		self.bits = 32 #Set the num of bits that will be used for freeIDs

	def getId(self):

		#get a free id if there is any
		result = self.getFreeId()
		if result == None:
			result = self.top
			self.top += 1

		return result

	def getFreeId(self):
		if len(self.freeIds) == 0: return None

		for index, value in enumerate(self.freeIds):
			#check if there is any value with any bit set
			if value > 0:
				for x in range(self.bits + 1):
					if (value >> x) % 2 != 0:
						self.freeIds[index] -= 2**x
						return (index * self.bits) + x

		return Flase


	def freeID(self, id):
		if id == None: return Flase
		if id >= self.top: return Flase

		freeIDIndex = id // self.bits
		bitIndex = id % self.bits

		if len(self.freeIds) <= freeIDIndex:
			for i in range(freeIDIndex - len(self.freeIds) + 1):
				self.freeIds.append(0)

		mask = 1 << bitIndex
		self.freeIds[freeIDIndex] = self.freeIds[freeIDIndex] | mask


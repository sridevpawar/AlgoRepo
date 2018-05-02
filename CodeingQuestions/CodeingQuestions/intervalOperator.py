class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __add__(self, interval2):
		return Interval(min(self.start, interval2.start), max(self.end, interval2.end))

	def __lt__(self, interval2):
		return self.start < interval2.start and self.end < interval2.end

	def __gt__(self, interval2):
		return self.end > interval2.end and self.start > interval2.start

	def __eq__(self, interval2):
		return self.start == interval2.start and self.end == interval2.end

	def __le__(self, interval2):
		return self.start < interval2.start and interval2.start < self.end < interval2.end

	def __ge__(self, interval2):
		return self.end > interval2.end and interval2.start < self.start < interval2.end
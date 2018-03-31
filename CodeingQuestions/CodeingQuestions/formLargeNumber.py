from functools import cmp_to_key
def formLargeNumber(arr):
	if len(arr) == 0:
		print("null")

	#print(" ".join(str(x) for x in sorted(arr, key=cmp_to_key(customeCompare))))
	print(sorted(arr, key=cmp_to_key(customeCompare), reverse=True))

def customeCompare(x,y):
	print ("x: {0}, y: {1}".format(x, y))
	if x < 10 and y < 10:
		res = 1 if x > y else -1 if y > x else o
		print("first", res)
		return res

	xLen = 0
	yLen = 0
	a = x
	while a > 0:
		a = int(a / 10)
		xLen += 1

	a = y
	while a > 0:
		a = int(a / 10)
		yLen += 1

	print ("xL: {0}, yL: {1}".format(xLen, yLen))
	for i in range(max(xLen, yLen)):
		if min(xLen,yLen) - 1 - i < 0:
			num = max(x, y)
			maxLen = max(xLen, yLen)
			lastDiv = (10 ** (maxLen - 1 - i))
			firstDIv = (10 ** (maxLen - 1))
			last = int(num / lastDiv) % 10
			first = int(num / firstDIv) % 10
			print ("last: {0}, first: {1}".format(last, first))
			pickLargeNumber = 1 if last > first else -1 if first > last else o
			if pickLargeNumber > 0:
				res = 1 if x > y else -1 if y > x else o
				print("unE",res)
				return res
			elif pickLargeNumber < 0:
				res = -1 if x > y else 1 if y > x else o
				print("unE",res)
				return res

		xDiv = (10 ** (xLen - 1 - i))
		yDiv = (10 ** (yLen - 1 - i))
		print ("xD: {0}, yD: {1}".format(xDiv, yDiv))
		xFirst = int(x / xDiv) % 10
		yFirst = int(y / yDiv) % 10
		print ("xF: {0}, yF: {1}".format(xFirst, yFirst))
		if xFirst > yFirst:
			print(1)
			return 1
		elif yFirst > xFirst:
			print(-1)
			return -1

	return 0


#formLargeNumber({})
#formLargeNumber([3, 30, 34, 5, 9])
#formLargeNumber([54, 546, 548, 60])
formLargeNumber([23, 235, 45, 456, 451, 452, 455])
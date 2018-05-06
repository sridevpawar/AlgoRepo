import collections
class SearchResult(object):
	def __init__(self, restults):
		self.restults = restults


class SearchResultToPageConverter(object):

	def __init__(self, pageSize):
		self.pageSize = pageSize

	def getResultPages(self, searchResultsObj):
		pagesDict = [collections.OrderedDict()]
		for x in searchResultsObj.restults:
			self.addToPagesDict(x, pagesDict)

		for index in range(len(pagesDict)):
			pagesDict[index] = list(pagesDict[index].values())

		for index in range(len(pagesDict)):
			if len(pagesDict[index]) < self.pageSize:
				if self.fillInCompletePage(pagesDict, index):
					while index + 1 < len(pagesDict):
						del pagesDict[index + 1]
					break
		
		return pagesDict

	def addToPagesDict(self, item, pagesDict):
		hostId = item.split(",")[0]
		pagesDictIndex = 0
		while hostId in pagesDict[pagesDictIndex] or len(pagesDict[pagesDictIndex]) == self.pageSize :
			pagesDictIndex += 1
			if pagesDictIndex == len(pagesDict):
				pagesDict.append(collections.OrderedDict())

		pagesDict[pagesDictIndex][hostId] = item

	def fillInCompletePage(self, pagesDict, index):
		for runner in range(index + 1, len(pagesDict)):
			while len(pagesDict[index]) < self.pageSize and len(pagesDict[runner]) != 0:
				pagesDict[index].append(pagesDict[runner][0])
				del pagesDict[runner][0]

			if len(pagesDict[index]) == self.pageSize:
				return False

		return True

res = ["hostId,listingId,Rank,City",
    "1,43,0.9,NYHXT",
    "2,32,1.0,NYKUT",
    "3,5,1.0,NYLSR",
    "9,33,1.4,JKHKJ",
    "5,89,1.5,JKLJHLK",
    "7,09,1.7,JKLKLJLKJ",
    "2,37,1.9,LPKHJK",
    "9,39,2.1,LPHKJHKJH",
    "4,95,2.3,LPHJNHJ",
    "5,83,2.5,NHKJLJLK",
    "6,28,2.7,NHJKHKJH",
    "8,83,2.8,NCDJFKHD",
    "1,03,2.9,NCJDFHJS",
    "7,73,3.0,NCDSFNH",
    "12,32,3.3,NCDSFHF",
    "11,73,3.5,NUSDFJ",
    "7,92,3.7,NUSDJKH",
    "3,58,3.7,NIDSFSD",
    "4,83,4.1,NIKJKJ",
    "9,29,4.2,NILKJK",
    "1,50,4.4,NISDFSDFD",
    "11,49,4.9,NFSDFSED",
    "2,48,5.1,NFKLJKHDS",
    "1,47,5.3,NFFAWEWE",
    "14,42,5.5,NFLJKHJHDS",
    "6,46,5.8,NFWERCXCK",
    "1,59,5.9,NFSDKLJSD",
    "4,58,6.0,NEWESL",
    "7,55,6.3,NEWSLJLKJ",
    "8,52,6.5,NEASWLKH",
    "2,56,6.7,NEGRLKLK",
    "6,51,6.8,NEWEQLK",
    "3,80,7.1,NWSDFSDFJK",
    "2,87,7.3,NWEDFKLJ",
    "4,89,7.6,NWPOSDAF",
    "2,79,7.8,NWXZXCKJJ",
    "1,78,7.9,NWCDZKCX",
    "7,77,8.0,NMQWXZXJ",
    "5,11,8.3,NMBNBJDU",
    "3,74,8.6,NMCMKSWU",
    "5,82,8.8,NMXXLOZS",
    "6,90,8.9,NMZCLIW",]
sr = SearchResult(res[1:])
pr = SearchResultToPageConverter(12)
arr = pr.getResultPages(sr)
for x in arr:
    for t in x:
        print(t)
    print("-------------------------------")
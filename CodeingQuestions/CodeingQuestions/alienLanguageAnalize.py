def getSortLetter(words, indexLetter=0):
	print(words)
	indexWords = 1
	res = words[0][indexLetter]
	backLogs = []
	while indexWords < len(words):
		if words[indexWords - 1][:indexLetter + 1] == words[indexWords][:indexLetter + 1]:
			similarWords = getSimilarWords(words[indexWords - 1:], indexLetter)
			backLogs.append(getSortLetter(similarWords, indexLetter + 1))

			indexWords += len(similarWords) - 1
			if indexWords == len(words): break

		res += words[indexWords][indexLetter]
		indexWords += 1

	for backLog in backLogs:
		res = mergeSortOrders(res, backLog)

	return res


def getSimilarWords(words, indexLetter):
	res = [words[0]]
	indexWords = 1
	while indexWords < len(words):
		if words[indexWords - 1][:indexLetter + 1] == words[indexWords][:indexLetter + 1]:
			res.append(words[indexWords])
		else:
			break
		indexWords += 1

	return res


def removeDupe(words):
	indexWords = 1
	res = [words[0]]
	while indexWords < len(words):
		if words[indexWords - 1] == words[indexWords]:
			while words[indexWords - 1] == words[indexWords]:
				indexWords += 1

		res.append(words(indexWords))
		indexWords += 1
    
    return res


def mergeSortOrders(mainSortOrder, subSortorder):
	if len(subSortorder) == 0: return mainSortOrder
	if len(mainSortOrder) <= 1: return subSortorder
	print(mainSortOrder)
	print(subSortorder)
	indexMain = 0
	res = ""
	while indexMain < len(mainSortOrder):
		indexSub = 0
		while indexSub < len(subSortorder):
			if mainSortOrder[indexMain] == subSortorder[indexSub]:
				indexSub = 0
				while indexSub < len(subSortorder):
                    if subSortorder[indexSub] == mainSortOrder[indexMain]:
                        subSortorder = subSortorder[indexSub + 1:]
                        break
                    
                    res += subSortorder[indexSub]
				    indexSub += 1

			indexSub += 1

		res += mainSortOrder[indexMain]
		indexMain += 1

    return res + subSortorder

def alienLanguageAnalize(words):
	removeDupe(words)
	sortOrders = getSortLetter(words)
	return sortOrders


strArray = ["baa", "abcd", "abca", "cab", "cad"]
print(alienLanguageAnalize(strS))
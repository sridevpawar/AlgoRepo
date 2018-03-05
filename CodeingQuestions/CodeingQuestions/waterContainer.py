def findLargestContainer(heights):
    if len(heights) < 2:
        return False

    if len(heights) == 2:
        return getVol(min(heights), 1)

    maxVol = 0
    count = 0
    for i in range(len(heights)):
        for j in range(len(heights))[::-1]:
            if j <= i:
                continue

            if max(i-j,j-i) * heights[i] <= maxVol:
                continue

            count += 1
            
            vol = getVol(min(heights[i], heights[j]), max(i-j,j-i))
            if vol > maxVol:
                maxVol = vol

    print(count)
    return maxVol

def getVol(height, width):
    return height * width



print("[3,2,6,8,5,4,9,3]", findLargestContainer([3,2,6,8,5,4,9,3]))
print("[4,2,6,8,5,4,9,4]", findLargestContainer([4,2,6,8,5,4,9,4]))
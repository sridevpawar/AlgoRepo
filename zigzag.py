print("Hi")

def check(array):
    if len(array) <= 2:
        return len(array)

    count = 0 
    res = []
    lastPos = array[0] - array[1] > 0

    for index in range(2, len(array)):
        currentPos = array[index - 1] - array[index] > 0

        if currentPos != lastPos:
            if count == 0:
                count = 3
            else:
                count += 1
        else:
            res.append(count)
            count = 0

        lastPos = currentPos

    max(res)
def glassOverFlow(K, I, J):
    g = 1
    k = K
    for i in range(I):
        if g >= k:
            if i < I - 1: return 0
            return k/g
        k -= g
        g += 1

    return 1




print(glassOverFlow(12,6,3))



def water_overflow(k, array, start_row, start_glass):
    if array[start_row][start_glass] + k <= 1:
        array[start_row][start_glass] += k
        return
    else:
        spill = array[start_row][start_glass] + k - 1
        array[start_row][start_glass] = 1
        water_overflow(spill/2, array, start_row+1, start_glass)
        water_overflow(spill/2, array, start_row+1, start_glass+1)

k = 12
i = 6
j = 3
glasses = [[0]*(i+1) for i in range(k)]
if j > len(glasses[i-1]):
    print(0.000000)
water_overflow(k, glasses, 0, 0)
result = glasses[i-1][j-1]
result = "{0:.6f}".format(result)
print(result)
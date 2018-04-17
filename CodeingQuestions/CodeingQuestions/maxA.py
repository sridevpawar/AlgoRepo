def maxA(n):
    if n <= 5: return n
    if n > 75: return -1
    a = 3
    n -= 3
    while n >= 5:
        a *= 4
        n -= 5
    
    if n > 0 and n < 3:
        a = a + (a/4)*n
    elif n >= 3:
        n -= 2
        a *= n + 1
        
    return a
        


#print(maxA(59))



def calcMaxAs2 ( maxAs, nPressed ):
  maxAs[ nPressed ] = max( ( maxAs[ i ] * ( nPressed - i - 1 ) ) for i in range( 1, nPressed - 2 ) )

maxAs2 = [ None ] * ( 75 + 1 )
maxAs2[ 1:7 ] = [ 1, 2, 3, 4, 5, 6 ]
nPressed = 59
if maxAs2[ nPressed ] == None:
    for i in range( 1, nPressed + 1 ):
      if maxAs2[ i ] == None:
        calcMaxAs2( maxAs2, i )

print(maxAs2[nPressed])
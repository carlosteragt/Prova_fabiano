array1 = [1,2,3,4,5,6,7,8,9,10]

def numPrimo(array1):
    x = 1
    contador = 0
    primos = []
    for i in array1:
        print(i)
        print(primos)
        while x <= i:
                contador = contador + (i % x )
                if(contador > 2):
                    break
                elif(x == i and contador == 2):
                    primos.append(i)
                x = x + 1

        
    return primos

primos = numPrimo(array1)
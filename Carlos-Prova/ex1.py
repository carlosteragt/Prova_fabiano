def palindromo(entrada):
    entrada = entrada.replace(" ","").lower()
    return entrada == entrada[::-1]

x = input("Digite um palindromo, ou não: ")
if(palindromo(x) == True):
    print(f"{x} é um palindromo")
else:
    print(f"{x} não é um palindromo")
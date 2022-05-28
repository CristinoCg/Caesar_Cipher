import string
import pprint
#Author:CristinoCg
#Data:28/05/22
abc = string.ascii_uppercase

abcCifrado = '' 

codificado = "CDBBCLLH"
cifrado = ''.join(input('Digite a cifra:').split())


codificado = cifrado
dictOrdem = dict()
print(f'Palavra cifrada: {codificado}')
for i in codificado:
    dictOrdem[i] = (abc.find(i))
print('Mapeamento:', end = '')    
pprint.pprint(dictOrdem)
for i in range(1,26):
    abcCifrado = abc[i:] + abc[:i]
    
    print(f'Descolocamento:{i}',abcCifrado)
    print('Decode:',' '.join([abcCifrado[dictOrdem[m]] for m in codificado]),'\n')
    

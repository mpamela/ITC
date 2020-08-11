
#------------------------------------------------------------------
# Calcula o MDC de dois números através do algoritmo de
# Euclides.
#
#------------------------------------------------------------
 
def main():
 '''
 Programa que lê um dois inteiro positivos n e m e imprime o 
 máximo divisor comum (mdc) de n e m.
 
 Exemplos de execução
 
 Digite o valor de n (n > 0): 15
 Digite o valor de m (m > 0): 24
 MDC(15,24)=3
 
 Digite o valor de n (n > 0): 315
 Digite o valor de m (m > 0): 125
 MDC(315,125)=5
 
 Digite o valor de n (n > 0): 7
 Digite o valor de m (m > 0): 5
 MDC(7,5)=1
 '''
 
 print("Determina o mdc de dois números n > 0 e m > 0\n")
 
 # leia o valor de n
 n = int(input("Digite o valor de n (n > 0): "))
 
 # leia o valor de m
 m = int(input("Digite o valor de m (m > 0): "))
 
 # aqui começa o algoritmo de Euclides
 anterior = n
 atual = m
 resto = anterior % atual
 
 while resto != 0:
 anterior = atual
 atual = resto
 resto = anterior % atual

 
 print("MDC(%d,%d)=%d" %(n,m,atual))
 if atual == 1:
 print("Os pares de números são primos")
 else:
 print("Os pares de números não são primos")
 
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()


'''Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor de x perteneciente a los reales (x dado en radianes), utilizando los primeros n terminos de la serie de Maclaurin'''

def aproxSin(x,n):
  s = 0
  for i in range(0,n+1):
    factorial = 1
    for j in range(1,(2*i + 1)+1):
      factorial = factorial*j
    print('Factorial de ' + str(2*i + 1) + ' = ' + str(factorial))
    s += ( ( (-1)**i ) * ( x**(2*i + 1 ) )) /factorial
    print('Denominador = ' + str(( ( (-1)**i ) * ( x**(2*i + 1 ) ))))
  return s

print(str(aproxSin(1.5708,20)))
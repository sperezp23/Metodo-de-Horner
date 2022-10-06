# Metodo de Horner

# %% Reset
from IPython import get_ipython
get_ipython().magic('reset -sf')

# %% Entradas
print("\nMetodo de Horner\n")
n = int(input("Ingrese el valor del grado del polinómio:\n"))
Xo = float(input("Ingrese el valor de Xo:\n"))

print("\nIngrese el valor de los coeficientes del polinomio\n")
aux = input("Para ingresar un archivo de texto escriba: Doc, para ingresar un vector escriba Vec:\n")

if aux == "Doc" or aux == "doc":
    nombre = input("Ingrese el nombre del archivo:\n")+".txt"
    datos=open(nombre,'r')
    v = datos.read().split('\n')
    datos.close()
    v = list(map(float,v))    
    
    del datos, nombre, aux
    
elif aux == "Vec" or aux == "vec": 
    v = list(map(float,input("Ingrese un string con el valor de los coeficientes: a0, a1, a2,...,an:\n").split(",")))
    
    del aux
    
# %% Metodo de Horner
y = v[-1]
z = v[-1]

for i in range(1,n).__reversed__():
    y = Xo*y+v[i]
    z = Xo*z+y

del i

y = Xo*y+v[0]

aux = input("¿Desea imprimir el valor de los coeficientes? y/n\n")

# %% Impresion de resultados
if aux == "y":
    print("-------------------------------------------------------------")
    print("Proceso exitoso")
    print("Coeficientes:",v)
    print("Grado del polinomio: ",n)
    print("Xo = ", Xo)
    print("P(Xo) = ",y)
    print("P'(Xo) = ",z)
    print("-------------------------------------------------------------")
    del aux
else:
    print("-------------------------------------------------------------")
    print("Proceso exitoso")
    print("Grado del polinomio: ",n)
    print("Xo = ", Xo)
    print("P(Xo) = ",y)
    print("P'(Xo) = ",z)
    print("-------------------------------------------------------------")
    del aux, v
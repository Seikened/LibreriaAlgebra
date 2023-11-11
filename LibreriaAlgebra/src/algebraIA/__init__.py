def matriz(cA, rA, cB, rB):
    
    import random
    
    def numeroMatriz():
        numero = random.randint(-10,10)
        return numero

    while True:
        # Matríz a
        columnasA =  cA
        renglonesA =  rA
        # Matríz b
        columnasB = cB
        renglonesB = rB
        if columnasA == renglonesB:
            break

    matrizA = [[numeroMatriz() for _ in range(columnasA)] for _ in range(renglonesA)]

    matrizB = [[numeroMatriz() for _ in range(columnasB)] for _ in range(renglonesB)]

    lista = [[] ]

    # Tamaño de la matríz c
    matrizC = [[0 for _ in range(len(matrizB[0]))] for _ in range(len(matrizA))]

    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizA[0])):
                posicionA = matrizA[i][k]
                posisionB = matrizB[k][j]
                matrizC[i][j] += posicionA * posisionB

    
    return matrizA, matrizB, matrizC


def vectorRestultante(*vectores):
    vectorResultante = [ sum(valores) for valores in zip(*vectores)]
    return vectorResultante

# gael codigos-----------------------------------------------------------------------
def producto_escalar():
#Importación de libreria
  import numpy as np
  #Definición de vectores
  v1 = np.array([20,30,40,50],float)
  v2 = np.array([100,200,300,400],float)
  #Calculo de PE
  r=np.dot(v1,v2)
  #Calculo de norma de vectores
  n1=np.linalg.norm(v1)
  n2=np.linalg.norm(v2)

  print("el producto escalar es: ", r)
  print("la norma de v1 es: ", n1)
  print("la norma de v2 es: ", n2)
  
  
  def Gauss_Jordan_pri():
  matriz = []
  res=[]
  #Funciones
  def matz(n):
      for i in range (n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
      return matriz

  def com(n):
    matriz=matz(n)
    for x in range (n):
      for y in range(n):
        matriz[x][y]=float(input('valor de [' + str(x)+']['+str(y)+']='))
      res.append(float(input('Resultado de matriz['+str(x)+']=')))

  def gauss(n):
    for z in range (n-1):
      for x in range(1, n-z):
          if (matriz[z][z]!=0 ):
              p=matriz[x+z][z]/matriz[z][z]
              for y in range (n):
                  matriz[x+z][y]=matriz[x+z][y]-(matriz[z][y]*p)
              res[x+z]=res[x+z]-(res[z]*p)

  def gauss_jordan(n):
    for z in range (n-1, 0, -1):
        for x in range (z):
          if (matriz[z][z] !=0):
              p = matriz[x][z]/matriz[z][z]
              matriz[x][z]= matriz[x][z]-(matriz[z][z]*p)
              res[x]= res[x]-(res[z]*p)

  def solu(n):
    for i in range (n):
        if (matriz[i][i] !=0):
            ms=True
        else:
          ms=False
          break
    if (ms == True):
        for i in range(n):
            print('El valor de x' +str(i)+'es='+str(res[i]/matriz[i][i]))
    else:
      print("No hay solucion")

  def det(n):
    dt=1
    for x in range (n):
      dt=matriz[x][x]*dt
    print("El determinante de la matriz es", dt)

  def im(n):
      for i in range (n):
          for j in range (n):
              print(matriz[i][j])
          print(n)

  #
  n = int(input("Tamaño de la matriz:" ))
  com(n)
  gauss(n)
  gauss_jordan(n)
  solu(n)
  det(n)
  im(n)
  
  
  
  def ecl(n):
  import numpy as np
  import matplotlib.pyplot as plt


  x = np.arange(-6,6)

  y_2 = -x+3
  y_3 = 2*x+1
  plt.figure()
  plt.plot(x, y_2)
  plt.plot(x, y_3)

  plt.xlim(-8,8)
  plt.ylim(-8,8)

  plt.axvline(x=0, color='grey')
  plt.axhline(y=0, color='grey')

  plt.show()
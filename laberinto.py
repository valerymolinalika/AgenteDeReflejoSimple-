import pygame

#Sensorizquierdo / Sensorarriba / Sensorderecho / Sensorabajo / HueleQueso
import numpy as np 

ACCIONES={
    'libre, libre, libre, libre, no': 'ir arriba',
    'libre, libre, libre, no libre, no': 'ir arriba',
    'libre, libre, no libre, libre, no': 'ir arriba',
    'libre, libre, no libre, no libre, no': 'ir izquierda',
    'libre, no libre, libre, libre, no': 'ir izquierda',
    'libre, no libre, libre, no libre, no': 'ir derecha',
    'libre, no libre, no libre, libre, no': 'ir izquierda',
    'libre, no libre, no libre, no libre, no': 'ir izquierda',
    'no libre, libre, libre, libre, no': 'ir arriba',
    'no libre, libre, libre, no libre, no': 'ir derecha',
    'no libre, libre, no libre, libre, no': 'ir abajo',
    'no libre, libre, no libre, no libre, no': 'ir arriba',
    'no libre, no libre, libre, libre, no': 'ir derecha',
    'no libre, no libre, libre, no libre, no': 'ir derecha',
    'no libre, no libre, no libre, libre, no': 'ir abajo',
    '*, *, *, *, si': 'tomar queso'   
}
print("--------Laberinto Raton-----------------")

N=int(input("tamaño del ancho del mapa: "))
M=int(input("tamaño del alto del mapa: "))
O=int(input("cantidad de obstaculos: "))

mapa=np.zeros((N,M),int)
posicionRaton=np.zeros(2, int)
percepcion=['libre', 'libre', 'libre', 'libre', 'no']

def obstaculo(N,M,O):
  
  for i in range(O):
    n=np.random.randint(N)
    m=np.random.randint(M)
    if (mapa[n,m]!=1):
      mapa[n,m]=1
    else: 
      while mapa[n,m] == 1:
        n = np.random.randint(N)
        m = np.random.randint(M)
      mapa[n,m]=1

  return mapa
def queso(M,N):
  n=np.random.randint(N)
  m=np.random.randint(M)
  if (mapa[n,m]!=1):
      mapa[n,m]=2
  else: 
      while mapa[n,m] == 1:
        n = np.random.randint(N)
        m = np.random.randint(M)
      mapa[n,m]=2

  return mapa

#Determina cual sera la posicion inicial del Raton en el mapa
def raton(M,N):
  n=np.random.randint(N)
  m=np.random.randint(M)
  if (mapa[n,m]!=1 and mapa[n,m]!=2 ):
      mapa[n,m]=3
  else: 
      while mapa[n,m] == 1 or mapa[n,m] == 2:
        n = np.random.randint(N)
        m = np.random.randint(M)
      mapa[n,m]=3
  posicionRaton[0]=n
  posicionRaton[1]=m


# obstaculo(M,N,O)
# queso(M,N)
# raton(M,N)

#Teniendo en cuenta la posicion del Raton verifica si tiene obstaculos
#a su alrededor y guarda la informacion en una variable de percepcion
def sinobstaculo(mapa, posicionRaton):
  
  x=posicionRaton[0]
  y=posicionRaton[1]
  
#  if (mapa[x-1,y]==2 or mapa[x+1,y]==7 or mapa[x,y+1]==7 or mapa[x,y-1]==7):
#    percepcion[4]="si"

  if((x-1>=0 and mapa[x-1,y]==1) or x-1<0 ):
    percepcion[1]='no libre'
    print("obstaculo arriba")
    print(mapa[x,y])
  if((x+1<=N-1 and mapa[x+1,y]==1)or x+1>N-1):
    percepcion[3]='no libre'
    print("obstaculo abajo")
    print(mapa[x,y])
  if((y+1<=N-1 and mapa[x,y+1]==1)or y+1>N-1):
    percepcion[2]='no libre'
    print("obstaculo derecha")
    print(mapa[x,y])
  if((y-1>=0 and mapa[x,y-1]==1)or y-1<0):
    percepcion[0]='no libre'
    print("obstaculo izquierda")
    print(mapa[x,y])
  percepcionFinal= percepcion[0] +', '+ percepcion[1] +', '+ percepcion[2] +', '+ percepcion[3]  +', '+ percepcion[4]
  print(percepcionFinal)
  return percepcionFinal


# print(mapa)
# print(posicionRaton)
#sinobstaculo(mapa, posicionRaton) 

##################################################################################################################################
class agenteRaton:
  #Agente de reflejo simple
  def __init__(self, acciones):
    self.acciones=acciones
    self.percepciones=" "
  def actuar(self, percepciones):
    """ Actua segun la percepcion devolviendo una accion"""
    if not percepciones:
      
       return 0
    elif percepciones in self.acciones.keys():
       
       return self.acciones[percepciones]
    

def ejecucion(mapa):
  obstaculo(M,N,O)
  queso(M,N)
  raton(M,N)
  x=posicionRaton[0]
  y=posicionRaton[1]

  agenteReflejoSimple= agenteRaton(ACCIONES)
  #print(percepcion)
  percepcion=sinobstaculo(mapa, posicionRaton)
  accion=agenteReflejoSimple.actuar(percepcion)
  count_pasos=0
  
  while (mapa[x][y]!=7 and count_pasos<20):
    
    count_pasos+=1
    print(mapa)
    if (accion=="ir arriba"):
      mapa[x][y]=0
      if(mapa[x-1][y]==2):
        mapa[x-1][y]=7
      else:
        mapa[x-1][y]=3
      posicionRaton[0]=x-1 
      posicionRaton[1]=y
      print(posicionRaton)
      percepcion=sinobstaculo(mapa, posicionRaton)
      accion=agenteReflejoSimple.actuar(percepcion)
    
    elif (accion=="ir abajo"):
      mapa[x][y]=0
      if(mapa[x+1][y]==2):
        mapa[x+1][y]=7
      else:
        mapa[x+1][y]=3
      posicionRaton[0]=x+1 
      posicionRaton[1]=y 
      print(posicionRaton)
      percepcion=sinobstaculo(mapa, posicionRaton)
      accion=agenteReflejoSimple.actuar(percepcion)
      
    elif (accion=="ir izquierda"):
      mapa[x][y]=0
      if(mapa[x][y-1]==2):
        mapa[x][y-1]=7
      else:

        mapa[x][y-1]=3
      posicionRaton[0]=x
      posicionRaton[1]=y-1 
      print(posicionRaton)
      percepcion=sinobstaculo(mapa, posicionRaton)
      accion=agenteReflejoSimple.actuar(percepcion)
       
    elif (accion=="ir derecha"):
      mapa[x][y]=0
      
      if(mapa[x][y+1]==2):
        
        mapa[x][y+1]=7
      else:
        
        mapa[x][y+1]=3
      posicionRaton[0]=x
      posicionRaton[1]=y-1 
      print(posicionRaton)
      percepcion=sinobstaculo(mapa, posicionRaton)
      accion=agenteReflejoSimple.actuar(percepcion) 
    

ejecucion(mapa)
#---------------------------------------------------------------------------------------------------------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# Crea la ventana
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Laberinto")

# Define las dimensiones de cada celda en la cuadrícula del laberinto
CELL_WIDTH = SCREEN_WIDTH // len(mapa[0])
CELL_HEIGHT = SCREEN_HEIGHT // len(mapa)

# Cargar imagenes 
#imagenQueso = pygame.image.load("imagenes\queso.png")
imagenQP = pygame.transform.scale(pygame.image.load("imagenes\queso.png"), (int(CELL_WIDTH-5), int(CELL_HEIGHT-5)))
imagenP = pygame.transform.scale(pygame.image.load("imagenes\piedra.png"), (int(CELL_WIDTH-5), int(CELL_HEIGHT-5)))
imagenRAR = pygame.transform.scale(pygame.image.load("imagenes\_raton_arriba.png"), (int(CELL_WIDTH-8), int(CELL_HEIGHT-8)))

# Define el color de fondo de la pantalla
BACKGROUND_COLOR = (255, 255, 255)

# Bucle principal
while True:
    # Dibuja el fondo de la pantalla
    screen.fill(BACKGROUND_COLOR)

    # Dibuja la cuadrícula del laberinto con bordes negros
    for y, row in enumerate(mapa):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * CELL_WIDTH, y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1) # Dibuja el borde negro
            if cell == 1:
                pygame.draw.rect(screen, (255, 255, 255), rect) # Dibuja el cuadro negro
                screen.blit(imagenP, (x * CELL_WIDTH, y * CELL_HEIGHT))
            elif cell == 2:
                pygame.draw.rect(screen, (255, 255, 255), rect) # Dibuja el cuadro amarillo
                screen.blit(imagenQP, (x * CELL_WIDTH, y * CELL_HEIGHT))
            elif cell == 3:
                pygame.draw.rect(screen, (255, 255, 255), rect) # Dibuja el cuadro del raton
                screen.blit(imagenRAR, (x * CELL_WIDTH, y * CELL_HEIGHT))
            elif cell==0: 
                pygame.draw.rect(screen, (255, 255, 255), rect) # Dibuja el cuadro blanco
            pygame.draw.rect(screen, (0, 0, 0), rect, 1) # Dibuja el borde negro

    # Actualiza la pantalla
    pygame.display.update()

    # Espera un poco para evitar que el programa se ejecute demasiado rápido
    pygame.time.wait(10)






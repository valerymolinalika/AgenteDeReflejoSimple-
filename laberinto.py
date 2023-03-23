import pygame

#Sensorizquierdo / Sensorarriba / Sensorderecho / Sensorabajo / HueleQueso
import numpy as np 

acciones={
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

mapa=np.zeros((N,M),float)
posicioRaton=np.zeros(2)
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
  posicioRaton[0]=n
  posicioRaton[1]=m
  

obstaculo(M,N,O)
queso(M,N)
raton(M,N)

print(mapa)
print(posicioRaton)
#laberinto= agenteRaton(acciones)
#percepcion=mapa

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






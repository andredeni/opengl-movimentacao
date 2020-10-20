import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
  (0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1),
  (0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)
)

arestas = (
  (0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3),
  (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7)
)

faces = (
  (0, 1, 2, 3), (0, 1, 5, 4), (1, 2, 6, 5),
  (2, 3, 7, 6), (3, 0, 4, 7), (4, 5, 6, 7)
)

def Cube():
  glBegin(GL_QUADS)
  for face in faces:
    for vertice in face:
      glColor3fv((1, 0, 1))
      glVertex3fv(vertices[vertice])
  glEnd()
  glBegin(GL_LINES)
  for aresta in arestas:
    for vertice in aresta:
      glColor3fv((0, 0, 0))
      glVertex3fv(vertices[vertice])
  glEnd()

pygame.init()
pygame.display.set_mode(
  [800, 600], DOUBLEBUF|OPENGL
)

gluPerspective(45, (800/600), 2, 50)
glTranslatef(0, 0, -5)

x_move = y_move = z_move = 0
x_camera = y_camera = z_camera = 0
camera_move = 0

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x_move = 0.1
      if event.key == pygame.K_RIGHT:
        x_move = -0.1
      if event.key == pygame.K_UP:
        z_move = 0.1
      if event.key == pygame.K_DOWN:
        z_move = -0.1
      if event.key == pygame.K_a:
        camera_move = 1
        y_camera = 1
      if event.key == pygame.K_d:
        camera_move = -1
        y_camera = 1
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        x_move = 0
      if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        z_move = 0
      if event.key == pygame.K_a or event.key == pygame.K_d:
        camera_move = y_camera = 0

  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

  glTranslatef(x_move, y_move, z_move)
  glRotatef(camera_move, x_camera, y_camera, z_camera)

  Cube()

  pygame.display.flip()
  pygame.time.wait(10)
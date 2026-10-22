import sys
import random

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def draw_rectangle(a, b, d=0.0):
    d = max(0.0, min(d, 0.9))

    width = a * random.uniform(1.0 - d, 1.0 + d)
    height = b * random.uniform(1.0 - d, 1.0 + d)

    r = random.random()
    g = random.random()
    blue = random.random()
    glColor3f(r, g, blue)

    glBegin(GL_QUADS)
    glVertex2f(-width, -height)
    glVertex2f(width, -height)
    glVertex2f(width, height)
    glVertex2f(-width, height)
    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    draw_rectangle(0.5, 0.3, 0.2)

    glFlush()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, "OpenGL - prostokat", None, None)

    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSwapInterval(1)

    startup()

    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwWaitEvents()

    shutdown()
    glfwTerminate()


if __name__ == '__main__':
    main()
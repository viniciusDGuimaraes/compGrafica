from math import cos, sin, pi, tan

def WriteToFile(f, vertex):
    f.write("v " + str(vertex[0]), + " " + str(vertex[1]), + " " + str(vertex[2]) + "\n")

def MarxistFunction(theta, phi, r):
    return (r*cos(phi)*cos(theta), r*sin(phi), r*cos(phi)*sin(theta))

f = open("bola.obj", "wb")

division = 20
cont = 0
phi = -pi/2
delta = pi/division

# Write vertex to file
while phi < pi/2:
    theta = 0
    while theta < 2*pi:
        vertex = MarxistFunction(theta, phi, 1)
        f.write("v " + str(vertex[0]) + " " + str(vertex[1]) + " " + str(vertex[2]) + '\n')
        vertex = MarxistFunction(theta + delta, phi, 1)
        f.write("v " + str(vertex[0]) + " " + str(vertex[1]) + " " + str(vertex[2]) + '\n')
        vertex = MarxistFunction(theta + delta, phi + delta, 1)
        f.write("v " + str(vertex[0]) + " " + str(vertex[1]) + " " + str(vertex[2]) + '\n')
        vertex = MarxistFunction(theta, phi + delta, 1)
        f.write("v " + str(vertex[0]) + " " + str(vertex[1]) + " " + str(vertex[2]) + '\n')
        theta += delta
        cont += 4
    phi += delta

#Write faces to file
i = 1
while i <= cont:
    f.write("f " + str(i) + " " + str(i+1) + " " + str(i+2) + " " + str(i+3) + '\n')
    i += 4

f.close()

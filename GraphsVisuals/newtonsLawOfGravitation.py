# According to Newton's law of universal gravitation, a body of mass m1 attracts 
# another body of mass m2 with an amount of force F accoridng to the Formula
# F = Gm1mm2/r^2
# where r is the distance b/w two bodies and G is the gravitational constant

import matplotlib.pyplot as plt

#Draw the Graph
def draw_graph(x,y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitaional force and distance')
    plt.show()

def genrate_F_r():
    #Genrate values for r 
    r = range(100, 1001, 50)
    # Empty list to store the calculated values of F
    
    F = []
    
    # Constant G
    G = pow(6.674,pow(10,-11))

    # Two masses 
    m1 = 0.5
    m2 = 1.5

    # Calculate force and add it to the list, F
    for dist in r:
        force = (G * (m1*m2))/pow(dist,2)
        F.append(force)

    # Call the Draw Graph Method
    draw_graph(r,F)

if __name__ == '__main__':
    genrate_F_r()
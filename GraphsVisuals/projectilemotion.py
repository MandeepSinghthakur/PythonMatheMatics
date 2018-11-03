# Lets graph a trajectory of a body which goes from point A to B as per figure on Page 48.
# When you throw a ball, it has initial velocity and the direction of that velocity which creates a certain angle with the ground.
# Lets call that intial velocity u and the angle that it makes with the ground theta . The ball will have two
# components  one along x axis  calculates by ux = u cos(theta) and other along the y direction where uy = u Sin(theta)
# As the ball moves , its velocity changes , and we will represent that changed velocity using v : the horizontal component is vx and the 
# vertical component (vy) decrease because of the force of gravity according to the equation
# vy = uy-gt. In this equation g is the gravitational acceleration and t is the time at which the velocity is measured .Because uy= uSin(theta) and we can substitue to get 
# vy =u Sin(theta) -gt
# Because the horizontal component of the velocity remains constant, the horizontal distance traveled (Sx)is given by
# Sx = u Cos(theta)t. The vertical distance travelled given by the formula
#     Sy = u(Sin(theta)t) -gt^2 /2
# In other Words Sx and Sy gives us the x and y cordinates of the ball at any given point in time
# during its flight.


####### - Mesurement Units - ########
# Time = t seconds
# velocity = v meter/second
# angle of projection = theta degress
# gravitational acceleration = meter/second^2
##################################### 

# Before we write our program, however we'll need to find out how long the ball will be in flight before it hits the ground so that we know
# when our program should stop plotting the trajectory of the ball. TO do so , we'll first 
# find how long the ball takes to reach its highest point. The ball reaches its highest point 
# when the vertical component of the velocity vy is 0 , which is when vy = u Sin(theta) - gt= 0
# SO we are looking for the value of t using the formula t = u Sin (theta) / g
# We'll call this time t_peak. After it reaches its highest point, the ball will hit the ground after being
# airborne for another t_peak seconds, so the total time of flight (t_flight) of the ball is 
# t(flight) = 2t(peak) = 2 * (u sin(theta) / g)

# Another point = There is not built in function for generating the floating numbers so we have to write that too. Its named as frange()

# Finally lets write a program to draw the trajectory of a ball thrown with a certain velocity and angle - both of which are supplied 
# as input to the program

from matplotlib import pyplot as plt 
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-cordinate')
    plt.ylabel('y-cordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final , interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start =  start + interval
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8 

    # Time of Flight
    t_flight = 2*u*math.sin(theta)/g
    
    #Find time intervals
    intervals = frange(0, t_flight, 0.001)

    # List of x and y cordinates 
    x = []
    y = []

    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    
    draw_graph(x,y)

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u, theta)
        plt.show()

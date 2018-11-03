# Fractals  are complex geometric patterns or shapes arising out of surprising simple mathematical
# formulas. Compared to geometric shapes, such as circles and rectangles , a fractal seems irregular
# and without any obvious pattern or description, but if you look closely, you see that patterns emerge 
# and the entire shape is composed of numerous copies of itself.Because fractals involve the repetetive
# application of same geometric transformation of points in a plane , computer programs are well suited 
# to create them.

#Transformation of points is a plane

# A Basic idea in creating fractals is that of the transformation of a point. Given a point, P(x,y)
# in an x-y plane , an example of a transformation is P(x,y) --> Q(x+1,y+1), which means that after applying
# the transformation, a new point , Q, which is one unit above and one unit to the right of P, is created
# If you then consider Q as the starting point, you'll get another point , R , that's one unit above and
# one unit to the right of Q.

##Example of selecting a transformation from two equal probable transformations
import matplotlib.pylab as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    return x + 1, y-1

def transformation_2(p):
    x = p[0]
    y = p[1]
    return x + 1, y + 1

def transform(p):
    #List of transformation functions
    transformations = [transformation_1, transformation_2]
    #Pick a random transformation function and call it
    t = random.choice(transformations)
    x, y = t(p)
    return x, y 

def build_trajectory(p,n):
    x = [p[0]]
    y = [p[1]]

    for i in range(n):
        p = transform(p)
        x.append(p[0])
        y.append(p[1])
    return x, y 

if __name__ == '__main__':
    p =(1,1)
    n = int(input('Ente the number of iterations: '))
    x, y = build_trajectory(p,n)

    # Plot
    plt.plot(x,y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
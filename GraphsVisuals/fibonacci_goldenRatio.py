#The Fobonacci sequence (1, 1, 2, 3, 5 ......) si the series of numbers where ith number in the series is the sum of the two previous numbers
# that is the numbers in the positon ( i -2 ) and (i -1 ). The successive numbers
# in this series display an intresting relationshsip. As you increase the number of terms
# in the series, the ratios of consecutive pairs of numbers are nearly equal to each other 
# This value approaches a special number 1.618033988..., and its been the subject of extensive study
# in music , architecture, and nature. 

# Write a Program that will plot on a graph  the ratio between consecutive Fibonacci numbers for
# say 100 numbers, which will demonstrate that the values approach the golden ratio.

from matplotlib import pyplot as plt 
import math

def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    # n > 2
    a = 1
    b = 1
    # First two members of the series
    series = [a, b]
    for i in range(n):
        c = a + b 
        series.append(c)
        a = b
        b = c 
    return series 

def draw_graph(x,y):
    plt.plot(x, y)
    plt.xlabel("No")
    plt.ylabel("Ratio")
    plt.title("Relationship of fib series numbers and golden ratio")

def draw_ratios(s):
     # List of x and y cordinates 
    x = []
    y = []
    for i in range(0,len(s)):
        number = s[i]
        if(i < 100):
            x.append(i)
            y.append(s[i+1]/number)
    draw_graph(x,y)
    plt.show()

if __name__ == '__main__':
    draw_ratios(fibo(100))
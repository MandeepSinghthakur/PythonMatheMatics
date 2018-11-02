#understanding of cartesian co-ordinates
from pylab import plot, show, title, xlabel,ylabel,legend
x_numbers =[1,2,3]
y_numbers =[2,4,6]
plot(x_numbers,y_numbers, marker ='o')
show()


nyc_temp =[53.9, 56.3, 56.4, 53.4,54.5,55.8,55.8,56.8,55.0,55.3,54.0,56.7,56.7,56.4,57.3]
plot(nyc_temp, marker ='o')
show()

#Graphing Average Annual Temperature in New York City
nyc_temp =[53.9, 56.3, 56.4, 53.4,54.5,55.8,55.8,56.8,55.0,55.3,54.0,56.7,56.7,56.4,57.3]
plot(nyc_temp, marker ='o')
show()

#Add Year Labels to x Axis 
nyc_temp =[53.9, 56.3, 56.4, 53.4,54.5,55.8,55.8,56.8,55.0,55.3,54.0,56.7,56.7,56.4,57.3]
years = range(2000,2013)
plot(nyc_temp, marker ='o')
show()

#Adding a Title and Labels
title("Temperature in NewYork")
xlabel('Years')
ylabel('Temperatue')
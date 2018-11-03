#A word about the initial Values
The Initial Value of the variable from which we start the iteration of the gradient ascent
method plays very important role in the algorithm. More info with diagram in the book.

#Role of Step Size and and Epilson
In Gradient Ascent Algorithm , the next value for the variable is calculated usign the equation
Theta (new) = theta(old) + lambda(dr/d(theta))

where lambda is the step Size. The step size determines the distance of the next step. It should be small to avoid going over a peak.That is, if the current value of x is close to the value that correspondes to the maximum value of the function.

#GRADIENT DESCENT ALGORITHM
 THE REVERSE ALGORITHM OF GRADIENT ASCENT ALGORITHM IS GRADIENT DESCENT ALGORITHM, WHICH IS A METHOD TO FIND THE MINIMUM VALUE OF THE FUNCTION, IT IS SIMILAR TO THE GRADIENT ASCENT ALGORITHM, BUT INSTEAD OF "CLIMBING UP" ALONG THE FUNCTION , WE "CLIMB DOWN".
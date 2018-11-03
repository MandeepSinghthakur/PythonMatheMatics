# THe range tells us the diffrence b/w 2 extremes in a set of numbers, but what if we want
# to know more about how all of the individual numbers vary from the mean? Are they all similar, clustered near
# the mean, or were they all diffrent , closer to the extremes? There are two related measures of dispersion
# that tell us more about a list of numbers along these lines: the Variance and the Standard Deviation
# The variance is the average of the squares of of those diffrences. A high variance
# means that values are far from the mean: a low variance means that the values are clustered close to the mean

def calculate_mean(numbers):
    s = sum (numbers)
    N = len(numbers)
    # Calculate the mean
    mean = s/N

    return mean

def find_diffrences(numbers):
    #Find the mean
    mean = calculate_mean(numbers)

    #Find the diffrences from the mean
    diff = []

    for num in numbers:
        diff.append(num-mean)
    return diff

def calculate_variance(numbers):
    #Find the list of diffrences
    diff = find_diffrences(numbers)
    #Find the squared diffrences
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers)
    return variance

if __name__ == '__main__':
    donations =[100,60,70,900,100,200,500,500,503,600,1000,1200]
    variance = calculate_variance(donations)
    print('The variance of the list of numbers is {0}'.format(variance))

    std = pow(variance, 0.5)
    print('The Standard deviation of the list of numbers is {0}'.format(std))
    
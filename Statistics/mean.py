# Mean = Sum of numbers divided by the length of numbers
# The Mean is common and inituitive way to summarize a set of numbers.
def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    # Calculate Mean
    mean = s/N

    return mean

if __name__ == '__main__':
    donations = [100,60,70,900,100,200,500,503,600,1000]
    mean = calculate_mean(donations)
    N = len(donations)
    print('Mean Donation over the last {0} days is {1}'.format(N,mean))

# The Median of a collection of numbers is another kind of average . 
# To find the median , we sort the numbers is ascending order. If the length of the list of numbers
# is odd, the number in the middle of the list is the median.
# If the list of numbers is even , we get median by taking mean of two middle numbers

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    #FIND THE MEDIAN
    if N % 2  == 0:
        #If N is even
        m1 = N/2
        m2 = (N/2) +1

        #Convert to integer, match position
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2])/2
    else:
        m =(N+1)/2

        #Convert to integer, match position
        m = int(m) -1 
        median = numbers[m]

    return median

if __name__ == '__main__':
    donations =[100,60,70,900,100,200,500,500,503,600,1000,1200]
    median = calculate_median(donations)
    N = len(donations)
    print('Median donation over the last {0} days is {1}'.format(N, median))
    
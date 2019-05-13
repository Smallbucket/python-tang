#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Prompt user for grades (0-100 with input validation) and compute the sum, average,
  minimum, and print the horizontal histogram.
An example to illustrate basic Python syntaxes and constructs, such as block indentation,
  conditional, for-loop, while-loop, input/output, list and function.
 
Usage: ./grade_statistics.py  (Unix/Mac OS)
       python3 grade_statistics.py  (All Platforms)
"""

# Define all the functions before using them
def my_sum(lst):
    """Return the sum of given list."""
    sum = 0
    for item in lst:
        sum += item
    return sum

def my_average(lst):
    """Return the average of the given list."""
    return my_sum(lst)/len(lst) #float

def my_min(lst):
    """Return the minimum of the given lst."""
    min = lst[0]
    for item in lst:
        if item < min:
            min = item
    return min

def print_histogram(lst):
    """Print the horizontal histogram."""
    # Create a list of 10 bins to hold grades of 0-9, 10-19, ..., 90-100.
    # bins[0] to bins[8] has 10 items, but bins[9] has 11 items.
    bins = [0] * 10 # Use repetition operator * to create a list of 10 zeros

    # Populate the histogram bins from the grades in the given lst.
    for grade in lst:
        if grade == 100:
            bins[9] += 1 # Special case
        else:
            bins[grade//10] += 1  # Use // for integer divide to get a truncated int

    print(bins)
    #Print histogram
    #2D pattern: rows are bins, columns are value of that particular bin in stars
    for row in range(len(bins)):
        # Print row header
        if row == 9: # Special case
            print('{:3d}-{:<3d}: '.format(90, 100), end='') # Formatted output (new style), no newline
        else:
            print('{:3d}-{:<3d}: '.format(row * 10, row * 10 + 9), end='') #Formatted output, no newline
            
        # Print one star per count
        for col in range(bins[row]):
            print('*', end='') # no newline
        print() # newline
        # Alternatively, use str's repetition operator * to create the output string
        #print('*'*bins[row])

def main():
    """The main function"""
    # Create an initial empty list for grades to receive from input
    grade_list = []
    # Read grades with input validation
    grade = int(input('Enter a grade between 0 and 100 (or -1 to end): '))
    while grade != -1:
        if 0 <= grade <= 100:
            grade_list.append(grade)
        else:
            print('invalid grade, try again...')
        grade = int(input('Enter a grade between 0 and 100 (or -1 to end): '))

    # Call function and print results
    print('-----------------')
    print('The list is:', grade_list)
    print('The minimum is:', my_min(grade_list))
    print('The minimum using built-in function is:', min(grade_list))  # Using built-in function min()
    print('The sum is:', my_sum(grade_list))
    print('The sum using built-in function is:', sum(grade_list))   # Using built-in function sum()
    print('The average is: %.2f' % my_average(grade_list))          # Formatted output (old style)
    print('The average is: {:.2f}'.format(my_average(grade_list)))  # Formatted output (new style)
    print('---------------')
    print_histogram(grade_list)

# Run the main() function
if __name__ == '__main__':
    main()


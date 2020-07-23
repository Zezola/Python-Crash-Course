"""
Using the range function to create a list of the squares of 
each number from 1 to 10
""" 

squares = []

for i in range(1,11):
    square = i**2
    squares.append(square)

for square in squares: 
    print(square)
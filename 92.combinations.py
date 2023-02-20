
#combnation of two numbers

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs


#Squares with in a range

squares = []
for x in range(10):
    squares.append(x**2)

squares

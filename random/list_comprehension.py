square = []

for i in range(6):
    square.append(i ** 2)
    
print(square)


sq = [i**2 for i in range(6)]
print(sq)



# we also can add the if condition in the list comprehension


squ = [i*i for i in range(6) if i%2 !=0]
print(squ)



sss = [i*i for i in range(6) if i%2 !=0]
print(sss)
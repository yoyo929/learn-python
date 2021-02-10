# for value in range(1,5):
#     print(value)
# numbers=list(range(1,5,2))
# print(numbers)

# squares=[]
# for value in range(1,11):
#     square=value**2
#     squares.append(square)
# print(squares)

digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
a=len(digits)
print(a)

def avg(a):
    return sum(a) / len(a)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(avg(digits))



def multiply(a, b):
    m=a*b
    return m

m = multiply(2, 4)
print(m)
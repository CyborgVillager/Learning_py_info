def squar(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = squar(x)
    b = squar(y)
    c = squar(z)

    return a + b + c

a = -5
b = 2
c = 3

result = sum_of_squares(a,b,c)
print(result)

def main():
    sum_of_squares(a,b,c)

main()

# calling other funcs to other funcs
# short tut by thinkcspy
# https://runestone.academy/runestone/books/published/thinkcspy/Functions/Functionscancallotherfunctions.html
import math

def square_of_sum(L):
	sum = 0;
	for x in L:
		sum = sum + x * x
	return sum

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])


def quadratic_equation(a, b, c):
    t = math.sqrt(b * b - 4 * a * c)
    return (-b + t) / (2 * a),( -b - t )/ (2 * a)

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)


def move(n, a, b, c):
    if n == 1:
        print a,'-->',c
        return
    move(n-1,a,c,b)
    print a,'-->',c
    move(n-1,b,a,c)

move(4, 'A', 'B', 'C')

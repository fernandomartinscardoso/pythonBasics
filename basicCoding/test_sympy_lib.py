from sympy import * #Symbol, symbols, solve, diff, integrate

init_printing(use_unicode=True)

x = Symbol('x')
y = x - 5*x + x*x + 3
print('y =',y)
print('The roots of y are:',solve(y))

xsubs = 3

ysubs = y.subs({x:xsubs})
print('If x is equal to %.1f then y is equal to %.1f'%(xsubs, ysubs))

a, b, c = symbols('a, b, c')
z = a*b + a*b - b*c + 3*b*c
print(z)

zsubs = z.subs({b:6})
print(zsubs)

print(diff(y,x))
print(integrate(y,x))
print(integrate(y,(x,0,1)))

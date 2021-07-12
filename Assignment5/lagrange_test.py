from sympy import symbols, diff, Symbol, factor
from sympy.physics.mechanics import dynamicsymbols, vpprint, vlatex

t = Symbol("t")
q = dynamicsymbols("x")
qdot = q.diff('t')

L = qdot ** 2
f = diff(diff(L, qdot), "t") - diff(L, q)

# Legendre Condition
legendre = diff(L, qdot, 2)
print("Legendre Condition:")
print(vpprint(legendre))
print("Latex Representation:")
print(vlatex(legendre))

# Weierstraus Condition
zdot = symbols("zdot")
weierstraus = L.subs(qdot, zdot) - L - (zdot - qdot) * diff(L, qdot)

print("\nWeierstraus Condition:")
print(vpprint(factor(weierstraus)))

print("Latex Representation:")
print(vlatex(weierstraus))
print(vlatex(factor(weierstraus)))
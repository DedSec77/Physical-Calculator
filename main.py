def A(f, s):
	print(f / s)

def F(m, g):
	print(m * g)
		
def N(a, t):
	print(a / t)

def Lever(a, b, c):
	print((a * b) / c)

def Formules():
	print("F = m * g")
	print("\n")
	print("A = F/S")
	print("\n")
	print("N = A/T")
	print("\n")
	print("η = A/Q * 100%")
	print("\n")
	print("S = V * T")
	print("V = S / T")
	print("T = S / V")

def Efficiency(a, q):
	print((a / q) * 100)

def S(v, t):
	print(v * t)
def V(s, t):
	print(s / t)
def T(s, v):
	print(s / v)


while True:
	answer = input("find A,N,F,Lever,Formules,Efficiency,V,T,S?: ")
	if answer == "A":
		f = int(input("F: "))
		s = int(input("S: "))
		A(f, s)
	elif answer == "F":
		m = int(input("M:" ))
		g = 10
		F(m, g)

	elif answer == "N":
		a = int(input("A: "))
		t = int(input("T: "))
		N(a, t)
	elif answer == "Lever":
		a = int(input("L1/F1: "))
		b = int(input("F1/L1: "))
		c = int(input("F2/L2: "))
		Lever(a, b, c)
	elif answer == "Efficiency":
		a = int(input("A: "))
		q = int(input("Q: "))
		Efficiency()
	elif answer == "S":
		v = int(input("V: "))
		t = int(input("T: "))
		S(v, t)
	elif answer == "V":
		s = int(input("S: "))
		t = int(input("T: "))
		V(v, t)
	elif answer == "T":
		s = int(input("S: "))
		v = int(input("V: "))
		V(v, t)
	elif answer == "exit":
		exit()
	else:
		print("Error")
		exit()

"""

author: DedSec77

"""

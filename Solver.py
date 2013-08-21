import math

__author__ = 'wombat'
__project__ = 'MySimplePythonApplication'
class Solver:
	def demo(self,a,b,c):
		d=b**2-4*a*c
		if d>=0:
			discriminant=math.sqrt(d)
			root1 = (-b+discriminant)/(2*a)
			root2 = (-b-discriminant)/(2*a)
			print(root1,root2)
		else:
			print("error")

Solver().demo(3,2,1)
import math

__author__ = 'wombat'
__project__ = 'MySimplePythonApplication'
class Solver:
	def demo(self,a,b,c):
		d=b**2-4*a*c
		if d>=0:
			discr=math.sqrt(d)
			root1 = (-b+discr)/(2*a)
			root2 = (-b-discr)/(2*a)
			print(root1,root2)
		else:
			print("error")

Solver().demo(3,2,1)

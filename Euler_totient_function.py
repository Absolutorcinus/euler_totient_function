from matplotlib import pyplot as plt
import numpy as np
#*********************************************************
def phi(n) :

	result = n
	p = 2
	while(p * p<= n) :

		# Check if prime factor.
		if (n % p == 0) :
			# update n
			while (n % p == 0) :
				n = n // p
			#result
			result = result *(1.0 - (1.0 / (float)(p)))
		p += 1
		
	if (n > 1) :
		result = result * (1.0 - (1.0 / (float)(n)))

	return (int)(result)

#***********************************************************
list_n = []
list_phi_n = []
for n in range(1, 100000) :
	#print("phi(", n, ") = ", phi(n))
	list_n.append(n)
	a=phi(n)
	#***************************
	list_phi_n.append(phi(n)/n)
	#list_phi_n.append(phi(n)/n)
	#list_phi_n.append(phi(n))
	#***************************

print(list_n)
print(list_phi_n)

x= list_n
y= list_phi_n
#*************************************************************
plt.scatter(x,y, label='EulerPhi', color='k',marker='.', s=1)

plt.xlabel('n')
plt.ylabel('Phi(n)')
plt.title('Graph plot Phi(n)')
plt.legend()
plt.show()

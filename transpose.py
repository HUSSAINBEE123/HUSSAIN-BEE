r1=input("enter no. of rows of m1")
c1=input("enter no. of columns of m1")
r2=input("enter no. of rows of m2")
c2=input("enter no. of columns of m2")
if(r1==r2):
	if(c1==c2):
		i=0
		a={}
		while(i<r1):
			j=0
			while(j<c1):
				m1=input("enter m1 elements")
				a[i,j]=m1
				j=j+1
			i=i+1
		b={}
		i=0
		while(i<r2):
			j=0
			while(j<c2):
				b[i,j]=a[j,i]
				j=j+1
			i=i+1
print("the given matrix is ")
i=0
while(i<r2):
	j=0
	while(j<c2):
		print a[i,j],
		j=j+1
	i=i+1
	print
print("the transpose of matrix is ")
i=0
while(i<r2):
	j=0
	while(j<c2):
		print b[i,j],
		j=j+1
	i=i+1
	print

list1=[1,2,3,4,5,6,7,8,9]

even_count=0
odd_count=0

for items in list1:
	if items%2==0 :
		even_count=even_count+1
	else:
		odd_count=odd_count+1

print("Number of Even numbers:",even_count)
print("Number of Odd numbers: ",odd_count)
	
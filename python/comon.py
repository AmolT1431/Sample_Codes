# Python program to find the common elements
# in two lists
def common_member(a, b):
	a_set = set(a)
	b_set = set(b)

	if (a_set & b_set):
		print(a_set & b_set)
	else:
		print("No common elements")
		

list1=["1 4604 85.66% DSE23146090 DESAI VRUSHALI DATTATRAY F OPEN - &LOPEN",
"2 6049 84.29% DSE23132990 KURADE SANDHYA LAXMAN F OPEN - ^LOPEN"
]

list2=["1 4604 85.66% DSE23146090 DESAI VRUSHALI DATTATRAY F OPEN - LOPEN",
"2 6049 84.29% DSE23132990 KURADE SANDHYA LAXMAN F OPEN - LOPEN"]

common_member(list1,list2)
print("Sets")
set_a ={'col', 'mex', 'bol'}
set_b ={'pe', 'bol'}
print("set_a", set_a)
print("set_b", set_b)
print("=" * 40)

#union
set_c = set_a.union(set_b)
print("Union", set_c)
#Utilizando operador |
print("Union '|'",set_a | set_b)
print("=" * 40)

#Intersection
set_c = set_a.intersection(set_b)
print("Intersection", set_c)
#Utilizando operador &
print("Intersection '&'",set_a & set_b)
print("=" * 40)

#Difference
set_c = set_a.difference(set_b)
print("Difference", set_c)
#Utilizando operador &
print("Difference '-'",set_a - set_b)
print("=" * 40)

#Symmetric Difference elimina los elementos en común
set_c = set_a.symmetric_difference(set_b)
print("Symmetric Difference", set_c)
#Utilizando operador ^
print("Symmetric Difference '^'",set_a ^ set_b)
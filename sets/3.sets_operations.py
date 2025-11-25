import numbers

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

#Union
union_set = set_a.union(set_b)
print("Union:", union_set)

#Intersction
intersection_set = set_a.intersection(set_b)
print("Intersection:", intersection_set)

#Difference
difference_set = set_a.difference(set_b)
#difference_set = set_a - set_b
print("Difference:", difference_set)

#Symmetric difference
symmetric_difference_set = set_a.symmetric_difference(set_b)
#symmetric_difference_set = set_a ^ set_b
print("Symmetric difference:", symmetric_difference_set)


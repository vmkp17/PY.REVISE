#A Set is an unordered collection of unique elements.
# names = {"MADHURI", "MAD", "Sara"}

#Combine both sets.
a = {1,2,3}
b = {3,4,5}
print(a.union(b))  #{1,2,3,4,5}


#Intersection:Common elements.
a = {1,2,3}
b = {3,4,5}
print(a.intersection(b))  #{3}

#Difference:Elements in first set but not second.
a = {1,2,3}
b = {3,4,5}
print(a.difference(b))   #{1,2}
# 1. Write a Python program to create a set
s1 = {1, 2, 3, 4, 5}
s2 = {5, 6, 7, 8, 9}

# 2. Write a Python program to iteration over sets
for s in s1:
    print(s)

# 3. Write a Python program to add member(s) in a set
s1.add(6)
print("After adding: ", s1)

# 4. Write a Python program to remove item(s) from a given set
s1.remove(5)
print("After removing: ", s1)

# 5. Write a Python program to remove an item from a set if it is present in the set.
if 3 in s1:
    s1.remove(3)
print("After removing if values is in set: ", s1)

# 6. Write a Python program to create an intersection of sets.
i = s1.intersection(s2)
print("Intersect: ", i)

# 7. Write a Python program to create a union of sets.
u = s1.union(s2)
print("Union: ", u)

# 8. Write a Python program to create set difference
d = s1.difference(s2)
print("Set difference (s1-s2): ", d)

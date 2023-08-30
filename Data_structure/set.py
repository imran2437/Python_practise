# Creating a set
my_set = {1, 2, 2, 3, 4}

# Adding and removing elements
my_set.add(5)
my_set.remove(2)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1)
union = set1.union(set2)
print(union)
intersection = set1.intersection(set2)
print(intersection)


# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of sets
union_result = set1.union(set2)  # {1, 2, 3, 4, 5, 6, 7}

# Intersection of sets
intersection_result = set1.intersection(set2)  # {3, 4, 5}

# Difference of sets
difference_result = set1.difference(set2)  # {1, 2}

# Symmetric Difference of sets
symmetric_difference_result = set1.symmetric_difference(set2)  # {1, 2, 6, 7}

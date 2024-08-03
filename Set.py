# Creating two sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Union: Combining elements from both sets, excluding duplicates
union_set = set1 | set2
print(f"Union: {union_set}")

# Intersection: Elements common to both sets
intersection_set = set1 & set2
print(f"Intersection: {intersection_set}")

# Difference: Elements in set1 but not in set2
difference_set = set1 - set2
print(f"Difference: {difference_set}")

# Subset: Check if set2 is a subset of set1
is_subset = set2 <= set1
print(f"Is set2 a subset of set1? {is_subset}")

# Check if a set is a subset of another
is_subset = {2, 3} <= set1
print(f"Is {{2, 3}} a subset of set1? {is_subset}")

my_set = {2, 4, 6, 8, 10}
print("Original set:", my_set)


my_tuple = tuple(num ** 2 for num in my_set)
print("Tuple of squares:", my_tuple)

my_list = list(my_set)
my_list.sort(reverse=True)
print("Sorted list (descending):", my_list)


intersection = my_set.intersection(set(my_tuple))
print("Intersection between set and tuple:", intersection)


print(f"Length of the tuple: {len(my_tuple)}")
print(f"Length of the set: {len(my_set)}")


try:
    my_tuple[0] = 100
except TypeError as e:
    print("Error when trying to modify tuple:", e)
numbers = [1, 5, 8, 12, 3, 7, 5, 2, 9, 4]
print("Original list:", numbers)

numbers.append(11)


if 5 in numbers:
    numbers.remove(5)


numbers.insert(2, 3)

print("Modified list:", numbers)

total_sum = sum(numbers)
print(f"Sum of all numbers: {total_sum}")

smallest = min(numbers)
print(f"Smallest number: {smallest}")

largest = max(numbers)
print(f"Largest number: {largest}")
from recursive_sorting import recursive_sorting
import random

def generate_random_array(size, min_val, max_val):

    array = []
    for _ in range(size):
        if random.choice([True, False]):
            array.append(random.randint(min_val, max_val))
        else:
            array.append(round(random.uniform(min_val, max_val), 2))
    return array

array_a = generate_random_array(6, 4, 15)
array_b = generate_random_array(12, -4, 5)
empty_array = []

print("Test:", array_a, "\nSorted array_a:", recursive_sorting(array_a), sep='')
print("Random array_b", array_b, "\nSorted array_b:", recursive_sorting(array_b), sep='')
print("Empty Array:", empty_array, "\nSorted Empty Array:", recursive_sorting(empty_array), sep='')
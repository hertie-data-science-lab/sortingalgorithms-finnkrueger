def recursive_sorting(input_list, bucket_size=5):

    # Base case: if input list contains 1 or fewer elements, it is already sorted
    if len(input_list) <= 1:
        return input_list

    max_val = max(input_list)
    min_val = min(input_list)

    # If the range of values in the input list is zero, it is already sorted
    if max_val == min_val:
        return input_list

    # Calculate the range
    range_size = max_val - min_val

    # Create empty buckets
    buckets = [[] for _ in range(bucket_size + 1)]

    # Distribute the elements of the input list into the buckets
    for elem in input_list:
        bucket_index = int((elem - min_val) / range_size * bucket_size)
        # Add the element to the corresponding bucket
        buckets[bucket_index].append(elem)

    # Sort the elements of each bucket recursively
    sorted_buckets = []
    for i in range(bucket_size + 1):
        if len(buckets[i]) > 0:
            sorted_bucket = recursive_sorting(buckets[i])
            sorted_buckets.extend(sorted_bucket)

    # Return the sorted elements from all buckets
    return sorted_buckets
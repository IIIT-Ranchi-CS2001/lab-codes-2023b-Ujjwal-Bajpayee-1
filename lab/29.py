def my_zip(list1, list2, list3, strct=True):
    if strct:
        if len(list1) == len(list2) == len(list3):
            return [(list1[i], list2[i], list3[i]) for i in range(len(list1))]
        else:
            return []
    else:
        min_length = min(len(list1), len(list2), len(list3))
        return [(list1[i], list2[i], list3[i]) for i in range(min_length)]

def my_sort(data, key=0):
    def sort_key(item):
        return item[key]

    for i in range(len(data)):
        for j in range(0, len(data) - i - 1):
            if sort_key(data[j]) > sort_key(data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Example usage:
customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [101, 102, 103]
shopping_points = [150, 200, 100]

zipped_data = my_zip(customer_names, customer_ids, shopping_points, strct=True)
print("Zipped Data:", zipped_data)

sorted_data = my_sort(zipped_data, key=2)
print("Sorted Data by Shopping Points:", sorted_data)
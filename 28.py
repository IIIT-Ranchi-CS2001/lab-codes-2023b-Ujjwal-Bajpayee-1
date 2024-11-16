def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return list(zip(customer_names, customer_ids, shopping_points))
        else:
            raise ValueError("All lists must be of equal length when strct is True")
    else:
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return list(zip(customer_names[:min_length], customer_ids[:min_length], shopping_points[:min_length]))

# Example usage:
customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [101, 102, 103]
shopping_points = [150, 200, 250]

print(my_zip(customer_names, customer_ids, shopping_points, strct=True))
print(my_zip(customer_names, customer_ids, shopping_points, strct=False))
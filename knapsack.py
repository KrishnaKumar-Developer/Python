class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.value_density = value / weight

def knapsack_greedy(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.value_density, reverse=True)
    
    total_value = 0
    total_weight = 0
    selected_items = []

    for item in items:
        if total_weight + item.weight <= capacity:
            selected_items.append(item)
            total_weight += item.weight
            total_value += item.value
    
    return total_value, selected_items

# Example usage
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
total_value, selected_items = knapsack_greedy(items, capacity)

print(f"Total value in knapsack: {total_value}")
for item in selected_items:
    print(f"Item - Value: {item.value}, Weight: {item.weight}")

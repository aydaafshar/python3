import sys


def parse_inventory(args):
    inventory = dict()

    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            continue

        name = parts[0]
        qty = int(parts[1])

        inventory.update({name: qty})

    return inventory


def total_items(inventory):
    total = 0
    for value in inventory.values():
        total += value
    return total


def most_and_least(inventory):
    most_item = None
    least_item = None

    for item, qty in inventory.items():
        if most_item is None or qty > inventory.get(most_item):
            most_item = item
        if least_item is None or qty < inventory.get(least_item):
            least_item = item

    return most_item, least_item


def categorize_items(inventory):
    categories = {"Abundant": dict(), "Moderate": dict(), "Scarce": dict()}

    for item, qty in inventory.items():
        if qty >= 6:
            categories["Abundant"].update({item: qty})
        elif qty >= 4:
            categories["Moderate"].update({item: qty})
        else:
            categories["Scarce"].update({item: qty})

    return categories


def restock_list(inventory):
    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)
    return restock


def main():
    inventory = parse_inventory(sys.argv[1:])

    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total_items(inventory))
    print("Unique item types:", len(inventory))
    print()
    print("=== Current Inventory ===")
    total = total_items(inventory)
    for item, qty in inventory.items():
        percent = (qty * 100) / total
        print(item + ":", qty, "units (" + str(round(percent, 1)) + "%)")
    print()
    print("=== Inventory Statistics ===")
    most, least = most_and_least(inventory)
    print("Most abundant:", most, "(" + str(inventory.get(most)) + " units)")
    print("Least abundant:", least, "(" + str(inventory.get(least)) + "units)")
    print()
    print("=== Item Categories ===")
    categories = categorize_items(inventory)
    for name, data in categories.items():
        if len(data) > 0:
            print(name + ":", data)
    print()
    print("=== Management Suggestions ===")
    print("Restock needed:", restock_list(inventory))
    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", list(inventory.keys()))
    print("Dictionary values:", list(inventory.values()))
    print("Sample lookup - 'sword' in inventory:",
          inventory.get("sword") is not None)


if __name__ == "__main__":
    main()

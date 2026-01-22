def item_total_value(item_data):
    qty = item_data.get("quantity", 0)
    price = item_data.get("price", 0)
    return qty * price


def inventory_value(inventory):
    total = 0
    for item_data in inventory.values():
        total += item_total_value(item_data)
    return total


def inventory_item_count(inventory):
    total = 0
    for item_data in inventory.values():
        total += item_data.get("quantity", 0)
    return total


def category_counts(inventory):
    counts = {}
    for item_data in inventory.values():
        cat = item_data.get("type", "unknown")
        qty = item_data.get("quantity", 0)
        counts[cat] = counts.get(cat, 0) + qty
    return counts


def print_inventory(title, inventory):
    print(f"\n{title}")
    for name, data in inventory.items():
        itype = data.get("type", "unknown")
        rarity = data.get("rarity", "common")
        qty = data.get("quantity", 0)
        price = data.get("price", 0)
        total = qty * price
        print(f"{name} ({itype}, {rarity}): {qty}x"
              f" @ {price} gold each = {total} gold")

    value = inventory_value(inventory)
    count = inventory_item_count(inventory)
    print(f"\nInventory value: {value} gold")
    print(f"Item count: {count} items")

    cats = category_counts(inventory)
    parts = []
    for cat, qty in cats.items():
        parts.append(f"{cat}({qty})")
    print("Categories:", ", ".join(parts))


def transfer_item(giver, receiver, item_name, qty):
    giver_item = giver.get(item_name)
    if giver_item is None:
        return False

    giver_qty = giver_item.get("quantity", 0)

    if qty <= 0 or giver_qty < qty:
        return False

    giver_item["quantity"] = giver_qty - qty
    giver.update({item_name: giver_item})

    recv_item = receiver.get(item_name)

    if recv_item is None:
        receiver[item_name] = {
            "type": giver_item.get("type", "unknown"),
            "rarity": giver_item.get("rarity", "common"),
            "quantity": qty,
            "price": giver_item.get("price", 0),
        }
    else:
        recv_item["quantity"] = recv_item.get("quantity", 0) + qty
        receiver.update({item_name: recv_item})
    return True


def rarest_items(players):
    rares = []
    for inv in players.values():
        for item_name, data in inv.items():
            if data.get("rarity") == "rare" and item_name not in rares:
                rares.append(item_name)
    return rares


def main():
    print("=== Player Inventory System ===")

    alice = {
        "sword": {"type": "weapon", "rarity": "rare", "quantity": 1,
                  "price": 500},
        "potion": {
            "type": "consumable",
            "rarity": "common",
            "quantity": 5,
            "price": 50,
        },
        "shield": {"type": "armor", "rarity": "uncommon", "quantity": 1,
                   "price": 200},
    }

    bob = {
        "magic_ring": {
            "type": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "price": 10,
        }
    }

    print_inventory("=== Alice's Inventory ===", alice)

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    ok = transfer_item(alice, bob, "potion", 2)
    if ok:
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice.get('potion').get('quantity')}")
    print(f"Bob potions: {bob.get('potion').get('quantity')}")

    print("\n=== Inventory Analytics ===")
    players = {"Alice": alice, "Bob": bob}

    most_value_name = None
    most_value_amount = None

    most_items_name = None
    most_items_amount = None

    for name, inv in players.items():
        val = inventory_value(inv)
        cnt = inventory_item_count(inv)

        if most_value_amount is None or val > most_value_amount:
            most_value_amount = val
            most_value_name = name

        if most_items_amount is None or cnt > most_items_amount:
            most_items_amount = cnt
            most_items_name = name

    print(f"Most valuable player: {most_value_name}"
          f" ({most_value_amount} gold)")
    print(f"Most items: {most_items_name} ({most_items_amount} items)")
    rares = rarest_items(players)
    print("Rarest items:", ", ".join(rares))


if __name__ == "__main__":
    main()

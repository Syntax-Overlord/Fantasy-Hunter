import json
import os


class Item:
    def __init__(self, id: str) -> None:
        self.id: str = id
        with open("data/items.json", "r") as file:
            data: dict = json.load(file)
            idData: dict = data.get(id, {})
            self.name: str = idData.get("name", "Unknown Item")
            self.description: str = idData.get(
                "description", "No description available."
            )
            self.category: str = idData.get("category", "consumable")
            if idData.get("durability") > -1 and idData.get("durability") != None:
                self.durability: int = idData.get("durability")
            else:
                self.durability: int = 0
            self.attack: int = idData.get("attack", 0)
            self.defense: int = idData.get("defense", 0)
            self.value: list = idData.get("value", [])
            self.cost: int = idData.get("cost", 0)

    def __repr__(self) -> str:
        """Return a string representation of the item."""
        return f"""
Item ID: {self.id: str}
Name: {self.name: str}
Description: {self.description: str}
Category: {self.category: str}
Durability: {self.durability: int}
Attack: {self.attack: int}
Defense: {self.defense: int}
Value: {self.value: list}
Cost: {self.cost: int}
"""

    def to_dict(self) -> dict:
        """Convert the item to a dictionary representation.

        Returns:
            dict: The dictionary representation of the item.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "durability": self.durability,
            "attack": self.attack,
            "defense": self.defense,
            "value": self.value,
            "cost": self.cost,
        }


class Inventory:
    def __init__(self):
        self.inventory: dict = {}
        self.weapons: list = []
        self.armors: list = []
        self.consumables: list = []
        self.loadInventory()

    def add(self, itemID: str, quantity: int = 1) -> None:
        """Add an item to the inventory.

        Args:
            itemID (str): The ID of the item to add.
            quantity (int, optional): The quantity of the item to add. Defaults to 1.
        """
        item: Item = Item(itemID)
        category: str = item.to_dict().get("category", "consumable")
        match category:
            case "weapon":
                self.weapons.append({itemID: quantity})
            case "armor":
                self.armors.append({itemID: quantity})
            case "consumable":
                self.consumables.append({itemID: quantity})

    def subtract(self, itemID: str, quantity: int = 1) -> None:
        """Subtract an item from the inventory.

        Args:
            itemID (str): The ID of the item to subtract.
            quantity (int, optional): The quantity of the item to subtract. Defaults to 1.
        """
        item: Item = Item(itemID)
        category: str = item.to_dict().get("category", "consumable")
        match category:
            case "weapon":
                for entry in self.weapons:
                    if itemID in entry:
                        if entry[itemID] > quantity:
                            entry[itemID] -= quantity
                        elif entry[itemID] == quantity:
                            self.weapons.remove(entry)
                        else:
                            print(f"Not enough {itemID} to subtract.")
                        break
            case "armor":
                for entry in self.armors:
                    if itemID in entry:
                        if entry[itemID] > quantity:
                            entry[itemID] -= quantity
                        elif entry[itemID] == quantity:
                            self.armors.remove(entry)
                        else:
                            print(f"Not enough {itemID} to subtract.")
                        break
            case "consumable":
                for entry in self.consumables:
                    if itemID in entry:
                        if entry[itemID] > quantity:
                            entry[itemID] -= quantity
                        elif entry[itemID] == quantity:
                            self.consumables.remove(entry)
                        else:
                            print(f"Not enough {itemID} to subtract.")
                        break

    def create(self) -> None:
        """Create an empty inventory file if it doesn't exist or erases the older one to create the new one."""
        with open("data/inventory.json", "w") as file:
            json.dump(self.inventory, file, indent=4)

    def save(self) -> None:
        """Saves the current inventory to the inventory file."""
        if not os.path.exists("data/inventory.json"):
            self.create()
        else:
            with open("data/inventory.json", "w") as file:
                json.dump(self.inventory, file, indent=4)

    def load(self) -> dict:
        """Loads the inventory from the inventory file."""
        inventory: dict = {}
        if os.path.exists("data/inventory.json"):
            with open("data/inventory.json", "r") as file:
                inventory = json.load(file)
            self.weapons: list = inventory.get("weapons", [])
            self.armors: list = inventory.get("armors", [])
            self.consumables: list = inventory.get("consumables", [])
            self.inventory: dict = {
                "weapons": self.weapons,
                "armors": self.armors,
                "consumables": self.consumables,
            }
            return self.inventory
        else:
            self.createInventory()
            return self.inventory

    def __repr__(self) -> str:
        """Return a string representation of the inventory."""
        return f"""
Inventory:
Weapons: {self.weapons: list}
Armors: {self.armors: list}
Consumables: {self.consumables: list}
"""

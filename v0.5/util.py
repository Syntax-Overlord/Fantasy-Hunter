import json
import os


class item:
    def __init__(self, id: str) -> None:
        self.id: str = id
        with open("data/items.json", "r") as file:
            data: dict = json.load(file)
            idData: dict = data.get(id, {})
            self.name: str = idData.get("name", "Unknown Item")
            self.description: str = idData.get(
                "description", "No description available."
            )
            if idData.get("durability") > -1 and idData.get("durability") != None:
                self.durability: int = idData.get("durability")
            else:
                self.durability: int = 0
            self.attack: int = idData.get("attack", 0)
            self.defense: int = idData.get("defense", 0)
            self.value: list = idData.get("value", [])
            self.cost: int = idData.get("cost", 0)

    def __repr__(self) -> str:
        return f"""
Item ID: {self.id: str}
Name: {self.name: str}
Description: {self.description: str}
Durability: {self.durability: int}
Attack: {self.attack: int}
Defense: {self.defense: int}
Value: {self.value: list}
Cost: {self.cost: int}
"""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
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

    def createInventory(self) -> None:
        """Create an empty inventory file if it doesn't exist or erases the older one to create the new one."""
        if not os.path.exists("data/inventory.json"):
            with open("data/inventory.json", "w") as file:
                json.dump({}, file)
        else:
            with open("data/inventory.json", "w") as file:
                self.inventory = json.load(file)

    def saveInventory(self) -> None:
        """Saves the current inventory to the inventory file."""
        with open("data/inventory.json", "w") as file:
            json.dump(self.inventory, file, indent=4)

    def loadInventory(self) -> dict:
        """Loads the inventory from the inventory file."""
        if os.path.exists("data/inventory.json"):
            with open("data/inventory.json", "r") as file:
                inventory = json.load(file)
        else:
            self.createInventory()

        return inventory

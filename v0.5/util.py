import json


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

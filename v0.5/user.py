from util import item


class User:
    def __init__(
        self, name: str, gender: str, job: tuple, skillTree: list, inventory: list
    ) -> None:
        self.name: str = name
        self.gender: str = gender
        self.job: tuple = job
        self.skillTree: list = skillTree
        self.inventory: dict = self.getInventory(inventory)

    def __repr__(self) -> str:
        return f"""
Name: {self.name: str}
Gender: {self.gender: str}
Job: {self.job: tuple}
SkillTree: {self.skillTree: list}
Inventory: {self.inventory: list}
"""

    def getInventory(inventory: list) -> dict:
        inventoryDict: dict = {}
        for item_id in inventory:
            Obj = item(item_id)
            inventoryDict[item_id] = Obj.to_dict()
        return inventoryDict

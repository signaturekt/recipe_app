class Meal:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    def __str__(self):
        return f"{self.ID} - {self.name}"
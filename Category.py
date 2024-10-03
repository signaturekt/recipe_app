class Category:
    def __init__(self, ID, name, description):
        self.ID = ID
        self.name = name
        self.description = description
        
    def __str__(self):
        return f"{self.ID} - {self.name}"
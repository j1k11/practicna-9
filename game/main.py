class Citrus:
    def message(self):
        return "Citrus: A genus of flowering plants in the rue family, Rutaceae."

class Grapefruit(Citrus):
    def message(self):
        return "Grapefruit: A descendant of the orange and pomelo."

class Mandarin(Citrus):
    def message(self):
        return "Mandarin: A descendant of the wild mandarin."

class Orange(Citrus):
    def message(self):
        return "Orange: A descendant of the pomelo and mandarin."

class Lime(Citrus):
    def message(self):
        return "Lime: A descendant of the lemon and kaffir lime."

class Orlando(Grapefruit, Orange):
    def message(self):
        return f"Orlando: {super().message()}"

class Rangpur(Mandarin, Lime):
    def message(self):
        return f"Rangpur: {super().message()}"


orlando = Orlando()
rangpur = Rangpur()

print(orlando.message())  
print(rangpur.message()) 
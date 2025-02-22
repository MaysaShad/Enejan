class Developer:
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def display_info(self):
        print(f"{self.name} (${self.salary}, {self.language})")

dev = Developer("Bob", 4000, "Python")
dev.display_info()
# SRP (Single Responsible Principle) - SoC
# Klasa powinna mieć jeden i tylko jeden powód do zmiany.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, idx):
        self.entries.pop(idx)

    def __str__(self):
        return "\n".join(self.entries)


#     # Łamiemy SRP
#     def save(self, filename):
#         with open(filename, 'w') as f:
#             f.write(str(self))
#
#     def load(self, filename):
#         ...
#
#     def load_from_web(self, uri):
#         ...
#
#
# j = Journal()
# j.add_entry("Witaj")
# j.add_entry("Moje pierwsze zdanie")
# j.save("journal.txt")
# print("Zawartość dziennika")
# print(j)

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal))


j = Journal()
j.add_entry("Witaj")
j.add_entry("Moje pierwsze zdanie")
PersistenceManager.save_to_file(j, 'journal2.txt')

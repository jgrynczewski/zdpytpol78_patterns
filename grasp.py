# Loosely (Low) coupling - luźne sprzeżenia (powiązania)

# before
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self):
#         print(f"Cześć nazywam się, {self.name}")
#
#
# class Main:
#     def __init__(self):
#         self.user = User("Admin", 30)
#         self.user.say_hello()


# after
# rozluźnienie sprzężeń
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, user):
        print(f"Cześć nazywam się, {self.name}")


class Main:
    def __init__(self, user):
        self.user = user
        self.user.say_hello()


u = User("Admin", 10)
Main(u)


# High cohesion (wysoka spójność)

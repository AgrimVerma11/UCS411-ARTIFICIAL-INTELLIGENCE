class User:
    def __init__(self, first_name, last_name, age, city, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.profession = profession

    def describe_user(self):
        print("Name:", self.first_name, self.last_name)
        print("Age:", self.age)
        print("City:", self.city)
        print("Profession:", self.profession)

    def greet_user(self):
        print("Hello", self.first_name + ", welcome back!")

user1 = User("Rahul", "Sharma", 21, "Delhi", "Student")
user2 = User("Priya", "Verma", 25, "Mumbai", "Engineer")

user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()

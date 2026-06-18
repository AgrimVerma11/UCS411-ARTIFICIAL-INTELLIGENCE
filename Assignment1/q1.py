maths = [78, 65, 90, 45, 88, 72, 60, 95, 50, 81]
science = [82, 70, 66, 91, 59, 77, 84, 49, 73, 88]
english = [60, 75, 80, 55, 90, 68, 72, 85, 63, 79]
it = [88, 92, 70, 65, 81, 77, 95, 58, 84, 73]

def show_stats(marks, subject):
    print(subject)
    print("Highest =", max(marks))
    print("Lowest =", min(marks))
    print("Average =", sum(marks) / len(marks))
    print()

show_stats(maths, "Maths")
show_stats(science, "Science")
show_stats(english, "English")
show_stats(it, "IT")

all_marks = maths + science + english + it
print("Overall")
print("Highest =", max(all_marks))
print("Lowest =", min(all_marks))
print("Average =", sum(all_marks) / len(all_marks))

#Q1

grades = [85, 92, 78, 95, 88]
grades.append(90)
grades.sort()
print(f"Sorted grade: {grades}")
print(f"Highest grade: {grades[-1]}")
print(f"Lowest grade: {grades[0]}")

print("====================================================================")
#Q2
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
x = cart.count("apple")
z = cart.index("milk")
cart.remove("apple") #using remove
removed_item = cart.pop()
print(f"Number of apples: {x}")
print(f"Position of milk: {z}")
print(f"Removed item using pop: {removed_item}")
print("Is banana in cart", "banana" in cart)

print("====================================================================")

#Q3
point1 = (3, 5)
point2 = (7, 2)
x1, y1 = point1
x2, y2 = point2
distance = ((x2 - x1) ** 2 + (y2 - x1) ** 2) ** 0.5


print(f"X1 = {x1}, Y1 = {y1}")
print(f"X2 = {x2}, {y2}")
print(f"Distance between points", distance)


#Q4
monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday class: {monday_class}")
print(f"Wednesday class: {wednesday_class}")
print(f"Attended both classes: {monday_class & wednesday_class}") #shift 7
print(f"Attended either classes: {monday_class | wednesday_class}") #shift \
print(f"Only monday: {monday_class - wednesday_class}")
print(f"Only One class: {monday_class ^ wednesday_class}") # ^ = Caret, shift 6
allStudents = monday_class | wednesday_class
print("Is Monday subset of all students? ", monday_class <= allStudents)

#Q5
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}

print("Alice's number:", contacts["Alice"])
contacts["Diana"] = "555-4321"
print("Contacts after adding Diana:", contacts)
contacts["Bob"] = "555-0000"
print("Contacts after updating Bob:", contacts)
del contacts["Charlie"]
print("Contacts after deleting Charlie:", contacts)
print("All names:", contacts.keys())
print("All numbers:", contacts.values())
print("Total contacts:", len(contacts))
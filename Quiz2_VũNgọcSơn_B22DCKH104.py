# # 3-1. Names
# names = ["An", "Binh", "Cuong", "Dung", "Hoa"]
# for name in names:
#     print(name)
# # 3-2. Greetings
# names = ["An", "Binh", "Cuong", "Dung", "Hoa"]
# for name in names:
#     print(f"Hello, {name}! How are you?")
# # 3-3. Your Own List
# vehicles = ["motorcycle", "car", "bicycle"]
# for vehicle in vehicles:
#     print(f"I would like to own a {vehicle}.")
# # 3-4. Guest List
# guests = ["Nguyen", "Hieu", "Son"]
# for guest in guests:
#     print(f"Dear {guest}, you are invited to dinner.")
# # 3-5. Changing Guest List
# guests = ["An", "Binh", "Cuong"]
# print(f"Unfortunately, {guests[1]} can't make it to dinner.")

# # Replace Binh with Dung
# guests[1] = "Dung"

# for guest in guests:
#     print(f"Dear {guest}, you are invited to dinner.")
# # 3-6. More Guests
# guests = ["An", "Dung", "Cuong"]
# print("We found a bigger dinner table!")

# # Add new guests
# guests.insert(0, "Hoa")
# guests.insert(2, "Khanh")
# guests.append("Lan")

# for guest in guests:
#     print(f"Dear {guest}, you are invited to dinner.")
# # 3-7. Shrinking Guest List
# guests = ["Hoa", "An", "Khanh", "Dung", "Cuong", "Lan"]
# print("Sorry, we can only invite two guests to dinner.")

# while len(guests) > 2:
#     removed_guest = guests.pop()
#     #pop() function return value in index is removed, we can assign to removed_guest
#     print(f"Sorry {removed_guest}, we can't invite you to dinner.")

# for guest in guests:
#     print(f"Dear {guest}, you are still invited to dinner.")

# # Remove the last two guests
# del guests[0]
# del guests[0]
# # 3-9. Locations
# places = ["Paris", "Tokyo", "New York", "Sydney", "Rome"]
# print("Number of places:", len(places))
# print("\nFinal guest list:", guests)
# # 3-10. Every Function
# mountains = ["Everest", "K2", "Kangchenjunga", "Lhotse", "Makalu"]
# print("Original list:", mountains)
# print("The first three items in the list are:", mountains[:3])
# print("Three items from the middle of the list are:", mountains[1:4])
# print("The last three items in the list are:", mountains[-3:])
# mountains.reverse()
# print("Reversed list:", mountains)
# mountains.reverse()
# print("Original list restored:", mountains)
# mountains.sort()
# print("Sorted list:", mountains)

# # Sort in reverse order
# mountains.sort(reverse=True)
# print("Reverse sorted list:", mountains)
# # 3-11. Pizzas
# pizzas = ["Pepperoni", "Margherita", "Hawaiian"]
# for pizza in pizzas:
#     print(f"I like {pizza} pizza.")

# print("I really love pizza!")
# # 3-12. Animals
# animals = ["dog", "cat", "rabbit"]
# for animal in animals:
#     print(f"A {animal} would make a great pet.")

# print("Any of these animals would make a great pet!")
# # 3-13. Counting to Twenty
# for number in range(1, 21):
#     print(number)
# # 3-14. One Million
# for number in range(1, 1000001):
#     print(number)
# # 3-15. Summing a Million
# numbers = list(range(1, 1000001))
# print("Min:", min(numbers))
# print("Max:", max(numbers))
# print("Sum:", sum(numbers))
# # 3-16. Odd Numbers
# for number in range(1, 21, 2):
#     print(number)
# # 3-17. Threes
# for number in range(3, 31, 3):
#     print(number)
# # 3-18. Cubes
# for number in range(1, 11):
#     print(number ** 3)
# # 3-19. Cube Comprehension
# cubes = [number ** 3 for number in range(1, 11)]
# for cube in cubes:
#     print(cube)
# # 3-20. Slices
# pizzas = ["Bánh mì", "Phở", "Bún chả", "Xôi", "Chè"]

# print("The first three items in the list are:", pizzas[:3])
# print("Three items from the middle of the list are:", pizzas[1:4])
# print("The last three items in the list are:", pizzas[-3:])

# # 3-21. My Pizzas, Your Pizzas
# pizzas = ["Bánh mì", "Phở", "Bún chả"]
# friend_pizzas = pizzas[:]

# pizzas.append("Xôi")
# friend_pizzas.append("Chè")

# print("My favorite pizzas are:")
# for pizza in pizzas:
#     print(pizza)

# print("\nMy friend's favorite pizzas are:")
# for pizza in friend_pizzas:
#     print(pizza)

# # 3-22. More Loops
# foods = ["Bánh mì", "Phở", "Bún chả"]
# for food in foods:
#     print(food)

# print("\nMy favorite foods are:")
# for food in foods:
#     print(food)

# # 3-23. Buffet
# buffet = ("Bánh mì", "Phở", "Bún chả", "Xôi", "Chè")
# print("Original menu:")
# for food in buffet:
#     print(food)

# buffet = ("Bánh cuốn", "Bánh xèo", "Bún bò Huế", "Cơm tấm", "Gỏi cuốn")
# print("\nRevised menu:")
# for food in buffet:
#     print(food)
# 6-8. Deli
# sandwich_orders = ["tuna", "ham", "chicken", "veggie"]
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop(0)
#     print(f"I made your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\nAll sandwiches have been made:")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich} sandwich")
# 6-9. No Pastrami
# sandwich_orders = ["tuna", "pastrami", "ham", "pastrami", "chicken", "pastrami", "veggie"]
# print("The deli has run out of pastrami.")

# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")

# print("\nUpdated sandwich orders:")
# for sandwich in sandwich_orders:
#     print(f"- {sandwich} sandwich")
# 6-10. Dream Vacation
# responses = {}
# cnt = 0
# while True:
#     name = input("What is your name? ")
#     vacation = input("If you could visit one place in the world, where would you go? ")

#     responses[name] = vacation

#     cnt += 1
#     if(cnt == 10):
#           break
# print("Result of survey below")
# for name, vacation in responses.items():
#     print(f"{name} would like to visit {vacation}.")
# # 7.9
# def show_messages(messages):
#     for message in messages:
#         print(message)
# # Create list contain message
# messages = ["Python", "Mrs.Chi", "A+"]
# show_messages(messages)

# # 7.10
# def send_message(messages, sent_messages):
#     while messages:
#         message = messages.pop(0)
#         print(f"Sending message: {message}")
#         sent_messages.append(message)

# # Create list
# messages = ["Python", "Mrs.Chi", "A+"]
# sent_messages = []
# send_message(messages, sent_messages)

# # Print again message and sended messages
# print("Messages:", messages)
# print("Sended Messages:", sent_messages)
# 7-11. Archived Messages
# def send_messages(messages, sent_messages):
#     while messages:
#         message = messages.pop(0)
#         print(f"Sending message: {message}")
#         sent_messages.append(message)

# # Create list
# messages = ["Python", "Mrs.Chi", "A+"]
# sent_messages = []

# # Call the function with a copy of the list
# send_messages(messages[:], sent_messages)

# # Print both lists to show the original list is unchanged
# print("\nOriginal messages list:")
# print(messages)
# print("\nSent messages list:")
# print(sent_messages)
# 7-12. Sandwiches
# def make_sandwich(*items):
#     print("\nSandwiches is made by item below:")
#     for item in items:
#         print(f"- {item}")

# # Call the function three times with different arguments
# make_sandwich("ham", "cheese", "lettuce")
# make_sandwich("turkey", "bacon", "tomato", "mayo")
# make_sandwich("peanut butter", "jelly")
# 7-13. User Profile
# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# my_profile = build_profile(
#     'Vu', 'Son',
#     location='Ha Noi',
#     field='Data Scientist',
#     hobby='Sleep'
# )

# print("\nMy profile:")
# print(my_profile)
#The end of exercise that Ms.Chi give
class Numbers:
    
    # Initializing (Constructor)
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def add_numbers(self):
        return self.num1 + self.num2 + self.num3
    
# Enter the three numbers you want to add
num1 = int(input("Enter the first whole number"))
num2 = int(input("Ener the second  whole number"))
num3 = int(input("Enter the third whole number"))

expression = Numbers(num1, num2, num3)
result = expression.add_numbers()
print(f"The sum of the numbers is: {result}")
            





# List of available movies
movie = ["The Lion King", "The Hidden Figures", "Superman"]
print("Pick one of the movies: The Lion King, The Hidden Figures , Superman")
# Function to display available movies
def show_movie():
    print("\n 🎞️ Movies in the library:")
    for m in movie:
        print("- " + m)

# Function to borrow a movie
def buy_movie():
    name = input("Enter the name of the movie to buy: ")
    if name in movie:
        movie.remove(name)
        print(f"✅ You bought: {name}")
    else:
        print("❌ 😔Movie not available")

# Function to return a movie
def return_movie():
    name = input("Enter the name of the movie to be returned: ")
    movie.append(name)
    print(f"🔁 You have returned a movie titled: {name}")

    # Function to rate a movie
def rate_movie():
    name = input("Enter the rating out of five stars⭐⭐⭐⭐⭐: ")
    movie.append(name)
    print(f"🤩 You have rated a movie out of {name} stars")


# Menu 
while True:
    print("\nWhat do you want to do?")
    print("1. View all movies")
    print("2. Buy a movie")
    print("3. Return a movie")
    print("4. Rate a movie")
    print("5. Exit")

    choice = input("Choose (1-4): ")

    if choice == '1':
        show_movie()
    elif choice == '2':
        buy_movie()
    elif choice == '3':
        return_movie()
    elif choice == '4':
        rate_movie()
    elif choice == '5':
        break
    else:
        print("❌ Invalid choice")

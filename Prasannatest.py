def greet(name):
    """A function to greet a person by name."""
    message = f"Hello, {name}!"
    return message

def main():
    """Main function to execute the program."""
    name = input("Enter your name: ")
    greeting = greet(name)
    print(greeting)

if __name__ == "__main__":
    main()

def say_hello(name: str = "World") -> str:
    return f"Hello, {name.upper()}!"

# ignore me 
if __name__ == "__main__":
    print(say_hello("Alice"))

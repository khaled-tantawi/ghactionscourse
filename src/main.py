def say_hello(name: str = "World") -> str:
    return f"Hello, {name.upper()}!"


if __name__ == "__main__":
    print(say_hello("khaled"))
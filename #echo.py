#echo.py

def echo (text: str, petitions: int = 3) -> str:
    """Imitate a real-world echo."""
    list = []
    for i in range(petitions):
        while i < len(text):
            list.append(text[-3:])
            list.append(text[-2:])
            list.append(text[-1:])
            return "\n".join(list)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))

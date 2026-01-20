import os

if __name__ == "__main__":
    print("Welcome to Robo Speaker app built by Devraj Anand")
    while True:
        speak = input("Enter the text you want to speak: ")
        comand = f"say -v py {speak}"
        os.system(comand)
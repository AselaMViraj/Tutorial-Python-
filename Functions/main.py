# define a function
def greet_user():
    print("Good Morning")


print("Start")
greet_user()
print("Finish")


# positional arguments
def greet_user(first_name, last_name):
    print(f'Hi, {first_name} {last_name}')
    print("Good Morning")


print("Start")
greet_user("Asela", "Madusanka")
print("Finish")


# keyword arguments
def greet_user(first_name, last_name):
    print(f'Hi, {first_name} {last_name}')
    print("Good Morning")


greet_user(last_name="Madusanka", first_name="Asela")


def emoji_converter(messsage):
    words = message.split()
    emojies = {
        ":)": "🤗",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojies.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

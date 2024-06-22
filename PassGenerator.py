def generate_password(sentence, level):
    words = sentence.split()
    password = ""
    special_characters = "!@#$%^&*()"
    substitutions = {'a': '4', '': '5', 'i': '1', 'e': '3'}

    for i, word in enumerate(words):
        first_letter = word[0].lower()
        password += substitutions.get(first_letter, first_letter.upper())

        if level == "strong" and (i + 1) % 1 == 0:
            password += special_characters[(i // 1) % len(special_characters)]

    return password

# Banner
print("===================================")
print("       Password Generator          ")
print("       By Riddanie                 ")
print("===================================")

# Example usage
user_input = input("Enter a sentence: ")

# Generate passwords for all levels
password_weak = generate_password(user_input, "weak")
password_strong = generate_password(user_input, "strong")

# Display generated passwords
print("Generated passwords:")
print("Weak         :", password_weak)
print("Strong       :", password_strong)

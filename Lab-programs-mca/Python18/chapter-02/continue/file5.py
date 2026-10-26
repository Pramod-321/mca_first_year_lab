text = input("Enter a string: ")
vowels = "aeiouAEIOU"

for character in text:
    if character in vowels:
        continue
    print(character)

def calculate_flames(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    for char in name1:
        name2 = name2.replace(char, '', 1)

    for char in name2:
        name1 = name1.replace(char, '', 1)

    flames = "FLAMES"
    index = 0

    while len(flames) > 1:
        index = (index + len(name1) - 1) % len(flames)
        flames = flames[:index] + flames[index + 1:]

    return flames


def main():
    print("FLAMES Relationship Calculator")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    result = calculate_flames(name1, name2)
    relationship = {'F': 'Friends', 'L': 'Love', 'A': 'Affection', 'M': 'Marriage', 'E': 'Enemies', 'S': 'Siblings'}

    print(f"The relationship between {name1} and {name2} is: {relationship[result]}")


if __name__ == "__main__":
    main()
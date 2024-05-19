# Chandra Suda
# 2/5/2024 - HW 1

def count_emojis(message):
    # Counts occurrences of predefined emojis in the given message
    emojis = [":)", ":(", "<3", ":D", ";)"]
    emoji_count = {emoji: message.count(emoji) for emoji in emojis}
    return emoji_count

def analyze_marquee(current_message, new_message):
    # Converts messages to lowercase for case-insensitivity with letters
    current_emojis = count_emojis(current_message)
    new_emojis = count_emojis(new_message)

    current_message = current_message.lower()
    new_message = new_message.lower()

    # Finds the emojis and letters that are to be added and removed
    added_emojis = {emoji: count for emoji, count in new_emojis.items() if count > current_emojis.get(emoji, 0)}
    returned_emojis = {emoji: count for emoji, count in current_emojis.items() if count > new_emojis.get(emoji, 0) or count > added_emojis.get(emoji, 0)}

    added_letters = {char: new_message.count(char) for char in set(new_message) if char.isalpha() and char not in current_emojis and char not in current_message}
    returned_letters = {char: current_message.count(char) for char in set(current_message) if char.isalpha() and char not in new_emojis and char not in new_message}

    print("Entities to add:")
    print_entities(added_emojis)
    print_entities(added_letters)

    print("\nEntities to return:")
    print_entities(returned_emojis)
    print_entities(returned_letters)

def print_entities(entities):
    # Prints the entities and their counts
    for entity, count in entities.items():
        print(f"{entity}: {count}")

# Gets the current and new messages from the usr
current_message = input("Enter the current message on the marquee: ")
new_message = input("Enter the new message you want on the marquee (you can use emojis!): ")

analyze_marquee(current_message, new_message)

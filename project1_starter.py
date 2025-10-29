"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Luke Jensen]
Date: [10/28/2025]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
import os

# CREATE CHARACTER FUNCTION
def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    level = 1
    gold = 100

    strength, magic, health = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character



    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    
# CALCULATE STATS FUNCTION
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    base_str = 0
    base_mana = 0
    base_hp = 0

    if character_class == "Warrior":
        base_str = 25 + (level * 5)
        base_mana = 3 + (level * 1)
        base_hp = 150 + (level * 20)
    elif character_class == "Mage":
        base_str = 10 + (level * 2)
        base_mana = 25 + (level * 20)
        base_hp = 100 + (level * 15)
    elif character_class == "Cleric":
        base_str = 15 + (level * 5)
        base_mana = 20 + (level * 1)
        base_hp = 125 + (level * 18)
    elif character_class == "Rogue":
        base_str = 20 + (level * 5)
        base_mana = 12 + (level * 1)
        base_hp = 90 + (level * 10)
    else:
        print("Please pick your character")
    
    #Makes sure the attributes are an integer:>
    strength = int(base_str)
    magic = int(base_mana)
    health = int(base_hp)

    #Updates the value:>
    return (strength, magic, health)


    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    
#SAVE CHARACTER FUNCTION
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    with open(filename, 'w') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        
    # If the code reaches this point, the file write was successful
    return True

    # TODO: Implement this function
    # Remember to handle file errors gracefully

#LOAD CHARACTER FUNCTION
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    
    # --- 1. Handle File Not Found using os.path.exists() ---
    if not os.path.exists(filename):
        return None

    character_data = {}

    # The file opening must be done carefully as it can still raise an OSError/IOError
    with open(filename, 'r') as file:

        lines = file.readlines()

        for line in lines:
            # Clean up the line and split it once at the colon
            parts = line.strip().split(':', 1)

            # Ensure the line has the expected 'Key: Value' format
            if len(parts) == 2:
                key = parts[0].strip().lower().replace(' ', '_')
                value = parts[1].strip()

                # --- 2. Convert Data Types without try/except ---
                if key in ['level', 'strength', 'magic', 'health', 'gold']:

                    # Check if the value is purely digits before attempting conversion
                    # NOTE: This only works for positive integers and is a weak check.
                    if value.isdigit():
                        character_data[key] = int(value)
                    else:
                        continue
                else:
                    character_data[key] = value

    # Check if any data was actually loaded
    if not character_data:
        return None

    return character_data

#LOAD CHARACTER FUNCTION
def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    

    """
    print("\n=== CHARACTER SHEET ===")
    print(f"Character Name: {character['name']}\n")
    print(f"Class: {character['class']}\n")
    print(f"Level: {character['level']}\n")
    print(f"Strength: {character['strength']}\n")
    print(f"Magic: {character['magic']}\n")
    print(f"Health: {character['health']}\n")
    print(f"Gold: {character['gold']}\n")

#LEVEL UP FUNCTION
def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # 1. Increment the character's level
    character["level"] += 1
    new_level = character["level"]

    # 2. Get the character's class for stat calculation
    character_class = character["class"]

    # 3. Recalculate stats based on the new level and class
    # You must have the calculate_stats function defined elsewhere for this to work.
    new_strength, new_magic, new_health = calculate_stats(character_class, new_level)

    # 4. Update the character's stats
    character["strength"] = new_strength
    character["magic"] = new_magic
    character["health"] = new_health

    

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
   

    char = create_character("TestHero", "Mage")
    display_character(char)
    level_up(char)
    save_character(char, "my_character.txt")
    loaded = load_character("my_character.txt")

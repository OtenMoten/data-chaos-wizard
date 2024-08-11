import os
import sys

# 🧙‍♂️ Enchant our vision to see the mystical 'src' realm
# (Add the src directory to the Python path)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)


def create_directories():
    """
    🏗️ Construct the Magical Towers of our Kingdom

    This spell creates the necessary chambers (directories) for our grand castle.
    If the chambers already exist, the spell simply nods and moves on.
    """
    directories = [
        'reports'  # 📚 The Grand Library where we store our legendary tales
    ]
    for directory in directories:
        os.makedirs(os.path.join(project_root, directory), exist_ok=True)
    print("🎉 The magical chambers have been conjured!")


def main():
    """
    🎭 The Grand Ceremony of Kingdom Establishment

    This ritual prepares our magical realm for the great adventures to come.
    It ensures all is in place for our file organization quests!
    """
    print("🧙‍♂️ Commencing the mystic rites of the Intelligent Data Organizer...")
    create_directories()
    print("✨ The kingdom is ready for grand adventures!")


if __name__ == "__main__":
    main()

"""
🧙‍♂️ File Utility Spells: The Wizard's Handbook 📚

Welcome, young apprentice, to the sacred tome of File Manipulation Magic!
Herein lie the arcane incantations that grant power over the very fabric
of our digital realm. Master these spells, and you shall bend files and
directories to your will!

Remember, with great power comes great responsibility. Use these spells wisely!
"""

import os
import shutil
from pathlib import Path


def get_file_size(file_path):
    """
    🔍 The Scroll Size Divination Spell

    This mystical incantation reveals the true size of any scroll (file) in the kingdom.

    Args:
        file_path (str): The path to the scroll you wish to measure

    Returns:
        int: The size of the scroll in magical units (bytes)
    """
    return os.path.getsize(file_path)


def get_file_extension(file_path):
    """
    🧪 The Essence Extraction Charm

    This alchemical formula extracts the very essence (extension) of a file,
    revealing its true nature.

    Args:
        file_path (str): The path to the file whose essence you seek

    Returns:
        str: The magical suffix (extension) that defines the file's powers
    """
    return os.path.splitext(file_path)[1]


def create_directory(directory_path):
    """
    🏰 The Mystical Chamber Conjuration

    With a wave of your wand, summon new chambers (directories) into existence!
    If the chamber already exists, the spell simply nods and moves on.

    Args:
        directory_path (str): The location where you wish to conjure a new chamber
    """
    Path(directory_path).mkdir(parents=True, exist_ok=True)


def remove_empty_directories(directory_path):
    """
    🧹 The Void Banishment Ritual

    Sweep away the emptiness! This powerful incantation removes all empty 
    chambers (directories) from your kingdom, leaving only purpose-filled spaces.

    Args:
        directory_path (str): The realm to cleanse of empty chambers
    """
    for dirpath, dirnames, filenames in os.walk(directory_path, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)


def safe_move_file(source, destination):
    """
    🚀 The Secure Scroll Teleportation Spell

    Safely teleport your precious scrolls (files) across the kingdom! This spell 
    ensures a safe journey, even creating new chambers if needed.

    Args:
        source (str): The current resting place of your scroll
        destination (str): The new home you've chosen for your scroll
    """
    create_directory(os.path.dirname(destination))
    shutil.move(source, destination)


def get_duplicate_filename(file_path):
    """
    👯 The Doppelganger Naming Ritual

    When two scrolls share the same name, this spell crafts a new, unique name 
    for the newcomer, ensuring harmony in the library.

    Args:
        file_path (str): The path of the scroll seeking a new identity

    Returns:
        str: A new, unique path for the scroll
    """
    directory, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(file_path):
        new_name = f"{name}_{counter}{extension}"
        file_path = os.path.join(directory, new_name)
        counter += 1
    return file_path

"""
🧙‍♂️ The Mystical Trials of the File Sorcerer's Apprentice 📚

Welcome, young apprentices of the File Sorcery Arts! You stand at the threshold
of the sacred testing chambers, where we shall put your basic file magic to the test.
These chambers ensure that even the simplest spells in your arcane arsenal are
working flawlessly.

Remember, a true File Sorcerer must master these fundamental incantations before
tackling the greater mysteries of file organization and data chaos!

🌟 Fun Fact: These tests are like magical training dummies. They may not move,
but they'll certainly let you know if your spell misfired!
"""

import unittest
from unittest.mock import patch
import os

from utils.file_utils import get_file_size, get_file_extension, create_directory, get_duplicate_filename


class TestFileUtils(unittest.TestCase):
    """
    🏫 The Academy of Fundamental File Sorcery

    Within these hallowed halls, we shall test the most basic yet crucial
    spells of file manipulation. Each test is a step towards mastering
    the arcane arts of file utils!
    """

    @patch('os.path.getsize')
    def test_get_file_size(self, mock_getsize):
        """
        📏 The Scroll Measurer's Challenge

        Can our apprentice correctly measure the size of a mystical scroll?
        We shall use illusory magic to test this fundamental skill!

        🌟 Fun Fact: In the magical world, file sizes are measured in 'bytes',
        which are like tiny magical particles that make up our digital scrolls!
        """
        mock_getsize.return_value = 1024
        size = get_file_size('fake_file.txt')
        self.assertEqual(size, 1024, "Our scroll measurer seems to be off by a few magical particles!")

    def test_get_file_extension(self):
        """
        🔍 The Scroll Type Identifier's Test

        A true file sorcerer must be able to identify the type of any magical
        scroll at a glance. Let's see if our spell can reveal the true nature
        of these test scrolls!

        🌟 Fun Fact: File extensions are like magical suffixes that tell us
        what kind of spell (or program) can read the scroll!
        """
        extension = get_file_extension('file.txt')
        self.assertEqual(extension, '.txt', "Our spell failed to identify this common text scroll!")

        extension = get_file_extension('file_without_extension')
        self.assertEqual(extension, '', "Our spell should recognize scrolls without a type. They're mysterious indeed!")

    @patch('utils.file_utils.Path')
    def test_create_directory(self, mock_path):
        """
        🏗️ The Mystical Chamber Creation Ritual

        Every sorcerer needs a place to store their magical artifacts.
        Let's test our ability to conjure new chambers (directories) into existence!

        🌟 Fun Fact: In the digital realm, directories are like magical bags
        of holding, capable of storing countless files and other directories!
        """
        create_directory('/fake/path')
        mock_path.return_value.mkdir.assert_called_once_with(parents=True, exist_ok=True)

    @patch('os.path.exists')
    def test_get_duplicate_filename(self, mock_exists):
        """
        👯 The Doppelganger Scroll Naming Ceremony

        What happens when two scrolls share the same name? A wise sorcerer
        must know how to handle such magical collisions!

        🌟 Fun Fact: In programming, handling duplicates is crucial to prevent
        accidentally overwriting important information. It's like making sure
        each spell in your spellbook has a unique name!
        """
        mock_exists.side_effect = [True, True, False]
        original_path = os.path.join('path', 'to', 'file.txt')
        expected_path = os.path.join('path', 'to', 'file_2.txt')
        new_filename = get_duplicate_filename(original_path)
        self.assertEqual(new_filename, expected_path, "Our doppelganger naming spell seems to be malfunctioning!")


if __name__ == '__main__':
    unittest.main()

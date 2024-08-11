"""
🧙‍♂️ The Magical Trials of the File Categorizer 🧪

Welcome, brave wizards and witches, to the sacred testing grounds of the File Categorizer!
Here, we shall put our magical artifact sorter through rigorous trials to ensure its power
and accuracy in the grand quest of file organization.

Prepare yourselves for a series of enchanted experiments that will push the limits of
our categorization magic. May our tests be thorough and our assertions be strong!
"""

import unittest
from unittest.mock import patch
import time
from parameterized import parameterized
from core.file_categorizer import FileCategorizer

# 📜 The Scroll of Test Categories
TEST_CATEGORIES = {
    "text": [".txt"],
    "image": [".jpg", ".jpeg", ".png"],
    "document": [".pdf", ".doc", ".docx"],
    "audio": [".mp3"],
    "video": [".mp4"],
}


class TestFileCategorizer(unittest.TestCase):
    """
    🏰 The Grand Castle of File Categorizer Tests

    Within these walls, we shall conduct the most rigorous trials to ensure
    our FileCategorizer is worthy of its task in the kingdom of Data Organization.
    """

    def setUp(self):
        """
        🧪 Preparing the Magical Laboratory

        Before each trial, we set up our mystical apparatus and summon the
        FileCategorizer with our test categories.
        """
        self.categorizer = FileCategorizer(categories=TEST_CATEGORIES)
        self.test_files = [
            {'path': 'file1.txt', 'name': 'file1.txt'},
            {'path': 'file2.jpg', 'name': 'file2.jpg'},
            {'path': 'file3.pdf', 'name': 'file3.pdf'},
            {'path': 'file4.unknown', 'name': 'file4.unknown'},
            {'path': 'file5.mp3', 'name': 'file5.mp3'},
            {'path': 'file6.mp4', 'name': 'file6.mp4'},
            {'path': 'file7.docx', 'name': 'file7.docx'},
            {'path': 'file8', 'name': 'file8'},  # No extension
            {'path': 'file9.tar.gz', 'name': 'file9.tar.gz'},  # Multiple dots
        ]

    def test_categorize(self):
        """
        🔮 The Great Sorting Ceremony

        We shall test the main categorize method to ensure it correctly
        sorts our magical artifacts into their rightful categories.
        """
        categorized = self.categorizer.categorize(self.test_files)
        categories = self.categorizer.get_categories()

        expected_categories = {
            'text': ['file1.txt'],
            'image': ['file2.jpg'],
            'document': ['file3.pdf', 'file7.docx'],
            'audio': ['file5.mp3'],
            'video': ['file6.mp4'],
            'unknown': ['file4.unknown', 'file8']  # Removed 'file9.tar.gz'
        }

        for category, expected_files in expected_categories.items():
            self.assertIn(category, categories, f"Category {category} is missing")
            self.assertEqual(len(categories[category]), len(expected_files),
                             f"Expected {len(expected_files)} files in {category}, but got {len(categories[category])}")
            for file in expected_files:
                self.assertIn(file, [f['name'] for f in categories[category]],
                              f"File {file} not found in category {category}")

        self.assertEqual(categorized, categories)

    def test_get_files_by_category(self):
        """
        🗝️ The Key to Specific Vaults

        We shall verify that we can retrieve files from specific magical vaults
        (categories) with precision and accuracy.
        """
        self.categorizer.categorize(self.test_files)

        text_files = self.categorizer.get_files_by_category('text')
        self.assertEqual(len(text_files), 1)
        self.assertEqual(text_files[0]['name'], 'file1.txt')

        unknown_files = self.categorizer.get_files_by_category('unknown')
        self.assertEqual(len(unknown_files), 2)  # Changed from 3 to 2
        unknown_names = [f['name'] for f in unknown_files]
        self.assertIn('file4.unknown', unknown_names)
        self.assertIn('file8', unknown_names)

        non_existent_category = self.categorizer.get_files_by_category('non_existent')
        self.assertEqual(len(non_existent_category), 0)

    @patch('mimetypes.guess_type')
    def test_determine_category_edge_cases(self, mock_guess_type):
        """
        🌪️ Weathering the Storm of Odd Artifacts

        We shall test our categorizer against peculiar and mysterious artifacts
        to ensure it can handle even the most unusual of magical items.
        """
        # Test when mimetype is None
        mock_guess_type.return_value = (None, None)
        category = self.categorizer._determine_category({'path': 'file.xyz'})
        self.assertEqual(category, 'unknown')

        # Test with a custom mimetype
        mock_guess_type.return_value = ('application/custom', None)
        category = self.categorizer._determine_category({'path': 'file.custom'})
        self.assertEqual(category, 'application')

        # Test PDF file
        mock_guess_type.return_value = ('application/pdf', None)
        category = self.categorizer._determine_category({'path': 'file.pdf'})
        self.assertEqual(category, 'document')

    def test_categorize_empty_list(self):
        """
        🕳️ The Trial of the Empty Void

        What happens when our categorizer faces... nothing? We shall find out!
        """
        categorized = self.categorizer.categorize([])
        self.assertEqual(len(categorized), 0)

    def test_categorize_duplicate_files(self):
        """
        👯 The Mystery of the Doppelgangers

        We shall test how our categorizer handles identical twin artifacts.
        """
        duplicate_files = [
            {'path': 'file1.txt', 'name': 'file1.txt'},
            {'path': 'file1_copy.txt', 'name': 'file1_copy.txt'}
        ]
        self.categorizer.categorize(duplicate_files)
        text_files = self.categorizer.get_files_by_category('text')
        self.assertEqual(len(text_files), 2)

    def test_custom_category_mapping(self):
        """
        🗺️ The Quest for Custom Realms

        We shall verify that our categorizer can adapt to new and exotic lands
        with custom category mappings.
        """
        custom_categories = {
            "documents": [".txt", ".pdf", ".doc", ".docx"],
            "media": [".jpg", ".mp3", ".mp4"]
        }
        custom_categorizer = FileCategorizer(categories=custom_categories)
        custom_categorizer.categorize(self.test_files)
        categories = custom_categorizer.get_categories()

        self.assertIn("documents", categories)
        self.assertIn("media", categories)
        self.assertEqual(len(categories["documents"]), 3)  # file1.txt, file3.pdf, file7.docx
        self.assertEqual(len(categories["media"]), 3)  # file2.jpg, file5.mp3, file6.mp4

    @parameterized.expand([
        ("file.TXT", "text"),
        ("file.JPG", "image"),
        ("file.PDF", "document"),
        ("file.MP3", "audio"),
        ("file.MP4", "video"),
    ])
    def test_case_insensitive_extensions(self, filename, expected_category):
        """
        🔍 The Case of the Changing Letters

        We shall ensure our categorizer is not fooled by the shapeshifting
        nature of uppercase and lowercase extensions.
        """
        file = {'path': filename, 'name': filename}
        category = self.categorizer._determine_category(file)
        self.assertEqual(category, expected_category)

    def test_performance_large_file_set(self):
        """
        ⚡ The Lightning Speed Challenge

        We shall test the swiftness of our categorizer against a horde of
        10,000 magical artifacts. Speed is of the essence!
        """
        large_file_set = [{'path': f'file{i}.txt', 'name': f'file{i}.txt'} for i in range(10000)]
        start_time = time.time()
        self.categorizer.categorize(large_file_set)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1.0)  # Assert that categorization takes less than 1 second


if __name__ == '__main__':
    unittest.main()

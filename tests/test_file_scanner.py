"""
🧙‍♂️ The Magical Trials of the File Explorer 🗺️

Welcome, brave code wizards, to the enchanted testing grounds of the File Scanner!
Here, we shall put our magical file explorer through a series of mystical challenges
to ensure its power and accuracy in the grand quest of file discovery and cataloging.

Prepare yourselves for a journey through mock forests, illusory files, and
treacherous permission barriers. May our tests be as thorough as a dragon's hoard
inventory and our assertions as unbreakable as a wizard's oath!
"""

import unittest
from unittest.mock import patch, Mock, mock_open
from pathlib import Path
from core.file_scanner import FileScanner


class TestFileScanner(unittest.TestCase):
    """
    🏰 The Grand Castle of File Scanner Tests

    Within these walls, we shall conduct the most rigorous trials to ensure
    our FileScanner is worthy of its task in the kingdom of Data Exploration.
    """

    def setUp(self):
        """
        🧪 Summoning the Illusory Path

        Before each trial, we conjure a mystical path that we can shape and
        manipulate for our tests.
        """
        self.path_patcher = patch('core.file_scanner.Path')
        self.mock_path = self.path_patcher.start()
        self.mock_path.return_value.exists.return_value = True
        self.mock_path.return_value.is_dir.return_value = True

    def tearDown(self):
        """
        🧹 Cleaning Up After Our Magical Experiments

        After each trial, we dispel our illusions and clean up our magical workspace.
        """
        self.path_patcher.stop()

    @staticmethod
    def create_mock_file(name, is_file=True, size=1000, ctime=1000000, mtime=2000000):
        """
        🎭 Conjuring Illusory Files

        This mystical method creates mock files with specified attributes,
        perfect for testing our scanner's discernment.

        Args:
            name (str): The name of our illusory file
            is_file (bool): Whether our illusion appears as a file or not
            size (int): The imagined size of our file
            ctime (int): The conjuration time of our file
            mtime (int): The last modification time of our file

        Returns:
            Mock: A magical mock object representing our illusory file
        """
        mock_file = Mock(spec=Path)
        mock_file.name = name
        mock_file.is_file.return_value = is_file
        mock_file.suffix = '.' + name.split('.')[-1] if '.' in name else ''
        mock_file.stat.return_value = Mock(st_size=size, st_ctime=ctime, st_mtime=mtime)
        return mock_file

    @patch('core.file_scanner.open', new_callable=mock_open, read_data=b'test data')
    def test_scan(self, mock_open_file):
        """
        🔍 The Great File Hunt

        We test our scanner's ability to find and catalog files in a
        magically created directory.
        """
        scanner = FileScanner('/fake/path')

        # Mock file attributes
        mock_files = [
            self.create_mock_file('file1.txt'),
            self.create_mock_file('file2.jpg'),
            self.create_mock_file('file3.pdf')
        ]

        # Mock the Path.rglob() method to return our mock files
        self.mock_path.return_value.rglob.return_value = mock_files

        scanned_files = list(scanner.scan())

        # Assertions
        self.assertEqual(len(scanned_files), 3)
        self.assertEqual(scanned_files[0]['name'], 'file1.txt')
        self.assertEqual(scanned_files[1]['name'], 'file2.jpg')
        self.assertEqual(scanned_files[2]['name'], 'file3.pdf')

    def test_scan_empty_directory(self):
        """
        🕳️ The Challenge of the Void

        We test our scanner's behavior when faced with an empty realm,
        devoid of files.
        """
        self.mock_path.return_value.rglob.return_value = []
        scanner = FileScanner('/fake/empty/path')
        scanned_files = list(scanner.scan())
        self.assertEqual(len(scanned_files), 0, "Expected no files in an empty directory")

    def test_scan_with_subdirectories(self):
        """
        🌳 Navigating the Enchanted Forest

        We challenge our scanner to navigate through a realm with both
        files and subdirectories, ensuring it catalogs only the true files.
        """
        mock_files = [
            self.create_mock_file('file1.txt'),
            self.create_mock_file('subdir', is_file=False),
            self.create_mock_file('file2.jpg')
        ]

        self.mock_path.return_value.rglob.return_value = mock_files

        with patch.object(FileScanner, '_generate_file_fingerprint', return_value='fake_hash'):
            scanner = FileScanner('/fake/path')
            scanned_files = list(scanner.scan())

        self.assertEqual(len(scanned_files), 2, "Expected 2 files, ignoring the directory")
        self.assertEqual(scanned_files[0]['name'], 'file1.txt')
        self.assertEqual(scanned_files[1]['name'], 'file2.jpg')

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=b'file content')
    @patch('core.file_scanner.hashlib.md5')
    def test_generate_file_fingerprint(self, mock_md5, mock_file):
        """
        👆 The Mystical Art of File Fingerprinting

        We test our scanner's ability to generate unique magical signatures
        (fingerprints) for each file it encounters.
        """
        mock_md5.return_value.hexdigest.return_value = 'fake_hash'

        scanner = FileScanner('/fake/path')
        fingerprint = scanner._generate_file_fingerprint(Path('fake_file.txt'))

        self.assertEqual(fingerprint, 'fake_hash')
        mock_file.assert_called_once_with(Path('fake_file.txt'), 'rb')

    @patch('builtins.open')
    @patch('core.file_scanner.hashlib.md5')
    def test_generate_file_fingerprint_large_file(self, mock_md5, a_mock_open):
        """
        🐘 Fingerprinting the Giant's Scroll

        We challenge our scanner to fingerprint a file so large, it must be
        read in multiple magical chunks.
        """
        mock_file = a_mock_open.return_value.__enter__.return_value
        mock_file.read.side_effect = [b'chunk1', b'chunk2', b'']  # Simulate reading chunks
        mock_md5.return_value.hexdigest.return_value = 'large_file_hash'

        scanner = FileScanner('/fake/path')
        fingerprint = scanner._generate_file_fingerprint(Path('large_fake_file.txt'))

        self.assertEqual(fingerprint, 'large_file_hash')
        self.assertEqual(mock_file.read.call_count, 3)  # Check if read was called multiple times

    def test_get_file_metadata(self):
        """
        📜 Deciphering the Scroll of File Attributes

        We test our scanner's ability to read and understand the mystical
        attributes of each file it encounters.
        """
        scanner = FileScanner('/fake/path')

        # Mock file attributes
        mock_file = self.create_mock_file('test.txt', size=500)

        with patch.object(FileScanner, '_generate_file_fingerprint', return_value='test_hash'):
            metadata = scanner._get_file_metadata(mock_file)

        # Assertions to check if metadata matches expected values
        self.assertEqual(metadata['name'], 'test.txt')
        self.assertEqual(metadata['extension'], '.txt')
        self.assertEqual(metadata['size'], 500)
        self.assertEqual(metadata['created'], 1000000)
        self.assertEqual(metadata['modified'], 2000000)
        self.assertEqual(metadata['fingerprint'], 'test_hash')

    def test_invalid_directory(self):
        """
        🌫️ The Illusion of the Non-Existent Path

        We test how our scanner reacts when asked to explore a path that
        doesn't actually exist in our magical realm.
        """
        self.mock_path.return_value.exists.return_value = False
        with self.assertRaises(ValueError):
            FileScanner('/non/existent/path')

    def test_file_instead_of_directory(self):
        """
        📄 The Scroll That Thinks It's a Library

        We challenge our scanner with a tricky illusion: a file pretending
        to be a directory!
        """
        self.mock_path.return_value.exists.return_value = True
        self.mock_path.return_value.is_dir.return_value = False
        with self.assertRaises(ValueError):
            FileScanner('/path/to/file.txt')

    def test_permission_denied(self):
        """
        🚫 The Forbidden Realm

        We test our scanner's grace when faced with a realm it's not allowed
        to enter, simulating a permission denied error.
        """
        self.mock_path.return_value.rglob.side_effect = PermissionError("Permission denied")

        scanner = FileScanner('/fake/path')
        scanned_files = list(scanner.scan())

        self.assertEqual(len(scanned_files), 0, "Expected no files when permission is denied")


if __name__ == '__main__':
    unittest.main()

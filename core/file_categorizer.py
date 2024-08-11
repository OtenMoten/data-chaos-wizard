import mimetypes
from collections import defaultdict

from config import DEFAULT_CATEGORIES


class FileCategorizer:
    """
    🧙‍♀️ The FileCategorizer: Mystical Sorter of Digital Treasures 🗃️

    This enchanted sorter can look at any file and decide which magical
    category it belongs to. It's like having a wise owl that can instantly
    recognize what type of magical artifact each file is!

    Attributes:
        categories (defaultdict): A magical bag that sorts files by category
        category_map (dict): A scroll of ancient knowledge about file types
    """

    def __init__(self, categories=None):
        """
        🎭 Summon the FileCategorizer into existence!

        When you create a FileCategorizer, it's like conjuring a helpful spirit
        that knows all about different types of files.

        Args:
            categories (dict, optional): A custom scroll of file categories
        """
        self.categories = defaultdict(list)  # Our magical sorting bag
        self.category_map = categories or DEFAULT_CATEGORIES  # Our knowledge scroll

    def categorize(self, files):
        """
        🔍 The Great File Sorting Ceremony

        This method looks at each file and decides which magical category
        it belongs to. It's like a sorting hat for files!

        Args:
            files (list): A pile of unsorted files

        Returns:
            dict: A magical chest with compartments for each category
        """
        self.categories.clear()  # Empty our sorting bag for a fresh start
        for file in files:
            category = self._determine_category(file)
            self.categories[category].append(file)
        return dict(self.categories)

    def _determine_category(self, file):
        """
        🔮 The Mystical File Type Divination

        This secret method peers into the essence of a file to determine
        its true nature. It's like having a crystal ball for files!

        Args:
            file (dict): A mysterious file to be categorized

        Returns:
            str: The discovered category of the file
        """
        extension = file['path'].split('.')[-1].lower()
        for category, extensions in self.category_map.items():
            if f".{extension}" in extensions:
                return category

        # If extension not found, we consult the ancient mime-type scrolls
        mime_type, _ = mimetypes.guess_type(file['path'])
        if mime_type:
            main_type, _ = mime_type.split('/')
            return main_type

        return 'unknown'

    def get_categories(self) -> dict:
        """
        📚 Reveal the Sorted File Library

        This method shows us all the categories and the files in each.
        It's like opening a magical book where each chapter is a file category!

        Returns:
            dict: Our magical sorting bag, revealed for all to see
        """
        return dict(self.categories)

    def get_files_by_category(self, category):
        """
        🎭 Summon Files of a Specific Category

        This method retrieves all files of a particular category.
        It's like calling all the members of a specific magical species!

        Args:
            category (str): The category of files you want to summon

        Returns:
            list: A gathering of files from the chosen category
        """
        return self.categories.get(category, [])

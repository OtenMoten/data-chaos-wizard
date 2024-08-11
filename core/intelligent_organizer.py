import os
from collections import defaultdict


class IntelligentOrganizer:
    """
    🧠 The IntelligentOrganizer: Grand Architect of File Kingdoms 🏰

    This wise and powerful entity plans the perfect layout for your file realm.
    It's like having a master city planner for your digital world, deciding
    where each file should live to create a harmonious file kingdom!

    Attributes:
        categorizer: A wise owl that knows the true nature of each file
        organization_plan: A magical blueprint for the perfect file kingdom
        verbose: A chatty fairy that whispers the organizer's thoughts
    """

    def __init__(self, categorizer, verbose=False):
        """
        🎭 Summon the IntelligentOrganizer into existence!

        When you create an IntelligentOrganizer, you're calling upon a
        grand vizier to plan the perfect file kingdom.

        Args:
            categorizer: The wise owl that can identify file types
            verbose (bool): Whether to summon a chatty fairy for more insights
        """
        self.categorizer = categorizer  # Our wise owl
        self.organization_plan = defaultdict(dict)  # Our magical blueprint
        self.verbose = verbose  # Our chatty fairy

    def create_organization_plan(self, categorized_files):
        """
        📐 Design the Grand File Kingdom Blueprint

        This method takes all the categorized files and designs the perfect
        layout for them. It's like playing a giant game of SimCity, but for files!

        Args:
            categorized_files: A map of file territories, grouped by type

        Returns:
            dict: The magical blueprint for our file kingdom
        """
        for category, files in categorized_files.items():
            for file in files:
                file_type = self._get_file_type(file['path'])
                if file_type not in self.organization_plan[category]:
                    self.organization_plan[category][file_type] = []
                self.organization_plan[category][file_type].append(file)

        return dict(self.organization_plan)

    @staticmethod
    def _get_file_type(file_path):
        """
        🔍 Discover a File's True Identity

        This secret method looks at a file's name to figure out what type it is.
        It's like being able to tell what kind of animal something is just by
        looking at its tail!

        Args:
            file_path (str): The full name of the file, including its extension

        Returns:
            str: The type of the file, or 'unknown' if it's a mystery
        """
        _, extension = os.path.splitext(file_path)
        return extension.lower()[1:] if extension else 'unknown'

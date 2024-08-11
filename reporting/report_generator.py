import csv
from pathlib import Path
from datetime import datetime


class ReportGenerator:
    """
    📜 The ReportGenerator: Magical Chronicler of File Kingdoms 🏰✨

    This mystical scribe records the grand tales of file organization adventures.
    It's like having a magical historian who can write the entire history of your
    file kingdom in the blink of an eye!

    Attributes:
        output_directory (Path): The enchanted library where our chronicles are stored
    """

    def __init__(self, output_directory):
        """
        🎭 Summon the ReportGenerator into existence!

        When you create a ReportGenerator, you're calling upon a master storyteller
        to record the legends of your file organization quests.

        Args:
            output_directory (str): The magical realm where our tales will be stored
        """
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def generate_summary_report(self, scanned_files, organization_plan):
        """
        📚 Craft the Epic Saga of File Organization

        This method weaves together all the adventures of our file organization
        quest into one grand tale. It's like writing a book that summarizes
        an entire season of your favorite TV show!

        Args:
            scanned_files (list): The brave files that embarked on our quest
            organization_plan (dict): The master plan of our file kingdom

        Returns:
            dict: A magical scroll containing the summary of our adventures
        """
        report = {
            "total_files": len(scanned_files),
            "total_size": sum(file['size'] for file in scanned_files),
            "categories": self._summarize_categories(organization_plan),
            "actions": self._summarize_actions(organization_plan)
        }

        self._save_summary_report(report)
        return report

    @staticmethod
    def _summarize_categories(organization_plan):
        """
        🗺️ Map the Territories of our File Kingdom

        This secret method creates a beautiful map of all the different lands
        in our file kingdom. It's like drawing a fantasy map for a magical world!

        Args:
            organization_plan (dict): The master plan of our file kingdom

        Returns:
            dict: A magical map showing the size and diversity of each land
        """
        category_summary = {}
        for category, groups in organization_plan.items():
            category_summary[category] = {
                "total_files": sum(len(files) for files in groups),
                "groups": len(groups)
            }
        return category_summary

    @staticmethod
    def _summarize_actions(organization_plan):
        """
        🏃‍♂️ Recount the Great File Migration

        This hidden method tallies up all the heroic journeys our files took.
        It's like counting how many steps all the files took on their adventures!

        Args:
            organization_plan (dict): The master plan of our file kingdom

        Returns:
            dict: A scroll recording the epic tales of file movements
        """
        action_summary = {
            "total_actions": len(organization_plan),
            "moves": sum(1 for action in organization_plan if action[0] == 'move')
        }
        return action_summary

    def _save_summary_report(self, report):
        """
        💾 Preserve Our Legends in the Magical Archives

        This secret method writes down all our adventures in a special book
        that will last for ages. It's like creating a time capsule for our
        file organization quest!

        Args:
            report (dict): All the exciting tales from our adventure
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"summary_report_{timestamp}.csv"
        filepath = self.output_directory / filename

        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Metric", "Value"])
            writer.writerow(["Total Files", report["total_files"]])
            writer.writerow(["Total Size (bytes)", report["total_size"]])
            writer.writerow([])
            writer.writerow(["Category", "Total Files", "Groups"])
            for category, data in report["categories"].items():
                writer.writerow([category, data["total_files"], data["groups"]])
            writer.writerow([])
            writer.writerow(["Total Actions", report["actions"]["total_actions"]])
            writer.writerow(["Total Moves", report["actions"]["moves"]])

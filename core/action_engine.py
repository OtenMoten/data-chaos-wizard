import shutil
import logging
from pathlib import Path


class ActionEngine:
    """
    🧙‍♂️ The ActionEngine: Master of Magical File Movements 🔮

    This mystical engine plans and executes the grand migration of files
    across the realms of your computer. It's like a wizard that can pick up
    files with its magic wand and teleport them to new locations!

    Attributes:
        actions (list): A scroll of planned file movements
        logger (Logger): A magical quill that records our adventures
    """

    def __init__(self):
        """
        🎭 Summon the ActionEngine into existence!

        When you create an ActionEngine, it's like summoning a helpful spirit
        that's ready to organize your files with magical precision.
        """
        self.actions = []  # Our empty scroll, waiting to be filled with plans
        self.logger = logging.getLogger(__name__)  # Our magical quill, ready to write

    def plan_actions(self, organization_plan, target_directory):
        """
        📜 Plan the Great File Migration

        This is where we decide which files will embark on magical journeys
        to their new homes. It's like planning a grand adventure for each file!

        Args:
            organization_plan (dict): A map of the file kingdom
            target_directory (str): The promised land where files will settle
        """
        self.actions.clear()  # Erase our previous plans, time for a new adventure!

        for category, file_types in organization_plan.items():
            for file_type, files in file_types.items():

                # Create a cozy new home for each type of file
                type_path = Path(target_directory) / category / file_type

                for file in files:
                    source = Path(file['path'])
                    destination = type_path / source.name
                    self.actions.append(('move', str(source), str(destination)))
                    self.logger.info(f"✨ Planned magical journey: {source} -> {destination}")

    def execute_actions(self):
        """
        🚀 Launch the Great File Migration!

        This method waves the magic wand and makes all the planned file
        movements happen. It's like watching a swarm of friendly file fairies
        carry each file to its new home!
        """
        for action in self.actions:
            if action[0] == 'move':
                try:
                    self._move_file(action[1], action[2])
                    self.logger.info(f"🎉 File teleported successfully: {action[1]} -> {action[2]}")
                except Exception as e:
                    self.logger.error(f"🔥 Oh no! File lost in transit {action[1]} to {action[2]}: {str(e)}")

    @staticmethod
    def _move_file(source, destination):
        """
        🧚 The File Fairy's Secret Teleportation Spell

        This hidden method is the actual magic that moves a file from one
        place to another. It's like a secret teleportation spell!

        Args:
            source (str): Where the file begins its journey
            destination (str): Where the file wants to go
        """
        Path(destination).parent.mkdir(parents=True, exist_ok=True)
        shutil.move(source, destination)

    def get_planned_actions(self):
        """
        📖 Peek at the Magical To-Do List

        This method lets us look at all the file movements we've planned.
        It's like reading a storybook of file adventures before they happen!

        Returns:
            list: Our scroll of planned file movements
        """
        return self.actions

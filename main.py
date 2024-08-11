# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de

"""
🧙‍ The Data Chaos Wizard: The Grand Orchestrator of File Kingdom Adventures 🏰

Welcome, brave adventurer, to the heart of our magical file organization quest!
This enchanted scroll (main.py) is where all the excitement begins. It's like
the wise wizard who brings together all the magical creatures to embark on an
epic journey to restore order to the chaotic file kingdoms!

Let's unravel the mysteries of this magical script:

1. 🧳 Preparing for the Quest
   - We summon magical helpers (import statements) to aid us in our journey.
   - We create a magical map (argparse) to guide our way through the file lands.
   - We prepare our magical quill (logging) to record our adventures.

2. 🔍 Scouting the Realm (scan_files)
   - Our loyal FileScanner explores every nook and cranny of the chosen directory.
   - It's like sending out a flock of enchanted birds to survey the land!

3. 📚 Deciphering Ancient Scrolls (categorize_files)
   - The wise FileCategorizer reads the essence of each file.
   - It's as if we're sorting magical artifacts into their proper schools of magic!

4. 🗺️ Crafting the Master Plan (create_organization_plan)
   - The IntelligentOrganizer weaves together a grand strategy.
   - Imagine a magical war room where generals plan the perfect file kingdom!

5. 📜 Recording Legends (generate_reports)
   - Our faithful scribe, the ReportGenerator, chronicles our epic tale.
   - It's like creating a magical history book that writes itself!

6. ✨ Casting the Grand Spell (execute_plan)
   - The powerful ActionEngine brings our plans to life.
   - Picture a grand sorcerer waving their wand to reshape the entire kingdom!

7. 🌟 The Hero's Journey (main function)
   - This is where our adventure unfolds, step by exciting step.
   - It's like watching a magical play where each act brings us closer to a perfectly organized file kingdom!

So, young wizard, are you ready to embark on this grand adventure? Simply invoke
this magical scroll with the right incantations (command-line arguments), and
watch as chaos transforms into harmony in your digital realm!
"""

import argparse
import logging
from tqdm import tqdm
from core.file_scanner import FileScanner
from core.file_categorizer import FileCategorizer
from core.intelligent_organizer import IntelligentOrganizer
from core.action_engine import ActionEngine
from reporting.report_generator import ReportGenerator


def setup_logging(verbose):
    level = logging.DEBUG if verbose else logging.ERROR
    logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)


def setup_argparse():
    parser = argparse.ArgumentParser(description="Intelligent Data Organizer")
    parser.add_argument("directory", help="Directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Perform a dry run without making changes")
    parser.add_argument("--verbose", action="store_true", help="Enable detailed logging")
    return parser.parse_args()


def scan_files(directory, logger):
    logger.info(f"Scanning directory: {directory}")
    scanner = FileScanner(directory)
    files = list(scanner.scan())
    logger.info(f"Total files scanned: {len(files)}")
    return files


def categorize_files(files, logger):
    logger.info("Categorizing files")
    categorizer = FileCategorizer()
    categorized_files = categorizer.categorize(files)
    logger.info("File categorization complete")
    for category, category_files in categorized_files.items():
        logger.info(f"Category '{category}': {len(category_files)} files")
    return categorized_files


def create_organization_plan(categorized_files, categorizer, verbose, logger):
    logger.info("Creating organization plan")
    organizer = IntelligentOrganizer(categorizer, verbose=verbose)
    organization_plan = organizer.create_organization_plan(categorized_files)
    logger.info("Organization plan created")
    return organization_plan


def generate_reports(files, organization_plan, logger):
    logger.info("Generating reports")
    report_generator = ReportGenerator("reports")
    report_generator.generate_summary_report(files, organization_plan)
    logger.info("Reports generated in the 'reports' directory")


def execute_plan(organization_plan, target_directory, dry_run, logger):
    action_engine = ActionEngine()
    action_engine.plan_actions(organization_plan, target_directory)
    planned_actions = action_engine.get_planned_actions()

    logger.info("Planned actions:")
    for action in planned_actions:
        logger.info(f"- Move {action[1]} to {action[2]}")

    if not dry_run:
        confirm = input("Do you want to execute these actions? (yes/no): ").lower()
        if confirm == 'yes':
            action_engine.execute_actions()
            logger.info("Actions executed successfully")
        else:
            logger.info("Action execution cancelled")
    else:
        logger.info("Dry run completed. No changes were made.")

    return action_engine


def main():
    """
    🎭 The Grand Adventure Begins!

    This is where our heroic tale unfolds. Each step is a thrilling chapter
    in our quest to bring order to the chaotic file lands!
    """
    args = setup_argparse()
    logger = setup_logging(args.verbose)

    try:
        with tqdm(total=5, disable=args.verbose) as pbar:

            # Scan files
            pbar.set_description("🔍 Scouting the Realm")
            files = scan_files(args.directory, logger)
            pbar.update(1)

            # Categorize files
            pbar.set_description("📚 Deciphering Ancient Scrolls")
            categorized_files = categorize_files(files, logger)
            pbar.update(1)

            # Create organization plan
            pbar.set_description("🗺️ Crafting the Master Plan")
            categorizer = FileCategorizer()
            organization_plan = create_organization_plan(categorized_files, categorizer, args.verbose, logger)
            pbar.update(1)

            # Generate report
            pbar.set_description("📜 Recording Legends")
            generate_reports(files, organization_plan, logger)
            pbar.update(1)

            # Execute plan
            pbar.set_description("✨ Casting the Grand Spell")
            execute_plan(organization_plan, args.directory, args.dry_run, logger)
            pbar.update(1)

        print("🎉 The file kingdom is now in perfect harmony! Your quest is complete!")

    except Exception as e:
        logger.error(f"🔥 Oh no! A wild dragon appeared: {str(e)}")
        if args.verbose:
            logger.exception("🕵️‍♂️ Detective's notes on the dragon:")


if __name__ == "__main__":
    main()

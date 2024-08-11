# 🧙‍♂️ Data Chaos Wizard: Your File System Sorcerer

Welcome to the Intelligent Data Organizer, where chaotic file systems transform into organized digital realms faster than you can say "where did I put that file?"

## 🌟 Project Overview

This Python application, lovingly crafted by data wizards, is a sophisticated, open-source toolkit designed to scan directories, categorize files, analyze relationships, and create organization plans that would make even the most meticulous librarian nod in approval. It's perfect for those looking to tame the wild beast that is their digital clutter and emerge with a zen-like file system.

This project brings together a fellowship of powerful components:

- **FileScanner**: The Directory Explorer, powered by Python's [pathlib](https://docs.python.org/3/library/pathlib.html)
- **FileCategorizer**: The Sorting Hat, empowered by [mimetypes](https://docs.python.org/3/library/mimetypes.html)
- **IntelligentOrganizer**: The Master Planner, orchestrating the grand reorganization
- **ActionEngine**: The Task Executor, bringing plans to life with [shutil](https://docs.python.org/3/library/shutil.html)
- **ReportGenerator**: The Chronicler, documenting the journey of your files using [csv](https://docs.python.org/3/library/csv.html)

Additional enchanted tools in our spellbook:

- **argparse**: The Command Interpreter, for parsing magical incantations (command-line arguments)
- **unittest**: The Test Wizard, ensuring our spells work as intended
- **os**: The System Whisperer, for low-level operating system sorcery
- **collections**: The Data Structurer, particularly the mighty `defaultdict`

## ✨ Capabilities

- **File Detection Sorcery**: Recursively scan and identify files in any directory 🕵️‍♂️
- **Categorization Magic**: Sort files into categories based on type and content 🎩
- **Relationship Divination**: Uncover hidden connections between your files 🔮
- **Organization Enchantments**: Create intelligent plans to restructure your digital realm 📊
- **Action Spells**: Execute reorganization with precision (or preview with a dry run) 🎭
- **Report Conjuring**: Generate comprehensive summaries of the organizing process 📜

## 🔮 Installation

To set up your own Intelligent Data Organizer sanctuary:

1. Clone this arcane repository:
   ```
   git clone https://github.com/OtenMoten/data-chaos-wizard.git
   ```
2. Enter the sacred circle:
   ```
   cd data-chaos-wizard
   ```
3. Summon the required artifacts:
   ```
   pip install -r requirements.txt
   ```

## 🧙‍♂️ Usage

1.) Setup the data organization ritual:

```python
python src/setup.py
```

2.) Summon the data organization ritual:

```python
python src/main.py /path/to/your/chaotic/directory
```

Optional: Perform a dry run and preview the magic without altering your realm:

```python
python src/main.py /path/to/your/chaotic/directory --dry-run
```

This will analyze your files, generate an organization plan, and create a comprehensive report of the proposed changes.

## 🧬 Running Tests

To ensure your Intelligent Data Organizer is operating at peak magical efficiency:

```
python scripts/run_tests.py
```

This will execute a series of rigorous trials, testing each component of the organizer.

## 📜 License

This project is licensed under the GPL3.0 License - see the [LICENSE](LICENSE) file for details.

## 🧙‍♂️ Authors
- Kevin Ossenbrück - Lead Developer at Team Bitfuture - [ossenbrück.de](https://ossenbrück.de)

## 🌟 Connect with Team BitFuture
- Website: [team-bitfuture.de](https://team-bitfuture.de)
- Email: [info@team-bitfuture.de](mailto:info@team-bitfuture.de)

May your files always be findable, and your directories always be tidy! 📂✨
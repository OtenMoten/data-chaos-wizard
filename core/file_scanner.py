from pathlib import Path
import hashlib
from typing import List, Dict, Generator


class FileScanner:
    """
    🕵️‍♂️ The FileScanner: Mystical Explorer of Digital Realms 🗺️

    This magical scanner can traverse the hidden paths of your computer,
    uncovering secrets about every file it encounters. It's like having
    a friendly ghost that can pass through walls and peek at all your files!

    Attributes:
        root_directory (Path): The starting point of our grand expedition
        scanned_files (List[Dict]): A treasure chest of file information
    """

    def __init__(self, root_directory: str):
        """
        🎭 Summon the FileScanner into existence!

        When you create a FileScanner, you're hiring a master explorer
        to map out the file landscape of a specific territory.

        Args:
            root_directory (str): The realm you want to explore

        Raises:
            ValueError: If the chosen realm doesn't exist or isn't a proper kingdom (directory)
        """
        self.root_directory = Path(root_directory)
        if not self.root_directory.exists():
            raise ValueError(f"🏜️ This realm does not exist: {root_directory}")
        if not self.root_directory.is_dir():
            raise ValueError(f"📜 This is but a scroll, not a grand kingdom: {root_directory}")
        self.scanned_files: List[Dict] = []

    def scan(self) -> Generator[Dict, None, None]:
        """
        🔍 Embark on the Great File Expedition!

        This method explores every nook and cranny of the chosen realm,
        uncovering the secrets of each file it finds. It's like a magical
        creature that can sniff out files!

        Yields:
            Dict: Mystical knowledge about each discovered file
        """
        print(f"🚀 Launching expedition into: {self.root_directory}")  # Expedition log
        try:
            for item in self.root_directory.rglob('*'):
                print(f"👀 Spotted: {item}")  # Expedition log
                if item.is_file():
                    try:
                        metadata = self._get_file_metadata(item)
                        self.scanned_files.append(metadata)
                        yield metadata
                    except PermissionError:
                        print(f"🚫 The guards won't let us near: {item}")
                    except Exception as e:
                        print(f"🌋 Encountered a magical barrier at {item}: {str(e)}")
        except PermissionError:
            print(f"🚫 We've been banished from: {self.root_directory}")
        except Exception as e:
            print(f"🌪️ A magical storm has interrupted our expedition: {str(e)}")
        print(f"📊 Treasure count: {len(self.scanned_files)}")  # Expedition summary

    def _get_file_metadata(self, file_path: Path) -> Dict:
        """
        🔮 Uncover the Secrets of a Single File

        This hidden method examines a file closely, revealing its innermost secrets.
        It's like having a magnifying glass that can see the true nature of files!

        Args:
            file_path (Path): The location of the file to examine

        Returns:
            Dict: A scroll containing all the file's secrets
        """
        return {
            'path': str(file_path),
            'name': file_path.name,
            'extension': file_path.suffix,
            'size': file_path.stat().st_size,
            'created': file_path.stat().st_ctime,
            'modified': file_path.stat().st_mtime,
            'fingerprint': self._generate_file_fingerprint(file_path)
        }

    @staticmethod
    def _generate_file_fingerprint(file_path: Path) -> str:
        """
        🖐️ Create a Unique Magical Signature for Each File

        This mystical method generates a unique fingerprint for each file,
        like creating a magical seal that can identify the file anywhere!

        Args:
            file_path (Path): The file to fingerprint

        Returns:
            str: A hex string representing the file's unique magical signature
        """
        hasher = hashlib.md5()
        try:
            with open(file_path, 'rb') as file:
                buf = file.read(65536)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = file.read(65536)
            return hasher.hexdigest()
        except PermissionError:
            print(f"🚫 This file is protected by powerful wards: {file_path}")
            return "Permission denied"
        except Exception as e:
            print(f"💥 Magic backfired while fingerprinting {file_path}: {str(e)}")
            return "Error"

from pathlib import Path

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ROOT_DIR = Path(__file__).parent.parent.resolve()

ENV_FILE = ROOT_DIR / ".env"
LOGS_DIR = ROOT_DIR / "logs"
RESOURCES_DIR = ROOT_DIR / "resources"
DATA_DIR = RESOURCES_DIR / "data"

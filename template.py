import os
from pathlib import Path
import logging

logging.basciConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflow/.gitkeep"
]
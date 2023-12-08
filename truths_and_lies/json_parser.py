from pathlib import Path
from .models import ListOfParticipants
import json


def parse_participants(json_file: Path) -> ListOfParticipants:
    """Parse a json file and return a dictionary"""

    with open(json_file, "r") as f:
        data = json.load(f)

    return ListOfParticipants(**data)


def write_participants(json_file: Path, participants: ListOfParticipants) -> None:
    """Write a dictionary to a json file"""

    with open(json_file, "w") as f:
        json.dump(participants.dict(), f, indent=4)

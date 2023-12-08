import argparse
import json
from pathlib import Path
from .models import ListOfParticipants, Participant, Statement
from .json_parser import parse_participants, write_participants
from .presentation_generator import create_presentation


def _add_participant(name: str, participants: ListOfParticipants) -> None:
    duplicate = participants.find_participant(name)

    if duplicate:
        raise ValueError(f"Participant '{name}' already exists.")

    participant = Participant(name=name)
    for i in range(1, 4):
        text = input(f"Enter statement {i}: ")
        isLie = input(f"Is statement {i} a lie? (yes/no): ").lower() == "yes"
        participant.add_statement(Statement(statement=text, isLie=isLie))

    participants.add_participant(participant)


def _remove_participant(name: str, participants: ListOfParticipants):
    participant = participants.find_participant(name)
    if not participant:
        raise ValueError(f"Participant '{name}' does not exist.")

    participants.remove_participant(name)
    print(f"Participant '{name}' removed successfully.")


def cli():
    parser = argparse.ArgumentParser(description="Two Truths and a Lie Game")
    subparsers = parser.add_subparsers(dest="command")

    # Add subcommand
    parser_add = subparsers.add_parser("add", help="Add a new participant")
    parser_add.add_argument("name", type=str, help="Name of the participant")

    # Remove subcommand
    parser_remove = subparsers.add_parser("remove", help="Remove a participant")
    parser_remove.add_argument(
        "name", type=str, help="Name of the participant to remove"
    )

    # Generate subcommand
    parser_generate = subparsers.add_parser(
        "generate", help="Generate a PowerPoint presentation"
    )
    parser_generate.add_argument(
        "--input",
        type=str,
        default="participants.json",
        help="Path to the input JSON file",
    )
    parser_generate.add_argument(
        "--output",
        type=str,
        default="presentation.pptx",
        help="Path to save the output PowerPoint file",
    )

    args = parser.parse_args()

    # Read the participants from the JSON file
    participants = parse_participants(Path("participants.json"))

    match args.command:
        case "add":
            try:
                _add_participant(args.name, participants)
                write_participants(Path("participants.json"), participants)
            except ValueError as e:
                raise e
        case "remove":
            _remove_participant(args.name, participants)
            write_participants(Path("participants.json"), participants)
        case "generate":
            create_presentation(participants, Path(args.output))
        case _:
            parser.print_help()


if __name__ == "__main__":
    cli()

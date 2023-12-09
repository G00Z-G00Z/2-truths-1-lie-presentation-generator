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
    statements: list[Statement] = []

    # Collect the statements
    for i in range(1, 4):
        text = input(f"Enter statement {i}: ").strip()
        statements.append(Statement(statement=text))

    # Ask for the number of the lie
    while True:
        try:
            lie_number = int(input("Which statement is the lie? (1, 2, or 3): "))
            if 1 <= lie_number <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Add statements to the participant
    for i, statement in enumerate(statements, start=1):
        statement.isLie = i == lie_number
        participant.add_statement(statement)

    # Funny statement
    participant.funny_phrase = input(
        "Write anything you want everyone to know (can be funny, a fact, a joke, something weird, etc): "
    ).strip()

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

    # Edit subcommand
    parser_edit = subparsers.add_parser("edit", help="Edit a participant")
    parser_edit.add_argument("name", type=str, help="Name of the participant")

    # Remove subcommand
    parser_remove = subparsers.add_parser("remove", help="Remove a participant")
    parser_remove.add_argument(
        "name", type=str, help="Name of the participant to remove"
    )

    # list subcommand
    parser_list = subparsers.add_parser("list", help="List all participants")

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

    # Reset subcommand
    parser_reset = subparsers.add_parser("reset", help="Reset the participant list")
    parser_reset.add_argument(
        "--force", action="store_true", help="Force reset without confirmation"
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

        case "edit":
            try:
                person = participants.find_participant(args.name)

                if not person:
                    raise ValueError(f"Participant '{args.name}' does not exist.")

                # Else delete the person
                participants.remove_participant(args.name)

                _add_participant(args.name, participants)
                write_participants(Path("participants.json"), participants)
            except ValueError as e:
                raise e

        case "list":
            for participant in participants.participants:
                print(f"{participant.name}")
        case "remove":
            _remove_participant(args.name, participants)
            write_participants(Path("participants.json"), participants)
        case "generate":
            create_presentation(participants, Path(args.output))
        case "reset":
            if args.force or input("Are you sure you want to reset? (y/n): ") == "y":
                participants.reset()
                write_participants(Path("participants.json"), participants)
            else:
                print("Reset aborted.")
        case _:
            parser.print_help()


if __name__ == "__main__":
    cli()

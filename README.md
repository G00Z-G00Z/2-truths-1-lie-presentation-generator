# Two Truths and a Lie Game

## Overview

The Two Truths and a Lie Game CLI (tlpg-cli, Truth and Lies Presentation Generator Cli) is a command-line tool for managing participants and generating PowerPoint presentations for the game "Two Truths and a Lie". This tool allows users to add, edit, remove, list participants, generate presentations, and reset the participant list.

The project works through a `cli` which you can install using pip: 

```bash
pip install git+https://github.com/G00Z-G00Z/2-truths-1-lie-presentation-generator.git
```

or if you are developing locally: 

```bash
pip install -e .
```

Then you can use the cli like this: 

```bash
tlpg-cli --help
```

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Libraries

- `pydantic` for data validation and serialization.
- `python-pptx` for creating PowerPoint presentations.

### Setup

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required libraries:
   ```bash
   pip install -r ./requirements.txt
   ```

## Usage

The tlpg-cli supports several commands:

### Add a Participant

```bash
tlpg-cli add
```

Use this command to add a new participant. You will be prompted to enter the participant's name and their statements.

### Edit a Participant

```bash
tlpg-cli edit
```

This command allows you to edit an existing participant's details.

### Remove a Participant

```bash
tlpg-cli remove
```

Use this command to remove a participant from the game.

### List Participants

```bash
tlpg-cli list
```

This command lists all the participants currently in the game.

### Generate a PowerPoint Presentation

```bash
tlpg-cli generate
```

Use this command to generate a PowerPoint presentation with the participants' statements.

### Reset the Participant List

```bash
tlpg-cli reset
```

This command resets the participant list. Use it with caution as it will clear all participant data.


# Contributing

Contributions to the `tlpg-cli` are welcome. Please follow the standard procedures for contributing to open-source projects:

1. Fork the repository.
1. Create a new branch for your feature or bug fix.
1. Submit a pull request with a clear description of your changes.

# License
This project is open-source and available under the MIT License.




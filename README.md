# Two Truths and a Lie Game

## Overview

This project implements a fun and interactive game called "Two Truths and a Lie". Participants provide two truths and one lie about themselves, and others guess which statement is the lie. The project consists of two main parts:

1. **Data Collection Script**: A Python script to collect participants' statements and save them into a JSON file. Each participant's entry includes their name and three statements, with a flag indicating which statement is a lie.

2. **Presentation Generator**: Another Python script reads the JSON file and generates a PowerPoint presentation. Each participant's statements are displayed on individual slides, with truths in green and the lie in red.

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

### Data Collection

Run the data collection script:

```bash
python truths_and_lie.py
```

Enter the participant's name and their three statements. Mark which one is a lie. 
The script will save the entries in a JSON file.

### Generating Presentation

Ensure the statements.json file is in the same directory as the presentation script.
Run the presentation generator script:

```bash
python generate_presentation.py
```

The script will create a PowerPoint presentation with the participants' statements.

# Contributing

Contributions to the project are welcome. Please follow the standard procedures for contributing to open-source projects:

1. Fork the repository.
1. Create a new branch for your feature or bug fix.
1. Submit a pull request with a clear description of your changes.

# License
This project is open-source and available under the MIT License.




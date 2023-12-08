from pydantic import BaseModel


class Statement(BaseModel):
    """
    A statement that a participant makes.
    """

    statement: str
    isLie: bool


class Participant(BaseModel):
    """
    A participant in the game.
    """

    name: str
    statements: list[Statement] = []

    def add_statement(self, statement: Statement) -> None:
        """
        Add a statement to the participant's list of statements.
        """
        self.statements.append(statement)


class ListOfParticipants(BaseModel):
    """
    A list of participants in the game.
    """

    participants: list[Participant] = []

    def find_participant(self, name: str) -> Participant | None:
        """
        Find a participant by name.
        """
        for participant in self.participants:
            if participant.name == name:
                return participant

        return None

    def add_participant(self, participant: Participant) -> None:
        """
        Add a participant to the list of participants.
        """
        self.participants.append(participant)

    def remove_participant(self, name: str) -> None:
        """
        Remove a participant from the list of participants.
        """
        self.participants = [p for p in self.participants if p.name != name]

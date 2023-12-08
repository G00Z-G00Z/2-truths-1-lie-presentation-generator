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

    participants: list[Participant]

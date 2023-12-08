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
    statements: list[Statement]


class ListOfParticipants(BaseModel):
    """
    A list of participants in the game.
    """

    participants: list[Participant]

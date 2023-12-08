from pathlib import Path
from pptx import Presentation
from pptx.dml.color import RGBColor
from .json_parser import parse_participants
from .models import ListOfParticipants


def create_presentation(
    participants: ListOfParticipants,
    presentation_path: Path,
) -> None:
    prs = Presentation()
    for participant in participants.participants:
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide.shapes.title
        title.text = f"Statements from {participant.name}"
        content = slide.placeholders[1]
        content.text = ""
        for statement in participant.statements:
            color = RGBColor(0, 128, 0) if not statement.isLie else RGBColor(255, 0, 0)
            p = content.text_frame.add_paragraph()
            p.text = statement.statement
            p.font.color.rgb = color

    prs.save(presentation_path)

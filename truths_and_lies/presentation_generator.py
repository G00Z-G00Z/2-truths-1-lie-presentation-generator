from pathlib import Path
from pptx import Presentation
from pptx.dml.color import RGBColor
from .models import ListOfParticipants
from random import shuffle


PPTX_TEMPLATE = "ppt-templates/funny-presentation.pptx"


def create_presentation(
    participants: ListOfParticipants,
    presentation_path: Path,
) -> None:
    if len(participants.participants) == 0:
        raise ValueError("No participants found.")

    prs = Presentation(PPTX_TEMPLATE)

    # Delete the first slide
    slide_id = prs.slides._sldIdLst[0].rId
    prs.part.drop_rel(slide_id)
    del prs.slides._sldIdLst[0]

    for participant in participants.participants:
        # Add a big slide with the participant name
        slide = prs.slides.add_slide(prs.slide_layouts[0])
        title = slide.shapes.title
        title.text = participant.name

        # Shuffle the statements
        statements = participant.statements.copy()
        shuffle(statements)

        # Add incremental slides for each statement
        for i in range(1, len(statements) + 1):
            slide = prs.slides.add_slide(prs.slide_layouts[1])
            title = slide.shapes.title
            title.text = f"Statements from {participant.name}"
            content = slide.placeholders[1]
            content.text = ""
            for statement in statements[:i]:
                p = content.text_frame.add_paragraph()
                p.text = statement.statement

        # Add a final slide with all statements colored
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide.shapes.title
        title.text = f"Statements from {participant.name} (Reveal)"
        content = slide.placeholders[1]
        content.text = ""
        for statement in statements:
            color = RGBColor(0, 128, 0) if not statement.isLie else RGBColor(255, 0, 0)
            p = content.text_frame.add_paragraph()
            p.text = statement.statement
            p.font.color.rgb = color

    prs.save(presentation_path)

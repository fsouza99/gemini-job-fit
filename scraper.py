import re
import requests

from bs4 import BeautifulSoup


def parse(html: str) -> tuple[str, str]:
    """Get title and description of a job offer from a Gupy page.

    Args:
        html: Page's HTML as string.

    Returns:
        Tuple with title and description of the job presented by the page.
    """
    def refine(piece: str) -> str:
        """Turn HTML piece into plain string respecting paragraphs and list items."""
        piece = piece.replace('<p', '\n<p').replace('<li', '\n- <li')
        return re.sub(r"<(.*?)>", '', piece)

    soup = BeautifulSoup(html, "html.parser")
    title = soup.find(id='h1').text
    target = (
        'Diferenciais',
        'Requisitos e qualificações',
        'Responsabilidades e atribuições',
    )
    out = []
    # For each <div> in the single <section> element on the page.
    for outter_div in soup.section.contents:
        # If there is a child <h2> with a title of interest.
        if outter_div.h2.text in target:
            # Store the title and its subsequent content.
            out.append(f"""### {outter_div.h2.text}{(
                refine(str(outter_div.div)))}""")

    return title.strip(), '\n\n'.join(out)


def get_page(url: str) -> str:
    """Download job page and return its content."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.replace('\u00A0', ' ')
    raise RuntimeError(f"Error downloading webpage: {response.status_code}")


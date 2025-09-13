def write_file(path: str, text: str, footnote: str | None = None) -> None:
    """Write some text in file with an optional footnote."""
    with open(path, 'w', encoding='utf8') as file:
        file.write(text)
        if footnote is not None:
            file.write(f'\n\n---\n\n{footnote}')
    return


def read_file(path: str) -> str:
    """Get file's content as string."""
    with open(path, encoding='utf8') as file:
        text = file.read()
    return text


"""Count the distinct words in a text."""


def unique_words(text: str) -> int:
    """Return the number of distinct whitespace-separated words in text, ignoring case."""
    return len({word.casefold() for word in text.split()})

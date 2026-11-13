"""Write a text in title case."""

_SMALL_WORDS = frozenset({"a", "an", "the", "of", "and", "or", "in", "on"})


def title_case(text: str) -> str:
    """Return text with each word capitalised, small words lowercase unless first."""
    words = []
    for index, word in enumerate(text.split()):
        lowered = word.lower()
        if index > 0 and lowered in _SMALL_WORDS:
            words.append(lowered)
        else:
            words.append(word[:1].upper() + word[1:].lower())
    return " ".join(words)

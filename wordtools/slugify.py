"""Turn a text into a URL slug."""


def slugify(text: str) -> str:
    """Return text lowercased, each word kept to its letters and digits, joined with hyphens."""
    words = ("".join(char for char in word if char.isalnum()) for word in text.lower().split())
    return "-".join(word for word in words if word)

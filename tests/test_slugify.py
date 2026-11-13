import unittest

from wordtools.slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_drops_punctuation_and_joins_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_drops_words_left_empty(self):
        self.assertEqual(slugify("C++ & Java"), "c-java")

    def test_keeps_one_word_without_separator(self):
        self.assertEqual(slugify("Hello/World"), "helloworld")

    def test_keeps_unicode_letters(self):
        self.assertEqual(slugify("Café"), "café")

    def test_empty_text_gives_empty_slug(self):
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()

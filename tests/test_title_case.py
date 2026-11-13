import unittest

from wordtools.title_case import title_case


class TitleCaseTest(unittest.TestCase):
    def test_small_words_lowercase_after_first(self):
        self.assertEqual(title_case("THE lord OF the rings"), "The Lord of the Rings")

    def test_first_word_capitalised_even_if_small(self):
        self.assertEqual(title_case("of mice and men"), "Of Mice and Men")

    def test_empty_text_stays_empty(self):
        self.assertEqual(title_case(""), "")


if __name__ == "__main__":
    unittest.main()

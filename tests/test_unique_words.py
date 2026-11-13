import unittest

from wordtools.unique_words import unique_words


class UniqueWordsTest(unittest.TestCase):
    def test_case_is_ignored_and_punctuation_kept(self):
        self.assertEqual(unique_words("The cat. the CAT"), 3)

    def test_words_are_compared_casefolded(self):
        self.assertEqual(unique_words("Straße STRASSE"), 1)

    def test_empty_text_has_no_words(self):
        self.assertEqual(unique_words(""), 0)


if __name__ == "__main__":
    unittest.main()

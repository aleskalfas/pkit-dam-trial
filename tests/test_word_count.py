import unittest

from wordtools.word_count import word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two  three"), 3)

    def test_empty_text_has_no_words(self):
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()

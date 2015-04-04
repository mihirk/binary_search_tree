import os
from unittest import TestCase
from TreeImpl import TextFile


class TestTextFile(TestCase):
    def test_count_of_words_in_file(self):
        text_file = TextFile(os.getcwd() + '/sample_file')
        self.assertEqual(143, text_file.word_count())

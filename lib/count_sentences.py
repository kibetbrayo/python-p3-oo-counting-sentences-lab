#!/usr/bin/env python3
import re


class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith("?"):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        else:
            return False

    def count_sentences(self):
        if self.value:
            # Split the value based on periods, exclamation marks, and question marks
            sentences = re.split(r'[.!?]', self.value)
            # Remove empty sentences caused by consecutive punctuation marks
            sentences = [sentence for sentence in sentences if sentence]
            return len(sentences)
        else:
            return 0
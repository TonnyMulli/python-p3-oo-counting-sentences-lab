#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, initial_value=None):
        self._value = None
        if initial_value is not None:
            self.value = initial_value
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
    
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        if self._value is None:
            return 0
        sentences = re.split(r'[.!?]+', self._value)
        sentences = [sentence for sentence in sentences if sentence]
        return len(sentences)

    




'''
Garrett Dickinson 
April 25, 2023 
Fuzzing utility for testing methods across project
'''

## Std imports
import json
import random

## Fuzzing imports
import parser
import scanner
import graphtaint


BAD_WORDS_PATH = "bad_words.json"


class Fuzzer():
    def main(self):
        self.load_bad_words()
        self.fuzz_functions()


    def load_bad_words(self):
        self.bad_words : list = json.loads(BAD_WORDS_PATH)


    def get_bad_word(self) -> str:
        bad_word : str = self.bad_words[
            random.randrange(0, len(self.bad_words))
        ]
        return bad_word


    def fuzz_functions(self):
        ## Test Read YAML As String
        parser.readYAMLAsStr(self.get_bad_word())

        ## Test Load YAML Script from String
        parser.loadMultiYAML(self.get_bad_word())

        ## Test Valid Username from String
        scanner.isValidUserName(self.get_bad_word())

        ## Test Load YAML Files from String
        scanner.getYAMLFiles(self.get_bad_word())

        ## Test Load YAML Files from String
        graphtaint.getSHFiles(self.get_bad_word())


if __name__ == "__main__":
    my_fuzzer = Fuzzer()
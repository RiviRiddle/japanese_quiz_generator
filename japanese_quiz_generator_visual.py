# Program for generating a quiz from a set of vocabulary words. Half of the quiz will be japanese to english, and the other half english to japanese.
# Sets of vocabulary words are stored in word_sets.py. Instructions for making more of those are at the end of that file.
# TODO:
# -don't forget to comment the code
# -Make it so vocabulary sets can be practiced one after the other (aside from whole units)
# -add built-in alternates to word_sets!
# -better extra (specify length of sets and units, append any extra)

import random
import word_sets
import jqg_config
from jqg_GUI import jqg_GUI

jqg_version = 'v3' # v1 of jqg_visual

print(f"japanese_quiz_generator {jqg_version}\n")
print(f"word_sets {word_sets.ws_version}\n")

program_description = """Program for generating a quiz from a set of vocabulary words. Half of the quiz will be japanese to english,
and the other half english to japanese.
-Sets of vocabulary words are stored in word_sets.py. Instructions for making more of those are at the end of
that file. (it can be opened and edited in notepad)
-Check what tango sets are available there. Also, whole units of tango quizzes can be practiced
at once if there are quizzes .1-.6 of that unit, by inputting just the first number (to practice all of
unit 1, input 1, etc.)
-Otherwise, input the decimal number to practice the tango set, for instance, 1.1.
-There's a bit of quizzing the program itself can do - it's not polished, but it works well enough.
Input 'y' when prompted about quizzing to use it.
-For standard use, just copy the generated quiz and use it to test yourself. If you want to use the kana or
kanji and the characters don't display in command line, copy them and paste them on notepad or
in a google doc, etc., and they should show up.
-Any input the program takes needs to be very exact to what it's asking for. Sorry about that.
-Can press enter on most inputs to use defaults. Tango number default is semi-random, quizzing
default is false, and Japanese display default is romaji.
    """

def main():
    gui_window = jqg_GUI()

main()

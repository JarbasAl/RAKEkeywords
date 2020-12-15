from RAKEkeywords import Rake
from pprint import pprint
from os.path import join, dirname

my_list = join(dirname(__file__), "stopwords", "en", "FoxStoplist.txt")
rake = Rake(stop_words_path=my_list)

for t in [
    "Compatibility of systems of linear constraints over the set of natural "
    "numbers. Criteria of compatibility of a system of linear Diophantine "
    "equations, strict inequations, and nonstrict inequations are "
    "considered. Upper bounds for components of a minimal set of solutions "
    "and algorithms of construction of minimal generating sets of solutions "
    "for all types of systems are given. These criteria and the "
    "corresponding algorithms for constructing a minimal supporting set of "
    "solutions can be used in solving all the considered types of systems "
    "and systems of mixed types.",

    "Mycroft is a free and open-source voice assistant for Linux-based "
    "operating systems that uses a natural language user interface",

]:
    print("TEXT:", t)
    keywords = rake.extract_keywords(t)
    pprint(keywords)

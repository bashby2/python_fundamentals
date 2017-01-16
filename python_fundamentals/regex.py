# Starting with the code snippet below, write a regex that will match:
#
# All words that contain a 'v'
# All words that contain a double-'s'
# All words that end with an 'e'
# All words that contain an 'b', any character, then another 'b'
# All words that contain an 'b', at least one character, then another 'b'
# All words that contain an 'b', any number of characters (including zero), then another 'b'
# All words that include all five vowels in order
# All words that only use the letters in 'regular expression' (each letter can appear any number of times)
# All words that contain a double letter

import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

print "Words that contain a 'v'=", get_matching_words(r"v")
print "words that contain a double-'s'=", get_matching_words(r"ss")
print "Words that end with an 'e'=", get_matching_words(r"e$")
print "Words that contain an 'b', any character, then another 'b'=", get_matching_words(r"b.b")
print "Words that contain an 'b', at least one character, then another 'b''=", get_matching_words(r"b+.b")
print "Words that contain an 'b', any number of characters (including zero), then another 'b'", get_matching_words(r"b.*b")
print "Words that include all five vowels in order", get_matching_words(r"a.*e.*i.*o.*u.*")
print "Words that only use the letters in 'regular expression'", get_matching_words(r"([regulaxpresion]+)")
print "Words that contain a double letter", get_matching_words(r"(.)\1")


# if re.search(r"a.*a", words):
#    print("That string had at least two 'a's in it!")
# else:
#    print("No more than one 'a' found!")

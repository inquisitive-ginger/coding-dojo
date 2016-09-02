import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball",
             "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight",
             "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress",
             "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb",
             "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]

regexs = {
    "Contains 'v'": r'v',
    "Contains 'ss'": r'ss',
    "Ends in 'e'": r'e$',
    "Contains 'b', any char, 'b'": r'b.b',
    "Contains 'b', at least 1 char, 'b'": r'b.+b',
    "Contains 'b', any # of chars, 'b'": r'b.*b',
    "Contains vowels in order": r'a.*e.*i.*o.*u',
    "Contains letters from 'regular expression'": r'[regula\sxpsion]+',
    "Contains any double letter": r'(\w)\1'
}

for regex in regexs.keys():
    print regex + '...'
    print get_matching_words(regexs[regex])
    print

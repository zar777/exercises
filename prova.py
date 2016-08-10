# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import sys
# import re
#
# Regex_Pattern = r'\w+@\w+\.\w+'
# match = []
# for line in sys.stdin:
#     match_regex = ("".join(re.findall(Regex_Pattern, line)))
#     if match_regex != "":
#         if match_regex not in match:
#             match.append(match_regex)
# match.sort()
# emails = ";".join(match)
# print emails




string = "1\n" \
         "foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.\n" \
         "1\n" \
         "foo\n"

import sys
import re

([^\W_]*tip+[^_\W]*)+
Regex_Pattern = r'[^\W_]*%s+[^_\W]*'
match = ""
count = 0
counter_text = 1
text_lines = 0
parse_word = -1
for line in sys.stdin.readline().strip("\n"):
    if text_lines == 0:
        text_lines = int(line)+1
        continue
    if counter_text < text_lines:
        match += line
        counter_text += 1
    elif counter_text == text_lines:
        parse_word = int(line)
        counter_text +=1
        continue
    if parse_word > -1:
        count += sum(1 for _ in re.finditer(Regex_Pattern % re.escape(line), match))
        print count


r'(\s\W)*%s+\W+'
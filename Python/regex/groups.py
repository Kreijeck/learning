# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"Der name ist (.+) mit dem Alter (.+)"

test_str = ("Der name ist Thomas mit dem Alter 35\n"
            "Der name ist Franz mit dem Alter 32\n"
            "Der name ist Mike mit dem Alter 33\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for match in matches:
    print(f"Fullmatch: {match.group()}")
    print(f"Groupmatches as Tuple: {match.groups()}")

#### AUTOGENERATED CODE FROM REGEX101 #####

# for matchNum, match in enumerate(matches, start=1):

#     print("Match {matchNum} was found at {start}-{end}: {match}".format(
#         matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1

#         print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
#               start=match.start(groupNum), end=match.end(groupNum), group=match.group(groupNum)))

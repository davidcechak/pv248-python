import sys
import collections
import re


def countTitlesByComposer():
    counter = collections.Counter()
    with open(sys.argv[1], 'r', encoding="utf8") as fileInput:
        for line in fileInput:
            r = re.compile(r"Composer: (.*)")
            match = r.match(line)
            if match is not None:
                trimmed = re.sub("\([^)]*\)", "", line)
                composer = trimmed.strip().split(":")[1].split(";")
                if composer[0].strip():
                    counter[str(composer[0])] += 1

    for keyValuePair in counter.items():
        print('{}: {}'.format(keyValuePair[0], keyValuePair[1]))


def countTitlesByCentury():
    counter = collections.Counter()
    with open(sys.argv[1], 'r', encoding="utf8") as fileInput:
        for line in fileInput:
            r = re.compile("Composition Year: (.*)")
            match = r.match(line)
            if match is not None:
                year = line.strip().split(":")[1]
                if year.strip():
                    yearMatched = re.search("[1,2]\d{3}", year)
                    if yearMatched and yearMatched[0]:
                        century = str(int(yearMatched[0]) // 100 + 1)
                        counter[century] += 1

    for keyValuePair in counter.items():
        print('{}th century: {}'.format(keyValuePair[0], keyValuePair[1]))


if sys.argv[2] == "composer":
    countTitlesByComposer()
elif sys.argv[2] == "century":
    countTitlesByCentury()
else:
    print("Inset 'composer' or 'century' as a second argument")

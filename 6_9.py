import re


s = input("Введіть рядок слів розділених одним або декількома пропусками\n")

words = re.split(r'\s+', s)
unique_words = set(words)

frequencies = {x: s.count(x) / len(unique_words) for x in words}

print(frequencies)

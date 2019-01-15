s = input("Введіть рядок: ")

frequencies = {x: s.count(x) for x in s}

max_count = 0
sym = None

for ch,cnt in frequencies.items():
    if cnt > max_count:
        sym = ch
        max_count  = cnt

print("Найбільшу кількість разів (%d) зустрічається символ %s" % (max_count, sym))

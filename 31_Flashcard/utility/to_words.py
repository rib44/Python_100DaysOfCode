
f = open("words", "w")
with open("german_words.txt", "r") as words:
    for w in words:
        f.write(w.split(" ")[0])
        f.write("\n")


f.close()

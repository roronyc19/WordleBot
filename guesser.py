from collections import Counter as Cnt
import re


class Wordle:
    def __init__(self, words=[], mode="manual"):
        self.words = words
        self.mode = mode

    def guess_word(self):

        # read in all possibilities
        with open('five-letter-words.txt') as file:
            words = Cnt()
            l = file.readlines()
            for line in l:
                words[line.rstrip()] = 0
        # print(words)
        # , "eldest.txt", "speeches.txt", "bible.txt", "bigshort.txt", "alfaromeo.txt", "intelinvest.txt"]
        fileList = ["moneyball.txt"]  # for now only one text file
        for fil in fileList:
            with open(fil) as f:
                for line in f:
                    for word in line.split(' '):
                        fin = re.sub(r'\W+', '', word).lower()
                        if fin in words:
                            words[fin] += 1
        words["amber"] = 5

        # print(words)
        # print([w for w in words.most_common() if w[1] == 0])
        guessed = False
        word = "irate"
        result = ""
        tries = 1
        confirmed = set()
        while not guessed:
            if self.mode == "manual":
                result = input(
                    f"Enter {word.upper()} result (x = gray, y = yellow, g = green): ")
            else:
                exit(1)
                #result = getRes(word)
            if result == 'ggggg' or result == '' or result == 'g':
                guessed = True
                print(f"Got it in {tries} tries!")
                break
            for i in range(5):
                print(len(words))
                if result.lower()[i] == 'g':
                    words = Cnt({key: value for (key, value) in words.items()
                                if key[i] == word[i]})  # breaks for double letters
                    confirmed.update(word[i])
                elif result.lower()[i] == 'y':
                    words = Cnt({key: value for (key, value) in words.items()
                                if key.find(word[i]) != -1 and key[i] != word[i]})
                    confirmed.update(word[i])
                else:
                    words = Cnt({key: value for (key, value) in words.items()
                                if key.find(word[i]) == -1})

            chardic = Cnt()  # either have this be from the words left or populate initially?
            for word in words:
                for ch in word:
                    if ch not in confirmed:
                        chardic[ch] += 1
            # print(chardic)
            letts = chardic.most_common(5 - len(confirmed))

            topCands = []
            bad = 0
            while len(topCands) == 0:
                for word in words.keys():
                    matchNum = 0
                    for l in letts:
                        if word.find(l[0]) != -1:
                            matchNum += 1
                    if matchNum == 5 - len(confirmed) - bad:
                        topCands.append(word)
                bad += 1  # no letters match all most common left

            cands = Cnt(
                {key: value for key, value in words.items() if key in topCands})
            word = cands.most_common(1)[0][0]

            # print("topcands ", topCands)
            # print("words ", words)
            # print("cands ", cands)
            tries += 1


# if __name__ == 'main':
words = ["shard", "could"]
wordle = Wordle(words, "manual")
wordle.guess_word()

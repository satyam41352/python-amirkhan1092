#solution of first problem
words = input().split(" ")
length = len(words)
chain = [words[0]]
words = words[1:]
for i in range(0,length - 1):
    for word in words:
        break_flag = False
        if word[0] == chain[-1][-1]:
            for temp_word in words:
                if len(words) != 1 and word[-1] == temp_word[0]:
                    chain.append(word)
                    words.remove(word)
                    break_flag = True
                    break
                elif len(words) == 1: chain.append(word)
            if break_flag: break
if len(chain) == length and chain[0][0] == chain[-1][-1]: print(chain)
else: print("This is not possibe to make circle")
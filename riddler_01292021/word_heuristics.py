import string

def get_matches(l, r):
    llist = list(l)
    rlist = list(r)

    exact = 0
    removes = []
    # exact matches first
    for i in range(5):
        if llist[i] == rlist[i]:
            exact += 1
            removes.append(i)

    for i in reversed(removes):
        llist.pop(i)
        rlist.pop(i)

    return exact
        

words = {}
with open('filtered_words.txt') as word_file:
    for word in word_file:
        words[str(word).strip()] = {'partial': 0, 'exact': 0}

chars = {}
for char in string.ascii_lowercase:
    dist = [0] * 5
    for word in words:
        for i in range(5):
            if word[i] == char:
                dist[i] += 1
    chars[char] = dist

print(chars)

word_scores = {}
for word in words:
    word_scores[word] = 0
    for i in range(5):
        word_scores[word] += chars[word[i]][i]

print({k: v for k, v in sorted(word_scores.items(), key=lambda item: item[1])})

#for word in words:
#    for matcher in words:
#        print(word + " " + matcher + " " + str(get_matches(word, matcher)))

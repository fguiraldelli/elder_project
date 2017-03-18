def ransom_note(magazine, ransom):
    dict_word_count = {}
    for word in magazine:
        if word in dict_word_count.keys():
            dict_word_count[word] += 1
        else:
            dict_word_count[word] = 1
    num_words_needed = 0
    for word in ransom:
        if word in dict_word_count.keys():
            #value = dict_word_count[word]
            if dict_word_count[word] > 0:
                dict_word_count[word] -= 1
                num_words_needed += 1
    return len(ransom) == num_words_needed
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
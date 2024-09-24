def single_root_words(root_word,*other_words):
    same_word = []
    list_=list(other_words)
    for i in other_words:
        i = str.lower(i)
        root_word_=root_word.lower()
        j = 0
        if root_word_ in i:
            same_word.append(other_words[j])
            j += 1
        elif i in root_word_:
            same_word.append(other_words[j])
            j += 1
        else:
            j += 1
    return same_word

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
try:
    file_name = input()
    word = input()

    anagrama_words = []
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                if len(word) != len(line) or word == line:
                    continue

                original_chars = list(word)
                original_chars.sort()
                new_word_chars = list(line)
                new_word_chars.sort()
                dif_chars = [original_chars[i] == new_word_chars[i] for i in range(0, len(word))]
                if False in dif_chars:
                    continue

                anagrama_words.append(line)

    anagrama_words.sort()
    for w in anagrama_words:
        print(w)
except:
    print("INVALID INPUT")
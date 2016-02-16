import re

input_string = input()

pattern = re.compile(r'\s+')
sentence = re.sub(pattern, '', input_string)

chars_dict = {}
if input_string:
    for ch in list(sentence):
        if ch not in chars_dict:
            chars_dict[ch] = 0

        chars_dict[ch] += 1

    sorted_chars = sorted(chars_dict.items(), key=lambda kv: kv[1], reverse=True)
    print(sorted_chars[0][0])
else:
    print("INVALID INPUT")



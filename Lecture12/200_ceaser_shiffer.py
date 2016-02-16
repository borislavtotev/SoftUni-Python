original_alphabet = []
try:
    key = int(input())
    key %= 24
    input_string = input()
    result = ''

    for i in range(65, 91):
        original_alphabet.append(chr(i))

    for ch in input_string:
        ch_ord = ord(ch)
        if ch_ord in range(65, 91):
            result += original_alphabet[ch_ord - 65 - key]
        else:
            result += ch

    print(result)
except:
    print("INVALID INPUT")



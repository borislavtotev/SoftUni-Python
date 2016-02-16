text1 = input()
text2 = input()

start_position = text1.find(text2)
if start_position == -1:
    print("text 2 is not available in text 1")
else:
    print(text1[start_position + len(text2):len(text1)])


name = input("Please write your name:")
name_parts = name.split()
special_titles = ['д-р', 'проф.', 'доктор', 'van', 'von']
result = []

for name in name_parts:
    if name in special_titles:
        continue
    else:
        result.append(name[0] + '.')

short_name = ' '.join(result)
print(short_name)
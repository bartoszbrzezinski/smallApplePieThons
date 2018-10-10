message = 'It was a bright, cold day of April and the clocks shown 1PM'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

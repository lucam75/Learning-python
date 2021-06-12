demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4, 5, 6))

print(list(range(1, 100)))

print(dir(colors))

print(len(demo_list))

print(colors[1])

print('green' in colors)
print(8 in colors)

colors.append('black')
colors.extend(('violet', 'yellow'))

colors.remove('green')
print(colors)
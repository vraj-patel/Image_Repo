from os import listdir

image_ids = set()

for name in listdir('images'):
    image_ids.add(name.split('.')[0])

description_file = open('descriptions.txt', 'w')

with open('all_descriptions.txt', 'r') as file:
    for line in file:
        id = line.split()[0]
        if id in image_ids: description_file.write(line)
        

junk = {}
key_materials = {'fragments': 0, 'motes':0 , 'shards':0}
win = {'fragments': 'Valanyr',
       'motes':'Dragonwrath',
       'shards':'Shadowmourne'
}
command = input()
o = {}
is_break = False
while command:
    row = command.split()
    for c in range(0, len(row), 2):
        value = int(row[c])
        key = row[c+1].lower()
        if key in key_materials:
            key_materials[key] += value
            for i, f in key_materials.items(): # (key , value)
                if key_materials[i] >= 250:
                    reward = win[i]
                    print(f'{reward} obtained!')
                    key_materials[i] -= 250
                    is_break = True
                    break
        else:
            if key in junk:
                junk[key] += value
            else:
                junk[key] = value
        if is_break:
            break

    if is_break:
        break

    command = input()
for key, value in sorted(key_materials.items(), key=lambda x:(-x[1], x[0])):
    print(f'{key}: {value}')
for key , value in sorted(junk.items(), key=lambda x:x[0]):
    print( f'{key}: {value}')
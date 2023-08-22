names = ["James", "Lebron", "Pete", "Charlie", "Jess"]

for name in names:
    if 'b' in name.lower():
        pass
    else:
        print(name, len(names))

for name in names:
    if 'p' in name.lower():
        break
    else:
        print(name)

# continue
# continue goes to the next item. pass does nothing

for name in names:
    if 'ch' in name.lower():
        continue
    else:
        print(name)


names = ['Amanda', 'Mercedes', 'Rachel',
         'Elisabeth', 'Tay', 'Xavier', 'Joaquin', 'Sam']

for name in names:
    if 'm' in name.lower():
        continue
    elif 'r' in name.lower():
        pass
    elif 'j' in name.lower():
        break
    else:
        print(name)

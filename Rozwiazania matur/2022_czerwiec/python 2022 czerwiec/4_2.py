file = open('przyklad.txt', 'r')
data = []

for line in file:
    data.append(line.strip())


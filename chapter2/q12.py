# coding: utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f:
        lines = f.readlines()

    col1 = []
    col2 = []

    for line in lines:
        cols = line.split('\t')
        col1.append(cols[0])
        col2.append(cols[1])

    with open('col1.txt', 'w') as f:
        f.write('\n'.join(col1))

    with open('col2.txt', 'w') as f:
        f.write('\n'.join(col2))

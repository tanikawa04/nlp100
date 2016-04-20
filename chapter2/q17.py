# coding: utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f:
        res = '\n'.join(set([line.split('\t')[0] for line in f.readlines()]))

    print(res)

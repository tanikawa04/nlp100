# coding: utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f:
        res = len(f.readlines())

    print(res)

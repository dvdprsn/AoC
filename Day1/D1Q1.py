def main():

    with open('input.txt') as f:

        input = f.readlines()
        f.close()
    res = [eval(i) for i in input]
    ex = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    numInc = 0
    for idx, x in enumerate(res):
        if (idx == 0):
            print(f'{x} (N/A - no previous measurement)')
            continue
        elif (x > res[idx-1]):
            print(f'{x} (increased)')
            numInc += 1
        else:
            print(f'{x} (decreased)')

    print(f'{numInc} increases')


if __name__ == '__main__':
    main()

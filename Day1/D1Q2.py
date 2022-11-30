def main():

    with open('input.txt') as f:

        input = f.readlines()
        f.close()
    res = [eval(i) for i in input]
    ex = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    numInc = 0
    prev = 0
    for idx, x in enumerate(res):
        if idx+2 >= len(res):
            break

        val = x + res[idx+1] + res[idx+2]
        if (idx == 0):
            print(f'{val} (N/A - no previous measurement)')
            prev = val
            continue
        if val > prev:
            print(f'{val} (increase)')
            numInc += 1
        elif val == prev:
            print(f'{val} (no change)')
        else:
            print(f'{val} (decrease)')
        prev = val

    print(f'{numInc} increases')


if __name__ == '__main__':
    main()

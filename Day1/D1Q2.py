def main():
    arr = []
    idx = 0
    prev = 0
    numInc = 0
    val = 0
    with open('input.txt') as f:
        input = f.readline()
        while input:
            arr.append(int(input))
            if idx == 2:
                val = arr[idx] + arr[idx-1] + arr[idx-2]
                print(f'{val} (N/A - no previous measurement)')
                prev = val
            if idx > 2:
                val = arr[idx] + arr[idx-1] + arr[idx-2]
                if val > prev:
                    print(f'{val} (increase)')
                    numInc += 1
                elif val == prev:
                    print(f'{val} (no change)')
                else:
                    print(f'{val} (decrease)')

                prev = val

            idx += 1
            input = f.readline()

        f.close()
    print(f'{numInc} increases')


if __name__ == '__main__':
    main()

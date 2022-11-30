'''Submission for day 1 question 2'''
def main():
    '''3's sum submarine'''

    arr = []
    idx = 0
    prev = 0
    num_inc = 0
    val = 0
    with open('input.txt', encoding="utf-8") as fi:
        line = fi.readline()
        while line:
            arr.append(int(line))
            if idx == 2:
                val = arr[idx] + arr[idx-1] + arr[idx-2]
                print(f'{val} (N/A - no previous measurement)')
                prev = val
            if idx > 2:
                val = arr[idx] + arr[idx-1] + arr[idx-2]
                if val > prev:
                    print(f'{val} (increase)')
                    num_inc += 1
                elif val == prev:
                    print(f'{val} (no change)')
                else:
                    print(f'{val} (decrease)')

                prev = val

            idx += 1
            line = fi.readline()

        fi.close()
    print(f'{num_inc} increases')


if __name__ == '__main__':
    main()

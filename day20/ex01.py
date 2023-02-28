#remember that this only work when the algo_line[0] == '#' and algo_line[511] == '.'
#if that is not the case than change it accordingly

import sys


def print_image(output_img):
    length_row = len(output_img[0])
    for x in range(len(output_img)):
        for y in range(length_row):
            if output_img[x][y] == '0':
                print('.', end='')
            else:
                print('#', end='')
        print()


def enhance(line, input_img, outside):
    rows = len(input_img)
    cols = len(input_img[0])
    # print_image(input_img)

    for i in range(rows):
        input_img[i].insert(0, outside)
        input_img[i].insert(0, outside)
        input_img[i].append(outside)
        input_img[i].append(outside)

    for i in range(2):
        row = [outside]*(cols + 4)
        input_img.insert(0,row)
        row = [outside]*(cols + 4)
        input_img.append(row)

    # print_image(input_img)

    output = []
    for x in range(rows + 2):
        output.append(['0'] * (cols + 2))
    rows += 4
    cols += 4

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            string = input_img[x - 1][y - 1] + input_img[x - 1][y] + input_img[x - 1][y + 1] + \
                     input_img[x][y - 1] + input_img[x][y] + input_img[x][y + 1] + \
                     input_img[x + 1][y - 1] + input_img[x + 1][y] + input_img[x + 1][y + 1]
            number = int(string, 2)
            if line[number] == '#':
                output[x-1][y-1] = '1'
            else:
                output[x-1][y-1] = '0'
    return output


def count_lit(input_img):
    rows = len(input_img)
    cols = len(input_img[0])
    count = 0
    for x in range(rows):
        for y in range(cols):
            if input_img[x][y] == '1':
                count += 1
    return count


def main() -> int:
    with open('inputday20.txt') as file:
        lines = file.read().splitlines()

    algo_line = lines[0]
    image = []
    length = len(lines)
    length_line = len(lines[2])

    for i in range(2, length):
        row = []
        for j in range(length_line):
            if lines[i][j] == '.':
                row.append('0')
            else:
                row.append('1')
        image.append(row)

    # print_image(image)
    output_img = image
    output_img = enhance(algo_line, output_img, '0')
    output_img = enhance(algo_line, output_img, '1')
    #print_image(output_img)
    print(count_lit(output_img))
    return 0


if __name__ == '__main__':
    sys.exit(main())
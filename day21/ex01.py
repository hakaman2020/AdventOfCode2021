import sys


def main():
    with open('inputday21.txt') as file:
        lines = file.read().splitlines()
    p1_pos = int(lines[0].split()[-1])
    print(p1_pos)
    p2_pos = int(lines[1].split()[-1])
    print(p2_pos)

    current_pos = [p1_pos, p2_pos]
    current_player = 0
    current_score = [0,0]
    total_dice_rolled = 0
    roll = 6
    latest_score = 0
    while latest_score < 1000:
        total_dice_rolled +=3
        new_pos = ((current_pos[current_player] - 1 + roll) % 10) + 1
        current_score[current_player] += new_pos
        current_pos[current_player] = new_pos
        latest_score = current_score[current_player]
        roll += 9
        current_player = (current_player + 1) % 2

    print(current_score, total_dice_rolled)
    print(current_score[current_player] * total_dice_rolled)
    return 0


if __name__ == '__main__':
    sys.exit(main())
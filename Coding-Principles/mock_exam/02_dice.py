import random


def get_dice_results(rolls):
    while True:
        first_dice = random.randrange(1, 7)
        second_dice = random.randrange(1, 7)

        print(f'{first_dice}.{second_dice}')
        rolls += 1

        if first_dice == 6 and second_dice == 6:
            return rolls


def main():
    rolls = get_dice_results(0)
    print(f'You required {rolls} rolls to achieve 6,6')


main()

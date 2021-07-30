def get_n():
    while True:
        try:
            n = int(input('How many numbers should the program produce: '))
            if 1 <= n <= 100:
                break
            else:
                print('The number should be between 1 and 100!')
        except ValueError:
            print('Please enter a positive whole number!')

    return n


def get_results(n):
    results = []
    for _ in range(n):
        while True:
            try:
                res = int(input('Enter a number: '))
                results.append(res)
                break
            except ValueError:
                print('Please enter a positive whole number!')

    return results


def main():
    n = get_n()
    results = get_results(n)

    results_str = ' '.join(list(map(str, results)))
    print(f'The results: {results_str}')


main()

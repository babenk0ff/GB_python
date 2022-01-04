def main(args):
    if len(args) > 1:
        result = currency_rates(args[1])
        if result:
            print(*result, sep=', ')
        else:
            print(None)
    else:
        print(None)


if __name__ == '__main__':
    import sys
    from utils import currency_rates

    main(sys.argv)

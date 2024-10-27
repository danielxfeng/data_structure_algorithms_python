# python3

import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.DEBUG)
# logging.Logger.disabled = True


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coins = [1, 3, 4]
    return get_min_counts(money, coins)


def get_min_counts(money, coins):
    memo = [money + 1] * (money + 1)

    memo[0] = 0

    for amt in range(1, money + 1):
        logging.debug("amount is %d" % amt)
        for coin in coins:
            logging.debug("coin is %d" % coin)
            if amt - coin < 0:
                continue
            logging.debug("compare is %d, %d" % (memo[amt], memo[amt - coin] + 1))
            memo[amt] = min(memo[amt], memo[amt - coin] + 1)
            logging.debug("memo[%d] is %d" % (amt, memo[amt]))

    logging.debug("memo is %s" % str(memo))
    return memo[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))

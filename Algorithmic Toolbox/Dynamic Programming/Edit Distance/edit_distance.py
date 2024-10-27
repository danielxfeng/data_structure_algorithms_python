# python3

import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.DEBUG)
# logging.Logger.disabled = True


def edit_distance(first_string, second_string):

    len1 = len(first_string)
    len2 = len(second_string)

    dp = [[0 for _ in range(len2 + 1)] for __ in range(len1 + 1)]
    # dp = [[0, 0] for _ in range(len1 + 1)]

    for f in range(len1 + 1):
        for s in range(len2 + 1):
            if f == 0:
                logging.debug("f==0")
                logging.debug("dp is %s: " % str(dp))
                dp[f][s] = s
            elif s == 0:
                logging.debug("s==0")
                dp[f][s] = f
            elif first_string[f - 1] == second_string[s - 1]:
                logging.debug("==, %s" % first_string[f - 1])
                dp[f][s] = dp[f - 1][s - 1]
            else:
                logging.debug("get_min, f_s-1 is: %d, f-1_s is %d, f-1_s-1 is %d" % (dp[f][s - 1],dp[0][s],dp[0][s-1]))
                dp[f][s] = 1 + min(dp[f][s - 1], dp[f - 1][s], dp[f - 1][s - 1])

            logging.debug("dp[f][s] is: f: %d, s: %d, dp: %d" % (f, s, dp[f][s]))

    logging.debug("res is dp: %s" % str(dp))
    return dp[f][s]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance("star", "end"))

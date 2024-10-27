def partition32(items):
    # Terminate early if:
    # 1. There aren't enough items;
    # 2. The sum of values isn't divisible by 3; or
    # 3. There is an item with value larger than the sum divided by 3.
    total_value = sum(items)
    num_items = len(items)
    each_value, mod = divmod(total_value, 3)

    if num_items < 3 or mod or max(items) > each_value:
        return False

    # We will use a 3D table, and consider a "slice" to be the grid when z is fixed to a certain value.
    # T[x][y][z] = true if person 1 can have value x and person 2 can have value y out of the first z items.
    # Restriction: only defined for x >= y, as otherwise we are just building something symmetric by swapping people.
    xy_length = each_value + 1
    z_length = num_items + 1
    T = [[([False] * z_length)[:] for _ in range(xy_length)] for _ in range(xy_length)]

    # For slice 0, the only condition that holds is that we can make values of 0 and 0 with 0 items:
    T[0][0][0] = True

    # Now iterate in the outside loop over the items.
    for z in range(1, z_length):
        item_value = items[z - 1]

        for x in range(xy_length):
            remain1 = x - item_value

            for y in range(xy_length):
                remain2 = y - item_value

                # The x=0, y=0 can always be made by taking no items.
                if x == 0 and y == 0:
                    T[0][0][z] = True

                elif item_value == x and True in [T[i][y][z-1] for i in range(xy_length)]:
                    T[x][y][z] = True

                # Case 2: same but with the players swapped.
                elif item_value == y and True in [T[x][i][z-1] for i in range(xy_length)]:
                    T[x][y][z] = True

                # Case 3: we already found a combination of items that gives the players x and y.
                elif T[x][y][z-1]:
                    T[x][y][z] = True

                # Case 4: Determine the remaining needed value if player 1 took the item.
                # If the item fits and we already have an entry with player 1 generating remain1, we are good.
                elif remain1 > 0 and T[remain1][y][z-1]:
                    T[x][y][z] = True

                # Case 5: same, but with players swapped.
                elif remain2 > 0 and T[x][remain2][z-1]:
                    T[x][y][z] = True

    # Now the answer is in the corner opposite where we started, i.e. T[each_value][each_value][num_items]:
    # Can we, using num_items items, divide them amongst two people so they each get 1/3rd of the total value
    # (thus leaving the other 1/3rd for the third person)?
    return T[each_value][each_value][num_items]
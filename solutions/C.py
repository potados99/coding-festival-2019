N, A, B = list(map(lambda x: int(x), input().split(' ')))

# Sorted ascending.
two_by_one_beauty = sorted(list(map(lambda x: int(x), input().split(' '))))
two_by_two_beauty = sorted(list(map(lambda x: int(x), input().split(' '))))

horizontal_size = 0
beauty = 0

# Make N even.
if N % 2 == 1:
    beauty += two_by_one_beauty.pop()
    N -= 1

# horizontal_size will only increase for amount of 2.
# If number of 2x1 < 2, ignore it.
# If number of 2x2 < 1, ignore it.
# If both? impossible.
while horizontal_size < N:
    from_2x1 = two_by_one_beauty[-1] + two_by_one_beauty[-2] if len(two_by_one_beauty) > 1 else 0
    from_2x2 = two_by_two_beauty[-1] if len(two_by_two_beauty) > 0 else 0

    if from_2x1 > from_2x2:
        beauty += from_2x1
        two_by_one_beauty.pop()
        two_by_one_beauty.pop()
    else:
        beauty += from_2x2
        two_by_two_beauty.pop()

    horizontal_size += 2

print(beauty)
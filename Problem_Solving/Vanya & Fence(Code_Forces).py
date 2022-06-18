from typing import List
from random import randint

"""Code Forces: Vanya and Fence"""


def road_min_width(friends_num: int = 3, fence_high: int = 7) -> int:
    friends_num, fence_high = map(int, input().split(' '))
    width = 0
    friends = list(map(int, input().split(" ")))
    while 1 <= friends_num <= 1000 and 1 <= fence_high <= 1000:
        for x in range(len(friends)):
            if friends[x] > fence_high:
                width += 2
            else:
                width += 1
        return width


print(road_min_width(3, 7))

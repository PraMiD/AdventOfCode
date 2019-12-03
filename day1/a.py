import math
import functools

DEBUG = False

def calc_fuel_req(mass : int) -> int:
    fuel = math.floor(mass / 3) - 2
    return fuel if fuel > 0 else 0

def calc_fuel_req_list(data : list) -> int:
    return functools.reduce(
        lambda x, y: x + calc_fuel_req(int(y)),
        data,
        0
    )

if __name__ == "__main__":
    data = [100756]
    if not DEBUG:
        with open("input.txt") as fp:
            data = fp.read().split("\n")
    print(calc_fuel_req_list(data))

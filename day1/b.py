from a import calc_fuel_req, calc_fuel_req_list

DEBUG = False

if __name__ == "__main__":
    data = [100756, 100756]

    if not DEBUG:
        with open("input.txt") as fp:
            data = fp.read().split("\n")

    overall = 0
    for m in [int(m) for m in data]:
        fuel_mass = calc_fuel_req(m)
        new_fuel = calc_fuel_req(fuel_mass)
        while new_fuel != 0:
            fuel_mass += new_fuel
            new_fuel = calc_fuel_req(new_fuel)
        overall += fuel_mass

    print(overall)

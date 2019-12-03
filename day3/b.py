from a import calc_points

def calc_min_dist_timing(path1, path2):
    points1 = calc_points(path1)
    points2 = calc_points(path2)

    dists = {}
    for p in set(points1).intersection(set(points2)):
        d1 = points1.index(p)
        d2 = points2.index(p)

        if p in dists.keys():
            dists[p] = min(d1 + d2, dists[p])
        else:
            dists[p] = d1 + d2

    return sorted(dists.items(), key = lambda x: x[1])[1]



if __name__ == "__main__":
    with open("input.txt") as fp:
            data = fp.read().split("\n")

            path1 = data[0]
            path2 = data[1]

            print(calc_min_dist_timing(path1.split(","), path2.split(",")))
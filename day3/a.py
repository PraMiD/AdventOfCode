DEBUG = False

def calc_points(path : list) -> list:
    last_point = (0,0)
    points = [last_point]
    for p in path:
        direction, num = p[0],p[1:]
        for i in range(int(num)):
            if direction == "R":
                last_point = (last_point[0] + 1, last_point[1]) 
            elif direction == "L":
                last_point = (last_point[0] - 1, last_point[1])
            elif direction == "U":
                last_point = (last_point[0], last_point[1] + 1)
            elif direction == "D":
                last_point = (last_point[0], last_point[1] - 1)
            points.append(last_point)
    return points

def calc_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calc_min_diff(path1, path2):
    points1 = set(calc_points(path1))
    points2 = set(calc_points(path2))

    diff = {}
    start = (0,0)
    
    for p in points1.intersection(points2):
        diff[p] = calc_dist(start, p)

    return sorted(diff.items(), key = lambda x: x[1])[1]
        

if __name__ == "__main__":
    if DEBUG:
        path = ["R8","U5","L5","D3"]
        points = calc_points(path)

        path2 = ["U7","R6","D4","L4"]
        points2 = calc_points(path2)

        intersection = points.intersection(points2)
        print(intersection)
        print(calc_min_diff(path, path2))
    else:
        with open("input.txt") as fp:
            data = fp.read().split("\n")

            path1 = data[0]
            path2 = data[1]

            print(calc_min_diff(path1.split(","), path2.split(",")))
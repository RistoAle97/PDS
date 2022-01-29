import numpy as np
import argparse


def parse_arguments(known=False):
    parser = argparse.ArgumentParser(description="python method to create the points file")
    parser.add_argument("--n", type=int, default=10000, help="number of points")
    parser.add_argument("--file", type=str, default="points.txt", help="where to save the points")
    parser.add_argument("--lbound", type=float, default=0, help="lower bound of the distribution")
    parser.add_argument("--ubound", type=float, default=10, help="upper bound of the distribution")
    parser.add_argument("--round", type=bool, store_action=True, help="round the points")
    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt


if __name__ == "__main__":
    opt_parser = parse_arguments()

    # take arguments
    n_points = opt_parser.n
    path = opt_parser.file
    l_bound = opt_parser.lbound
    u_bound = opt_parser.ubound
    round_points = opt_parser.round
    save = opt_parser.save

    # create points
    points = np.random.uniform(l_bound, u_bound, (n_points, 2))
    if round_points:
        points = np.round(points, 2)

    with open(path, "w+") as datafile:
        for point in points:
            datafile.write("{0},{1}\n".format(point[0], point[-1]))

    print("{0} points created and stored in file {1}, you're now ready to perform KNN on them".format(n_points, path))

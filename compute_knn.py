import os
import argparse


def parse_arguments(known=False):
    parser = argparse.ArgumentParser(description="python method to create the points file")
    parser.add_argument("--file", type=str, default="datasets/points_10k.txt", help="points dataset")
    parser.add_argument("--k", type=int, default=10, help="k, the number of nearest neighbours")
    parser.add_argument("--nw", type=int, default=256, help="nw, the number of workers")
    parser.add_argument("--runs", type=int, default=10, help="how many runs you want to do")
    parser.add_argument("--execute", type=str, default="spf", help="which implementation to run")
    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt


if __name__ == "__main__":
    opt_parser = parse_arguments()
    dataset_path = opt_parser.file
    k = opt_parser.k
    nw = opt_parser.nw
    runs = opt_parser.runs
    execute = opt_parser.execute
    if "s" in execute:
        print("Sequential KNN execution for {0} runs".format(runs))
        for i in range(runs):
            os.system("./knn_sequential {0} {1}".format(dataset_path, k))
            print()

    if "p" in execute:
        print("Parallel KNN execution for {0} runs".format(runs))
        for i in range(runs):
            os.system("./knn_parallel {0} {1} {2}".format(dataset_path, k, nw))
            print()

    if "f" in execute:
        print("FastFlow KNN execution for {0} runs".format(runs))
        for i in range(runs):
            os.system("./knn_ff {0} {1} {2}".format(dataset_path, k, nw))
            print()

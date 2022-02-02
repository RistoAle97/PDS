import matplotlib.pyplot as plt
import argparse
import numpy as np


def parse_arguments(known=False):
    parser = argparse.ArgumentParser(description="python method to plot knn results")
    parser.add_argument("--s", action="store_true", help="plot speedup")
    parser.add_argument("--scalab", action="store_true", help="plot scalability")
    parser.add_argument("--e", action="store_true", help="plot efficiency")
    parser.add_argument("--exectime", action="store_true", help="plot execution time")
    parser.add_argument("--compare", action="store_true", help="plot comparisons")
    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt


def plot_performance(workers, performance, performance_results, implementation):
    figure, ax = plt.subplots(1, 1)
    performance_path = performance
    if "execution time" in performance:
        performance_results = [performance_result/1000000 for performance_result in performance_results]
        performance_path = "results"

    ax.plot(workers, performance_results[0], marker="o", label="{0} 10k".format(implementation))
    ax.plot(workers, performance_results[1], marker="o", label="{0} 20k".format(implementation))
    ax.plot(workers, performance_results[2], marker="o", label="{0} 50k".format(implementation))
    ax.plot(workers, performance_results[-1], marker="o", label="{0} 100k".format(implementation))
    ax.legend()
    if "stdlib" in implementation:
        plot_path = "knn_parallel_{0}".format(performance_path)
        ax.set_title("{0} for parallel knn".format(performance))
    else:
        plot_path = "knn_fastflow_{0}".format(performance_path)
        ax.set_title("{0} for fastflow knn".format(performance))

    if "execution time" in performance:
        ax.set(xlabel="workers", ylabel="Execution time in seconds")
    else:
        ax.set(xlabel="workers", ylabel=performance)

    figure.savefig(plot_path)


def plot_compare_performance(workers, performance, performance_results, n_points_results, implementations):
    figure, ax = plt.subplots(1, 1)
    performance_path = performance
    if "execution time" in performance:
        performance_results = [performance_result/1000000 for performance_result in performance_results]
        performance_path = "results"

    for performance_result, n_points, implementation in zip(performance_results, n_points_results, implementations):
        ax.plot(workers, performance_result, marker="o", label="{0}, {1}".format(implementation, n_points))

    ax.legend()
    if "execution time" in performance:
        ax.set(xlabel="workers", ylabel="Execution time in seconds")
    else:
        ax.set(xlabel="workers", ylabel=performance)

    figure.savefig("knn_comparison_{0}".format(performance_path))


if __name__ == "__main__":
    opt_parser = parse_arguments()

    # take arguments
    speedup = opt_parser.s
    scalability = opt_parser.scalab
    efficiency = opt_parser.e
    execution = opt_parser.exectime
    comparison = opt_parser.compare

    knn_sequential = np.array([4187051, 15973321, 95360616, 375058248])  # knn sequential results [10k, 20k, 50k, 100k]

    # parallel knn results
    knn_p_10k = np.array([4195076, 2150114, 1324868, 726914, 322046, 182296, 133958, 99786, 99371])
    knn_p_20k = np.array([16573213, 8006220, 4072286, 2030168, 1087086, 677542, 434134, 308973, 256716])
    knn_p_50k = np.array([98816008, 50251728, 27676599, 13578018, 6741971, 3472759, 2151317, 1590471, 1046949])
    knn_p_100k = np.array([377017508, 201949754, 99481003, 51113708, 24312895, 14382776, 8876960, 6123643, 3969818])

    # fastflow knn results
    knn_f_10k = np.array([4198343, 2124308, 1072248, 539050, 316082, 210621, 141363, 106730, 95743])
    knn_f_20k = np.array([15989082, 8018496, 4034389, 2021035, 1062674, 588005, 400733, 318886, 274393])
    knn_f_50k = np.array([96277045, 48329593, 24244181, 12098202, 6183317, 3461644, 2278688, 1665072, 1122244])
    knn_f_100k = np.array([406293436, 201459406, 99968804, 50136748, 26882276, 14591443, 9016368, 6326216, 4312146])

    # workers
    knn_workers = np.array([pow(2, i) for i in range(9)])
    knn_workers_plot = [str(workers) for workers in knn_workers]

    # performance models for parallel knn
    knn_p_10k_speedup = knn_sequential[0]/knn_p_10k
    knn_p_10k_scalability = knn_p_10k[0]/knn_p_10k
    knn_p_10k_efficiency = knn_p_10k_speedup/knn_workers
    knn_p_20k_speedup = knn_sequential[1]/knn_p_20k
    knn_p_20k_scalability = knn_p_20k[0]/knn_p_20k
    knn_p_20k_efficiency = knn_p_20k_speedup/knn_workers
    knn_p_50k_speedup = knn_sequential[2]/knn_p_50k
    knn_p_50k_scalability = knn_p_50k[0]/knn_p_50k
    knn_p_50k_efficiency = knn_p_50k_speedup/knn_workers
    knn_p_100k_speedup = knn_sequential[-1]/knn_p_100k
    knn_p_100k_scalability = knn_p_100k[0]/knn_p_100k
    knn_p_100k_efficiency = knn_p_100k_speedup/knn_workers

    # performance models for fastflow knn
    knn_f_10k_speedup = knn_sequential[0]/knn_f_10k
    knn_f_10k_scalability = knn_f_10k[0]/knn_f_10k
    knn_f_10k_efficiency = knn_p_10k_speedup/knn_workers
    knn_f_20k_speedup = knn_sequential[1]/knn_f_20k
    knn_f_20k_scalability = knn_f_20k[0]/knn_f_20k
    knn_f_20k_efficiency = knn_f_20k_speedup/knn_workers
    knn_f_50k_speedup = knn_sequential[2]/knn_f_50k
    knn_f_50k_scalability = knn_f_50k[0]/knn_f_50k
    knn_f_50k_efficiency = knn_f_50k_speedup/knn_workers
    knn_f_100k_speedup = knn_sequential[-1]/knn_f_100k
    knn_f_100k_scalability = knn_f_100k[0]/knn_f_100k
    knn_f_100k_efficiency = knn_f_100k_speedup/knn_workers

    # plot execution time
    if execution:
        plot_performance(knn_workers_plot, "execution time", [knn_p_10k, knn_p_20k, knn_p_50k, knn_p_100k], "stdlib")
        plot_performance(knn_workers_plot, "execution time", [knn_f_10k, knn_f_20k, knn_f_50k, knn_f_100k], "ff")
        if comparison:
            plot_compare_performance(knn_workers_plot,
                                     "execution time",
                                     [knn_p_50k, knn_p_100k,
                                      knn_f_50k, knn_f_100k],
                                     ["50k", "100k", "50k", "100k"],
                                     ["stdlib", "stdlib", "ff", "ff"])
            print("Comparison between execution times plotted")

        print("Execution time plotted\n")

    # plot speedup
    if speedup:
        plot_performance(knn_workers_plot, "speedup", [knn_p_10k_speedup, knn_p_20k_speedup,
                                                       knn_p_50k_speedup, knn_p_100k_speedup], "stdlib")
        plot_performance(knn_workers_plot, "speedup", [knn_f_10k_speedup, knn_f_20k_speedup,
                                                       knn_f_50k_speedup, knn_f_100k_speedup], "ff")
        if comparison:
            plot_compare_performance(knn_workers_plot,
                                     "speedup",
                                     [knn_p_50k_speedup, knn_p_100k_speedup,
                                      knn_f_50k_speedup, knn_f_100k_speedup],
                                     ["50k", "100k", "50k", "100k"],
                                     ["stdlib", "stdlib", "ff", "ff"])
            print("Comparison between speedups plotted")

        print("Speedup plotted\n")

    # plot scalability
    if scalability:
        plot_performance(knn_workers_plot, "scalability", [knn_p_10k_scalability, knn_p_20k_scalability,
                                                           knn_p_50k_scalability, knn_p_100k_scalability], "stdlib")
        plot_performance(knn_workers_plot, "scalability", [knn_f_10k_scalability, knn_f_20k_scalability,
                                                           knn_f_50k_scalability, knn_f_100k_scalability], "ff")
        if comparison:
            plot_compare_performance(knn_workers_plot,
                                     "scalability",
                                     [knn_p_50k_scalability, knn_p_100k_scalability,
                                      knn_f_50k_scalability, knn_f_100k_scalability],
                                     ["50k", "100k", "50k", "100k"],
                                     ["stdlib", "stdlib", "ff", "ff"])
            print("Comparison between scalabilities plotted")

        print("Scalability plotted\n")

    # plot efficiency
    if efficiency:
        plot_performance(knn_workers_plot, "efficiency", [knn_p_10k_efficiency, knn_p_20k_efficiency,
                                                          knn_p_50k_efficiency, knn_p_100k_efficiency], "stdlib")
        plot_performance(knn_workers_plot, "efficiency", [knn_f_10k_efficiency, knn_f_20k_efficiency,
                                                          knn_f_50k_efficiency, knn_f_100k_efficiency], "ff")
        if comparison:
            plot_compare_performance(knn_workers_plot,
                                     "efficiency",
                                     [knn_p_50k_efficiency, knn_p_100k_efficiency,
                                      knn_f_50k_efficiency, knn_f_100k_efficiency],
                                     ["50k", "100k", "50k", "100k"],
                                     ["stdlib", "stdlib", "ff", "ff"])
            print("Comparison between efficiencies plotted")

        print("Efficiency plotted\n")

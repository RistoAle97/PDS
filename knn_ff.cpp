#include <iostream>
#include <queue>
#include <cmath>
#include <string>
#include "utimer.cpp"
#include "ff/ff.hpp"
#include "ff/parallel_for.hpp"
#include "utilities.h"

using namespace std;
using namespace ff;

int main(int argc, char* argv[])  {
    //check the arguments correctness
    if (argc==1 | argc>4) {
        cerr << "Wrong arguments, use instead: ./knn_ff points_file k nw" << endl;
        return-1;
    }
    vector<pair<float, float>> points; //points
    int k = int(stol(argv[2])); //k, the number of best neighbours with respect to the distance
    int nw = int(stol(argv[3])); //number of workers
    {
        utimer knn_read("The reading part was");
        points = read_points_file(argv[1]); //fill the points by reading them from a file
    }
    vector<string> points_neighs(points.size()); //outputs of each thread's work

    //check if k is not bigger than the number of points
    if (k>=points.size()) {
        cout << "WARNING: the value of k must be smaller than the number of points, KNN will be executed with k=sqrt(n)" << endl;
        k = int(sqrt(points.size()));
    }
    {
        utimer knn_sequential("KNN fastflow was");
        ParallelFor ff_pf(nw);
        ff_pf.parallel_for(0, long(points.size()), 1, [&](const int i){
            priority_queue<pair<int, float>, vector<pair<int, float>>, decltype(comparison)> top_k(comparison);
            knn_distances(ref(top_k), i, ref(points), k);
            points_neighs[i].append(build_results(top_k, i));
            }, nw);
    }
    {
        utimer knn_write("The writing part was");
        ofstream datafile("knn_ff_" + to_string(points.size()) + "_" + to_string(k) + ".txt");
        for (auto &point_results: points_neighs) {
            datafile << point_results; //write results to file
        }
    }
    return 0;
}

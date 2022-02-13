#include <iostream>
#include <queue>
#include <cmath>
#include <string>
#include <fstream>
#include "utimer.cpp"
#include "utilities.h"

using namespace std;

int main(int argc, char* argv[])  {
    //check the arguments correctness
    if (argc==1 | argc>4) {
        cerr << "Wrong arguments, use instead: ./knn_ff points_file k nw" << endl;
        return-1;
    }
    vector<pair<float, float>> points; //points
    int k = int(stol(argv[2])); //k, the number of best neighbours with respect to the distance
    int nw = int(stol(argv[3])); //number of workers
    vector<string> thread_outputs(nw); //outputs of each thread's work
    {
        utimer knn_read("The reading part was");
        points = read_points_file(argv[1]); //fill the points by reading them from a file
    }

    //check if k is not bigger than the number of points
    if (k>=points.size()) {
        cout << "WARNING: the value of k must be smaller than the number of points, KNN will be executed with k=sqrt(n)" << endl;
        k = int(sqrt(points.size()));
    }
    string knn_results;
    {
        utimer knn_sequential("KNN omp was");
        #pragma omp for schedule(static, 1)
        for (int i=0;i<points.size();i++) {
            priority_queue<pair<int, float>, vector<pair<int, float>>, decltype(comparison)> top_k(comparison);
            #pragma omp critical
            {
                knn_distances(ref(top_k), i, ref(points), k);
                knn_results.append(build_results(top_k, i));
            }
        }
    }
    {
        utimer knn_write("The writing part was");
        ofstream datafile("knn_omp_" + to_string(points.size()/1000) + "k_" + to_string(k) +  "_" + to_string(nw) + ".txt");
        datafile << knn_results;
    }
    return 0;
}

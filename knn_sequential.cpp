#include <iostream>
#include <queue>
#include <cmath>
#include <string>
#include <fstream>
#include "utimer.cpp"
#include "utilities.h"

using namespace std;

string knn(vector<pair<float, float>> &points, int k) {
    string knn_results;
    priority_queue<pair<int, float>, vector<pair<int, float>>, decltype(comparison)> top_k(comparison);
    for (int i=0;i<points.size();i++) {
        knn_distances(top_k, i, points, k);

        //update the final string containing the results
        knn_results.append(build_results(top_k, i));
    }
    return knn_results;
}

int main(int argc, char* argv[])  {
    //check the arguments correctness
    if (argc==1 | argc>3) {
        cerr << "Wrong arguments, use instead: ./knn_sequential points_file k" << endl;
        return-1;
    }
    vector<pair<float, float>> points; //points
    int k = int(stol(argv[2])); //k, the number of best neighbours with respect to the distance
    {
        utimer knn_read("The reading part was");
        points = read_points_file(argv[1]); //fill the points by reading them from a file
    }

    //check if k is not bigger than the number of points
    if (k>=points.size()) {
        cout << "WARNING: the value of k must be smaller than the number of points, KNN will be executed with k=sqrt(n)" << endl;
        k = int(sqrt(points.size()));
    }

    string knn_results; //string containing the results of knn
    {
        utimer knn_sequential("KNN sequential was");
        knn_results = knn(points, k); //apply knn on the points
    }
    {
        utimer knn_write("The writing part was");
        ofstream datafile("knn_sequential_" + to_string(points.size()/1000) + "k_" + to_string(k) + ".txt");
        datafile << knn_results; //write results to file
    }
}

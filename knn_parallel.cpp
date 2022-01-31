#include <iostream>
#include <queue>
#include <cmath>
#include <string>
#include <thread>
#include <fstream>
#include "utimer.cpp"
#include "utilities.h"

using namespace std;

void knn_task(vector<pair<float, float>> &points, int k, int workload, int batch_end, string &knn_results) {
    priority_queue<pair<int, float>, vector<pair<int, float>>, decltype(comparison)> top_k(comparison);
    for (int i=batch_end-workload;i<batch_end;i++) {
        knn_distances(ref(top_k), i, ref(points), k);

        //update the string containing the results of the thread's work
        knn_results.append(build_results(top_k, i));
    }
}

int main(int argc, char* argv[])  {
    //check the arguments correctness
    if (argc==1 | argc>4) {
        cerr << "Wrong arguments, use instead: ./knn_parallel points_file k nw" << endl;
        return-1;
    }
    vector<pair<float, float>> points; //points
    int k = int(stol(argv[2])); //k, the number of best neighbours with respect to the distance
    int nw = int(stol(argv[3])); //number of workers
    vector<thread> threads; //threads
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
    vector<int> workload (nw, int(points.size()/nw)); //workload for each thread

    //distribute the workload in excess to equally between the threads
    for (int i=0;i<points.size()%nw;i++) {
        workload[i]++;
    }
    {
        utimer knn_sequential("KNN parallel was");
        int batch_end=0; //it will store the end of one thread batch work
        for (int i=0;i<nw;i++) {
            batch_end += workload[i]; //update the batch end

            //compute knn
            threads.emplace_back(&knn_task, ref(points), k, workload[i], batch_end, ref(thread_outputs[i]));
        }
        for(thread &t: threads) {
            t.join(); //wait for all the threads to end
        }
    }
    {
        utimer knn_write("The writing part was");
        ofstream datafile("knn_parallel_" + to_string(points.size()/1000) + "k_" + to_string(k) + "_" + to_string(nw) +  ".txt");
        for (auto &thread_results: thread_outputs) {
            datafile << thread_results; //write results to file
        }
    }
    return 0;
}

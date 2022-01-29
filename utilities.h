//
// Created by risto97 on 8/30/21.
//

#ifndef PDS_UTILITIES_H
#define PDS_UTILITIES_H

#include <string>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<float, float>> read_points_file(const string &file);

float points_distance(pair<float, float> first_p, pair<float, float> second_p);

inline auto comparison = [](pair<int, float> p1, pair<int, float> p2) {return p1.second<p2.second;};

inline void knn_distances(priority_queue<pair<int, float>, vector<pair<int, float>>, decltype(comparison)> &top_k, int i, vector<pair<float, float>> &points, int k) {
    for (int j = 0; j < points.size(); j++) {
        if (i == j) {
            continue;
        }
        float distance = points_distance(points[i], points[j]);
        if (top_k.size() < k) {
            top_k.emplace(make_pair(j + 1, distance));
        } else {
            if (distance < top_k.top().second) {
                top_k.pop();
                top_k.emplace(make_pair(j + 1, distance));
            }
        }
    }
}

inline string build_results(priority_queue<pair<int, float>, vector<pair<int, float>>, decltype(comparison)> &top_k, int i) {
    string knn_results;
    knn_results.append(to_string(i + 1) + ": ");
    while (!top_k.empty()) {
        pair<int, float> point = top_k.top();
        top_k.pop();
        knn_results.append("<" + to_string(point.first) + ", " + to_string(point.second) + "> ");
    }
    knn_results.append("\n");
    return knn_results;
}

#endif //PDS_UTILITIES_H

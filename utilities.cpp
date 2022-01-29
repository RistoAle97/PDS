//
// Created by risto97 on 8/30/21.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include "utilities.h"

using namespace std;

vector<pair<float, float>> read_points_file(const string &file) {
    ifstream datafile(file);
    string row;
    vector<pair<float, float>> points;
    while (getline(datafile, row)) {
        int i = int(row.find(','));
        vector<string> split = {row.substr(0, i), row.substr(i+1, row.length())};
        points.emplace_back(make_pair(stof(split[0]), stof(split[1])));
    }
    return points;
}

float points_distance(pair<float, float> first_p, pair<float, float> second_p) {
    return float(sqrt(pow(first_p.first-second_p.first, 2) + pow(first_p.second-second_p.second, 2)));
}

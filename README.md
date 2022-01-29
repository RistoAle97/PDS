# PDS
Parallel and Distributed Systems project for the a.y. 2020/2021.
## K-Nearest Neighbours (KNN)
Given a set of points in a 2D space, we require to compute in parallel for each one of the points in the set of points the set of k closest points. Point i is the point whose coordinates are listed in line i in the file. The input of the program is a set of floating-point coordinates (one per line, comma separated) and the output is a set of lines each hosting a point id and a list of point ids representing its KNN set ordered with respect to distance.

## How to run
Compile with ```make```, then run the following commands as you prefer:
- sequential implementation
 ```
./knn_sequential datasets/points_dataset.txt
```
- parallel implementation (stdlib threads)
```
./knn_parallel datasets/points_dataset.txt workers
```
- fastflow implementation
```
./knn_ff datasets/points_dataset.txt workers
```
The reults will be saved in the corresponding directory with the name knn_implementation_points_workers.txt.

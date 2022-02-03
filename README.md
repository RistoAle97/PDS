# PDS
Parallel and Distributed Systems project for the a.y. 2020/2021.
## K-Nearest Neighbours (KNN)
Given a set of points in a 2D space, we require to compute in parallel for each one of the points in the set of points the set of k closest points. Point i is the point whose coordinates are listed in line i in the file. The input of the program is a set of floating-point coordinates (one per line, comma separated) and the output is a set of lines each hosting a point id and a list of point ids representing its KNN set ordered with respect to distance.

## Generate datasets
To generate the points that will be used during the KNN use the following command:
 ```
python generate_points.py --n 100000 --file datasets/points_file.txt --lbound 0 --ubound 10
```
It's suggested to save the datasets in the respective directory for a better organization.

## How to run
Compile with ```make```, then run the following commands as you prefer:
### sequential implementation
 ```
./knn_sequential datasets/points_dataset.txt
```
### parallel implementation (stdlib threads)
```
./knn_parallel datasets/points_dataset.txt n_workers
```
### fastflow implementation
```
./knn_ff datasets/points_dataset.txt n_workers
```
The results will be saved with the name knn_implementation_points_workers.txt.

### run more versions with one method
If you want to run more versions at the same time for more runs use the following command:
```
python --file datasets/points_10k.txt --k 10 --nw 256 --runs 10 --execute spf
```
The last argument determines which versions to run (s for sequential, p for parallel and f for fastflow), then you can use knn_plot.py to plot the results (beware that you need to manually change them).
## Plot results
To plot the results use ```knn_plot.py``` in the following way:
```
python knn_plot.py --s --scalab --e --exectime --compare
```
You can choose which kind of metrics to plot by typing ```--s``` for the speedup, ```--scalab``` for the scalability, ```e``` for efficiency and ```--exectime``` for the execution time. Then you can also ```--compare``` to plot the comparison for the metrics chosen before.

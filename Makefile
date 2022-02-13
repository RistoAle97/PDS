all: clean knn_sequential knn_parallel knn_ff knn_omp

COMPILER = g++
ARGUMENTS = -pthread -O3 -std=c++17 utilities.cpp utilities.h utimer.cpp

knn_sequential: knn_sequential.cpp
	${COMPILER} ${ARGUMENTS} knn_sequential.cpp -o knn_sequential
knn_parallel: knn_parallel.cpp
	${COMPILER} ${ARGUMENTS} knn_parallel.cpp -o knn_parallel
knn_ff: knn_ff.cpp
	${COMPILER} ${ARGUMENTS} -DNO_DEFAULT_MAPPING  knn_ff.cpp -o knn_ff
knn_omp: knn_omp.cpp
	${COMPILER} ${ARGUMENTS} -fopenmp knn_omp.cpp -o knn_omp

clean:
	@rm -rvf knn_sequential knn_parallel knn_ff knn_omp
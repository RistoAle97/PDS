all: clean knn_sequential knn_parallel knn_ff

COMPILER = g++
UTILITIES = utilities.cpp utilities.h utimer.cpp
ARGUMENTS = -pthread -O3 -std=c++17
FF = -DNO_DEFAULT_MAPPING

knn_sequential: knn_sequential.cpp
	${COMPILER} ${ARGUMENTS} ${UTILITIES} knn_sequential.cpp -o knn_sequential
knn_parallel: knn_parallel.cpp
	${COMPILER} ${ARGUMENTS} ${UTILITIES} knn_parallel.cpp -o knn_parallel
knn_ff: knn_ff.cpp
	${COMPILER} ${ARGUMENTS} ${UTILITIES} ${FF}  knn_ff.cpp -o knn_ff

clean:
	@rm -rvf knn_sequential knn_parallel knn_ff
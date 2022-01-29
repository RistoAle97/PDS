all: clean knn_sequential knn_parallel knn_ff

CC = g++
UTILITIES = utilities.cpp utilities.h utimer.cpp
LIBS = -pthread -O3 -std=c++17
LIBS_FF = -DNO_DEFAULT_MAPPING

knn_sequential: knn_sequential.cpp
	${CC} ${LIBS} ${UTILITIES} knn_sequential.cpp -o knn_sequential
knn_parallel: knn_parallel.cpp
	${CC} ${LIBS} ${UTILITIES} knn_parallel.cpp -o knn_parallel
knn_ff: knn_ff.cpp
	${CC} ${LIBS} ${UTILITIES} ${LIBS_FF}  knn_ff.cpp -o knn_ff

clean:
	@rm -rvf knn_sequential knn_parallel knn_ff
#include <iostream>
#include <chrono>

using namespace std;

#define START(timename) auto timename = chrono::system_clock::now();
#define STOP(timename,elapsed)  auto elapsed = chrono::duration_cast<chrono::microseconds>(chrono::system_clock::now() - timename).count();

class utimer {
    chrono::system_clock::time_point start;
    chrono::system_clock::time_point stop;
    string message;
    using usecs = chrono::microseconds;

private:
    long * us_elapsed;

public:

    utimer(const string m) : message(m),us_elapsed((long *)nullptr) {
        start = chrono::system_clock::now();
    }

    utimer(const string m, long * us) : message(m),us_elapsed(us) {
        start = chrono::system_clock::now();
    }

    ~utimer() {
        stop = chrono::system_clock::now();
        chrono::duration<double> elapsed = stop - start;
        auto musec = chrono::duration_cast<chrono::microseconds>(elapsed).count();

        cout << message << " computed in " << musec << " usec " << endl;
        if(us_elapsed != nullptr)
            (*us_elapsed) = musec;
    }
};

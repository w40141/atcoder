#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
    int num;
    int counter = 0;
    std::cin >> num;
    while (num > 2019) {
        int num_tmp = num;
        while (num_tmp > 2019) {
            std::cout << num_tmp << std::endl;
            if (num_tmp % 2019 == 0) {
                counter++;
            }
            num_tmp /= 10;
        }
        num /= 10;
    }
    std::cout << counter << std::endl;
    return 0;
}

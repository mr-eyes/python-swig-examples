#include <iostream>
#include "example.hpp"
#include <map>

using namespace std;

vector<int> kDataframe::get_it_abs()
{
    auto color = mp->find(1);
    return color->second;
}

kDataframe* kDataframe::load(){
    return new kDataframeMQF();
}

void kDataframeMQF::insert()
{

    static const int arr[] = {16, 2, 77, 29};
    vector<int> vec(arr, arr + sizeof(arr) / sizeof(arr[0]));

    this->mp = &this->mapOfOccur;
}

vector<int> kDataframeMQF::get_it()
{
    auto color = mp->find(1);
    return color->second;
}

// int main()
// {
//     kDataframeMQF K = kDataframeMQF();
//     K.insert();
//     vector<int> x = K.get_it();
// }
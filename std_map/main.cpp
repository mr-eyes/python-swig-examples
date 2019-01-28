#include "stdMap.hpp"

int main()
{

    testMap _testMap_ob = testMap();
    std::map<std::string, std::vector<int>> _map;

    _map = _testMap_ob.returnMap();

    std::map<std::string, std::vector<int>>::iterator it = _map.begin();
    while (it != _map.end())

    {
        std::cout << it->first << " :: ";

        for (auto const &i : it->second)
        {
            std::cout << i << ", ";
        }
        std::cout << std::endl;

        it++;
    }
}
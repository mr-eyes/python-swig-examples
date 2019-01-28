#include "stdMap.hpp"

std::map<std::string, std::vector<int>> testMap::returnMap()
{

    std::map<std::string, std::vector<int>> mapOfWords;
    // Inserting data in std::map

    std::vector<int> x = {1,2,3};

    mapOfWords.insert(std::make_pair("earth", x));
    mapOfWords.insert(std::make_pair("moon", x));
    mapOfWords["sun"] = x;

    return mapOfWords;
}
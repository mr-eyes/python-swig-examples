#include <iostream>
#include <queue>
#include <string>
#include "q.hpp"

int main()
{

    std::queue<std::string> kmers;
    std::string seq = "ATGAGGGGGATGCCCCTCTTTGAGCCCAAGGACGTAGCCTATATTTTGCAACGCGTGAC";

    inputModule *mod = moduleFactory::createModule("default");
    const std::vector<int> params = {21};
    mod->setParams(params);
    mod->fill_q(kmers, seq);
    int count = 0;
    std::cout << kmers.size() << " kmers\n" << std::endl;
    while (!kmers.empty())
    {
        std::cout << ++count << ": " << kmers.front() << std::endl;
        kmers.pop();
    }

    const std::vector<int> sk_params = {3,3,27};
    std::queue<std::string> skipmers;
    inputModule *sk = moduleFactory::createModule("skipmers");
    sk->setParams(sk_params);
    sk->fill_q(skipmers, seq);

    count = 0;
    std::cout << kmers.size() << " skipmers\n" << std::endl;
    while (!skipmers.empty())
    {
        std::cout << ++count << ": " << skipmers.front() << std::endl;
        skipmers.pop();
    }

}
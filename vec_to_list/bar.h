#ifndef _BAR_H
#define _BAR_H

#include "foo.h"
#include <vector>

class bar
{
  public:
    bar();
    bar(std::vector<foo> vectors);
    ~bar();

    std::vector<foo> get_vectors() { return m_vectors; }

    std::vector<foo> m_vectors;
};

#endif
//bar.cxx:
//-------------------------------------------
#include "bar.h"

bar::bar() {}

bar::bar(std::vector<foo> vectors)
{
    m_vectors = vectors;
}

bar::~bar() {}

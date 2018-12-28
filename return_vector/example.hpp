#include <string>
#include <vector>
#include <map>

using namespace std;

class kDataframe
{
  protected:
    map<int, vector<int>> *mp;
    map<int,vector<int>> mapOfOccur = {{1, {3, 4, 5, 6}}};

  public:
    virtual void insert() = 0 ;
    virtual vector<int> get_it()= 0;
    vector<int> get_it_abs();
    static kDataframe* load();
};


class kDataframeMQF : public kDataframe{
public:
    void insert();
    vector<int> get_it();
};

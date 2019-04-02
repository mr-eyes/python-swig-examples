#include <queue>
#include <string>
#include <vector>

class inputModule
{
  public:
    virtual void fill_q(std::queue<std::string> &kmers, std::string &seq) = 0;
    virtual void setParams(const std::vector<int> &params) = 0;
};

class inputModuleDefault : public inputModule
{
  private:
    int kSize;

  public:
    inputModuleDefault(){};
    void fill_q(std::queue<std::string> &kmers, std::string &seq);
    void setParams(const std::vector<int> &params);
};

class InputModuleSkipmers : public inputModule
{
  private:
    int m, n, k;
    int S;

  public:
    InputModuleSkipmers() {}
    void fill_q(std::queue<std::string> &kmers, std::string &seq);
    void setParams(const std::vector<int> &parms);
    virtual ~InputModuleSkipmers() {}
};

class moduleFactory
{

  public:
    static inputModule *createModule(const std::string mode)
    {   
        if (mode == "default"){
            return new inputModuleDefault;
        }else if(mode == "skipmers"){
            return new InputModuleSkipmers;
        }
        
    }
};
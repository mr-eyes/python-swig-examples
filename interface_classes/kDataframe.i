/* File : example.i */
%module kDataframe

%{
#include "kDataframe.hpp"
%}

/* Let's just grab the original header file here */
class Circle : public Shape
{
  private:
    double radius;

  public:
    Circle(double r);
    virtual double area();
    virtual double perimeter();
};
#include "kDataframe.hpp"
#include "math.h"

/* Move the shape to a new location */
void Shape::move(double dx, double dy)
{
    x += dx;
    y += dy;
}

int Shape::nshapes = 0;

Square::Square(double r){
    this->width = r;
}

double Square::area(){
    return std::pow(this->width, 2);
}

double Square::perimeter(){
    return this->width * 4;
}


Circle::Circle(double r){
    this->radius = r;
}

double Circle::area(){
    return 3.14 * std::pow(this->radius, 2);
}

double Circle::perimeter(){
    return 2 * this->radius * 3.14;
}
#ifndef _FOO_H
#define _FOO_H

class foo
{
  public:
    foo();
    foo(float x, float y, float z);
    ~foo();

    float m_x;
    float m_y;
    float m_z;

    float mag();
};

#endif
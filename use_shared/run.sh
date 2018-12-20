rm *cxx mqf.py mqf_wrap.c
swig -c++ -python mqf.i
python setup.py build_ext --inplace
#python mqf.py
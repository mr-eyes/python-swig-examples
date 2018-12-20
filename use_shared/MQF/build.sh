rm *cxx mqf.py
swig -c++ -python mqf.i
python setup.py build_ext --inplace
python mqf.py
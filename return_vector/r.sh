rm *cxx *so *pyc example.pyc
swig -c++ -python example.i
python setup.py build_ext --inplace
python run.py
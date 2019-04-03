rm *cxx *so *pyc callback.pyc
swig -c++ -python callback.i
python setup.py build_ext --inplace
python run.py
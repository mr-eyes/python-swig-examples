rm -rf *cxx *so *pyc *gch example.py build
swig -c++ -python example.i
python setup.py build_ext --inplace
python run.py
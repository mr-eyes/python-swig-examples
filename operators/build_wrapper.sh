rm -rf *cxx *so *pyc *gch operators.py build
swig -c++ -python operators.i
python setup.py build_ext --inplace
python run.py
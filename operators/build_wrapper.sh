rm -rf *cxx *so *pyc *gch callback.py build
swig -c++ -python callback.i
python setup.py build_ext --inplace
# python run.py
rm -rf build/ *cxx *so
swig -c++ -python example.i
python setup.py build_ext --inplace
python run.py
rm -rf build *cxx *so *pyc swigMap.pyc swigMap.py
swig -c++ -python swig_map.i
python setup.py build_ext --inplace
python run.py
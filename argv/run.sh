rm -rf *cxx argv.py *so *pyc
swig -c++ -python argv.i
python setup.py build_ext --inplace
python call_main.py It worked like a charm!
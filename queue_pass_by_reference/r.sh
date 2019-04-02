rm -rf *cxx *so *gch *pyc inputModule.pyc
swig -c++ -python inputModuleSwigInterface.i
python setup.py build_ext --inplace
#python run.py
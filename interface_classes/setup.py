"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


kDataframe_module = Extension(name='_kDataframe',
                              sources=['kDataframe_wrap.cxx', "src/kDataframe.cpp"],
                       include_dirs=["include"],
                       language='c++',
                       )

setup(name='kDataframe',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[kDataframe_module],
      py_modules=["kDataframe"],
      )

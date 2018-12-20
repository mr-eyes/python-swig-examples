"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


mqf_module = Extension(name='_argv',
                       sources=['argv_wrap.cxx', "main.cpp", "hellYeah.cpp"],
                       include_dirs=["include"],
                       language='c++',
                       )

setup(name='argv',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[mqf_module],
      py_modules=["argv"],
      )

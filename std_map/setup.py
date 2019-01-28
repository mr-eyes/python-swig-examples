"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


swigMap_module = Extension('_swigMap',
                           sources=['swig_map_wrap.cxx', 'stdMap.cpp'],
                           )

setup(name='swigMap',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[swigMap_module],
      py_modules=["swigMap"],
      )

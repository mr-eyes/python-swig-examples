"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


mqf_module = Extension(name = '_mqf',
                           sources=['mqf.i','mqf_wrap.cxx', 'src/gqf.cpp', 'src/utils.cpp'],
                           include_dirs=["include"]
                           )

setup(name='mqf',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[mqf_module],
      py_modules=["mqf"],
      )

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


operators_module = Extension('_operators',
                           sources=['operators_wrap.cxx', 'operators.cpp'],
                           )

setup(name='operators',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[operators_module],
      py_modules=["operators"],
      )

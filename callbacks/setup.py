"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


callback_module = Extension('_callback',
                           sources=['callback_wrap.cxx', 'callback.cpp'],
                           )

setup(name='callback',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[callback_module],
      py_modules=["callback"],
      )

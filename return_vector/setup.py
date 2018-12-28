"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


example_module = Extension('_example',
                           sources=['example_wrap.cxx', 'example.cpp'],
                           extra_compile_args=['-Wall', "-lgomp", '-Wextra', '-std=c++14', '-fPIC', '-fopenmp',
                                               '-W', '-Wall', '-pedantic', '-lrt', '-lpthread', '-lbz2', '-lz', '-DSEQAN_HAS_ZLIB=1',
                                               '-DSEQAN_HAS_BZIP2=1', '-DSEQAN_HAS_OPENMP=1', "-DSEQAN_HAS_EXECINFO=1"],

                           extra_link_args=["-fopenmp", "-lgomp", "-lbz2"]
                           )

setup(name='example',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[example_module],
      py_modules=["example"],
      )

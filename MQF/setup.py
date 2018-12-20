"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension


mqf_module = Extension(name='_MQF',
                       sources=['mqf_wrap.cxx'],
                       include_dirs=["include"],
                       language='c++',
                       #extra_link_args=['-static'],
                       libraries=["MQF"],
                       library_dirs=['MQF/build/']
                       )

setup(name='MQF',
      version='0.1',
      author="SWIG Docs",
      description="""Simple swig example from docs""",
      ext_modules=[mqf_module],
      py_modules=["MQF"],
      )

all: clean py 

py: 
	python setup.py build_ext --inplace 

test: 
	python test.py 

clean: 
	rm -rf build rm *_wrap.* *.o *.so bar.py *.pyc 

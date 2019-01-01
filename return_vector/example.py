# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _example
else:
    import _example

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _example.delete_SwigPyIterator

    def value(self):
        return _example.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _example.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _example.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _example.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _example.SwigPyIterator_equal(self, x)

    def copy(self):
        return _example.SwigPyIterator_copy(self)

    def next(self):
        return _example.SwigPyIterator_next(self)

    def __next__(self):
        return _example.SwigPyIterator___next__(self)

    def previous(self):
        return _example.SwigPyIterator_previous(self)

    def advance(self, n):
        return _example.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _example.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _example.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _example.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _example.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _example.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _example.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _example:
_example.SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def iterator(self):
        return _example.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _example.IntVector___nonzero__(self)

    def __bool__(self):
        return _example.IntVector___bool__(self)

    def __len__(self):
        return _example.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _example.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _example.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _example.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _example.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _example.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _example.IntVector___setitem__(self, *args)

    def pop(self):
        return _example.IntVector_pop(self)

    def append(self, x):
        return _example.IntVector_append(self, x)

    def empty(self):
        return _example.IntVector_empty(self)

    def size(self):
        return _example.IntVector_size(self)

    def swap(self, v):
        return _example.IntVector_swap(self, v)

    def begin(self):
        return _example.IntVector_begin(self)

    def end(self):
        return _example.IntVector_end(self)

    def rbegin(self):
        return _example.IntVector_rbegin(self)

    def rend(self):
        return _example.IntVector_rend(self)

    def clear(self):
        return _example.IntVector_clear(self)

    def get_allocator(self):
        return _example.IntVector_get_allocator(self)

    def pop_back(self):
        return _example.IntVector_pop_back(self)

    def erase(self, *args):
        return _example.IntVector_erase(self, *args)

    def __init__(self, *args):
        _example.IntVector_swiginit(self, _example.new_IntVector(*args))

    def push_back(self, x):
        return _example.IntVector_push_back(self, x)

    def front(self):
        return _example.IntVector_front(self)

    def back(self):
        return _example.IntVector_back(self)

    def assign(self, n, x):
        return _example.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _example.IntVector_resize(self, *args)

    def insert(self, *args):
        return _example.IntVector_insert(self, *args)

    def reserve(self, n):
        return _example.IntVector_reserve(self, n)

    def capacity(self):
        return _example.IntVector_capacity(self)
    __swig_destroy__ = _example.delete_IntVector

# Register IntVector in _example:
_example.IntVector_swigregister(IntVector)

class kDataframe(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def insert(self):
        return _example.kDataframe_insert(self)

    def get_it(self):
        return _example.kDataframe_get_it(self)

    def get_it_abs(self):
        return _example.kDataframe_get_it_abs(self)
    load = staticmethod(_example.kDataframe_load)
    __swig_destroy__ = _example.delete_kDataframe

# Register kDataframe in _example:
_example.kDataframe_swigregister(kDataframe)

def kDataframe_load():
    return _example.kDataframe_load()

class kDataframeMQF(kDataframe):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def insert(self):
        return _example.kDataframeMQF_insert(self)

    def get_it(self):
        return _example.kDataframeMQF_get_it(self)

    def __init__(self):
        _example.kDataframeMQF_swiginit(self, _example.new_kDataframeMQF())
    __swig_destroy__ = _example.delete_kDataframeMQF

# Register kDataframeMQF in _example:
_example.kDataframeMQF_swigregister(kDataframeMQF)




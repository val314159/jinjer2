#!/usr/bin/env python
"""
Static Macro File Generator (cmd line generator using jinja2)

Ever want to just apply a model to a bunch of files?  Now you can!

### Usage:

```sh
  export VERBOSE=1 # to turn on verbosity
```

```sh
  # command line usage
  python -mjinger2
```

```python
  # python usage
  >>> import jinger2
  >>> jinjer2.generate()
```
"""
import os, sys, json, jinja2
from pprint import pprint

verbose=os.environ.get('VERBOSE')

def load_models(modname):
    if verbose: print ">> import models ( __import__('%s') )" % modname
    return dict((k,v) for k,v
                in __import__(modname).__dict__.iteritems()
                if not k.startswith('__'))

class obj(object):
    def __init__(_,**kw): [ setattr(_,k,v) for k,v in kw.iteritems() ]
    def _iterkeys (_):return( x for x in dir(_) if not x.startswith('_') )
    def _iteritems(_):return((x,getattr(_,x))for x in _._iterkeys())
    def _keys(_): return list(_._iterkeys())
    def __repr__(_):return str(dict(_._iteritems()))
    def __str__ (_):return str(_._keys())
    pass

class objt(obj):
    def _template(_): return jinja2.Template(_.contents)
    def _render(_):   return _._template().render(**_.models)
    pass

def mmkdir(*a):
    if verbose: print ">> mmkdir", (os.path.join(*a))
    try: os.mkdir(os.path.join(*a))
    except: pass
    pass

def dump(str,f):
    f=open(os.path.join(*f),'w+')
    f.write(str)
    f.close()
    return str

def good(x):
    if '/.ve' in x:        return
    if x.endswith('~'):    return
    return True

def generate(
    outputdir='output',
    inputdirs='content'.split(),
    includedirs='include'.split(),
    models=load_models('models'),
    ):
    mmkdir(outputdir)
    for indirname in inputdirs:
        mmkdir(outputdir,indirname)
        for prefix,dirs,files in os.walk(indirname):
            for dname in dirs:
                mmkdir(outputdir,prefix,dname)
                pass
            for fname in files:
                fullname = os.path.join(prefix,fname)
                if good(fullname):
                    if verbose: print ">> START ", '-'*40, fullname
                    contents=open(fullname).read()
                    output = objt(fname=fullname,
                              models=models,
                              contents=contents,
                              )._render()
                    if verbose:
                        print '>>', repr(output)
                        pass
                    dump(output,('output',fullname))
                    if verbose: print ">> FINISH", '-'*40, fullname

if __name__=='__main__': generate()

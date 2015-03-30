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
from utils57 import *

verbose=os.environ.get('VERBOSE')

def good(x):
    if '/.ve' in x:        return
    if x.endswith('~'):    return
    return True

def xwalk1(src_dir, dst_dir, func, good=good):
    for orig_prefix,dirs,files in os.walk(src_dir):
        prefix = orig_prefix[len(src_dir)+1:]
        for dname in dirs:
            out_name = os.path.join( dst_dir, prefix, dname )
            if verbose: print ">> mkdir", out_name
            force( lambda: os.makedirs(out_name) )
            pass
        for fname in files:
            inp_name = os.path.join( src_dir, prefix, fname )
            out_name = os.path.join( dst_dir, prefix, fname )
            if good(inp_name):
                func(inp_name,out_name)
                pass
            pass
        pass
    pass

def xwalkN(src_dirs, dst_dir, func, good=good):
    for src_dir in src_dirs.split(','):
        xwalk1(src_dir, dst_dir, func, good)
    pass

##
def load_models(modname):
    if verbose: print ">> import models ( __import__('%s') )" % modname
    return dict((k,v) for k,v
                in __import__(modname).__dict__.iteritems()
                if not k.startswith('__'))

def gen_file(fullname,fulloutput,models=load_models('models')):
    if verbose: print ">> GF", fullname,'|'
    contents=load(fullname)
    output = objt(fname=fullname,
                  models=models,
                  contents=contents,
    )._render()
    if verbose: print output,'\n<<','-'*60
    force(lambda:os.unlink(fulloutput))
    return dump(fulloutput,output)

def copy_file(fullname,fulloutput,models=load_models('models')):
    if verbose: print ">> CF", fullname
    force(lambda:os.unlink(fulloutput))
    return os.link(fullname,fulloutput)

def generate(outdir='output',
             indirs='content,content2',
             statics='static,static2',
             includes='include,include2',
):
    xwalkN(indirs,  outdir, gen_file)
    xwalkN(statics, outdir, copy_file)
    includes = includes.split(',')
    pass

if __name__=='__main__': generate()

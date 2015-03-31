#!/usr/bin/env python
"""
Static Macro File Generator (cmd line generator using jinja2)

Ever want to just apply a model to a bunch of files?  Now you can!

### Usage:

```sh
  # command line usage
  jinger2
```

```python
  # python usage
  >>> import jinger2
  >>> jinjer2.generate()
```
"""
__version__='0.1.1'
__author__='Joel Ward'
import os, sys, json
##
class untrue(object):
    """
    new type of object to comunicate untruth
    """
    def __nonzero__(_): return False
    pass
def force(thunk):
    """
    if you pass this a thunk, it will evaluate it and eat the errors.
    """
    try: return thunk()
    except: untrue()
##
def loadf(f):     str=f.read(); f.close(); return str
def dumpf(f,str): f.write(str); f.close(); return str

def dump(f,str):
    if type(f) in (type(()),type([])): f = os.path.join(f)
    if type(f) is  type(''): f = open(f,'w+')
    return dumpf(f,str)

def load(f):
    if type(f) in (type(()),type([])): f = os.path.join(f)
    if type(f) is  type(''): f = open(f)
    return loadf(f)
##
class obj(object):
    "Generic object.  Toss in whatever you want."
    def __init__(_,**kw): [ setattr(_,k,v) for k,v in kw.iteritems() ]
    def _iterkeys (_):return( x for x in dir(_) if not x.startswith('_') )
    def _iteritems(_):return((x,getattr(_,x))for x in _._iterkeys())
    def _keys(_): return list(_._iterkeys())
    def __repr__(_):return str(dict(_._iteritems()))
    def __str__ (_):return str(_._keys())
    pass
class objt(obj):
    def _template(_): import jinja2; return jinja2.Template(_.contents)
    def _render(_):   return _._template().render(**_.models)
    pass
##
##
def good(x):
    if '/.ve' in x:        return
    if x.endswith('~'):    return
    return True

def xwalk1(src_dir, dst_dir, func, good=good):
    for orig_prefix,dirs,files in os.walk(src_dir):
        prefix = orig_prefix[len(src_dir)+1:]
        for dname in dirs:
            out_name = os.path.join( dst_dir, prefix, dname )
            if options.verbose: print ">> mkdir", out_name
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

def xwalkN(src_dirs, *a, **kw):
    for src_dir in src_dirs.split(','):
        xwalk1(src_dir, *a, **kw)
    pass
##
def copy_file(fullname,fulloutput):
    if options.verbose: print ">> CF", fullname
    force(lambda:os.unlink(fulloutput))
    return os.link(fullname,fulloutput)

models = {}

def yload_models(filename):
    global models
    import yaml
    models=yaml.load(load(filename))
    return models

def pload_models(filename):
    global models
    globals={}
    execfile(filename,globals)
    models = dict((k,v) for k,v in globals.iteritems()
                  if not k.startswith('__'))
    return models

def load_models(filename):
    return(pload_models(filename)
           if filename.endswith('.py') else
           yload_models(filename))

def gen_file(fullname,fulloutput):
    if options.verbose: print ">> GF", fullname,'|'
    contents=load(fullname)
    output = objt(fname=fullname,
                  models=models,
                  contents=contents,
                  )._render()
    if options.verbose: print output,'\n<<','-'*60
    force(lambda:os.unlink(fulloutput))
    return dump(fulloutput,output)
####
def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--models', dest='models',   default='models.py',
                        help='directory for source input')
    parser.add_argument('-i','--input',  dest='inputdir', default='content',
                        help='directory for source input')
    parser.add_argument('-o','--output', dest='outputdir',default='output',
                        help='directory for generated output')
    parser.add_argument('-s','--static', dest='staticdir',default='static',
                        help='directory for static input')
    parser.add_argument('-r','--recurse',action='store_true',
                        help='whether to recurse')
    parser.add_argument('-v','--verbose',action='store_true',
                        help='increase output verbosity')
    return parser.parse_args()

def main():
    global options
    options=parse_args()
    load_models(options.models)
    force(lambda:os.mkdir(options.outputdir))
    xwalkN(options.staticdir, options.outputdir,copy_file)
    xwalkN(options.inputdir,  options.outputdir, gen_file, good)
    pass

if __name__=='__main__': main()

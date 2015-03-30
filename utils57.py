import os, sys, json, jinja2
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

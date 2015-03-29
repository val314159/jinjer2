"""
Models file.

Basically this is just a big giant namespace
to hold various models (of various domains).
default model space is 'model' or 'M' for short.

The environment will inject a bunch of stuff into the 
toplevel namespace.

"""

# put the "real" model in a seperate namespace
# so the global injection doesnt mess it all up.
M = model = {} 


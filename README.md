# jinjer2

<div style="float: right">

<img style="float:left" src="http://www.patsusmilch.com/wp-content/uploads/2014/11/600px-orange-cat.jpg"
 width="100px">
 <div>
 <i>Ginger: a cat who loves macros!</i>
 </div>
</div>

jinjer2 is a jinja2 command line macro tool (recursive file processor)

## Install:

```sh
python setup.py install
```

## Run:

```sh
export VERBOSE=1

jinjer2.py
```

## What did it just do?

1. load models (import models.py)
1. walk template directories (content), render against local -> output dir
2. local = models + <root_dir>/site.py + <next_root_dir>/site.py + <bottom_dir>/site.py
1. walk static directories (static), copy/link -> output dir

- how do includes work?  relative to root?

- template inheritance example?

- when walking directories, probably dont need to copy the toplevel name<br>
 *(i.e. dont copy into ./output/content/stuff/blah.xxx -> do output/stuff/blah.xxx)*

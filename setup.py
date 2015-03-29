from setuptools import setup, find_packages
setup(
    name = "Jinjer2",
    version = "0.1",
    packages = find_packages(),
    scripts = ['jinjer2.py'],

    install_requires = ['Jinja2==2.7.3',
                        'pyaml==15.3.1',
                        ],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        #'': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        #'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author = "Joel Ward",
    author_email = "jmward@gmail.com",
    description = "Static Macro File Generator (cmd line generator using jinja2)",
    license = "Apache",
    keywords = "jinja2 static file generator macro",
    url = "http://ccl.io/jinjer2/",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)

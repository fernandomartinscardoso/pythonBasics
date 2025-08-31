# Designing with Python Using Library py5

Repository created to add the abstract and notes on the Domestika course [Designing with Python: Programming for a Visual Context](https://www.domestika.org/en/courses/4307-designing-with-python-programming-for-a-visual-context) by the visual artist Alexandre Villares.

The course is based on __py5__ library resources, and it was originally conceived to work with [Thonny IDE](https://thonny.org/), but I adapted the codes to a more general approach with any Python IDE.

The course, as per resources available on August 17<sup>th</sup> 2025, is composed by 4 units and one final project. The .py codes refer to the units as per reference in their names, e.g, `<name>_u2_v3.py` is a code based on Unit 2, Video 3.

It is noticeable how Villares doesn't use `from py5 import *` option, or even `import py5`, because he is running the code using Imported Mode. My adaptation also avoids `from py5 import *` because the [py5 web documentation](https://py5coding.org/content/py5_modes.html) explains that py5’s Module Mode is dependent on the module __getattr__ and __dir__ functionality described in [PEP 562](https://peps.python.org/pep-0562/).

For more information and full documentation, check [py5 web site.](https://py5coding.org/)

import os

# Automatically imports all modu
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or os.path.isdir(__file__):
        continue
    __import__("modules."+module, locals(), globals())
    del module # remove from scope

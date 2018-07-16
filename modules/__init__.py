import os

# Automatically imports all modules
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or os.path.isdir(__file__): #module[-3:] != '.py'
        continue
    __import__("modules."+module, locals(), globals())
    #del module

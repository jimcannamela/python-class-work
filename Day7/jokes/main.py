# create virtual environment
# python -m venv ./my_env

# activate the virtual environment
# source ./my_env/bin/activate (MAC OS)
#        ./my_env/Scripts/activate (Windows)

# pip install pyjokes (install the pyjokes package)

import pyjokes
#print(pyjokes)


print(pyjokes.get_joke())


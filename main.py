import os
import subprocess

if os.path.isfile('paths.txt'):
    print("O arquivo 'paths.txt' existe. Executando filho.py...")
    subprocess.run(['python', 'filho.py'])
else:
    print("O arquivo 'paths.txt' não existe. Executando pai.py...")
    subprocess.run(['python', 'pai.py'])

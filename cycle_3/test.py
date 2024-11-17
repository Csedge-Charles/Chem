import os
import sys
sys.path.append(os.path.abspath('/Users/charlesshao/Chem-2'))
from func import balance, sigfig, combustion




print(balance('CO2', 'H2O', 'C6H12O6', 'O2'))

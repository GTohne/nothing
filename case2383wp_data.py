from case import Case
import pandas as pd

bus = pd.read_excel('case2383wp_data/bus.xlsx',header=None)
bus = bus.values
gen = pd.read_excel('case2383wp_data/gen.xlsx',header=None)
gen = gen.values
branch = pd.read_excel('case2383wp_data/branch.xlsx',header=None)
branch = branch.values
MVA = 100
KV = 220

case2383wp = Case(bus,gen,branch,MVA,KV)
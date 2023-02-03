from case import Case
import pandas as pd

bus = pd.read_excel('case4gs_data/bus.xlsx',header=None)
bus = bus.values
gen = pd.read_excel('case4gs_data/gen.xlsx',header=None)
gen = gen.values
branch = pd.read_excel('case4gs_data/branch.xlsx',header=None)
branch = branch.values
MVA = 100
KV = 230

case4gs = Case(bus,gen,branch,MVA,KV)
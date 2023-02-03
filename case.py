class Case():
    def __init__(self,bus,gen,branch,MVA,KV):
        self.bus = bus
        self.gen = gen
        self.branch = branch
        self.baseMVA = MVA
        self.baseKV = KV
from central_limit_theorem import CLT
from law_of_large_numbers import LLN
from bessels_correction import BC

def run_bessels_correction(data = 'normal', sample = None):
    BC().run(data, sample)

def run_law_of_large_number(data = 'normal', sample = None):
    LLN().run(data, sample)

def run_CLT(data = 'normal'):
    CLT().run(data)
from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1] # contract [-1] gets us the most recent  deployment
    # go takethe index that is one less than the length
    # ABI
    # Address
    print(simple_storage.retreive())
    
def main():
    read_contract()
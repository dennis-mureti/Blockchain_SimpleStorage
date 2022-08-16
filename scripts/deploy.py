from brownie import accounts, config, SimpleStorage, network

# all logic goes to this function
def deploy_simple_storage():
    # ways to add accounts
    # 1. Buils-in localgenache Accounts
    # account = accounts[0]  # [0] for when working with a development account e.g. Ganache
    account = get_account()
    simple_storage = SimpleStorage.deploy(
        {"from": account}
    )  # to deploy to a local chain
    stored_value = (
        simple_storage.retreive()
    )  # brownie will tell if it's  a call or transaction
    # to update
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retreive  # to check if it has been updated
    print(updated_stored_value)

    # 2. Encrypted command line
    # account = accounts.load("dennis-block-account") #to work with account created
    # print(account)
    # 3. Environment variables and Brownie config(have private key as environment variable(.env))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage() 

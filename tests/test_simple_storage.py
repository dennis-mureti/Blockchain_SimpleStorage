from brownie import SimpleStorage, accounts

# defining our test
def test_deploy():
    # arrange
    account = accounts[0]  # to grap our account
    # act
    simple_storage = SimpleStorage.deploy({"from": account})  # deploying
    starting_value = simple_storage.retreive()  # call to see what starting value is
    expected = 0
    # assert
    assert starting_value == expected

    # to test updating with 15


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(
        expected, {"from": account}
    )  # to store 15 in our smart contract
    # Assert
    assert expected == simple_storage.retreive()

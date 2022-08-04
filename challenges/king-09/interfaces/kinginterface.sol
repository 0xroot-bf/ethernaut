// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface KingInterface {
    function _whoIsKing() external view returns (address payable);
}
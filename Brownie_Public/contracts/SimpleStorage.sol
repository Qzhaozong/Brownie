// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract SimpleStorage {
    uint256 private value;
    address public owner;

    event ValueChanged(uint256 newValue);

    constructor() {
        owner = msg.sender;
        value = 100;
    }

    // 修改器定义
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    // 只有所有者可以设置值
    function setValue(uint256 newValue) public onlyOwner {
        value = newValue;
        emit ValueChanged(newValue);
    }

    // 任何人都可以获取值
    function getValue() public view returns (uint256) {
        return value;
    }

    // 任何人都可以递增（或者也可以加上 onlyOwner，根据需求）
    function increment() public {
        value += 1;
        emit ValueChanged(value);
    }
}

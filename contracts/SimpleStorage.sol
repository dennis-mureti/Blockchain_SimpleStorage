// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract SimpleStorage {
    // type and declaringg variable. // public keyword defines visibility of keywork or the function
    uint256 favoriteNumber; // will get initialized to 0!
    // bool favoriteBool  = false;
    // string favoriteStrng = "string";
    // int256 favoriteInt = -5;
    // address favoriteAddress = 0x24837DcC229991800241D264B89B7D6037d2cB00;
    // bytes32 favoriteBytes  = "cat";

    // ways todefine new types in solidity.(new object)
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    // creating an array.Dynamic array
    People [] public people;

    // create a data structure
    // mapping takes key and gives variable it is mapped to
    mapping(string => uint256) public nameToFavoriteNumber;

    People public person = People ({favoriteNumber: 2, name: "Dennis"});

    function store (uint256 _favoriteNumber) public returns (uint256){
        favoriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }
    // view functions helps read state in blockchain (does not change state of blockchain).
    // pure functions are functions that purely do math.
    function retreive() public view returns (uint256) {
        return favoriteNumber;
    }

    // function to add person to People Array.
    // memory means that it will be only be stored during excecution. storage means that data will still be there after excecution
    function addPerson (string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber [_name] = _favoriteNumber;
    }

}
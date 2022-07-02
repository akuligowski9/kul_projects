pragma solidity >=0.5.0 <0.6.0;

contract ZombieFactory {

    //statevariables permanently stored in contract storage, blockchain, or writing to DB
    uint dnaDigits = 16;
    //uint is actually an alias for uint256, a 256-bit unsigned integer.
    uint dnaModulus = 10 ** dnaDigits;

    struct Zombie {
        uint dna;
        string name;
    }
    //structs are more complex data types with multiple properties

    //array are used for a collection; there are two types: fixed and dynamic
    // array with a fixed length of 2 elements:

    //    uint[2] fixedArray;
    //    // another fixed Array, can contain 5 strings:
    //
    //    string[5] stringArray;
    //    // a dynamic Array - has no fixed size, can keep growing:
    //
    //    uint[] dynamicArray;
    //
    //    Person[] people; // dynamic Array, we can keep adding to it

    Zombie[] public zombies; // declaring an array as public will automatically create a getter

    function _createZombie(string memory _name, uint _dna) private {
        zombies.push(Zombie(_name, _dna));
    }
}

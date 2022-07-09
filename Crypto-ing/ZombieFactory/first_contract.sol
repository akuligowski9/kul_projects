pragma solidity >=0.5.0 <0.6.0;

contract ZombieFactory {

    // Events are a way for your contract to communicate that something happened on the blockchain to your app front-end, which can be 'listening' for certain events and take action when they happen.
    event NewZombie(uint zombieId, string name, uint dna);

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
        // We want an event to let our front-end know every time a new zombie was created, so the app can display it.
        uint id = zombies.push(Zombie(_name, _dna)) - 1;
        emit NewZombie(id, _name, _dna);
    }
    // In Solidity, the function declaration contains the type of the return value
    // we could declare it as a view function, meaning it's only viewing the data but not modifying it
    // Solidity also contains pure functions, which means you're not even accessing any data in the app — its return value depends only on its function parameter
    function _generateRandomDna(string memory _str) private view returns (uint) {
        uint rand = uint(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }

    function createRandomZombie(string memory _name) public {
        uint randDna = _generateRandomDna(_name);
        _createZombie(_name, randDna);
    }
}

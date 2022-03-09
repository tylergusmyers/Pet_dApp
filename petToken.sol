pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract ArtToken is ERC721Full {
    uint256  _parent1;
    uint256  _parent2;
    address public _breeder;

    uint public _birthDateTime;
    string public _petType;
    string public _breed;
    string public _petURI;

    mapping(uint256 => string) updates;

    constructor() public ERC721Full("PetToken", "PET") {}

    function createPet(string memory petURI, string memory petType, string memory breed, uint  birthDateTime, uint256  parent1, uint256  parent2)
        public
        returns (uint256)
    {
        uint256 tokenId = totalSupply();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, petURI);
        _breeder = msg.sender;
        _parent1 = parent1;
        _parent2 = parent2;
        _birthDateTime = birthDateTime;
        _petType = petType;
        _breed = breed;
       
        return tokenId;
    }

    function updatePet(uint256 tokenId, string memory update) public
    {
        require(msg.sender == ownerOf(tokenId), "You do not have permission to Update this  Pet!");
        // Possible to extend the same to a Vet address.
        updates[tokenId] = string(abi.encodePacked(update, updates[tokenId]));
    }

    function terminatePet(uint256 tokenId) public
    {
        require(msg.sender == ownerOf(tokenId), "You do not have permission to Update this  Pet!");
        _burn(tokenId); /* Should we be burning token?? */
    }
}


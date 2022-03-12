# Pet_dApp

![Pet ID](https://assets.orvis.com/is/image/orvisprd/2SFY048VD_MSSW?wid=1200&src=is($object$:1-1))

---
Using Blockchain Technology, this dApp develops a new way to store and keep track of your Pet's information. Whether you want to keep track of the linage of your prized breed, vaccinations, or completion of transfer to a new owner. Ideal use for pet owners, breeders, vetenarians, and regulators alike.
---
## Technologies
Implements ERC721 Token(https://eips.ethereum.org/EIPS/eip-721) 
- streamlit
- Ganache/Ethereum
- Solidity
---

## Installation Guide

- Clone this repo
- Deploy  Contract token in your Ethereum network
  - load  "petToken.sol" in https://remix.ethereum.org/ and compile
  - Deploy the Contract and get the address of the contract
  - *** Warning *** The contract abi in the repository is from the same revision of petToken.sol. Any chnages in this file will fail the deployment
-  Initialize variables needed in your environment
  - `WEB3_HTTP_PROVIDER='YOUR_WEB_HTTP_PROVIDER'`
  - `CONTRACT_TOKEN_ADDRESS='Adress of the contract deployed above'`
- Install the dependencies
  - `pip install -r requirements.txt`
- Deploy the app
  - `streamlit run create_pet.py`
- Select the account from the dropdown in the sidebar and start using the app.
---

## Usage
Owners will have the ability to mint new tokens representing a verified identity of your pet.
Choose approved vetenarians where required vaccines are instantly verified and updated on the blockchain.
Verify the linage of their pets by breeders who have linked connections to the parent animals. 
This dApp creates transapancy in the pet market. 


## Contributors

This code was created in 2022 for a project for University of California - Berkeley, Fintech Bootcamp

Tyler Myers - tylergusmyers@gmail.com

Anil Vinnakota - anil.vinnakota@gmail.com

Tristen Pulido - tristenpulido@gmail.com

Dominik Tortes - domtortes@berkeley.edu

---
## License

MIT License

Copyright (c) 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




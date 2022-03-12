from web3 import Web3
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import dogapi
import json


# For now start with 3 pet types
types_of_pets = ["cat", "dog", "horse"]

# Current pet_token_id
pet = 0

# Temp variables for states
update = ""
account = ""
breeds = {}
provider = "http://127.0.0.1:7545"
contract_address = "0x7e71494397937377f6B4a191C1377cE07C766D50"
if "current_account_tokens" not in st.session_state:
    st.session_state["current_account_tokens"] = "value"
action = ""
updates = []

# Variables to store contract and Web3 instance we are working with
contract = ""
w3 = ""


# Static init cats and Horse. Fetch the dogs
breeds["cat"] = [
    "Abyssinian",
    "Aegean",
    "American Bobtail",
    "American Curl",
    "American Ringtail",
    "American Shorthair",
    "American Wirehair",
    "Aphrodite Giant",
    "Arabian Mau",
    "Asian",
    "Asian Semi-longhair",
    "Australian Mist",
    "Balinese",
    "Bambino",
    "Bengal",
    "Birman",
    "Bombay",
    "Brazilian Shorthair",
    "British Longhair",
    "British Shorthair",
    "Burmese",
    "Burmilla",
    "California Spangled",
    "Chantilly-Tiffany",
    "Chartreux",
    "Chausie",
    "Colorpoint Shorthair",
    "Cornish Rex",
    "Cymric, Manx Longhair or Long-haired Manx[a]",
    "Cyprus",
    "Devon Rex",
    '"Donskoy or',
    'Don Sphynx"',
    '"Dragon Li or',
    'Chinese Li Hua"',
    "Dwelf",
    "Egyptian Mau",
    "European Shorthair",
    "Exotic Shorthair",
    "Foldex[10]",
    "German Rex",
    "Havana Brown",
    "Highlander",
    '"Himalayan or',
    'Colorpoint Persian[c]"',
    "Japanese Bobtail",
    '"Javanese or',
    'Colorpoint Longhair[e]"',
    "Kanaani",
    "Khao Manee",
    "Kinkalow",
    "Korat",
    "Korean Bobtail",
    "Korn Ja",
    '"Kurilian Bobtail or',
    'Kuril Islands Bobtail"',
    "Lambkin",
    "LaPerm",
    "Lykoi",
    "Maine Coon",
    "Manx",
    "Mekong Bobtail",
    "Minskin",
    "Napoleon",
    "Munchkin",
    "Nebelung",
    "Norwegian Forest Cat",
    "Ocicat",
    "Ojos Azules",
    '"Oregon Rex',
    '(extinct)"',
    "Oriental Bicolor",
    "Oriental Longhair[f]",
    "Oriental Shorthair[f]",
    "Persian (modern)",
    "Persian (traditional)",
    "Peterbald",
    "Pixie-bob",
    '"Ragamuffin or',
    'Liebling (obsolete)"',
    "Ragdoll",
    "Raas",
    "Russian Blue",
    "Russian White, Russian Black and Russian Tabby",
    "Sam Sawet",
    "Savannah",
    "Scottish Fold",
    "Selkirk Rex",
    "Serengeti",
    "Serrade Petit",
    '"Siamese (modern)',
    '(for traditional, see Thai below)"',
    '"Siberian or',
    "Siberian Forest Cat;",
    'Neva Masquerade (colorpoint variety)"',
    "Singapura",
    "Snowshoe",
    "Sokoke",
    "Somali",
    "Sphynx",
    "Suphalak",
    '"Thai or',
    "Traditional, Classic, or Old-style Siamese;",
    'Wichien Maat[g]"',
    "Thai Lilac, Thai Blue Point and Thai Lilac Point",
    "Tonkinese",
    "Toybob",
    "Toyger",
    "Turkish Angora",
    "Turkish Van",
    "Turkish Vankedisi",
    "Ukrainian Levkoy",
    "York Chocolate",
]

breeds["dog"] = [
    "affenpinscher",
    "Afghan hound",
    "Airedale terrier",
    "Akita",
    "Alaskan Malamute",
    "American Staffordshire terrier",
    "American water spaniel",
    "Australian cattle dog",
    "Australian shepherd",
    "Australian terrier",
    "basenji",
    "basset hound",
    "beagle",
    "bearded collie",
    "Bedlington terrier",
    "Bernese mountain dog",
    "bichon frise",
    "black and tan coonhound",
    "bloodhound",
    "border collie",
    "border terrier",
    "borzoi",
    "Boston terrier",
    "bouvier des Flandres",
    "boxer",
    "briard",
]

breeds["horse"] = [
    "Dawand",
    "Herati",
    "Kohband",
    "Mazari",
    "Qatgani",
    "Qazal",
    "Samand",
    "Tooraq",
    "Waziri",
    "Yabu",
    "Yargha",
    "Arab",
    "Comune",
    "Haflinger",
    "Nonius",
    "Arabe Barbe",
    "Barbe",
    "Bagual",
    "Crioulo",
    "Falabella Pony",
    "American Saddlebred",
    "Andalusian",
    "Appaloosa",
    "Australian Brumby",
    "Australian Draught Horse",
    "Australian Pony",
    "Australian Stockhorse",
    "Australian Waler",
    "Belgian Draught",
    "Belgian Warmblood",
    "Brumbie",
    "Caspian",
    "Cleveland Bay",
    "Clydesdale",
    "Coffin Bay Pony",
    "Connemara",
    "Dales",
    "Danish Warmblood",
    "Dartmoor",
    "Egyptian Arabian",
    "English Arabian",
    "English Riding Pony",
    "English Spotted Pony",
    "Exmoor",
    "Falabella",
]


def create_connection():
    """ For now connect to local Ganache. App may be extended to work with any W3 provide """
    w3 = Web3(Web3.HTTPProvider(provider))
    if not w3.isConnected():
        st.error("Unable to connect to Ethereum network 'http://127.0.0.1:7545'")

    with open(Path("./petToken.sol.abi.json")) as f:
        contract_abi = json.load(f)

    # This contract address is only for testing purpose. Should be reading this one from user too
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
    return w3, contract


def create_pet():
    b_date = int(birth_date.strftime("%s"))
    tx_hash = contract.functions.createPet(
        uri, pet_type, breed, b_date, int(parent_0), int(parent_1)
    ).transact({"from": account, "gas": 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    return True


def update_pet():
    u = str(datetime.datetime.now()) + ":" + update
    id = int(pet_id)
    tx_hash = contract.functions.updatePet(id, u).transact(
        {"from": account, "gas": 1000000}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    return True


def terminate_pet():
    id = int(pet_id)
    st.warning("We currently don't support terminating pets")
    return True
    # tx_hash = contract.functions.terminatePet(id).transact(
    #    {"from": account, "gas": 1000000}
    # )
    # receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    # st.write("Transaction receipt mined:")
    # st.write(dict(receipt))
    # return True


@st.cache
def get_dogs():
    import requests

    url = "https://dog-breeds2.p.rapidapi.com/dog_breeds"
    headers = {
        "x-rapidapi-host": "dog-breeds2.p.rapidapi.com",
        "x-rapidapi-key": "341eceec8emsh8bc3a3cda8cb48ep1763d6jsn41cd8584105a",
    }
    response = requests.request("GET", url, headers=headers).json()
    dogs = []
    for d in response:
        dogs.append(d["breed"])
    return dogs


def update_user():
    """ New user selected. Fetch this owners pets and render the page"""
    total_tokens = contract.functions.totalSupply().call()
    st.write("Total pets in universe: {}".format(total_tokens))

    st.session_state.current_account_tokens = []
    for id in range(total_tokens):
        owner = contract.functions.ownerOf(id).call()
        # st.write("owner:account -- {}:{}.".format(owner, account))
        if owner == account:
            st.session_state.current_account_tokens.append(id)

    st.write(
        "Current Breeder has {} pets".format(
            len(st.session_state.current_account_tokens)
        ),
        st.session_state.current_account_tokens,
    )


w3, contract = create_connection()
account = st.sidebar.selectbox("List of Account", w3.eth.accounts)
st.sidebar.button("select Breeder Account", on_click=update_user)
current = st.sidebar.selectbox(
    "Select the transaction", ["createPet", "UpdatePet", "TerminatePet"]
)

if current == "createPet":
    breeds["dogs"] = get_dogs()
    action = "Create"
    st.title(f"Pet {action} APP")
    birth_date = st.date_input(
        "Birth Date", max_value=datetime.datetime.today(), key="birth_date_widget"
    )

    pet_type = st.selectbox("Type of Pet", types_of_pets)

    breed = st.selectbox("Breed", breeds[pet_type], index=0)

    uri = st.text_input("Image URL link")
    parent_0 = st.text_input("Parent 0", "0")
    parent_1 = st.text_input("Parent 1", "0")
    st.button("Create", on_click=create_pet)

elif current == "UpdatePet":
    st.write("current owner pets:{}".format(st.session_state.current_account_tokens))
    pet_id = st.selectbox("Pet ID", st.session_state.current_account_tokens)
    st.title(f"Updates for {pet}")
    update = st.text_input(f"Whats new on {pet}", "", on_change=update_pet)
elif current == "TerminatePet":
    # st.sidebar.text_input("Pet Address", "")
    action = "Terminate"
    st.title(f"Pet {action} APP")
    pet_id = st.selectbox("Pet ID", st.session_state.current_account_tokens)
    st.button("Terminate", on_click=terminate_pet)

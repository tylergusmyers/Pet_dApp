from web3 import Web3
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import dogapi

types_of_pets = ["cat", "dog", "horse"]

breeds = {}
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


action = ""
updates = []


@st.cache()
def create_connection():
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
    if not w3.isConnected():
        st.error("Unable to connect to Ethereum network 'http://127.0.0.1:7545'")
    return w3


@st.cache(allow_output_mutation=True)
def history(pet):
    """ Fetch Pets history from the block chain
  """
    return updates


def create_pet():
    st.success("Pet created successully")
    return True


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


w3 = create_connection()
account = st.sidebar.selectbox("Select Account", w3.eth.accounts)

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

    uploaded_file = st.file_uploader("Upload Files", type=["png", "jpeg"])
    if uploaded_file is not None:
        file_details = {
            "FileName": uploaded_file.name,
            "FileType": uploaded_file.type,
            "FileSize": uploaded_file.size,
        }
        st.write(file_details)

    color = st.color_picker("Color of the Pet")
    weight = st.number_input("Enter weight (in kgs)")
    st.button("Create", on_click=create_pet)

elif current == "UpdatePet":
    pet = st.sidebar.text_input("Pet Address", "")

    st.title(f"Updates for {pet}")

    history = history(pet)
    update = st.text_input(f"Whats new on {pet}", "")
    u = str(datetime.datetime.now()) + ":" + update
    history.append(u)

    updates = history
    placeholder = st.empty()
    placeholder.text(history)

elif current == "TerminatePet":
    st.sidebar.text_input("Pet Address", "")
    action = "Terminate"
    st.title(f"Pet {action} APP")


import streamlit as st
from dataclasses import dataclass
from typing import Any, List
import datetime as datetime
import pandas as pd
import hashlib


@dataclass
class Title():
    sender:str
    receiver:str
    title:str




@dataclass
class Ownership:
    record:Title
    creator_id: int
    prev_hash: str = "0"
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        record = str(self.record).encode()
        sha.update(record)

        creator_id = str(self.creator_id).encode()
        sha.update(creator_id)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()

@dataclass
class TransferOwnership:
    chain: List[Ownership]
    difficulty: int = 10 

    def proof_of_work(self, ownership):

        calculated_has = ownership.hash_block()

        num_of_zeros = "0" + self.difficulty

        while not calulated_has.startswith(num_of_zero):

            ownership.nonce += 1

            calculated_hash = ownership.hash_block()

        print("Title Transfered", calculated_hash)
        return ownership

    def add_block(self, newOwner):
        ownership = self.proof_of_work(newOwner)
        self.chain +=[ownership]

    def is_valid(self):
        block_has = self.chain[0].hash_block()

        for ownership in self.chain[1:]:
            if block_hash != ownership.prev_hash:
                print("Title cannot be Transferred!")
                return False

            block_hash = ownership.hash_block()

        print("Title has been Transferred")
        return True



@st.cache(allow_output_mutation = True)
def setup():
    print("Initializing Title Information")
    return TransferOwnership([Ownership("Title" , 0)])

st.markdown("# Transfer Ownership Title")
st.markdown("## Input address of who you would like to Transfer the Ownership to ")

titleTransfer = setup()


input_sender_id=st.text_input("Current Owner ID")

input_receiver_id=st.text_input("New Owner ID")

input_title= st.text("Pet Name ID")

if st.button("Transfer Title"):
    prev_block = titleTransfer.chain[-1]
    prev_block_hash = prev_block.hash_block()


    new_owner = Ownership(
            title=Title(
                sender=input_sender_id,
                receiver=input_receiver_id,
                title = input_title),
            creator_id=42,
            prev_hash=prev_block_hash
    )

    titleTransfer.add_block(new_owner)

st.balloons()


st.markdown("## Transfer Pet Ownership")

Transfer_df = pd.DataFrame(titleTransfer.chain).astype(str)
st.write(Transfer_df)

difficulty = st.sidbar.slider("Block Difficulty", 1, 5, 2)
titleTransfer.difficulty = difficulty

st.sidbar.write("# Owner History")
selected_block = st.sidebar.selectbox(
    "Which Owner would you like to see?", titleTransfer.chain
)

st,sidebar.write(selected_block)

if st.button(" Transfer Complete"):
    st.write(titleTransfer.is_valid())

    
    #NExt Steps:

    """GAnache Interface, 
    
    Drop down menus 
    Token Creation in Solidity
    insert Token into fields 
    
    Picture URLs for dog pictures 
    Add independant funtions into the token then merge later 
    
    Update, """
    ## Pet Token Address

    # Drop Down menu for Pet Token Address

    #
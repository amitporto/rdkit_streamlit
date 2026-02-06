import streamlit as st
from rdkit import Chem

st.set_page_config(page_title="SMILES to Canonical SMILES", layout="centered")

st.title("🧪 SMILES → Canonical SMILES")
st.write("Enter a SMILES notation to convert it into its canonical form using RDKit.")

# Input box
smiles_input = st.text_input("Enter SMILES:", placeholder="e.g. CC(=O)Oc1ccccc1C(=O)O")

if smiles_input:
    mol = Chem.MolFromSmiles(smiles_input)

    if mol is None:
        st.error("❌ Invalid SMILES notation. Please check your input.")
    else:
        canonical_smiles = Chem.MolToSmiles(mol, canonical=True)
        st.success("✅ Canonical SMILES generated:")
        st.code(canonical_smiles)
import streamlit as st

def word_and_char_count(user_para: str):    
    total_words = user_para.strip().split()
    st.success(f"Total Words: {len(total_words)}")

    total_char = 0 
    for char in user_para:
        total_char += 1
    st.success(f"Character Length: {total_char}")
    
    avg_word_len = total_char / len(total_words)
    st.success(f"Average Word Length: {avg_word_len}")  


def vowel_count(user_para: str):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    
    for char in user_para:
        for vowel in vowels:
            if char == vowel:
                vowel_count += 1
    st.success(f"Total Vowels: {vowel_count}")


def search_and_replace(user_para: str):
    search_word = st.text_input("Enter a word to search:")
    if search_word:
        if search_word in user_para:
            replaced_word = st.text_input("Enter a word to replace:")
            if replaced_word:
                modified_para = user_para.replace(search_word, replaced_word)
                st.success("Modified paragraph: " + modified_para)
        else:
            st.success(f"Word '{search_word}' not found in the paragraph.")


def upper_case(user_para: str):
    st.success(user_para.upper())


def lower_case(user_para: str):
    st.success(user_para.lower())


def check_word_existance(user_para: str):
    input_word = st.text_input("Enter a word to check its existence:")
    if input_word:
        if input_word in user_para:
            st.success("True")
        else:
            st.success("False")


st.title("📝 Text Analyzer")

user_para = st.text_area("Enter a paragraph:")

options = [
    "Word & Length Count",
    "Vowel Count",
    "Search & Replace word",
    "Convert text into uppercase",
    "Convert text into lowercase",
    "Check word existence"
]

user_choice = st.selectbox("Choose a function to perform:", options)

if user_para.strip():
    if user_choice == "Word & Length Count":
        word_and_char_count(user_para)
    elif user_choice == "Vowel Count":
        vowel_count(user_para)
    elif user_choice == "Search & Replace word":
        search_and_replace(user_para)
    elif user_choice == "Convert text into uppercase":
        upper_case(user_para)
    elif user_choice == "Convert text into lowercase":
        lower_case(user_para)
    elif user_choice == "Check word existence":
        check_word_existance(user_para)
else:
    st.info("Paragraph must contain some letters.")
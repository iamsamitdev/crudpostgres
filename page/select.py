import streamlit as st

import sys

sys.path.insert(1, 'controller')

import client as client

def select_all():
    st.title("Select All Person")

    rows = client.select_all()
    
    if rows:
        st.table(rows)
    else:
        st.write("## ยังไม่มีข้อมูลในตาราง person")
import streamlit as st

current_page=st.navigation([st.Page("Home.py"),
                            st.Page("Predict.py", title="Premium Amount Calculator")
                            ])

current_page.run()
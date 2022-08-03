import streamlit as st

def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.sidebar.text_input("Username", on_change=password_entered, key="username")
        st.sidebar.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.sidebar.text_input("Username", on_change=password_entered, key="username")
        st.sidebar.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        #st.error("😕 User not known or password incorrect")
        return False
    
    else:
        # Password correct.
        return True

    
def authenticator():
	
	with st.sidebar.form("reg", clear_on_submit=True):
	
		st.write("Admin Login")
	
		username=st.text_input(label='User Name')
		password=st.text_input(label='Password',type="password")
	
		sub3 = st.form_submit_button(label='Login')
		
	if sub3==True and username in st.secrets["passwords"] and password==st.secrets["passwords"][username]:
		del username
		del password
		cn=True
		st.balloons()
	else:
		st.sidebar.write("User name or password incorrect")
		cn=False
	
	return cn

import streamlit as st

st.set_page_config(
     page_title="Campus olympics",
     page_icon="ð§",
     layout="wide",
     initial_sidebar_state= "collapsed",
     menu_items={
         'Get Help': 'https://instagram.com/keralauniversitydsu?igshid=YmMyMTA2M2Y=',
         'Report a bug': "https://www.linkedin.com/in/prabinrajkp18/",
         'About': "# Departments union sports club - campus olympics web app"
     }
 )


import pandas as pd
from data import athletics
import dataframe_image as dfi
#import gspread as gs
from PIL import Image
import json
import datetime
from data import registration
from auth import check_password
from union import admin
from data import reg
from auth import authenticator
import plotly.express as px







image= Image.open('logo.png')

st.image(image)

st.markdown('#  Campus olympics')

st.markdown('##### Departments Union Sports Club')
st.write('**6 teams | 7 days | 20 events | One excitement**')

with open("campus olympics rules.pdf", "rb") as file:
    btn=st.download_button(
    label="click here download rules",
    data=file,
    file_name="dowloaded.pdf",
    mime="application/octet-stream"
)





st.write('---')

c=check_password()

if c==True:
	
	admin()

else:
	
	


	tab1, tab2,tab3,tab4 = st.tabs(["Event Wise Result","Leader Board","Registration","Gallery"])

	df=athletics()
	evn=df['Event'].unique()

	with tab1:

		c1,c2=st.columns(2)
		#with c1:
		st.markdown('###### Event result')
		option = st.selectbox('',evn,key='event')

		st.write('Results For ', option)

		ev=df[df['Event']==option]
		ev=ev[['Name','Faculty','Department','Position']]
			
			
		
			
		st.dataframe(ev)
		
		st.write('---')	       
		#with c2:
		st.markdown('###### Leaderboard - Individual')
		dpt=df[df['Department']!='']
		dpt=dpt.groupby(['Name']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False).head(10)
		st.dataframe(dpt.style.hide_index().background_gradient(cmap='autumn'))
			

		
	with tab2:
		c1,c2=st.columns(2)
		
		with c1:
		
			
			st.markdown('###### Leaderboard - Faculty wise')
			facp=df.groupby(['Faculty']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False)
			st.dataframe(facp.style.background_gradient(cmap='autumn'))
			
		
		with c2:
			
			st.markdown('###### Leaderboard - Department wise')
			dpt=df.groupby(['Department']).sum()['Points'].reset_index().sort_values(by='Points', ascending=False)
			dpt=dpt.head(10)
			st.dataframe(dpt[dpt['Department']!=''].style.background_gradient(cmap='autumn'))
			

		
		


	with tab3:

		#name,mob,mail= None
		with st.form("reg23", clear_on_submit=True):
			st.write('**Athletics registration**')
			tb1,tb2=st.columns(2)
		
			#st.write('name')
			with tb1:
				name=st.text_input(label='Name')
				mob=st.text_input(label='Phone')
				mail=st.text_input(label='E-mail')
			with tb2:
				gen=st.selectbox('Gender',('Male','Female','Transgender'))
				d = st.date_input( "Date of birth",datetime.date(1999, 1, 1))
				
				fac=st.selectbox('Faculty',
				('Applied Science and Technology','Arts, Education & Music','IMk, Commerce & Law','OrientalStudies','Science','Social Science'))
			
			items = st.multiselect(
		 'Events (Maximum 3 events)',
		 ['100 meter','200 meter','400 meter','1500 meter','Walking (3000 meter)','Shot put','Discus Throw','Javelin throw','Cricket Ball Throw'])
			
			
			submit_button = st.form_submit_button(label='Submit')
		#st.write(len(name),len(mob),len(mail))
		
		
			
		if len(items)>3 and submit_button==True:
			st.error('Error: items cannot be more than 3')
		#st.write(name,mob,mail,fac)
		elif submit_button==True and ((len(name) and len(mob) and len(mail))<1)  :
			st.error("Error: all fields must be filled")
			
		elif submit_button==True:
			st.success(str(name)+' Successfully registered for ' + str(items))
			
			for event in items:
				
				lst=[name,str(mob),mail,gen,fac,str(d),event]
				registration(lst)
		with tab4:
			img=["images/WhatsApp Image 2022-08-27 at 9.18.03 AM (1).jpeg","images/WhatsApp Image 2022-08-27 at 9.18.02 AM.jpeg"]
			
			
			#im=Image.open(image=https://www.instagram.com/p/Chv9XNdrtpY/?utm_source=ig_web_copy_link)
			st.image(img)
				
with st.sidebar.expander("Developers"):
 	st.markdown('#### [Prabin Raj K P](https://www.linkedin.com/in/prabinrajkp18/)')
 	st.markdown('#### [Vijay V Venkitesh](https://www.linkedin.com/in/vijay-v-venkitesh-673177204/)')
 	st.write('##### MSc Data Science \n Department of Futures Studies')
 	
     #st.image("https://static.streamlit.io/examples/dice.jpg")
			
		
		
	
	
	
	#st.write('ssbsbbs')

#st.dataframe(df)
	
	


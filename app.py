import streamlit as st
import gspread
import pandas as pd
from geopy.geocoders import Nominatim
from oauth2client.service_account import ServiceAccountCredentials
from geopy.geocoders import Nominatim
from urllib3.exceptions import ReadTimeoutError
from geopy.exc import GeocoderTimedOut
import plotly.express as px
import pdfkit
# from weasyprint import HTML
from io import BytesIO
from time import sleep

# Create two columns
col1, col2 = st.columns(2)

# Content for the left column
with col1:
    # st.header("Left Column")
    credentials = {
  "type": "service_account",
  "project_id": "keen-quest-388604",
  "private_key_id": "daf2a808a49576b6b990c50d08297eb1b85c5003",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXU1+ZJDf7GybW\n+lGUYE8WFuDuwSOPpBtWZvl1dfTRVZxPjWnc6ZVRvCxc5/g2Xonl3t0W3J/JvUeg\nKmBSX3HN051EcM0awihYSo2f35sKAx/aDDrHzEp6LJ7zuCqEUnggnX9uI6dfS9cV\nLi9z90oqZU3xtcn2ywTVB81bSXCZAWuEjBf1sb4kV6OEiF4rpbYhijFU0M+ls2nF\nTjKhS7a8VAEnfkWDy7fTt+0MQ2iS7/YAS+Kvd8uP60aW1ohXN/mqYuT+St27HdyX\nI5lOfpsu+2Nyk2zeiSfMWlI5ZZmpQfBHic/k6pf8jk5dEkgVoI2Khh0rIISsBNhR\nnpwptrkhAgMBAAECggEARMnBQhKkgadAZrAsLKsByOxBKnTwD9zc0OLvsZsfvVpM\np8tk9Op4RdbIE1wV2wSjqBhk5/9OWqwJvDydbeNI33jJhopEs9Yv/li+2sKb7Hxo\nCggbJSX56wLjOrfseT5BWyYFhiGEwDhhu0X4aeMnwdiAKIYrQZjE7+tgqteQzYfk\nvRh4Dw10ETVwSVhXu7spRa9cy208H1VWJI2EWAxWTqQokXmcEFuFPnlOhrKCGw9E\nkfJ9H/4yS343tmnDcRi5KAu5bAihinTJTziu/Omh+JfY9VpkBWquIcfEZJAxAdU5\ny1a9C3zn9LeT0A+xNMh9h8t7080roFqC4UcgOiJN4wKBgQD7aUPzeDxbbWpfrbTo\n+s7lBue7NryJur1qTyeTBYUrRoBkedtnmqq4Y5vJHTgmPkdL/1rgE7Zrr9i9qmLX\n5SGfKUMa/drJxUSaKVklOaKrmw7uKdUfYDIJKm0kltWhdmN+MWo4pR96W0MOEFKS\npjrGYwpjoa1pBQddPnmDLJw1lwKBgQDbQX8Ed1OJ3vi9knqmGxToYxGBVrj1OmDz\nogCu1kT8BsPd2uTYfoqLPZRRXvSOHZgVAnNosIN+db4KaSXSDGO863rgurjsDhRY\na3rcxyC0VtTYp3ik+7fWk58g2nDX/DWZ8nYuUQp0Yd6oqM2bqoVgPplf9INiNeQD\npU/Qa/UOBwKBgANr/1zE+i1UY+pBdwDkyQQc//JwYEiPnhxgT22U2acpIn47mlzi\nogg4ctpd53G9z0KdiyMZoZX9ormSJB5EJB0CdsNbSSsN4E0o2unCyxAC4EUllJ0E\ntimhxjKFSwsTjW8eRQ/YT4Fe1J7QYg9U69/fYTjR7oZLZzpBq225obapAoGBAJd1\nbyDOrU6YUIvkHAWSv6aoiPcnySzd3wtt5brhGVZf9f3TsDI9d8coCsULKzThDKW2\nw7KV/L/m5hia+h1Xoa5nnMKROh0WvMc3t++7PsRVF0NyrMyLdjssTsiLHViWSRDH\nhQwJv4cV9JHdyeq2qNwLYjf+2KOHRrOeBrybVvURAoGAAyWhfiMMM51xLw+NQqHa\nyOUiPCLTdihG8IREF0d1n8hugVKUDG+jlsIXZZmu5Nq2fvcbnL89f7RMPjG1lbGS\nZs/wkQJpBvIjMNsqfnvRGg4X2x66Joz2g+42WSkUuPmDf+bkb2Rzx+GzXltpxnPP\nzOdQhCxrwCDiiyUH3R+8gE8=\n-----END PRIVATE KEY-----\n",
  "client_email": "serviceacc1@keen-quest-388604.iam.gserviceaccount.com",
  "client_id": "104037426221423372910",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/serviceacc1%40keen-quest-388604.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
    # Set up Google Sheets credentials
    creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials)
    client = gspread.authorize(creds)
    
    # Access the Google Sheet
    sheet = client.open('urologist').sheet1

    # # Read data from the sheet
    data = sheet.get_all_records()


    # # Display data in Streamlit
    # st.write(data)
    # Convert data to pandas DataFrame
    st.markdown('## Form : ')
    # st.write(' A urologist is a medical doctor specializing in conditions that affect the urinary tract in men, women and children, and diseases that affect the reproductive system. These conditions range from peeing too much or too little to being unable to father a child. ')

    df = pd.DataFrame(data)

    # Handle the conversion issue in 'Cost2' column
    df['Cost2'] = pd.to_numeric(df['Cost2'], errors='coerce')
    df['Experience(years)'] = pd.to_numeric(df['Experience(years)'], errors='coerce')

    # st.write(df.head())

    with st.form("my_form"):
        number = st.number_input("Enter a Value")
        st.write("Enter the necessary information " )
        option1 = st.multiselect("Select a speciality", df['Specialization'].unique())
        option2 = st.multiselect("Select a Location", df['Location'].unique())
        option3 = st.multiselect("Select years of experience",['1-5','6-10','11-15','16-20','21-25','>25'])
        submit_button = st.form_submit_button("Submit")
    
    # Add content to the left column
f = 0
# Content for the right column
with col2:
    st.header("Output : ")
    
    if submit_button:
        number_of_people = 0
        for option in option3:
            if option == '1-5':
                number_of_people += len(df[(df['Specialization'].isin(option1)) & (df['Location'].isin(option2)) & (df['Experience(years)']<= 5)])
            elif option == '6-10':
                number_of_people += len(df[(df['Specialization'].isin(option1)) & (df['Location'].isin(option2)) & ((df['Experience(years)']>=6) & (df['Experience(years)']<=10))])
            elif option == '11-15':
                number_of_people += len(df[(df['Specialization'].isin(option1)) & (df['Location'].isin(option2)) & ((df['Experience(years)']>=11) & (df['Experience(years)']<=15))])
            elif option == '16-20':
                number_of_people += len(df[(df['Specialization'].isin(option1)) & (df['Location'].isin(option2)) & ((df['Experience(years)']>=16) & (df['Experience(years)']<=20))])
            elif option == '21-25':
                number_of_people += len(df[(df['Specialization'].isin(option1)) & (df['Location'].isin(option2)) & ((df['Experience(years)']>=21) & (df['Experience(years)']<=25))])
            elif option == '>25':
                number_of_people += len(df[(df['Specialization'].isin(option1)) & (df['Location'].isin(option2)) & ((df['Experience(years)']>25))])
        
        st.write(f"Number of People: {number_of_people}")
        st.write("The number of the doctors are : "+ str((number_of_people)))
        st.write("Calculating your TAM Value")
        st.write(str(number_of_people*number))
        f = 1
        st.write("Enter your email to get TAM value")
        with st.form("email_form"):
            email = st.text_input(" Enter the email : ")
            button_submit = st.form_submit_button("Submit email")
        # with st.form("email_form"):
        #     email = st.text_input(" Enter the email : ")
        #     submit_button = st.form_submit_button("Submit")
        if button_submit:    
            sheet = client.open('form_to_sheet').sheet1
            tam_value = number_of_people*number
                # b = st.button('Click this button')
                # if b:
            l = [number, ' '.join(option1),' '.join(option2),' '.join(option3),tam_value,email]
            st.write(l)
            sheet.append_row(l)
            
            # # Read data from the sheet
            # data = sheet.get_all_records()
            

            
        
    # if f==1:
    #     # Create an HTML string with the input and output
    #     st.write(number)
    #     st.write(option1)
    #     st.write(option2)
    #     st.write(option3)
    #     html_content = f"""
    #     <html>
    #     <body>
    #         <h2>User Inputs:</h2>
    #         <p>Value: {number}</p>
    #         <p>Specialization: {option1}</p>
    #         <p>Location: {option2}</p>
    #         <p>Years of Experience: {option3}</p>

    #         <h2>Output:</h2>
    #         <p>The number of doctors is: {number_of_people}</p>
    #         <p>TAM Value: {number_of_people * number}</p>
    #     </body>
    #     </html>
    #     """
    #     pdf_bytes = HTML(string=html_content).write_pdf()

    #     # Display the PDF
    #     st.write(pdf_bytes, unsafe_allow_html=True)
    #     st.download_button(
    #         label='Download PDF',
    #         data=pdf_bytes,
    #         file_name='output.pdf',
    #         mime='application/pdf'
    #     )

        # # Create a BytesIO object to hold the PDF data
        # pdf_file = BytesIO()

        # # Convert the HTML to PDF and save it in the BytesIO object
        # pdfkit.from_string(html_content, pdf_file)

        # # Set the BytesIO object's position to the start
        # pdf_file.seek(0)

        # # Provide the option to download the PDF file
        # st.download_button(
        #     label='Download PDF',
        #     data=pdf_file,
        #     file_name='output.pdf',
        #     mime='application/pdf'
        # )
        
    # Add content to the right column


# Manually provide the credentials
# credentials = {
#   "type": "service_account",
#   "project_id": "keen-quest-388604",
#   "private_key_id": "daf2a808a49576b6b990c50d08297eb1b85c5003",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDXU1+ZJDf7GybW\n+lGUYE8WFuDuwSOPpBtWZvl1dfTRVZxPjWnc6ZVRvCxc5/g2Xonl3t0W3J/JvUeg\nKmBSX3HN051EcM0awihYSo2f35sKAx/aDDrHzEp6LJ7zuCqEUnggnX9uI6dfS9cV\nLi9z90oqZU3xtcn2ywTVB81bSXCZAWuEjBf1sb4kV6OEiF4rpbYhijFU0M+ls2nF\nTjKhS7a8VAEnfkWDy7fTt+0MQ2iS7/YAS+Kvd8uP60aW1ohXN/mqYuT+St27HdyX\nI5lOfpsu+2Nyk2zeiSfMWlI5ZZmpQfBHic/k6pf8jk5dEkgVoI2Khh0rIISsBNhR\nnpwptrkhAgMBAAECggEARMnBQhKkgadAZrAsLKsByOxBKnTwD9zc0OLvsZsfvVpM\np8tk9Op4RdbIE1wV2wSjqBhk5/9OWqwJvDydbeNI33jJhopEs9Yv/li+2sKb7Hxo\nCggbJSX56wLjOrfseT5BWyYFhiGEwDhhu0X4aeMnwdiAKIYrQZjE7+tgqteQzYfk\nvRh4Dw10ETVwSVhXu7spRa9cy208H1VWJI2EWAxWTqQokXmcEFuFPnlOhrKCGw9E\nkfJ9H/4yS343tmnDcRi5KAu5bAihinTJTziu/Omh+JfY9VpkBWquIcfEZJAxAdU5\ny1a9C3zn9LeT0A+xNMh9h8t7080roFqC4UcgOiJN4wKBgQD7aUPzeDxbbWpfrbTo\n+s7lBue7NryJur1qTyeTBYUrRoBkedtnmqq4Y5vJHTgmPkdL/1rgE7Zrr9i9qmLX\n5SGfKUMa/drJxUSaKVklOaKrmw7uKdUfYDIJKm0kltWhdmN+MWo4pR96W0MOEFKS\npjrGYwpjoa1pBQddPnmDLJw1lwKBgQDbQX8Ed1OJ3vi9knqmGxToYxGBVrj1OmDz\nogCu1kT8BsPd2uTYfoqLPZRRXvSOHZgVAnNosIN+db4KaSXSDGO863rgurjsDhRY\na3rcxyC0VtTYp3ik+7fWk58g2nDX/DWZ8nYuUQp0Yd6oqM2bqoVgPplf9INiNeQD\npU/Qa/UOBwKBgANr/1zE+i1UY+pBdwDkyQQc//JwYEiPnhxgT22U2acpIn47mlzi\nogg4ctpd53G9z0KdiyMZoZX9ormSJB5EJB0CdsNbSSsN4E0o2unCyxAC4EUllJ0E\ntimhxjKFSwsTjW8eRQ/YT4Fe1J7QYg9U69/fYTjR7oZLZzpBq225obapAoGBAJd1\nbyDOrU6YUIvkHAWSv6aoiPcnySzd3wtt5brhGVZf9f3TsDI9d8coCsULKzThDKW2\nw7KV/L/m5hia+h1Xoa5nnMKROh0WvMc3t++7PsRVF0NyrMyLdjssTsiLHViWSRDH\nhQwJv4cV9JHdyeq2qNwLYjf+2KOHRrOeBrybVvURAoGAAyWhfiMMM51xLw+NQqHa\nyOUiPCLTdihG8IREF0d1n8hugVKUDG+jlsIXZZmu5Nq2fvcbnL89f7RMPjG1lbGS\nZs/wkQJpBvIjMNsqfnvRGg4X2x66Joz2g+42WSkUuPmDf+bkb2Rzx+GzXltpxnPP\nzOdQhCxrwCDiiyUH3R+8gE8=\n-----END PRIVATE KEY-----\n",
#   "client_email": "serviceacc1@keen-quest-388604.iam.gserviceaccount.com",
#   "client_id": "104037426221423372910",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/serviceacc1%40keen-quest-388604.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }

# # Set up Google Sheets credentials
# creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials)
# client = gspread.authorize(creds)

# # Access the Google Sheet
# sheet = client.open('urologist').sheet1

# # # Read data from the sheet
# data = sheet.get_all_records()


# # # Display data in Streamlit
# # st.write(data)
# # Convert data to pandas DataFrame
# st.markdown('# Urologist data : ')
# # st.write(' A urologist is a medical doctor specializing in conditions that affect the urinary tract in men, women and children, and diseases that affect the reproductive system. These conditions range from peeing too much or too little to being unable to father a child. ')

# df = pd.DataFrame(data)

# # Handle the conversion issue in 'Cost2' column
# df['Cost2'] = pd.to_numeric(df['Cost2'], errors='coerce')
# df['Experience(years)'] = pd.to_numeric(df['Experience(years)'], errors='coerce')

# # st.write(df.head())

# with st.form("my_form"):
#     number = st.number_input("Enter a Value")
#     st.write("Enter the necessary information " )
#     option1 = st.selectbox("Select a speciality", df['Specialization'].unique())
#     option2 = st.selectbox("Select a Location", df['Location'].unique())
#     option3 = st.selectbox("Select years of experience", df['Experience(years)'].unique())
#     submit_button = st.form_submit_button("Submit")
    
# Process the form submission
# if submit_button:
#     number_of_people = len(df[(df['Specialization']==option1) & (df['Location'] == option2) & (df['Experience(years)']== option3)])
#     st.write("The number of the doctors are : "+ str((number_of_people)))
#     st.write("Calculating your TAM Value")
#     st.write(str(number_of_people*number))

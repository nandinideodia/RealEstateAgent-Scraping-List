import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    agent_cards = soup.find_all('div', {'data-testid': 'component-agentCard'})

    data = []
    for card in agent_cards:
        name_tag = card.find('span', {'class': 'jsx-3873707352 text-bold'})
        name = name_tag.get_text() if name_tag else 'No Name'

        phone_button = card.find('a', {'class': 'jsx-3873707352', 'data-contact-container': True})
        phone_number = phone_button.get('href')[4:] if phone_button else 'No Number'

        data.append({'Name': name, 'Number': phone_number})

    df = pd.DataFrame(data, columns=['Name', 'Number'])
    return df

file_path = 'D:\Programming\html_content.txt'  #yaha apni .txt file ka path daal dena, mne jo daala h wo mere laptop m h
with open(file_path, 'r', encoding = 'utf-8') as file:
    static_html = file.read()

# url = 'https://www.realtor.com/realestateagents/los-angeles_ca'
df = extract_data_from_html(static_html)
print(df)
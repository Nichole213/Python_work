# Analysis on frequently tested topics based on the database that I created myself

from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)

worksheet_list = gc.open_by_url('https://docs.google.com/spreadsheets/d/1vwwF87ZpeQZhWGpHjONmneshX5-7WHFKIShGs_K3st8/edit?usp=sharing').worksheets()

import pandas as pd

all_data = []
for worksheet in worksheet_list:
    rows = worksheet.get_all_values()
    df = pd.DataFrame.from_records(rows)
    all_data.append(df)

combined_df = pd.concat(all_data)
print(combined_df)

cimc_df = combined_df[combined_df[2].str.contains("CIMC")]
print(cimc_df)

# A5
cimc_A5 = cimc_df[cimc_df[2].str.contains("A5")]
cimc_A5_sorted = cimc_A5.sort_values(by=0)
print(cimc_A5_sorted)

# Count the frequency of each topic
topic_counts_A5 = cimc_A5[0].value_counts()
print(topic_counts_A5)

# Sort the topics by frequency in descending order
sorted_topics_A5 = topic_counts_A5.sort_values(ascending=False)

# Print the most popular topics
print(sorted_topics_A5.index.tolist())

# A6
cimc_A6 = cimc_df[cimc_df[2].str.contains("A6")]
topic_counts_A6 = cimc_A6[0].value_counts()
print(topic_counts_A6)

# B1
cimc_B1 = cimc_df[cimc_df[2].str.contains("B1")]
topic_counts_B1 = cimc_B1[0].value_counts()
print(topic_counts_B1)

# B2
cimc_B2 = cimc_df[cimc_df[2].str.contains("B2")]
topic_counts_B2 = cimc_B2[0].value_counts()
print(topic_counts_B2)

# B3
cimc_B3 = cimc_df[cimc_df[2].str.contains("B3")]
topic_counts_B3 = cimc_B3[0].value_counts()
print(topic_counts_B3)



# Analysis on Grades Cut-offs

!pip install requests beautifulsoup4 PyPDF2 pandas spacy
!python -m spacy download en_core_web_sm
!pip install statsmodels

# Fetch the past contest results from the CEMC website.
import requests
from bs4 import BeautifulSoup

# URL of the CEMC past contest results
url = 'https://www.cemc.uwaterloo.ca/contests/past_contests.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links to past contest PDFs or pages
contest_links = soup.find_all('a', href=True)

# Filter the links of CIMC past contest results
cimc_links_raw = list({link['href'] for link in contest_links if 'CxMCResults' in link['href']})
cimc_links = sorted(cimc_links_raw, key=lambda x: int(x.split('/')[1].split('C')[0]), reverse=True)

# Print the links for verification
for link in cimc_links:
    print(link)

# Visulize the CIMC Honor Roll grade cut-offs

import requests
from PyPDF2 import PdfReader
import re
import matplotlib.pyplot as plt

def get_grade_cutoff(pdf_url):
    # Download the PDF
    response = requests.get(pdf_url)

    # Save the PDF to a temporary file
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF
    reader = PdfReader('temp.pdf')

    # Extract text from all pages
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    # Use a regular expression to find the cut-off
    matches = re.findall(r"Scores/Notes.*?(\d+).*?(\d+)", text)
    if matches:
        return int(matches[-1][1])
    else:
        return None

years = []
cutoffs = []

for link in cimc_links:
    pdf_url = 'https://www.cemc.uwaterloo.ca/contests/' + link
    cutoff = get_grade_cutoff(pdf_url)
    year = int(link.split('/')[1][:4])
    years.append(year)
    cutoffs.append(cutoff)

plt.figure(figsize=(10, 6))
plt.plot(years, cutoffs, '-', color='#70cefa')
plt.plot(years, cutoffs, 'o', color='#fc9608')
plt.xlabel('Year')
plt.ylabel('Honor Roll Cut-off')
plt.title('CIMC Honor Roll Cut-offs (International)')
plt.grid(True)
plt.xticks(years)
plt.show()




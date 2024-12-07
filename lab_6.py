# using selenium and beautiful soup for extraction
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome()
# Open the Bloomberg Billionaire Index URL
url = 'https://www.bloomberg.com/billionaires/'
driver.get(url)
# Wait for the page to load fully
time.sleep(10)

# Get the page source and parse with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

def get_table(classname):
    table_chart = soup.find('div', {'class': classname})
    return table_chart

def extract_colnames(table_chart):
    header_row = table_chart.find('div', class_='table-rowx') if table_chart else None
    if header_row:
        # Extract text from each column in the header
        headers = [cell.text.strip() for cell in header_row.find_all('div', class_='table-cell')]
        return headers
    return []

def extract_rows(table_chart):
    rows = table_chart.find_all('div',class_="table-row") if table_chart else []
    if len(rows) == 0 :
        print('Rows extraction unsucessful')
        return
    data = []
    for row in rows:
        cells = row.find_all('div',class_='table-cell')
        cell_data = [cell.text.strip() for cell in cells]
        data.append(cell_data)
    return data

def form_dataFrame(headers,rows):
    df = pd.DataFrame(rows,columns=headers)
    return df

table_chart = get_table('table-chart')
headers = extract_colnames(table_chart)
rows = extract_rows(table_chart)
df = form_dataFrame(headers,rows)
df.set_index('Rank')
df.to_csv('bloomberg_billionaires.csv',index=False)
print("Data extracted and saved successfully!")
# Close the WebDriver
driver.quit()

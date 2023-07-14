import requests
from bs4 import BeautifulSoup
import csv
import datetime
import csv
import json

def crawl_and_save_table_data(url): #, file_path):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    table = soup.find('table')
    if table is not None:
        rows = table.find_all('tr')
        data = []

        for row in rows:
            cells = row.find_all('td')
            row_data = []
            for cell in cells:
                row_data.append(cell.text.strip())
            if row_data:
                data.append(row_data)
    #     with open(file_path, 'w', newline='') as file:
    #         writer = csv.writer(file)
    #         for row in data:
    #             writer.writerow(row)

    #     print("Dữ liệu đã được ghi vào tệp tin:", file_path)
    # else:
    #     print("Không tìm thấy bảng dữ liệu trên trang web.")
        return data

# dim table
    

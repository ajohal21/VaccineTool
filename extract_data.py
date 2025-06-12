import os
import zipfile
import json
from bs4 import BeautifulSoup

def extract_data_to_json():
    """Extract data from HTML files and save to JSON"""
    data = {}
    
    # Read the zip file
    with zipfile.ZipFile('data/countries.zip', 'r') as zip_ref:
        # Get all .htm files
        htm_files = [f for f in zip_ref.namelist() if f.endswith('.htm')]
        
        # Process each file
        for htm_file in htm_files:
            print(f"\nProcessing {htm_file}")
            # Read the HTML content
            with zip_ref.open(htm_file) as file:
                html_content = file.read().decode('utf-8')
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extract country name from filename (remove .htm extension)
                country_name = os.path.splitext(os.path.basename(htm_file))[0]
                
                # Initialize country data
                data[country_name] = []
                
                # 1. Find the <h3> with the right text
                vaccines_header = soup.find('h3', string=lambda s: s and 'Vaccines and Medicines' in s)
                if vaccines_header:
                    # 2. Find the next table after this header
                    table = vaccines_header.find_next('table', class_='disease')
                    if table:
                        # 3. Find all <td class="clinician-disease">
                        for td in table.find_all('td', class_='clinician-disease'):
                            a = td.find('a')
                            if a:
                                vaccine_name = a.get_text(strip=True)
                                # Exclude unwanted vaccines
                                if vaccine_name.lower() in ["routine vaccines", "covid-19", "tick-borne encephalitis"]:
                                    continue
                                print(f"Found vaccine: {vaccine_name}")
                                data[country_name].append(vaccine_name)
                            else:
                                print("No <a> tag found in clinician-disease td")
                    else:
                        print("No table found after Vaccines and Medicines header")
                else:
                    print("No Vaccines and Medicines header found")
    
    # Save to JSON file
    with open('data/vaccine_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("\nData successfully extracted to data/vaccine_data.json")
    # Print summary
    for country, vaccines in data.items():
        print(f"{country}: {len(vaccines)} vaccines")

if __name__ == "__main__":
    extract_data_to_json() 
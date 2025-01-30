import json
from typing import Dict, List, Union

def json_to_bibtex(json_file: str, bibtex_file: str) -> None:
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        entries = [data] if isinstance(data, dict) else data
        
        with open(bibtex_file, 'w') as bibtex:
            for item in entries:
                write_bibtex_entry(bibtex, item)
                
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file: {json_file}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {json_file}")

def write_bibtex_entry(bibtex_file, item: Dict) -> None:
    """Write a single BibTeX entry to the file."""
    required_fields = ['title', 'authors', 'journal', 'publication_year']
    if not all(field in item for field in required_fields):
        raise ValueError(f"Missing required fields: {required_fields}")
    
    # Get first author's last name
    first_author = item['authors'][0].split()[-1]  # Takes the last word as the surname
    id_entry = f"{first_author}{item['publication_year']}"
    
    bibtex_file.write(f"@article{{{id_entry},\n")
    
    # Write required fields
    bibtex_file.write(f'  author = {{{" and ".join(item["authors"])}}},\n')
    bibtex_file.write(f'  title = {{{item["title"]}}},\n')
    bibtex_file.write(f'  journal = {{{item["journal"]}}},\n')
    bibtex_file.write(f'  year = {{{item["publication_year"]}}},\n')
    
    # Write optional fields
    #optional_fields = ['abstract', 'pmid']
    optional_fields = ['pmid']
    for field in optional_fields:
        if field in item:
            bibtex_file.write(f'  {field} = {{{item[field]}}},\n')
    
    bibtex_file.write('}\n\n')

if __name__ == '__main__':
    json_file_path = r'C:\Users\ssimo\projects\ai_medicine\parsed_literature.json'
    bibtex_file_path = r'C:\Users\ssimo\projects\ai_medicine\output.bib'
    json_to_bibtex(json_file_path, bibtex_file_path)
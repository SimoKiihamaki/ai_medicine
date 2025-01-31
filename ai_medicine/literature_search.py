import json
from Bio import Entrez

# Configure your email (required by Entrez)
Entrez.email = 'simo.kiihamaki@gmail.com'  # Replace with your actual email

# Define the search parameters
ai_terms = '"artificial intelligence" OR "machine learning" OR "deep learning"'
domain_terms = '"personalized medicine" OR "precision medicine" OR "drug discovery" OR "diagnostic imaging" OR "patient outcome prediction"'
ethics_terms = '"data privacy" OR "algorithmic bias" OR "ethical challenges"'

boolean_query = f'(({ai_terms}) AND ({domain_terms}) AND ({ethics_terms}))'

# Filters
# PubMed filters can be applied via the Entrez parameters
def search_pubmed(query, max_results=1000):
    handle = Entrez.esearch(
        db='pubmed',
        sort='relevance',
        retmax=max_results,
        retmode='xml',  # Ensure retmode is 'xml' to get XML response
        term=query,
        mindate='2017',
        maxdate='2025',
        datetype='pdat'
    )
    results = Entrez.read(handle)
    handle.close()
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    handle = Entrez.efetch(
        db='pubmed',
        retmode='xml',
        id=ids
    )
    results = handle.read()
    handle.close()
    
    # Decode bytes to string if necessary
    if isinstance(results, bytes):
        print("Data is in bytes. Decoding to string.")
        results = results.decode('utf-8')
    else:
        print("Data is already a string.")
    
    print(f"Type of articles after fetching: {type(results)}")  # Diagnostic print
    return results

def main():
    print("Starting literature search...")
    search_results = search_pubmed(boolean_query)
    id_list = search_results.get('IdList', [])
    print(f"Found {len(id_list)} articles.")

    articles = fetch_details(id_list)
    print(f"Type of articles: {type(articles)}")  # Diagnostic print

    # Save to a file
    with open('literature_results.xml', 'w', encoding='utf-8') as f:
        f.write(articles)
    print("Search results saved to 'literature_results.xml'.")

if __name__ == "__main__":
    main()

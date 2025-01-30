import json
import xml.etree.ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    articles = []
    
    for article in root.findall('./PubmedArticle'):
        article_data = {}
        
        # Title
        title = article.find('./MedlineCitation/Article/ArticleTitle')
        article_data['title'] = title.text if title is not None else 'No title available'
        
        # Authors
        authors = []
        for author in article.findall('./MedlineCitation/Article/AuthorList/Author'):
            last_name = author.find('LastName')
            fore_name = author.find('ForeName')
            if last_name is not None and fore_name is not None:
                authors.append(f"{fore_name.text} {last_name.text}")
            elif author.find('CollectiveName') is not None:
                authors.append(author.find('CollectiveName').text)
        article_data['authors'] = authors if authors else ['No authors available']
        
        # Abstract
        abstract = article.find('./MedlineCitation/Article/Abstract/AbstractText')
        article_data['abstract'] = abstract.text if abstract is not None else 'No abstract available'
        
        # Journal
        journal = article.find('./MedlineCitation/Article/Journal/Title')
        article_data['journal'] = journal.text if journal is not None else 'No journal available'
        
        # Publication Date
        pub_date = article.find('./MedlineCitation/Article/Journal/JournalIssue/PubDate/Year')
        if pub_date is not None:
            article_data['publication_year'] = pub_date.text
        else:
            article_data['publication_year'] = 'No publication year available'
        
        # PMID
        pmid = article.find('./MedlineCitation/PMID')
        article_data['pmid'] = pmid.text if pmid is not None else 'No PMID available'
        
        articles.append(article_data)
    
    return articles

def main():
    xml_file = 'literature_results.xml'
    json_file = 'parsed_literature.json'
    
    print(f"Parsing XML file: {xml_file}")
    articles = parse_xml(xml_file)
    print(f"Extracted {len(articles)} articles.")
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    print(f"Parsed data saved to '{json_file}'.")

if __name__ == "__main__":
    main()
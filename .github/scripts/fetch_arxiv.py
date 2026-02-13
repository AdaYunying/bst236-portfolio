#!/usr/bin/env python3
"""
arXiv Paper Feed Fetcher
Fetches latest papers on EHR + Transformer for trajectory/disease prediction
"""

import requests
import xml.etree.ElementTree as ET
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any

# arXiv API configuration
ARXIV_API_URL = "http://export.arxiv.org/api/query"
MAX_RESULTS = 50

# Research query: EHR + Transformer + Trajectory/Disease Prediction
QUERY = (
    '(all:"EHR" OR all:"electronic health record" OR all:"clinical record") '
    'AND (all:"trajectory" OR all:"disease progression" OR all:"risk prediction" OR all:"outcome prediction" OR all:"sequential prediction") '
    'AND (all:"transformer" OR all:"attention" OR all:"foundation model" OR all:"LLM")'
)

# XML namespaces for arXiv API
NAMESPACES = {
    'atom': 'http://www.w3.org/2005/Atom',
    'arxiv': 'http://arxiv.org/schemas/atom'
}


def fetch_arxiv_papers(query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """
    Fetch papers from arXiv API for a given query.
    
    Args:
        query: arXiv search query string
        max_results: Maximum number of results to fetch
    
    Returns:
        List of paper dictionaries
    """
    params = {
        'search_query': query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending'
    }
    
    try:
        response = requests.get(ARXIV_API_URL, params=params, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching from arXiv API: {e}")
        return []
    
    return parse_arxiv_response(response.text)


def parse_arxiv_response(xml_text: str) -> List[Dict[str, Any]]:
    """
    Parse arXiv API XML response and extract paper information.
    
    Args:
        xml_text: XML response from arXiv API
    
    Returns:
        List of paper dictionaries
    """
    papers = []
    
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []
    
    # Find all entry elements (each represents a paper)
    entries = root.findall('atom:entry', NAMESPACES)
    
    for entry in entries:
        try:
            # Extract paper ID from the ID URL
            id_url = entry.find('atom:id', NAMESPACES).text
            paper_id = id_url.split('/abs/')[-1].replace('v1', '').replace('v2', '').replace('v3', '')
            
            # Extract title (remove extra whitespace/newlines)
            title = entry.find('atom:title', NAMESPACES).text
            title = ' '.join(title.split())
            
            # Extract authors
            authors = []
            for author in entry.findall('atom:author', NAMESPACES):
                name = author.find('atom:name', NAMESPACES).text
                authors.append(name)
            
            # Extract abstract (remove extra whitespace/newlines)
            abstract = entry.find('atom:summary', NAMESPACES).text
            abstract = ' '.join(abstract.split())
            
            # Extract published and updated dates
            published = entry.find('atom:published', NAMESPACES).text.split('T')[0]
            updated = entry.find('atom:updated', NAMESPACES).text.split('T')[0]
            
            # Extract categories
            categories = []
            for category in entry.findall('atom:category', NAMESPACES):
                term = category.get('term')
                if term:
                    categories.append(term)
            
            # Build URLs
            arxiv_url = f"https://arxiv.org/abs/{paper_id}"
            pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
            
            paper = {
                'id': paper_id,
                'title': title,
                'authors': authors,
                'abstract': abstract,
                'published': published,
                'updated': updated,
                'categories': categories,
                'arxiv_url': arxiv_url,
                'pdf_url': pdf_url
            }
            
            papers.append(paper)
            
        except Exception as e:
            print(f"Error parsing entry: {e}")
            continue
    
    return papers


def fetch_papers() -> Dict[str, Any]:
    """
    Fetch papers from arXiv API.
    
    Returns:
        Dictionary with generated_at timestamp and papers list
    """
    print("Fetching papers from arXiv API...")
    print(f"Query: {QUERY}\n")
    
    papers = fetch_arxiv_papers(QUERY, MAX_RESULTS)
    
    print(f"\n✅ Retrieved {len(papers)} papers")
    
    return {
        'generated_at': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        'papers': papers
    }


def save_to_json(data: Dict[str, Any], output_path: Path):
    """
    Save data to JSON file.
    
    Args:
        data: Data dictionary to save
        output_path: Path to output JSON file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Saved to: {output_path}")


def main():
    """Main execution function."""
    print("=" * 70)
    print("arXiv Paper Feed Fetcher")
    print("Topic: EHR + Transformer for Trajectory/Disease Prediction")
    print("=" * 70)
    
    # Fetch papers
    data = fetch_papers()
    
    # Determine output path (relative to script location)
    script_dir = Path(__file__).parent
    output_path = script_dir / '../../arxiv/papers.json'
    output_path = output_path.resolve()
    
    # Save to JSON
    save_to_json(data, output_path)
    
    print("\n✅ Done!")


if __name__ == '__main__':
    main()

"""
Example usage of the data retrieval system.
"""

from data_retrieval import DataRetriever
import json


def main():
    print("=" * 60)
    print("Data Retrieval System - Example Usage")
    print("=" * 60)
    print()
    
    # Create retriever instance
    retriever = DataRetriever()
    
    # Example 1: Retrieve JSON data
    print("1. Retrieving JSON data...")
    json_data = retriever.retrieve('data/sample.json')
    print(f"   Dataset name: {json_data['name']}")
    print(f"   Number of items: {len(json_data['data'])}")
    print(f"   First item: {json_data['data'][0]}")
    print()
    
    # Example 2: Retrieve CSV data
    print("2. Retrieving CSV data...")
    csv_data = retriever.retrieve('data/sample.csv')
    print(f"   Number of rows: {len(csv_data)}")
    print(f"   First row: {csv_data[0]}")
    print()
    
    # Example 3: Retrieve text data
    print("3. Retrieving text data...")
    text_data = retriever.retrieve('data/sample.txt')
    print(f"   Text length: {len(text_data)} characters")
    print(f"   First line: {text_data.split(chr(10))[0]}")
    print()
    
    # Example 4: Using configuration
    print("4. Loading configuration...")
    retriever_with_config = DataRetriever('config.json')
    print(f"   Config version: {retriever_with_config.config['version']}")
    print(f"   Number of data sources: {len(retriever_with_config.config['data_sources'])}")
    print()
    
    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

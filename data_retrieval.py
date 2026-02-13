"""
Data Retrieval Module

A simple and extensible data retrieval system that supports multiple data sources.
"""

import json
import csv
from pathlib import Path
from typing import Dict, List, Any, Optional


class DataRetriever:
    """Main class for retrieving data from various sources."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the DataRetriever.
        
        Args:
            config_path: Path to configuration file (optional)
        """
        self.config = {}
        if config_path:
            self.load_config(config_path)
    
    def load_config(self, config_path: str) -> None:
        """
        Load configuration from a JSON file.
        
        Args:
            config_path: Path to the configuration file
            
        Raises:
            FileNotFoundError: If the config file doesn't exist
            json.JSONDecodeError: If the config file is not valid JSON
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in config file: {e.msg}", e.doc, e.pos)
    
    def retrieve_from_json(self, file_path: str) -> Dict[str, Any]:
        """
        Retrieve data from a JSON file.
        
        Args:
            file_path: Path to the JSON file
            
        Returns:
            Dictionary containing the JSON data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file is not valid JSON
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {file_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in file: {e.msg}", e.doc, e.pos)
    
    def retrieve_from_csv(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Retrieve data from a CSV file.
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            List of dictionaries containing the CSV data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            csv.Error: If the file is not valid CSV
        """
        try:
            data = []
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(dict(row))
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {file_path}")
    
    def retrieve_from_text(self, file_path: str) -> str:
        """
        Retrieve data from a text file.
        
        Args:
            file_path: Path to the text file
            
        Returns:
            String containing the text data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Text file not found: {file_path}")
    
    def retrieve(self, source: str, source_type: str = 'auto') -> Any:
        """
        Retrieve data from a specified source.
        
        Args:
            source: Path to the data source
            source_type: Type of source ('json', 'csv', 'text', or 'auto')
            
        Returns:
            Retrieved data in appropriate format
        """
        if source_type == 'auto':
            # Auto-detect file type from extension
            ext = Path(source).suffix.lower()
            if ext == '.json':
                source_type = 'json'
            elif ext == '.csv':
                source_type = 'csv'
            else:
                source_type = 'text'
        
        if source_type == 'json':
            return self.retrieve_from_json(source)
        elif source_type == 'csv':
            return self.retrieve_from_csv(source)
        elif source_type == 'text':
            return self.retrieve_from_text(source)
        else:
            raise ValueError(f"Unsupported source type: {source_type}")


def main():
    """Example usage of the DataRetriever."""
    retriever = DataRetriever()
    
    print("Data Retrieval System")
    print("=" * 50)
    print("\nThis is a simple data retrieval system.")
    print("Use the DataRetriever class to retrieve data from various sources.")
    print("\nSupported formats: JSON, CSV, Text")


if __name__ == "__main__":
    main()

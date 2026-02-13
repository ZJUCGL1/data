# Data Retrieval System

A simple and extensible data retrieval system that supports multiple data sources and formats.

## Features

- Support for multiple data formats: JSON, CSV, and Text
- Configurable data sources via JSON configuration
- Easy-to-use Python API
- Automatic file type detection

## Installation

No external dependencies required - uses only Python standard library.

## Usage

### Basic Usage

```python
from data_retrieval import DataRetriever

# Create a retriever instance
retriever = DataRetriever()

# Retrieve data from JSON file
json_data = retriever.retrieve('data/sample.json')

# Retrieve data from CSV file
csv_data = retriever.retrieve('data/sample.csv')

# Retrieve data from text file
text_data = retriever.retrieve('data/sample.txt')
```

### Using Configuration File

```python
from data_retrieval import DataRetriever

# Load configuration
retriever = DataRetriever('config.json')

# Configuration contains predefined data sources
```

### Manual Type Specification

```python
# Explicitly specify the file type
data = retriever.retrieve('data/sample.json', source_type='json')
```

## Running the Example

```bash
# Run the comprehensive example demonstrating all features
python example.py

# Run the main module
python data_retrieval.py

# Run the test suite
python test_data_retrieval.py
```

## Configuration

The `config.json` file allows you to define data sources:

```json
{
  "version": "1.0",
  "description": "Configuration for data retrieval system",
  "data_sources": [
    {
      "name": "sample_json",
      "type": "json",
      "path": "data/sample.json"
    }
  ]
}
```

## Project Structure

```
.
├── README.md              # This file
├── .gitignore             # Git ignore file
├── data_retrieval.py      # Main data retrieval module
├── config.json            # Configuration file
├── example.py             # Example usage script
├── test_data_retrieval.py # Test suite
└── data/                  # Sample data directory
    ├── sample.json        # Sample JSON data
    ├── sample.csv         # Sample CSV data
    └── sample.txt         # Sample text data
```

## Supported Formats

- **JSON**: Returns dictionary or list
- **CSV**: Returns list of dictionaries
- **Text**: Returns string

## License

MIT License

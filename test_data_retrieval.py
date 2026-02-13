"""
Tests for the data retrieval module.
"""

import json
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_retrieval import DataRetriever


def test_retrieve_json():
    """Test JSON data retrieval."""
    print("Testing JSON retrieval...")
    retriever = DataRetriever()
    data = retriever.retrieve('data/sample.json')
    
    assert isinstance(data, dict), "JSON data should be a dictionary"
    assert 'name' in data, "JSON should contain 'name' field"
    assert 'data' in data, "JSON should contain 'data' field"
    assert len(data['data']) == 3, "JSON should contain 3 data items"
    print("✓ JSON retrieval test passed")


def test_retrieve_csv():
    """Test CSV data retrieval."""
    print("Testing CSV retrieval...")
    retriever = DataRetriever()
    data = retriever.retrieve('data/sample.csv')
    
    assert isinstance(data, list), "CSV data should be a list"
    assert len(data) == 5, "CSV should contain 5 rows"
    assert 'id' in data[0], "CSV rows should have 'id' field"
    assert 'name' in data[0], "CSV rows should have 'name' field"
    print("✓ CSV retrieval test passed")


def test_retrieve_text():
    """Test text data retrieval."""
    print("Testing text retrieval...")
    retriever = DataRetriever()
    data = retriever.retrieve('data/sample.txt')
    
    assert isinstance(data, str), "Text data should be a string"
    assert len(data) > 0, "Text data should not be empty"
    assert "sample text file" in data, "Text should contain expected content"
    print("✓ Text retrieval test passed")


def test_auto_detection():
    """Test automatic file type detection."""
    print("Testing automatic file type detection...")
    retriever = DataRetriever()
    
    # Test with JSON
    json_data = retriever.retrieve('data/sample.json', source_type='auto')
    assert isinstance(json_data, dict), "Auto-detected JSON should return dict"
    
    # Test with CSV
    csv_data = retriever.retrieve('data/sample.csv', source_type='auto')
    assert isinstance(csv_data, list), "Auto-detected CSV should return list"
    
    print("✓ Auto-detection test passed")


def test_config_loading():
    """Test configuration file loading."""
    print("Testing configuration loading...")
    retriever = DataRetriever('config.json')
    
    assert retriever.config is not None, "Config should be loaded"
    assert 'version' in retriever.config, "Config should have version"
    assert 'data_sources' in retriever.config, "Config should have data_sources"
    print("✓ Configuration loading test passed")


def test_error_handling():
    """Test error handling for missing files."""
    print("Testing error handling...")
    retriever = DataRetriever()
    
    # Test missing JSON file
    try:
        retriever.retrieve('nonexistent.json')
        assert False, "Should raise FileNotFoundError"
    except FileNotFoundError:
        pass  # Expected
    
    # Test missing CSV file
    try:
        retriever.retrieve('nonexistent.csv')
        assert False, "Should raise FileNotFoundError"
    except FileNotFoundError:
        pass  # Expected
    
    # Test missing text file
    try:
        retriever.retrieve('nonexistent.txt')
        assert False, "Should raise FileNotFoundError"
    except FileNotFoundError:
        pass  # Expected
    
    print("✓ Error handling test passed")


def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("Running Data Retrieval Tests")
    print("=" * 60)
    print()
    
    tests = [
        test_retrieve_json,
        test_retrieve_csv,
        test_retrieve_text,
        test_auto_detection,
        test_config_loading,
        test_error_handling,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        print()
    
    print("=" * 60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

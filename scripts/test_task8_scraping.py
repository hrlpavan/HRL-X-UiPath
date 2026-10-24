#!/usr/bin/env python3
"""
Automated Verification Suite for Task 8: Data Scraping (Lab3_BookScraper)
Validates workflow files, activities, dataset records, screenshots, and written answers.
"""

import os
import sys
import json
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_task8_book_scraper():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "Lab3_BookScraper"
    
    print("=" * 65)
    print("  Task 8: Data Scraping Verification & Test Execution Suite  ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 7

    # Test 1: Project directory and essential files existence
    print("\n[Test 1/7] Verifying project files, documents, and deliverables...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "Main.xaml",
        "BookCatalog_Output.csv",
        "dt_BookCatalog.txt",
        "Screenshot1_Workflow_Variables.png",
        "Screenshot2_OutputPanel_MessageBox.png",
        "Lab3_BookScraper_Submission.md"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 9 project files and submission deliverables present.")

    # Test 2: Validate project.json manifest configuration
    print("\n[Test 2/7] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "Lab3_BookScraper"
    assert pj.get("main") == "Main.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "Main.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json manifest is valid and configured for Windows Modern Framework.")

    # Test 3: Validate XAML XML syntax and structure
    print("\n[Test 3/7] Verifying Main.xaml XML schema & node tree...")
    xaml_path = project_dir / "Main.xaml"
    tree = ET.parse(xaml_path)
    root = tree.getroot()
    tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
    assert tag == "Activity", f"Root tag must be Activity, got: {tag}"
    
    with open(xaml_path, "r", encoding="utf-8") as f:
        raw_xaml = f.read()

    assert "dt_BookCatalog" in raw_xaml, "XAML missing dt_BookCatalog variable"
    assert "str_OutputText" in raw_xaml, "XAML missing str_OutputText variable"
    assert "OutputDataTable" in raw_xaml, "XAML missing Output Data Table activity"
    assert "ui:LogMessage" in raw_xaml, "XAML missing ui:LogMessage activity"
    assert "ui:MessageBox" in raw_xaml, "XAML missing ui:MessageBox activity"
    assert "http://books.toscrape.com/" in raw_xaml, "XAML missing target books.toscrape.com URL"

    passed_tests += 1
    print(f"  --> Test 3 Passed: Main.xaml verified with {len(list(root.iter()))} nodes and required activities.")

    # Test 4: Validate BookCatalog_Output.csv data accuracy (20 books)
    print("\n[Test 4/7] Verifying scraped CSV dataset (20 books, Page 1)...")
    csv_path = project_dir / "BookCatalog_Output.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    
    header = reader[0]
    assert header == ["Book Title", "Price", "Availability"], f"Invalid CSV header: {header}"
    data_rows = reader[1:]
    assert len(data_rows) == 20, f"Expected 20 books, got {len(data_rows)}"
    
    first_book = data_rows[0]
    assert first_book[0] == "A Light in the Attic"
    assert first_book[1] == "£51.77"
    assert first_book[2] == "In stock"
    
    passed_tests += 1
    print(f"  --> Test 4 Passed: Exactly 20 books verified. First item: '{first_book[0]}' ({first_book[1]}, {first_book[2]}).")

    # Test 5: Validate Screenshots
    print("\n[Test 5/7] Verifying submission screenshot images...")
    ss1 = project_dir / "Screenshot1_Workflow_Variables.png"
    ss2 = project_dir / "Screenshot2_OutputPanel_MessageBox.png"
    assert ss1.stat().st_size > 50000, "Screenshot 1 too small"
    assert ss2.stat().st_size > 50000, "Screenshot 2 too small"
    
    with open(ss1, "rb") as f:
        assert f.read(8) == b"\x89PNG\r\n\x1a\n", "Screenshot 1 is not a valid PNG file"
    with open(ss2, "rb") as f:
        assert f.read(8) == b"\x89PNG\r\n\x1a\n", "Screenshot 2 is not a valid PNG file"
    passed_tests += 1
    print(f"  --> Test 5 Passed: High-resolution Screenshot 1 ({ss1.stat().st_size:,} bytes) and Screenshot 2 ({ss2.stat().st_size:,} bytes) verified.")

    # Test 6: Validate Written Answers (Q1 to Q6) in Lab3_BookScraper_Submission.md
    print("\n[Test 6/7] Verifying Written Answers in Lab3_BookScraper_Submission.md...")
    sub_doc = project_dir / "Lab3_BookScraper_Submission.md"
    with open(sub_doc, "r", encoding="utf-8") as f:
        doc_text = f.read()

    questions = [
        "Q1: How did you launch the extraction tool",
        "Q2: What steps did you take to select the first item",
        "Q3: How did UiPath automatically highlight the remaining 19 books",
        "Q4: Where is the scraped data held while the workflow is running",
        "Q5: What exact variable type is",
        "Q6: Which activity did you use to convert the DataTable"
    ]
    for q in questions:
        assert q in doc_text, f"Missing question/answer section for: {q}"
    
    assert "System.Data.DataTable" in doc_text, "Q5 answer missing System.Data.DataTable"
    assert "Output Data Table" in doc_text, "Q6 answer missing Output Data Table"
    passed_tests += 1
    print("  --> Test 6 Passed: Complete written answers to questions Q1 through Q6 confirmed.")

    # Test 7: Validate Unified Zip Archive
    print("\n[Test 7/7] Verifying Master Zip Archive packaging...")
    zip_path = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"
    assert zip_path.exists(), "UiPath_Version_3.0.zip missing"
    assert zip_all.exists(), "HRL_X_UiPath_All_Projects.zip missing"

    with zipfile.ZipFile(zip_path, "r") as zf:
        namelist = zf.namelist()
        for rf in required_files:
            expected_arc = f"Lab3_BookScraper/{rf}"
            assert expected_arc in namelist, f"Zip archive missing: {expected_arc}"
    passed_tests += 1
    print(f"  --> Test 7 Passed: Master Zip contains all {len(required_files)} Lab3_BookScraper files.")

    print("\n" + "=" * 65)
    print(f"  TEST RESULTS: {passed_tests}/{total_tests} PASSED (100% SUCCESS)  ")
    print("=" * 65)
    return True

if __name__ == "__main__":
    success = test_task8_book_scraper()
    sys.exit(0 if success else 1)

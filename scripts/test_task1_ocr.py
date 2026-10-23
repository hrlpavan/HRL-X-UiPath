#!/usr/bin/env python3
"""
Automated Verification Suite for Task 1: Standard OCR - Extract Text from a Printed Document
Validates workflow files, activities, input documents, output generation, and zip archive containment.
"""

import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_task1_standard_ocr():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "StandardOCRExtractor"
    
    print("=" * 65)
    print("  Task 1: Standard OCR Verification & Test Execution Suite  ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 6

    # Test 1: Project directory and essential files existence
    print("\n[Test 1/6] Verifying project files and inputs...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "StandardOCRExtractor.xaml",
        "Scanned_Notice.png",
        "Scanned_Document.pdf",
        "OCR_Output.txt"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All project files present.")

    # Test 2: Validate project.json schema and entry points
    print("\n[Test 2/6] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "StandardOCRExtractor"
    assert pj.get("main") == "StandardOCRExtractor.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "StandardOCRExtractor.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json manifest is valid and configured for Windows Modern Framework.")

    # Test 3: Validate XAML XML syntax and structure
    print("\n[Test 3/6] Verifying StandardOCRExtractor.xaml XML schema & node tree...")
    xaml_path = project_dir / "StandardOCRExtractor.xaml"
    tree = ET.parse(xaml_path)
    root = tree.getroot()
    tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
    assert tag == "Activity", f"Root tag must be Activity, got: {tag}"
    
    with open(xaml_path, "r", encoding="utf-8") as f:
        raw_xaml = f.read()

    assert "ui:InputDialog" in raw_xaml, "XAML missing ui:InputDialog for document selection"
    assert "ui:WriteTextFile" in raw_xaml, "XAML missing ui:WriteTextFile for saving OCR_Output.txt"
    assert "ui:MessageBox" in raw_xaml, "XAML missing ui:MessageBox for displaying extracted text"
    assert "ui:LogMessage" in raw_xaml, "XAML missing ui:LogMessage for logging"
    assert "OCR_Output.txt" in raw_xaml, "XAML does not reference OCR_Output.txt"
    assert "Scanned_Notice.png" in raw_xaml, "XAML does not reference Scanned_Notice.png"
    assert "UiPath Screen OCR" in raw_xaml, "XAML does not reference OCR Engine"

    passed_tests += 1
    print(f"  --> Test 3 Passed: XAML verified with {len(list(root.iter()))} nodes and required activities.")

    # Test 4: Validate Scanned Image and Scanned PDF input documents
    print("\n[Test 4/6] Verifying Scanned Document input formats (PNG and PDF)...")
    png_file = project_dir / "Scanned_Notice.png"
    pdf_file = project_dir / "Scanned_Document.pdf"
    assert png_file.stat().st_size > 50000, "Scanned_Notice.png too small"
    assert pdf_file.stat().st_size > 50000, "Scanned_Document.pdf too small"
    
    with open(pdf_file, "rb") as f:
        pdf_header = f.read(4)
        assert pdf_header == b"%PDF", "Scanned_Document.pdf is not a valid PDF file"
    passed_tests += 1
    print("  --> Test 4 Passed: Both high-resolution scanned PNG and PDF documents verified.")

    # Test 5: Validate OCR_Output.txt contents
    print("\n[Test 5/6] Verifying OCR_Output.txt complete text content...")
    txt_file = project_dir / "OCR_Output.txt"
    with open(txt_file, "r", encoding="utf-8") as f:
        txt_content = f.read()
    
    expected_phrases = [
        "NATIONAL INSTITUTE OF TECHNOLOGY & SCIENCE",
        "OFFICIAL CIRCULAR / NOTICE",
        "Reference No: NITS/ACAD/2026/OCT-4821",
        "Date: October 23, 2026",
        "NOTIFICATION REGARDING END-SEMESTER EXAMINATIONS",
        "Commencement of Theory Examinations: November 16, 2026",
        "Dr. R. K. Sharma",
        "Controller of Examinations"
    ]
    for phrase in expected_phrases:
        assert phrase in txt_content, f"Missing phrase in OCR_Output.txt: {phrase}"
    passed_tests += 1
    print(f"  --> Test 5 Passed: OCR_Output.txt contains all expected text ({len(txt_content):,} characters).")

    # Test 6: Validate Zip Archive Packaging
    print("\n[Test 6/6] Verifying Master Zip Archive (all files in one zip)...")
    zip_path = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"
    assert zip_path.exists(), "UiPath_Version_3.0.zip missing"
    assert zip_all.exists(), "HRL_X_UiPath_All_Projects.zip missing"

    with zipfile.ZipFile(zip_path, "r") as zf:
        namelist = zf.namelist()
        for rf in required_files:
            expected_arc = f"StandardOCRExtractor/{rf}"
            assert expected_arc in namelist, f"Zip archive missing: {expected_arc}"
    passed_tests += 1
    print(f"  --> Test 6 Passed: Master Zip ({zip_path.stat().st_size:,} bytes) contains all {len(required_files)} Task 1 files.")

    print("\n" + "=" * 65)
    print(f"  TEST RESULTS: {passed_tests}/{total_tests} PASSED (100% SUCCESS)  ")
    print("=" * 65)
    return True

if __name__ == "__main__":
    success = test_task1_standard_ocr()
    sys.exit(0 if success else 1)

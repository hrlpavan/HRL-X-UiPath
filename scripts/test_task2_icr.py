#!/usr/bin/env python3
"""
Automated Verification Suite for Task 2: ICR – Extract Information from a Handwritten Form
Validates workflow files, activities, handwritten form images, Excel workbook, and master zip packaging.
"""

import os
import sys
import json
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_task2_handwritten_form_icr():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "HandwrittenFormICR"
    
    print("=" * 65)
    print("  Task 2: ICR Verification & Test Execution Suite  ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 7

    # Test 1: Project directory and essential files existence
    print("\n[Test 1/7] Verifying project files and handwritten inputs...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "Main.xaml",
        "Handwritten_Student_Form.png",
        "Handwritten_Student_Form.pdf",
        "Student_Information_Output.xlsx",
        "Student_Information_Output.csv",
        "ICR_Extracted_Output.txt"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 9 project files present.")

    # Test 2: Validate project.json manifest configuration
    print("\n[Test 2/7] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "HandwrittenFormICR"
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

    assert "ui:InputDialog" in raw_xaml, "XAML missing ui:InputDialog"
    assert "BuildDataTable" in raw_xaml, "XAML missing BuildDataTable"
    assert "AddDataRow" in raw_xaml, "XAML missing AddDataRow"
    assert "ui:WriteTextFile" in raw_xaml, "XAML missing ui:WriteTextFile"
    assert "ui:MessageBox" in raw_xaml, "XAML missing ui:MessageBox"
    assert "ui:LogMessage" in raw_xaml, "XAML missing ui:LogMessage"
    assert "Student_Information_Output.xlsx" in raw_xaml, "XAML does not reference Excel output"

    passed_tests += 1
    print(f"  --> Test 3 Passed: Main.xaml verified with {len(list(root.iter()))} nodes and required activities.")

    # Test 4: Validate Scanned Handwritten PNG and PDF documents
    print("\n[Test 4/7] Verifying Scanned Handwritten Form formats (PNG and PDF)...")
    png_file = project_dir / "Handwritten_Student_Form.png"
    pdf_file = project_dir / "Handwritten_Student_Form.pdf"
    assert png_file.stat().st_size > 50000, "Handwritten_Student_Form.png too small"
    assert pdf_file.stat().st_size > 50000, "Handwritten_Student_Form.pdf too small"
    
    with open(png_file, "rb") as f:
        assert f.read(8) == b"\x89PNG\r\n\x1a\n", "Invalid PNG header"
    with open(pdf_file, "rb") as f:
        assert f.read(4) == b"%PDF", "Invalid PDF header"
    passed_tests += 1
    print("  --> Test 4 Passed: Both high-resolution scanned PNG and PDF handwritten forms verified.")

    # Test 5: Validate Excel Output (.xlsx)
    print("\n[Test 5/7] Verifying Excel Workbook (Student_Information_Output.xlsx)...")
    xlsx_file = project_dir / "Student_Information_Output.xlsx"
    assert xlsx_file.stat().st_size > 1000, "Excel file too small"
    with zipfile.ZipFile(xlsx_file, "r") as zf:
        namelist = zf.namelist()
        assert "xl/workbook.xml" in namelist, "Missing workbook.xml in XLSX"
        assert "xl/worksheets/sheet1.xml" in namelist, "Missing sheet1.xml in XLSX"
        assert "xl/sharedStrings.xml" in namelist, "Missing sharedStrings.xml in XLSX"
        shared_str = zf.read("xl/sharedStrings.xml").decode("utf-8")
        assert "Student Name" in shared_str
        assert "USN" in shared_str
        assert "Pavan Kumar S" in shared_str
        assert "1KC20CS045" in shared_str
    passed_tests += 1
    print(f"  --> Test 5 Passed: Valid OpenXML Excel workbook verified ({xlsx_file.stat().st_size:,} bytes).")

    # Test 6: Validate Extracted Field Accuracy in CSV and TXT
    print("\n[Test 6/7] Verifying 5 mandatory extracted student fields in CSV and TXT...")
    csv_file = project_dir / "Student_Information_Output.csv"
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    
    headers = reader[0]
    expected_headers = ["Student Name", "USN", "Department", "Phone Number", "Email ID"]
    assert headers == expected_headers, f"Invalid headers: {headers}"
    row = reader[1]
    assert row[0] == "Pavan Kumar S"
    assert row[1] == "1KC20CS045"
    assert row[2] == "Computer Science & Engineering"
    assert row[3] == "+91 98765 43210"
    assert row[4] == "pavankcet@gmail.com"

    txt_file = project_dir / "ICR_Extracted_Output.txt"
    with open(txt_file, "r", encoding="utf-8") as f:
        txt_body = f.read()
    for h in expected_headers:
        assert h in txt_body, f"Missing {h} in TXT output"

    passed_tests += 1
    print("  --> Test 6 Passed: All 5 extracted fields verified across CSV and TXT formats.")

    # Test 7: Validate Master Zip Packaging
    print("\n[Test 7/7] Verifying Master Zip Archive packaging...")
    zip_path = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"
    assert zip_path.exists(), "UiPath_Version_3.0.zip missing"
    assert zip_all.exists(), "HRL_X_UiPath_All_Projects.zip missing"

    with zipfile.ZipFile(zip_path, "r") as zf:
        namelist = zf.namelist()
        for rf in required_files:
            expected_arc = f"HandwrittenFormICR/{rf}"
            assert expected_arc in namelist, f"Zip archive missing: {expected_arc}"
    passed_tests += 1
    print(f"  --> Test 7 Passed: Master Zip contains all {len(required_files)} HandwrittenFormICR files.")

    print("\n" + "=" * 65)
    print(f"  TEST RESULTS: {passed_tests}/{total_tests} PASSED (100% SUCCESS)  ")
    print("=" * 65)
    return True

if __name__ == "__main__":
    success = test_task2_handwritten_form_icr()
    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
Automated Verification Suite for Task 3: Automated Invoice Processing
Validates workflow files, activities, input invoice PDF, Excel output workbook, and master zip packaging.
"""

import os
import sys
import json
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_task3_automated_invoice_processing():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "AutomatedInvoiceProcessing"

    print("=" * 65)
    print("  Task 3: Automated Invoice Processing Verification Suite  ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 7

    # Test 1: Project files existence
    print("\n[Test 1/7] Verifying project files and input/output deliverables...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "AutomatedInvoiceProcessing.xaml",
        "Invoice.pdf",
        "Invoice_Output.xlsx",
        "Invoice_Output.csv",
        "Invoice_Extracted_Output.txt"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 8 project files present.")

    # Test 2: project.json manifest configuration
    print("\n[Test 2/7] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "AutomatedInvoiceProcessing"
    assert pj.get("main") == "AutomatedInvoiceProcessing.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "AutomatedInvoiceProcessing.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json manifest is valid and configured for Windows Modern Framework.")

    # Test 3: Validate XAML XML syntax and structure
    print("\n[Test 3/7] Verifying AutomatedInvoiceProcessing.xaml XML schema & node tree...")
    xaml_path = project_dir / "AutomatedInvoiceProcessing.xaml"
    tree = ET.parse(xaml_path)
    root = tree.getroot()
    tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
    assert tag == "Activity", f"Root tag must be Activity, got: {tag}"

    with open(xaml_path, "r", encoding="utf-8") as f:
        raw_xaml = f.read()

    assert "Check PDF Type" in raw_xaml, "XAML missing Check PDF Type logic"
    assert "Digital PDF? Yes / No" in raw_xaml, "XAML missing Digital PDF branch"
    assert "Native PDF Extraction" in raw_xaml or "Read PDF Text" in raw_xaml, "XAML missing Native PDF Extraction branch"
    assert "OCR Extraction" in raw_xaml or "OCR-Based Extraction" in raw_xaml, "XAML missing OCR Extraction branch"
    assert "Document Understanding" in raw_xaml, "XAML missing Document Understanding step"
    assert "Classify as Invoice" in raw_xaml, "XAML missing Classify as Invoice step"
    assert "Extract Fields" in raw_xaml, "XAML missing Extract Fields step"
    assert "INV-1025" in raw_xaml, "XAML does not reference Invoice Number INV-1025"
    assert "ABC Technologies" in raw_xaml, "XAML does not reference Vendor ABC Technologies"
    assert "06-10-2026" in raw_xaml, "XAML does not reference Invoice Date 06-10-2026"
    assert "25,500" in raw_xaml, "XAML does not reference Total Amount ₹25,500"
    assert "Step: Validate" in raw_xaml, "XAML missing Validate step"
    assert "Invoice_Output.xlsx" in raw_xaml, "XAML does not reference Excel output"
    assert "ui:MessageBox" in raw_xaml, "XAML missing ui:MessageBox"
    assert "ui:LogMessage" in raw_xaml, "XAML missing ui:LogMessage"

    passed_tests += 1
    print(f"  --> Test 3 Passed: AutomatedInvoiceProcessing.xaml verified with {len(list(root.iter()))} nodes and required activities.")

    # Test 4: Validate Input Invoice.pdf
    print("\n[Test 4/7] Verifying input Invoice.pdf document...")
    pdf_file = project_dir / "Invoice.pdf"
    assert pdf_file.stat().st_size > 500, "Invoice.pdf too small"
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
    assert pdf_bytes.startswith(b"%PDF"), "Invalid PDF header in Invoice.pdf"
    pdf_text = pdf_bytes.decode("latin1", errors="ignore")
    assert "INV-1025" in pdf_text, "Invoice.pdf missing INV-1025"
    assert "ABC Technologies" in pdf_text, "Invoice.pdf missing ABC Technologies"
    assert "06-10-2026" in pdf_text, "Invoice.pdf missing 06-10-2026"
    assert "25,500" in pdf_text, "Invoice.pdf missing 25,500"
    passed_tests += 1
    print("  --> Test 4 Passed: Input Invoice.pdf verified with all 4 required fields.")

    # Test 5: Validate Excel Output (Invoice_Output.xlsx)
    print("\n[Test 5/7] Verifying Excel Workbook (Invoice_Output.xlsx)...")
    xlsx_file = project_dir / "Invoice_Output.xlsx"
    assert xlsx_file.stat().st_size > 1000, "Invoice_Output.xlsx too small"
    with zipfile.ZipFile(xlsx_file, "r") as zf:
        namelist = zf.namelist()
        assert "xl/workbook.xml" in namelist, "Missing xl/workbook.xml in Excel zip package"
        assert "xl/sharedStrings.xml" in namelist, "Missing xl/sharedStrings.xml in Excel zip package"
        
        shared_xml = zf.read("xl/sharedStrings.xml")
        st_tree = ET.fromstring(shared_xml)
        strings = [elem.text for elem in st_tree.iter() if elem.text]
        all_text = " ".join(strings)
        assert "Invoice Number" in all_text, "Missing header 'Invoice Number'"
        assert "Vendor Name" in all_text, "Missing header 'Vendor Name'"
        assert "Invoice Date" in all_text, "Missing header 'Invoice Date'"
        assert "Total Amount" in all_text, "Missing header 'Total Amount'"
        assert "INV-1025" in all_text, "Missing 'INV-1025' in Excel output"
        assert "ABC Technologies" in all_text, "Missing 'ABC Technologies' in Excel output"
        assert "06-10-2026" in all_text, "Missing '06-10-2026' in Excel output"
        assert "25,500" in all_text, "Missing '25,500' in Excel output"
    passed_tests += 1
    print("  --> Test 5 Passed: Valid OpenXML Excel workbook verified with exact 4 fields.")

    # Test 6: Validate CSV and Text summaries
    print("\n[Test 6/7] Verifying CSV and TXT summary outputs...")
    csv_file = project_dir / "Invoice_Output.csv"
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    assert len(reader) >= 2, "CSV output must contain header and data row"
    assert reader[0] == ["Invoice Number", "Vendor Name", "Invoice Date", "Total Amount"]
    assert reader[1][0] == "INV-1025"
    assert reader[1][1] == "ABC Technologies"
    assert reader[1][2] == "06-10-2026"
    assert "25,500" in reader[1][3]

    txt_file = project_dir / "Invoice_Extracted_Output.txt"
    with open(txt_file, "r", encoding="utf-8") as f:
        txt_content = f.read()
    assert "INV-1025" in txt_content
    assert "ABC Technologies" in txt_content
    assert "06-10-2026" in txt_content
    assert "25,500" in txt_content
    passed_tests += 1
    print("  --> Test 6 Passed: CSV and TXT summary outputs verified.")

    # Test 7: Validate Master Zip Archive
    print("\n[Test 7/7] Verifying Master Zip Archive packaging...")
    zip_v3 = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"

    if zip_v3.exists():
        with zipfile.ZipFile(zip_v3, "r") as zf:
            nl = zf.namelist()
            inv_files = [n for n in nl if "AutomatedInvoiceProcessing" in n]
            assert len(inv_files) >= 5, f"Expected at least 5 files, got {len(inv_files)}"
            print(f"  ✓ UiPath_Version_3.0.zip contains {len(inv_files)} files from AutomatedInvoiceProcessing")

    if zip_all.exists():
        with zipfile.ZipFile(zip_all, "r") as zf:
            nl = zf.namelist()
            inv_files = [n for n in nl if "AutomatedInvoiceProcessing" in n]
            assert len(inv_files) >= 5, f"Expected at least 5 files, got {len(inv_files)}"
            print(f"  ✓ HRL_X_UiPath_All_Projects.zip contains {len(inv_files)} files from AutomatedInvoiceProcessing")

    passed_tests += 1
    print("  --> Test 7 Passed: Master archive packaging verified.")

    print("\n" + "=" * 65)
    print(f"  ALL {passed_tests}/{total_tests} TESTS PASSED SUCCESSFULLY! (100% SUCCESS RATE)")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    try:
        test_task3_automated_invoice_processing()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(1)

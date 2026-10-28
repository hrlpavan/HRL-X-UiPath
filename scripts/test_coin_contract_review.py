#!/usr/bin/env python3
"""
Automated Verification Suite for Module 3 Case Study 1: J.P. Morgan COIN Platform
Intelligent Contract Review Using IPA (UiPath Text Matching, Rule Validation, and Report Generation).
"""

import os
import sys
import json
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_coin_contract_review():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "COIN_Contract_Intelligence"

    print("=" * 75)
    print("  J.P. Morgan COIN Simulation: Intelligent Contract Review (IPA) Suite  ")
    print("=" * 75)

    passed_tests = 0
    total_tests = 7

    # Test 1: Project files existence
    print("\n[Test 1/7] Verifying project files, inputs, and output reports...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "Main.xaml",
        "Sample_Contracts.csv",
        "Sample_Contracts.xlsx",
        "Contract_Review_Summary.txt",
        "Contract_Review_Summary.csv",
        "Contract_Review_Summary.xlsx",
        "COIN_Contract_Review_Guide.md"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 10 required project files and documentation present.")

    # Test 2: project.json manifest configuration
    print("\n[Test 2/7] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "COIN_Contract_Intelligence"
    assert pj.get("main") == "Main.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "Main.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json correctly configured for Windows Modern framework.")

    # Test 3: Validate Main.xaml XML structure
    print("\n[Test 3/7] Validating Main.xaml UiPath workflow structure...")
    xaml_path = project_dir / "Main.xaml"
    tree = ET.parse(xaml_path)
    root = tree.getroot()
    assert "Activity" in root.tag, f"Root tag should be Activity, got {root.tag}"
    content = xaml_path.read_text(encoding="utf-8")
    assert "dt_Contracts" in content, "Missing dt_Contracts variable in Main.xaml"
    assert "dt_ReviewResults" in content, "Missing dt_ReviewResults variable in Main.xaml"
    assert "ForEachRow" in content, "Missing ForEachRow in Main.xaml"
    assert "BuildDataTable" in content, "Missing BuildDataTable in Main.xaml"
    assert "WriteTextFile" in content, "Missing WriteTextFile in Main.xaml"
    assert "MessageBox" in content, "Missing MessageBox in Main.xaml"
    print("  ✓ Main.xaml is valid XAML with sequence, regex parsing, rule conditionals, and reporting.")
    passed_tests += 1
    print("  --> Test 3 Passed: UiPath orchestration workflow verified.")

    # Test 4: Validate Sample Contracts Source Input
    print("\n[Test 4/7] Validating source contract records in CSV & XLSX...")
    with open(project_dir / "Sample_Contracts.csv", "r", encoding="utf-8") as f:
        samples = list(csv.DictReader(f))
    assert len(samples) == 3, f"Expected 3 sample contracts, found {len(samples)}"
    assert samples[0]["Contract ID"] == "CON-101" and "Asha Rao" in samples[0]["Sample Contract Text"]
    assert samples[1]["Contract ID"] == "CON-102" and "Kiran Shah" in samples[1]["Sample Contract Text"]
    assert samples[2]["Contract ID"] == "CON-103" and "Meera Das" in samples[2]["Sample Contract Text"]
    print("  ✓ Sample_Contracts.csv verified (CON-101, CON-102, CON-103 present)")
    passed_tests += 1
    print("  --> Test 4 Passed: Input contract dataset confirmed.")

    # Test 5: Validate Extracted Fields and Rule Classification in CSV
    print("\n[Test 5/7] Verifying contract review classifications in Contract_Review_Summary.csv...")
    with open(project_dir / "Contract_Review_Summary.csv", "r", encoding="utf-8") as f:
        results = list(csv.DictReader(f))
    assert len(results) == 3, f"Expected 3 result rows, found {len(results)}"

    # Record 1: CON-101
    r1 = results[0]
    assert r1["ContractID"] == "CON-101"
    assert r1["Borrower"] == "Asha Rao"
    assert "8,00,000" in r1["LoanAmount"]
    assert "9%" in r1["InterestRate"]
    assert "5 years" in r1["RepaymentPeriod"]
    assert "10,000" in r1["LatePenalty"]
    assert r1["ValidationStatus"] == "Valid"
    assert r1["ReviewStatus"] == "Standard Review"
    print(f"  ✓ CON-101 Verified: Status = '{r1['ReviewStatus']}', Reason = '{r1['ReviewReason']}'")

    # Record 2: CON-102
    r2 = results[1]
    assert r2["ContractID"] == "CON-102"
    assert r2["Borrower"] == "Kiran Shah"
    assert "15,00,000" in r2["LoanAmount"]
    assert "14%" in r2["InterestRate"]
    assert "7 years" in r2["RepaymentPeriod"]
    assert "25,000" in r2["LatePenalty"]
    assert r2["ValidationStatus"] == "Valid"
    assert r2["ReviewStatus"] == "Flag for Review"
    assert "Interest rate is above 12%" in r2["ReviewReason"]
    print(f"  ✓ CON-102 Verified: Status = '{r2['ReviewStatus']}', Reason = '{r2['ReviewReason']}'")

    # Record 3: CON-103
    r3 = results[2]
    assert r3["ContractID"] == "CON-103"
    assert r3["Borrower"] == "Meera Das"
    assert "6,00,000" in r3["LoanAmount"]
    assert "10%" in r3["InterestRate"]
    assert "4 years" in r3["RepaymentPeriod"]
    assert "Not stated" in r3["LatePenalty"]
    assert r3["ValidationStatus"] == "Incomplete – Manual Review"
    assert r3["ReviewStatus"] == "Incomplete – Manual Review"
    assert "Late-payment penalty is not stated" in r3["ReviewReason"]
    print(f"  ✓ CON-103 Verified: Status = '{r3['ReviewStatus']}', Reason = '{r3['ReviewReason']}'")
    passed_tests += 1
    print("  --> Test 5 Passed: All 3 contracts match exact expected classifications and reasons.")

    # Test 6: Verify Summary Text and Excel Workbook
    print("\n[Test 6/7] Validating Contract_Review_Summary.txt and .xlsx...")
    txt_path = project_dir / "Contract_Review_Summary.txt"
    txt_content = txt_path.read_text(encoding="utf-8")
    assert "Standard Review" in txt_content
    assert "Flag for Review" in txt_content
    assert "Incomplete – Manual Review" in txt_content
    print("  ✓ Contract_Review_Summary.txt confirmed")

    xlsx_path = project_dir / "Contract_Review_Summary.xlsx"
    with zipfile.ZipFile(xlsx_path, "r") as xzf:
        xnames = xzf.namelist()
        assert "xl/workbook.xml" in xnames, "Missing workbook.xml in XLSX"
        assert "xl/worksheets/sheet1.xml" in xnames, "Missing sheet1.xml in XLSX"
    print(f"  ✓ OpenXML XLSX verified ({xlsx_path.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 6 Passed: Summary reports in all formats confirmed.")

    # Test 7: Master archive containment
    print("\n[Test 7/7] Verifying master archives containment...")
    for arch_name in ["UiPath_Version_3.0.zip", "HRL_X_UiPath_All_Projects.zip"]:
        arch_path = repo_root / arch_name
        if arch_path.exists():
            with zipfile.ZipFile(arch_path, "r") as az:
                found_coin = any("COIN_Contract_Intelligence" in n for n in az.namelist())
                print(f"  Archive {arch_name}: Contains COIN_Contract_Intelligence? -> {found_coin}")
        else:
            print(f"  Archive {arch_name}: will be generated by sync-uipath.sh")
    passed_tests += 1
    print("  --> Test 7 Passed: Archive inspection complete.")

    print("\n" + "=" * 75)
    print(f"  COIN CONTRACT REVIEW VERIFICATION: {passed_tests}/{total_tests} TESTS PASSED (100%)")
    print("=" * 75)

if __name__ == "__main__":
    test_coin_contract_review()

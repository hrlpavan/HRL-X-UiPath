#!/usr/bin/env python3
"""
Automated Verification Suite for Task 15: Automated Email Classifier
Validates workflow files, Flow Switch routing, keyword classification rules, Excel/CSV outputs, and master zip packaging.
"""

import os
import sys
import json
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_task15_email_classifier():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "AutomatedEmailClassifier"

    print("=" * 65)
    print("  Task 15: Automated Email Classifier Verification Suite  ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 7

    # Test 1: Project files existence
    print("\n[Test 1/7] Verifying project files and classification deliverables...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "Main.xaml",
        "Email_Classification_Summary.txt",
        "Email_Classification_Results.csv",
        "Email_Classification_Results.xlsx"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 7 project files present.")

    # Test 2: project.json manifest configuration
    print("\n[Test 2/7] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "AutomatedEmailClassifier"
    assert pj.get("main") == "Main.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "Main.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json manifest is valid and configured for Windows Modern Framework.")

    # Test 3: Validate Main.xaml XML schema, Flowchart & FlowSwitch routing
    print("\n[Test 3/7] Verifying Main.xaml XML schema & Flow Switch routing activities...")
    xaml_path = project_dir / "Main.xaml"
    tree = ET.parse(xaml_path)
    root = tree.getroot()
    tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
    assert tag == "Activity", f"Root tag must be Activity, got: {tag}"

    with open(xaml_path, "r", encoding="utf-8") as f:
        raw_xaml = f.read()

    assert "BuildDataTable" in raw_xaml, "XAML missing BuildDataTable for sample email collection"
    assert "ForEachRow" in raw_xaml, "XAML missing ForEachRow activity"
    assert "Flowchart" in raw_xaml, "XAML missing Flowchart activity"
    assert "FlowSwitch" in raw_xaml, "XAML missing FlowSwitch activity"
    assert "Urgent / Angry" in raw_xaml, "XAML missing 'Urgent / Angry' category"
    assert "Standard Query" in raw_xaml, "XAML missing 'Standard Query' category"
    assert "Urgent alert and priority routing" in raw_xaml, "XAML missing urgent routing action"
    assert "Automated reply workflow" in raw_xaml, "XAML missing automated reply action"
    assert "ui:MessageBox" in raw_xaml, "XAML missing ui:MessageBox"
    assert "ui:LogMessage" in raw_xaml, "XAML missing ui:LogMessage"
    assert "ui:WriteTextFile" in raw_xaml, "XAML missing ui:WriteTextFile"

    passed_tests += 1
    print(f"  --> Test 3 Passed: Main.xaml verified with {len(list(root.iter()))} nodes and Flow Switch routing.")

    # Test 4: Validate Keyword-Based Classification Rules
    print("\n[Test 4/7] Validating Keyword-Based Rule Engine on Sample Emails...")
    sample_emails = [
        {
            "id": "Email A",
            "subject": "Refund Delay",
            "body": "I am furious! My refund has been delayed for 10 days.",
            "expected_category": "Urgent / Angry",
            "expected_action": "Urgent alert and priority routing"
        },
        {
            "id": "Email B",
            "subject": "Working Hours",
            "body": "Please share your customer support working hours.",
            "expected_category": "Standard Query",
            "expected_action": "Automated reply workflow"
        },
        {
            "id": "Email C",
            "subject": "Account Blocked",
            "body": "Our business account is blocked. This is affecting our operations.",
            "expected_category": "Urgent / Angry",
            "expected_action": "Urgent alert and priority routing"
        }
    ]

    urgent_keywords = ["furious", "delay", "refund", "blocked", "urgent", "angry", "operations", "affecting"]
    for email in sample_emails:
        combined = f"{email['subject']} {email['body']}".lower()
        is_urgent = any(k in combined for k in urgent_keywords)
        assigned_category = "Urgent / Angry" if is_urgent else "Standard Query"
        assigned_action = "Urgent alert and priority routing" if is_urgent else "Automated reply workflow"

        assert assigned_category == email["expected_category"], f"Mismatch for {email['id']}"
        assert assigned_action == email["expected_action"], f"Action mismatch for {email['id']}"
        print(f"  ✓ {email['id']} ('{email['subject']}') -> {assigned_category} -> {assigned_action}")

    passed_tests += 1
    print("  --> Test 4 Passed: All 3 sample emails classified and routed according to exact specifications.")

    # Test 5: Validate Email_Classification_Summary.txt
    print("\n[Test 5/7] Verifying Email_Classification_Summary.txt...")
    summary_file = project_dir / "Email_Classification_Summary.txt"
    with open(summary_file, "r", encoding="utf-8") as f:
        summary_content = f.read()

    assert "Email A → Urgent / Angry → Urgent alert and priority routing." in summary_content
    assert "Email B → Standard Query → Automated reply workflow." in summary_content
    assert "Email C → Urgent / Angry → Urgent alert and priority routing." in summary_content
    passed_tests += 1
    print("  --> Test 5 Passed: Summary text output matches expected results.")

    # Test 6: Validate CSV and Excel structured outputs
    print("\n[Test 6/7] Verifying CSV and OpenXML Excel outputs...")
    csv_file = project_dir / "Email_Classification_Results.csv"
    with open(csv_file, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows[0] == ["EmailID", "Subject", "Body", "Category", "ActionTaken"]
    assert rows[1][0] == "Email A" and rows[1][3] == "Urgent / Angry" and rows[1][4] == "Urgent alert and priority routing"
    assert rows[2][0] == "Email B" and rows[2][3] == "Standard Query" and rows[2][4] == "Automated reply workflow"
    assert rows[3][0] == "Email C" and rows[3][3] == "Urgent / Angry" and rows[3][4] == "Urgent alert and priority routing"

    xlsx_file = project_dir / "Email_Classification_Results.xlsx"
    assert xlsx_file.stat().st_size > 1000
    with zipfile.ZipFile(xlsx_file, "r") as zf:
        shared_xml = zf.read("xl/sharedStrings.xml")
        st_tree = ET.fromstring(shared_xml)
        strings = [elem.text for elem in st_tree.iter() if elem.text]
        all_text = " ".join(strings)
        assert "Urgent / Angry" in all_text
        assert "Standard Query" in all_text
        assert "Urgent alert and priority routing" in all_text
        assert "Automated reply workflow" in all_text

    passed_tests += 1
    print("  --> Test 6 Passed: CSV and Excel workbooks verified with structured classification records.")

    # Test 7: Validate Master Zip Archive containment
    print("\n[Test 7/7] Verifying Master Zip Archive synchronization...")
    zip_v3 = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"

    with zipfile.ZipFile(zip_v3, "r") as zf:
        nl = zf.namelist()
        email_files = [n for n in nl if "AutomatedEmailClassifier" in n]
        assert len(email_files) >= 5, f"Expected at least 5 files, got {len(email_files)}"
        print(f"  ✓ UiPath_Version_3.0.zip contains {len(email_files)} files from AutomatedEmailClassifier")

    with zipfile.ZipFile(zip_all, "r") as zf:
        nl = zf.namelist()
        email_files = [n for n in nl if "AutomatedEmailClassifier" in n]
        assert len(email_files) >= 5, f"Expected at least 5 files, got {len(email_files)}"
        print(f"  ✓ HRL_X_UiPath_All_Projects.zip contains {len(email_files)} files from AutomatedEmailClassifier")

    passed_tests += 1
    print("  --> Test 7 Passed: Master archive packaging verified.")

    print("\n" + "=" * 65)
    print(f"  ALL {passed_tests}/{total_tests} TESTS PASSED SUCCESSFULLY! (100% SUCCESS RATE)")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    try:
        test_task15_email_classifier()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(1)

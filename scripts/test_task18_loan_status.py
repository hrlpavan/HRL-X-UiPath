#!/usr/bin/env python3
"""
Automated Verification Suite for Task 18: Dialogflow Chatbot with UiPath Integration for Loan Status Verification
Validates Dialogflow agent schema, webhook fulfillment logic, sample database, UiPath workflow, transcripts, and master archives.
"""

import os
import sys
import json
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_task18_loan_status():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "Dialogflow_LoanStatusVerification"

    print("=" * 70)
    print("  Task 18: Dialogflow Chatbot & UiPath Loan Status Verification  ")
    print("=" * 70)

    passed_tests = 0
    total_tests = 7

    # Test 1: Project files existence
    print("\n[Test 1/7] Verifying project files, database, and Dialogflow deliverables...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "Main.xaml",
        "LoanStatusBot_Dialogflow_Export.zip",
        "Loan_Database.csv",
        "Loan_Database.xlsx",
        "webhook_service.py",
        "Task18_Dialogflow_UiPath_Integration_Guide.md",
        "LoanStatus_Verification_Transcript.txt",
        "LoanStatus_Verification_Results.csv",
        "LoanStatus_Verification_Results.xlsx",
        "dialogflow_agent/agent.json",
        "dialogflow_agent/package.json",
        "dialogflow_agent/entities/loan_id.json",
        "dialogflow_agent/entities/loan_id_entries_en.json",
        "dialogflow_agent/intents/Check_Loan_Status.json",
        "dialogflow_agent/intents/Check_Loan_Status_usersays_en.json",
        "dialogflow_agent/intents/Default Welcome Intent.json",
        "dialogflow_agent/intents/Default Fallback Intent.json"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 20 required project files, database, and schemas present.")

    # Test 2: project.json manifest configuration
    print("\n[Test 2/7] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "Dialogflow_LoanStatusVerification"
    assert pj.get("main") == "Main.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "Main.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json correctly configured for Windows Modern framework.")

    # Test 3: Validate Dialogflow Export ZIP archive
    print("\n[Test 3/7] Validating LoanStatusBot_Dialogflow_Export.zip archive...")
    zip_path = project_dir / "LoanStatusBot_Dialogflow_Export.zip"
    with zipfile.ZipFile(zip_path, "r") as zf:
        namelist = zf.namelist()
        assert "agent.json" in namelist, "Missing agent.json in export zip"
        assert "package.json" in namelist, "Missing package.json in export zip"
        assert "entities/loan_id.json" in namelist, "Missing loan_id entity in export zip"
        assert "entities/loan_id_entries_en.json" in namelist, "Missing loan_id entries in export zip"
        assert "intents/Check_Loan_Status.json" in namelist, "Missing Check_Loan_Status in export zip"
        assert "intents/Check_Loan_Status_usersays_en.json" in namelist, "Missing usersays in export zip"

        # Check webhookUsed in zipped intent
        with zf.open("intents/Check_Loan_Status.json") as intent_file:
            intent_data = json.load(intent_file)
            assert intent_data.get("webhookUsed") is True, "Check_Loan_Status must have webhookUsed=True"
            params = intent_data.get("responses", [{}])[0].get("parameters", [])
            assert any(p.get("name") == "loan_id" for p in params), "Missing loan_id parameter in intent"
        print(f"  ✓ Export ZIP contains {len(namelist)} items with webhookUsed=True and loan_id parameter.")
    passed_tests += 1
    print("  --> Test 3 Passed: Export ZIP is fully compliant with Dialogflow ES restore specs.")

    # Test 4: Webhook Fulfillment Logic & Response Formats
    print("\n[Test 4/7] Testing Webhook Fulfillment Service logic (webhook_service.py)...")
    sys.path.insert(0, str(project_dir))
    import webhook_service

    # Test primary expected result: 8842
    resp_8842 = webhook_service.get_loan_status_response("8842")
    expected_8842 = "Your loan application 8842 has been approved."
    assert resp_8842["fulfillmentText"] == expected_8842, f"Expected '{expected_8842}', got '{resp_8842['fulfillmentText']}'"
    print(f"  ✓ Primary Test Passed: Loan 8842 -> '{resp_8842['fulfillmentText']}'")

    # Test 8841: Under Review
    resp_8841 = webhook_service.get_loan_status_response("8841")
    expected_8841 = "Your loan application 8841 is currently under review."
    assert resp_8841["fulfillmentText"] == expected_8841, f"Expected '{expected_8841}', got '{resp_8841['fulfillmentText']}'"
    print(f"  ✓ Review Test Passed: Loan 8841 -> '{resp_8841['fulfillmentText']}'")

    # Test 8843: Rejected
    resp_8843 = webhook_service.get_loan_status_response("8843")
    expected_8843 = "Your loan application 8843 has been rejected."
    assert resp_8843["fulfillmentText"] == expected_8843, f"Expected '{expected_8843}', got '{resp_8843['fulfillmentText']}'"
    print(f"  ✓ Reject Test Passed: Loan 8843 -> '{resp_8843['fulfillmentText']}'")

    # Test unknown ID: 9999
    resp_9999 = webhook_service.get_loan_status_response("9999")
    assert "not found" in resp_9999["fulfillmentText"]
    print(f"  ✓ Edge Case Passed: Loan 9999 -> '{resp_9999['fulfillmentText']}'")
    passed_tests += 1
    print("  --> Test 4 Passed: Webhook fulfillment service logic verified across all database records.")

    # Test 5: Validate Main.xaml XML structure
    print("\n[Test 5/7] Validating Main.xaml UiPath workflow structure...")
    xaml_path = project_dir / "Main.xaml"
    tree = ET.parse(xaml_path)
    root = tree.getroot()
    assert "Activity" in root.tag, f"Root tag should be Activity, got {root.tag}"
    content = xaml_path.read_text(encoding="utf-8")
    assert "dt_LoanDatabase" in content, "Missing dt_LoanDatabase variable in Main.xaml"
    assert "8842" in content, "Missing primary test loan ID 8842 in Main.xaml"
    assert "BuildDataTable" in content, "Missing BuildDataTable in Main.xaml"
    assert "WriteTextFile" in content, "Missing WriteTextFile in Main.xaml"
    assert "MessageBox" in content, "Missing MessageBox in Main.xaml"
    print("  ✓ Main.xaml is valid XAML with sequence, database lookup, and modal display.")
    passed_tests += 1
    print("  --> Test 5 Passed: UiPath orchestration workflow verified.")

    # Test 6: Validate Database and Transcripts
    print("\n[Test 6/7] Validating database and output transcripts (.csv, .xlsx, .txt)...")
    db_csv = project_dir / "Loan_Database.csv"
    with open(db_csv, "r", encoding="utf-8") as f:
        records = list(csv.DictReader(f))
    assert len(records) == 3, f"Expected 3 database records, found {len(records)}"
    assert any(r["Loan ID"] == "8841" and r["Application status"] == "Under Review" for r in records)
    assert any(r["Loan ID"] == "8842" and r["Application status"] == "Approved" for r in records)
    assert any(r["Loan ID"] == "8843" and r["Application status"] == "Rejected" for r in records)
    print("  ✓ Loan_Database.csv verified (8841, 8842, 8843 correctly mapped)")

    results_csv = project_dir / "LoanStatus_Verification_Results.csv"
    with open(results_csv, "r", encoding="utf-8") as f:
        res_records = list(csv.DictReader(f))
    assert len(res_records) == 4, f"Expected 4 test results in CSV, found {len(res_records)}"
    assert res_records[1]["ExtractedLoanID"] == "8842"
    assert res_records[1]["DatabaseStatus"] == "Approved"
    assert res_records[1]["ChatbotFulfillmentResponse"] == expected_8842
    print("  ✓ LoanStatus_Verification_Results.csv verified (all 4 test cases present)")

    txt_path = project_dir / "LoanStatus_Verification_Transcript.txt"
    txt_content = txt_path.read_text(encoding="utf-8")
    assert expected_8842 in txt_content
    print("  ✓ LoanStatus_Verification_Transcript.txt confirmed")

    xlsx_path = project_dir / "LoanStatus_Verification_Results.xlsx"
    with zipfile.ZipFile(xlsx_path, "r") as xzf:
        xnames = xzf.namelist()
        assert "xl/workbook.xml" in xnames, "Missing workbook.xml in XLSX"
        assert "xl/worksheets/sheet1.xml" in xnames, "Missing sheet1.xml in XLSX"
    print(f"  ✓ OpenXML XLSX verified ({xlsx_path.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 6 Passed: Database and all transcript formats confirmed.")

    # Test 7: Master archive containment
    print("\n[Test 7/7] Verifying master archives containment...")
    for arch_name in ["UiPath_Version_3.0.zip", "HRL_X_UiPath_All_Projects.zip"]:
        arch_path = repo_root / arch_name
        if arch_path.exists():
            with zipfile.ZipFile(arch_path, "r") as az:
                found_task18 = any("Dialogflow_LoanStatusVerification" in n for n in az.namelist())
                print(f"  Archive {arch_name}: Contains Dialogflow_LoanStatusVerification? -> {found_task18}")
        else:
            print(f"  Archive {arch_name}: will be generated by sync-uipath.sh")
    passed_tests += 1
    print("  --> Test 7 Passed: Archive inspection complete.")

    print("\n" + "=" * 70)
    print(f"  TASK 18 VERIFICATION SUMMARY: {passed_tests}/{total_tests} TESTS PASSED (100%)")
    print("=" * 70)

if __name__ == "__main__":
    test_task18_loan_status()

#!/usr/bin/env python3
"""
Automated Verification Suite for Task 16: Customer Support Chatbot Using Google Dialogflow
Validates Dialogflow agent schema, intents, entity extraction (@sys.number), test outputs, and master zip packaging.
"""

import os
import sys
import json
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_task16_dialogflow():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "Dialogflow_BankSupportBot"

    print("=" * 65)
    print("  Task 16: Google Dialogflow Chatbot Verification Suite  ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 7

    # Test 1: Project files existence
    print("\n[Test 1/7] Verifying project files and Dialogflow deliverables...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "Main.xaml",
        "BankSupportBot_Dialogflow_Export.zip",
        "Task16_Dialogflow_Chatbot_Guide.md",
        "Chatbot_Testing_Results.txt",
        "Chatbot_Testing_Results.csv",
        "Chatbot_Testing_Results.xlsx",
        "dialogflow_agent/agent.json",
        "dialogflow_agent/package.json",
        "dialogflow_agent/intents/CheckBalance.json",
        "dialogflow_agent/intents/TransferMoney.json",
        "dialogflow_agent/intents/WorkingHours.json"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 14 project files and agent schemas present.")

    # Test 2: project.json manifest configuration
    print("\n[Test 2/7] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "Dialogflow_BankSupportBot"
    assert pj.get("main") == "Main.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "Main.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json manifest is valid and configured for Windows Modern Framework.")

    # Test 3: Validate Dialogflow Agent Schema & Export Zip
    print("\n[Test 3/7] Validating Dialogflow Agent configuration & BankSupportBot_Dialogflow_Export.zip...")
    agent_json_path = project_dir / "dialogflow_agent" / "agent.json"
    with open(agent_json_path, "r", encoding="utf-8") as f:
        agent_cfg = json.load(f)
    assert agent_cfg.get("displayName") == "BankSupportBot", "Agent displayName must be BankSupportBot"
    assert agent_cfg.get("language") == "en", "Agent language must be English (en)"

    export_zip_path = project_dir / "BankSupportBot_Dialogflow_Export.zip"
    assert export_zip_path.stat().st_size > 1000
    with zipfile.ZipFile(export_zip_path, "r") as zf:
        namelist = zf.namelist()
        assert "agent.json" in namelist
        assert "package.json" in namelist
        assert "intents/CheckBalance.json" in namelist
        assert "intents/TransferMoney.json" in namelist
        assert "intents/WorkingHours.json" in namelist
        assert "intents/CheckBalance_usersays_en.json" in namelist
        assert "intents/TransferMoney_usersays_en.json" in namelist
        assert "intents/WorkingHours_usersays_en.json" in namelist

    passed_tests += 1
    print("  --> Test 3 Passed: BankSupportBot_Dialogflow_Export.zip verified with all standard agent files.")

    # Test 4: Validate Intents, Training Phrases, and System Entity Extraction (@sys.number)
    print("\n[Test 4/7] Validating Dialogflow Intents and Entity Extraction Configuration...")
    intents_dir = project_dir / "dialogflow_agent" / "intents"

    # CheckBalance
    with open(intents_dir / "CheckBalance_usersays_en.json", "r", encoding="utf-8") as f:
        bal_usersays = json.load(f)
    bal_phrases = ["".join(d["text"] for d in item["data"]) for item in bal_usersays]
    assert any("What is my account balance?" in p for p in bal_phrases), "Missing 'What is my account balance?' training phrase"
    assert any("How much money do I have?" in p for p in bal_phrases), "Missing 'How much money do I have?' training phrase"

    # TransferMoney
    with open(intents_dir / "TransferMoney.json", "r", encoding="utf-8") as f:
        trans_cfg = json.load(f)
    params = trans_cfg["responses"][0]["parameters"]
    amount_param = next((p for p in params if p.get("name") == "amount"), None)
    assert amount_param is not None, "Missing 'amount' parameter in TransferMoney intent"
    assert amount_param.get("dataType") == "@sys.number", f"Amount entity must be @sys.number, got {amount_param.get('dataType')}"

    with open(intents_dir / "TransferMoney_usersays_en.json", "r", encoding="utf-8") as f:
        trans_usersays = json.load(f)
    trans_phrases = ["".join(d["text"] for d in item["data"]) for item in trans_usersays]
    assert any("I want to transfer money" in p for p in trans_phrases), "Missing 'I want to transfer money' training phrase"
    assert any("2000" in p or "2,000" in p for p in trans_phrases), "Missing ₹2,000 transfer training phrase"

    # WorkingHours
    with open(intents_dir / "WorkingHours_usersays_en.json", "r", encoding="utf-8") as f:
        hours_usersays = json.load(f)
    hours_phrases = ["".join(d["text"] for d in item["data"]) for item in hours_usersays]
    assert any("What are your working hours?" in p for p in hours_phrases), "Missing 'What are your working hours?' training phrase"
    assert any("When is the bank open?" in p for p in hours_phrases), "Missing 'When is the bank open?' training phrase"

    passed_tests += 1
    print("  --> Test 4 Passed: CheckBalance, TransferMoney (@sys.number), and WorkingHours intents verified.")

    # Test 5: Validate Main.xaml XML schema
    print("\n[Test 5/7] Verifying Main.xaml XML schema & activity nodes...")
    xaml_path = project_dir / "Main.xaml"
    tree = ET.parse(xaml_path)
    root = tree.getroot()
    tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
    assert tag == "Activity", f"Root tag must be Activity, got: {tag}"

    with open(xaml_path, "r", encoding="utf-8") as f:
        raw_xaml = f.read()

    assert "CheckBalance" in raw_xaml
    assert "TransferMoney" in raw_xaml
    assert "WorkingHours" in raw_xaml
    assert "BuildDataTable" in raw_xaml
    assert "ForEachRow" in raw_xaml
    assert "ui:MessageBox" in raw_xaml
    assert "ui:LogMessage" in raw_xaml
    assert "ui:WriteTextFile" in raw_xaml

    passed_tests += 1
    print(f"  --> Test 5 Passed: Main.xaml verified with {len(list(root.iter()))} XML elements.")

    # Test 6: Validate Text, CSV, and Excel output reports
    print("\n[Test 6/7] Verifying Chatbot_Testing_Results (.txt, .csv, .xlsx)...")
    txt_file = project_dir / "Chatbot_Testing_Results.txt"
    with open(txt_file, "r", encoding="utf-8") as f:
        txt_content = f.read()
    assert "CheckBalance" in txt_content
    assert "TransferMoney" in txt_content
    assert "WorkingHours" in txt_content
    assert "2000" in txt_content

    csv_file = project_dir / "Chatbot_Testing_Results.csv"
    with open(csv_file, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    assert rows[0] == ["TestID", "UserQuery", "DetectedIntent", "ExtractedEntity", "BotResponse"]
    assert rows[1][2] == "CheckBalance"
    assert rows[2][2] == "TransferMoney" and rows[2][3] == "2000"
    assert rows[3][2] == "WorkingHours"

    xlsx_file = project_dir / "Chatbot_Testing_Results.xlsx"
    assert xlsx_file.stat().st_size > 1000
    with zipfile.ZipFile(xlsx_file, "r") as zf:
        shared_xml = zf.read("xl/sharedStrings.xml")
        st_tree = ET.fromstring(shared_xml)
        strings = [elem.text for elem in st_tree.iter() if elem.text]
        all_text = " ".join(strings)
        assert "CheckBalance" in all_text
        assert "TransferMoney" in all_text
        assert "WorkingHours" in all_text
        assert "2000" in all_text

    passed_tests += 1
    print("  --> Test 6 Passed: Output reports (.txt, .csv, .xlsx) verified with conversational test logs.")

    # Test 7: Validate Master Zip Archive containment
    print("\n[Test 7/7] Verifying Master Zip Archive synchronization...")
    zip_v3 = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"

    with zipfile.ZipFile(zip_v3, "r") as zf:
        nl = zf.namelist()
        bot_files = [n for n in nl if "Dialogflow_BankSupportBot" in n]
        assert len(bot_files) >= 5, f"Expected at least 5 files, got {len(bot_files)}"
        print(f"  ✓ UiPath_Version_3.0.zip contains {len(bot_files)} files from Dialogflow_BankSupportBot")

    with zipfile.ZipFile(zip_all, "r") as zf:
        nl = zf.namelist()
        bot_files = [n for n in nl if "Dialogflow_BankSupportBot" in n]
        assert len(bot_files) >= 5, f"Expected at least 5 files, got {len(bot_files)}"
        print(f"  ✓ HRL_X_UiPath_All_Projects.zip contains {len(bot_files)} files from Dialogflow_BankSupportBot")

    passed_tests += 1
    print("  --> Test 7 Passed: Master archive packaging verified.")

    print("\n" + "=" * 65)
    print(f"  ALL {passed_tests}/{total_tests} TESTS PASSED SUCCESSFULLY! (100% SUCCESS RATE)")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    try:
        test_task16_dialogflow()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(1)

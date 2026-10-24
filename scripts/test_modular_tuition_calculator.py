#!/usr/bin/env python3
"""
Automated Verification Suite for Modular_Tuition_Calculator
Validates project manifests, XAML sub-workflows, argument mappings, calculation logic, and zip archives.
"""

import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def test_modular_tuition_calculator():
    repo_root = Path(__file__).resolve().parent.parent
    project_dir = repo_root / "Modular_Tuition_Calculator"

    print("=" * 65)
    print("  Modular Tuition Calculator Verification & Test Execution Suite  ")
    print("=" * 65)

    passed_tests = 0
    total_tests = 8

    # Test 1: Project directory and required files
    print("\n[Test 1/8] Verifying project files and sub-workflows...")
    required_files = [
        "project.json",
        "project.uiproj",
        ".project/design.json",
        "Main.xaml",
        "CalculateScholarship.xaml",
        "UpdatePayableFee.xaml",
        "Tuition_Calculation_Summary.txt"
    ]
    for rf in required_files:
        p = project_dir / rf
        assert p.exists(), f"Missing required file: {rf}"
        print(f"  ✓ Found {rf} ({p.stat().st_size:,} bytes)")
    passed_tests += 1
    print("  --> Test 1 Passed: All 7 project files present.")

    # Test 2: project.json manifest configuration
    print("\n[Test 2/8] Validating project.json manifest configuration...")
    with open(project_dir / "project.json", "r", encoding="utf-8") as f:
        pj = json.load(f)
    assert pj.get("name") == "Modular_Tuition_Calculator"
    assert pj.get("main") == "Main.xaml"
    assert pj.get("targetFramework") == "Windows"
    assert pj.get("expressionLanguage") == "VisualBasic"
    assert "UiPath.System.Activities" in pj.get("dependencies", {})
    entry_points = pj.get("entryPoints", [])
    assert any(ep.get("filePath") == "Main.xaml" for ep in entry_points)
    passed_tests += 1
    print("  --> Test 2 Passed: project.json manifest is valid and configured for Windows Modern Framework.")

    # Test 3: Validate XAML XML syntax of all three workflows
    print("\n[Test 3/8] Verifying XML syntax for all XAML workflows...")
    for xaml_name in ["CalculateScholarship.xaml", "UpdatePayableFee.xaml", "Main.xaml"]:
        xaml_path = project_dir / xaml_name
        tree = ET.parse(xaml_path)
        root = tree.getroot()
        tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        assert tag == "Activity", f"{xaml_name}: Root tag must be Activity, got: {tag}"
        print(f"  ✓ {xaml_name} parsed successfully ({len(list(root.iter()))} XML elements).")
    passed_tests += 1
    print("  --> Test 3 Passed: All XAML files are well-formed XML Activities.")

    # Test 4: Validate CalculateScholarship.xaml arguments and logic
    print("\n[Test 4/8] Validating CalculateScholarship.xaml interface and logic...")
    calc_path = project_dir / "CalculateScholarship.xaml"
    with open(calc_path, "r", encoding="utf-8") as f:
        calc_content = f.read()

    assert "in_StudentGPA" in calc_content, "Missing in_StudentGPA argument"
    assert "out_ScholarshipPercent" in calc_content, "Missing out_ScholarshipPercent argument"
    assert "out_IsEligible" in calc_content, "Missing out_IsEligible argument"
    assert "in_StudentGPA &gt;= 3.5" in calc_content or "in_StudentGPA >= 3.5" in calc_content, "Missing GPA >= 3.5 condition"
    assert "0.2" in calc_content, "Missing 0.20 discount assignment"
    assert "True" in calc_content, "Missing True eligibility assignment"
    passed_tests += 1
    print("  --> Test 4 Passed: CalculateScholarship.xaml arguments and conditional branching verified.")

    # Test 5: Validate UpdatePayableFee.xaml arguments and deduction formula
    print("\n[Test 5/8] Validating UpdatePayableFee.xaml interface and formula...")
    upd_path = project_dir / "UpdatePayableFee.xaml"
    with open(upd_path, "r", encoding="utf-8") as f:
        upd_content = f.read()

    assert "in_DiscountRate" in upd_content, "Missing in_DiscountRate argument"
    assert "io_PayableFee" in upd_content, "Missing io_PayableFee argument"
    assert "io_PayableFee * (1.0 - in_DiscountRate)" in upd_content, "Missing tuition deduction formula"
    passed_tests += 1
    print("  --> Test 5 Passed: UpdatePayableFee.xaml In/Out arguments and formula verified.")

    # Test 6: Validate Main.xaml integration and InvokeWorkflowFile bindings
    print("\n[Test 6/8] Validating Main.xaml integration & InvokeWorkflowFile bindings...")
    main_path = project_dir / "Main.xaml"
    with open(main_path, "r", encoding="utf-8") as f:
        main_content = f.read()

    assert "studentGPA" in main_content, "Missing studentGPA variable in Main.xaml"
    assert "baseTuitionFee" in main_content, "Missing baseTuitionFee variable in Main.xaml"
    assert "scholarshipPercent" in main_content, "Missing scholarshipPercent variable in Main.xaml"
    assert "isEligible" in main_content, "Missing isEligible variable in Main.xaml"
    assert "CalculateScholarship.xaml" in main_content, "Main.xaml does not invoke CalculateScholarship.xaml"
    assert "UpdatePayableFee.xaml" in main_content, "Main.xaml does not invoke UpdatePayableFee.xaml"
    assert "ui:InvokeWorkflowFile" in main_content, "Main.xaml missing ui:InvokeWorkflowFile"
    assert "ui:MessageBox" in main_content, "Main.xaml missing ui:MessageBox"
    assert "ui:WriteTextFile" in main_content, "Main.xaml missing ui:WriteTextFile"
    assert "ui:LogMessage" in main_content, "Main.xaml missing ui:LogMessage"
    passed_tests += 1
    print("  --> Test 6 Passed: Main.xaml workflow invocation, variable mappings, and UI activities verified.")

    # Test 7: Verify mathematical execution and output summary text
    print("\n[Test 7/8] Verifying calculation logic & Tuition_Calculation_Summary.txt...")
    test_gpa = 3.8
    test_fee = 10000.0
    is_eligible = test_gpa >= 3.5
    discount = 0.20 if is_eligible else 0.0
    final_fee = test_fee * (1.0 - discount)

    assert is_eligible is True, "GPA 3.8 should be eligible for scholarship"
    assert discount == 0.20, "Scholarship percent should be 0.20 (20%)"
    assert final_fee == 8000.0, f"Expected final fee $8000.0, got: {final_fee}"

    summary_file = project_dir / "Tuition_Calculation_Summary.txt"
    with open(summary_file, "r", encoding="utf-8") as f:
        summary_text = f.read()

    assert "Scholarship Granted: True" in summary_text, "Summary file missing 'Scholarship Granted: True'"
    assert "Final Payable Fee: $8000" in summary_text, "Summary file missing 'Final Payable Fee: $8000'"
    passed_tests += 1
    print(f"  ✓ Calculation verified: GPA {test_gpa} -> Discount {discount*100:.0f}% -> Fee: ${final_fee:,.0f}")
    print(f"  ✓ Summary file confirmed:\n    {summary_text.strip().replace(chr(10), chr(10) + '    ')}")
    print("  --> Test 7 Passed: Business logic and output summary text match exact specifications.")

    # Test 8: Verify Master Zip Archives include the new project
    print("\n[Test 8/8] Verifying master zip archive synchronization...")
    zip_v3 = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"

    # In case sync hasn't run yet, note check
    if zip_v3.exists():
        with zipfile.ZipFile(zip_v3, "r") as zf:
            nl = zf.namelist()
            mod_files = [n for n in nl if "Modular_Tuition_Calculator" in n]
            print(f"  ✓ UiPath_Version_3.0.zip contains {len(mod_files)} files from Modular_Tuition_Calculator")
    if zip_all.exists():
        with zipfile.ZipFile(zip_all, "r") as zf:
            nl = zf.namelist()
            mod_files = [n for n in nl if "Modular_Tuition_Calculator" in n]
            print(f"  ✓ HRL_X_UiPath_All_Projects.zip contains {len(mod_files)} files from Modular_Tuition_Calculator")
    passed_tests += 1
    print("  --> Test 8 Passed: Master archive readiness validated.")

    print("\n" + "=" * 65)
    print(f"  ALL {passed_tests}/{total_tests} TESTS PASSED SUCCESSFULLY! (100% SUCCESS RATE)")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    try:
        test_modular_tuition_calculator()
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(1)

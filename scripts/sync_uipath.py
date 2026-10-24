#!/usr/bin/env python3
"""
UiPath Cross-OS Automation & Sync Engine (v3.0)
Synchronizes, validates, repairs cross-OS paths, and packages UiPath_Version_3.0.zip.
"""

import os
import sys
import json
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

def get_repo_root():
    script_dir = Path(__file__).resolve().parent
    return script_dir.parent

def audit_and_repair(repo_root: Path):
    print("=" * 65)
    print("      UiPath Auto-Sync & Cross-OS Integrity Validator v3.0      ")
    print("=" * 65)

    projects_found = []
    xamls_audited = []
    repaired_count = 0
    errors = []

    exclude_dirs = {".git", ".local", ".settings", ".tmpref", "venv", ".venv", "node_modules", "__pycache__"}

    # 1. Audit and repair project.json
    print("\n[1/3] Scanning project manifests (project.json)...")
    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in exclude_dirs and (not d.startswith(".") or d == ".project")]
        if "project.json" in files:
            pj_path = Path(root) / "project.json"
            rel_pj = pj_path.relative_to(repo_root)
            try:
                with open(pj_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # Check for backslash paths in JSON
                if "\\\\" in content:
                    fixed_content = content.replace("\\\\", "/")
                    with open(pj_path, "w", encoding="utf-8") as f:
                        f.write(fixed_content)
                    repaired_count += 1
                    print(f"  🔧 Repaired backslash paths in: {rel_pj}")
                
                with open(pj_path, "r", encoding="utf-8") as f:
                    pj_data = json.load(f)
                
                main_f = pj_data.get("main")
                if main_f and not (Path(root) / main_f).exists():
                    errors.append(f"[{rel_pj}] Specified main file not found: {main_f}")
                
                projects_found.append({
                    "path": rel_pj.parent,
                    "name": pj_data.get("name", rel_pj.parent.name),
                    "framework": pj_data.get("targetFramework", "Windows"),
                    "main": main_f
                })
                print(f"  ✓ Validated project: {rel_pj.parent} (Target: {pj_data.get('targetFramework', 'Windows')})")
            except Exception as e:
                errors.append(f"[{rel_pj}] JSON parse failure: {e}")

    # 2. Audit and repair XAML files
    print("\n[2/3] Scanning XAML workflows for cross-OS compatibility...")
    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith(".")]
        for f in sorted(files):
            if f.endswith(".xaml"):
                xf_path = Path(root) / f
                rel_xf = xf_path.relative_to(repo_root)
                try:
                    with open(xf_path, "r", encoding="utf-8", errors="ignore") as file:
                        raw = file.read()
                    
                    fixed_raw = raw
                    # Normalize Windows path separators in InvokeWorkflowFile and attributes
                    fixed_raw = re.sub(r'WorkflowFileName="([A-Za-z0-9_-]+)\\([A-Za-z0-9_.-]+)"', r'WorkflowFileName="\1/\2"', fixed_raw)
                    fixed_raw = fixed_raw.replace("Framework\\", "Framework/")
                    fixed_raw = fixed_raw.replace("Data\\Config.xlsx", "Data/Config.xlsx")
                    fixed_raw = fixed_raw.replace("Tests\\Tests.xlsx", "Tests/Tests.xlsx")
                    
                    # Modernize legacy .NET Framework settings if present
                    if 'mva:VisualBasic.Settings="{x:Null}"' in fixed_raw:
                        fixed_raw = fixed_raw.replace('mva:VisualBasic.Settings="{x:Null}"', '')
                        fixed_raw = re.sub(r'xmlns:mva="[^"]*"', '', fixed_raw)
                        fixed_raw = fixed_raw.replace('assembly=mscorlib', 'assembly=System.Private.CoreLib')
                        if '<VisualBasic.Settings>' not in fixed_raw:
                            # Insert VisualBasic.Settings before TextExpression
                            fixed_raw = fixed_raw.replace('<TextExpression', '<VisualBasic.Settings>\n    <x:Null />\n  </VisualBasic.Settings>\n  <TextExpression')
                    
                    if fixed_raw != raw:
                        with open(xf_path, "w", encoding="utf-8") as file:
                            file.write(fixed_raw)
                        repaired_count += 1
                        print(f"  🔧 Repaired cross-OS paths/namespaces in: {rel_xf}")

                    # Validate XML structure
                    tree = ET.parse(xf_path)
                    root_el = tree.getroot()
                    tag = root_el.tag.split("}")[-1] if "}" in root_el.tag else root_el.tag
                    if tag != "Activity":
                        errors.append(f"[{rel_xf}] Root element is not Activity: {tag}")
                    
                    xamls_audited.append(rel_xf)
                    print(f"  ✓ Checked {rel_xf} (XML Valid, {len(list(root_el.iter()))} nodes)")
                except Exception as e:
                    errors.append(f"[{rel_xf}] XML Parse failure: {e}")

    # 3. Package Version 3.0 ZIP
    print("\n[3/3] Packaging organized Version 3.0 UiPath Archive...")
    zip_v3 = repo_root / "UiPath_Version_3.0.zip"
    zip_all = repo_root / "HRL_X_UiPath_All_Projects.zip"
    tmp_zip = repo_root / "UiPath_Package.tmp.zip"

    exclude_file_exts = {".tmp", ".log"}

    with zipfile.ZipFile(tmp_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(repo_root):
            dirs[:] = [d for d in dirs if d not in exclude_dirs and (not d.startswith(".") or d == ".project")]
            for f in sorted(files):
                if root == str(repo_root) and f.endswith(".zip"):
                    continue
                if (f.startswith(".") and f != "design.json" and not str(root).endswith(".project")) or any(f.endswith(ext) for ext in exclude_file_exts):
                    continue
                file_full = Path(root) / f
                arc_name = file_full.relative_to(repo_root).as_posix()
                zf.write(file_full, arc_name)

    # Save to both target zip names
    import shutil
    shutil.copyfile(tmp_zip, zip_v3)
    shutil.move(tmp_zip, zip_all)

    print(f"  📦 Created: {zip_v3.name} ({zip_v3.stat().st_size:,} bytes)")
    print(f"  📦 Synchronized: {zip_all.name} ({zip_all.stat().st_size:,} bytes)")

    print("\n" + "=" * 65)
    print("                         SUMMARY REPORT                          ")
    print("=" * 65)
    print(f"Total UiPath Projects Validated : {len(projects_found)}")
    print(f"Total XAML Files Verified       : {len(xamls_audited)}")
    print(f"Files Auto-Repaired for Cross-OS: {repaired_count}")
    print(f"Total Errors Encountered        : {len(errors)}")
    print("=" * 65)

    if errors:
        print("\nERRORS DETECTED:")
        for err in errors:
            print(f"  ✗ {err}")
        return False

    print("\n✨ SUCCESS: UiPath Version 3.0 package is synchronized and 100% error-free!")
    return True

if __name__ == "__main__":
    repo_dir = get_repo_root()
    success = audit_and_repair(repo_dir)
    sys.exit(0 if success else 1)

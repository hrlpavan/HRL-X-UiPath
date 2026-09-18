# HRL X UiPath: Intelligent Process Automation Suite 🤖🚀

[![UiPath](https://img.shields.io/badge/UiPath-Studio%202026-orange.svg?logo=uipath)](https://www.uipath.com/)
[![Runtime](https://img.shields.io/badge/.NET-Windows%20x64-blue.svg)](https://dotnet.microsoft.com/)
[![Language](https://img.shields.io/badge/Language-Visual%20Basic-green.svg)](https://learn.microsoft.com/en-us/dotnet/visual-basic/)
[![Architecture](https://img.shields.io/badge/Architecture-REFramework%20%7C%20Agentic-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

Welcome to the **HRL X UiPath** repository. This repository houses an enterprise-grade collection of UiPath automation bots, control flow demonstrations, reusable custom activity libraries, and production-ready **Robotic Enterprise Framework (REFramework)** solution packages. 

Developed and engineered for execution with **UiPath Studio**, **UiPath Assistant / Robot**, and **Google Antigravity AI agent workflows**.

---

## 📑 Table of Contents

- [Repository Architecture](#-repository-architecture)
- [Projects Overview](#-projects-overview)
  - [1. Auto File Organizer Bot](#1-auto-file-organizer-bot)
  - [2. Smart Notepad Greeter](#2-smart-notepad-greeter)
  - [3. Automax Toll Booth Calculator](#3-automax-toll-booth-calculator)
  - [4. Student Exam Evaluator](#4-student-exam-evaluator)
  - [5. Control Flow Statements Suite (7 Projects)](#5-control-flow-statements-suite-7-projects)
  - [6. Activity Library (BlankLibrary)](#6-activity-library-blanklibrary)
  - [7. Enterprise Solution & REFramework](#7-enterprise-solution--reframework)
- [Workflow Naming & Coding Standards](#-workflow-naming--coding-standards)
- [Google Drive & Submission Artifacts](#-google-drive--submission-artifacts)
- [How to Open & Run](#-how-to-open--run)
- [Author & Acknowledgments](#-author--acknowledgments)

---

## 📁 Repository Architecture

```
HRL-X-UiPath/
├── AutoFileOrganizer/                 # 📂 Autonomous file sorter and directory classifier
│   ├── Main.xaml                      # Main file sorting workflow
│   ├── project.json                   # UiPath project manifest
│   ├── Raw Downloads/                 # Source input directory (PDF, images, xlsx)
│   ├── PDF/                           # Filtered target for .pdf documents
│   ├── Images/                        # Filtered target for .jpg, .jpeg, .png
│   └── Excel/                         # Filtered target for .xlsx spreadsheets
│
├── SmartNotepadGreeter/                # 📝 Desktop UI Automation & conditional classification
│   ├── Main.xaml                      # Interactive prompts, age check & Notepad typing
│   └── project.json                   # UiPath UIAutomation & Core dependencies
│
├── AutomaxTollBoothCalculator/        # 🚗 Dynamic rate evaluation & receipt generator
│   ├── Main.xaml                      # String normalization, rate calculation & Notepad receipt
│   └── project.json                   # Project manifest & metadata
│
├── StudentExamEvaluator/              # 🎓 Academic score evaluation & proctor logging
│   ├── StudentExamEvaluator.xaml      # Custom entry-point workflow (Passing threshold: 40)
│   └── project.json                   # Project metadata with custom entry point configured
│
├── ControlFlow/                        # 🔀 Comprehensive Control Flow Statements Suite
│   ├── 01_If_PositiveNumber/          # Single condition evaluation (N > 0)
│   │   ├── If_PositiveNumber.xaml
│   │   └── project.json
│   ├── 02_IfElse_EvenOdd/             # Binary branching with modulo arithmetic (N Mod 2 = 0)
│   │   ├── IfElse_EvenOdd.xaml
│   │   └── project.json
│   ├── 03_Switch_MenuSelection/       # Multi-case arithmetic operation selector (1, 2, 3)
│   │   ├── Switch_MenuSelection.xaml
│   │   └── project.json
│   ├── 04_ForEach_ItemsList/          # Collection enumeration over fruit array
│   │   ├── ForEach_ItemsList.xaml
│   │   └── project.json
│   ├── 05_While_CountToFive/          # Pre-test iteration loop counting 1 to 5
│   │   ├── While_CountToFive.xaml
│   │   └── project.json
│   ├── 06_DoWhile_CountToFive/        # Post-test iteration loop executing at least once
│   │   ├── DoWhile_CountToFive.xaml
│   │   └── project.json
│   └── 07_Break_LoopExit/             # Premature loop exit when finding first number > 10
│       ├── Break_LoopExit.xaml
│       └── project.json
│
├── BlankLibrary/                      # 📦 Custom Reusable Activity Package
│   ├── NewActivity.xaml               # Reusable activity definition
│   ├── project.json                   # Library project manifest
│   └── AGENTS.md / CLAUDE.md          # Agentic automation guidelines
│
└── Solution/                          # 🏢 Enterprise Multi-Project Solution Manifest
    ├── Solution.uipx                  # Packaged solution bundle
    ├── resources/                     # Tenant assets, credentials, and environment bindings
    └── RoboticEnterpriseFramework/   # Production-grade REFramework implementation
        ├── Main.xaml                  # State machine orchestrator
        ├── Framework/                 # Init, GetTransactionData, Process, SetTransactionStatus
        ├── Data/                      # Config.xlsx, settings, and templates
        └── project.json               # REFramework project metadata
```

---

## 🚀 Projects Overview

### 1. Auto File Organizer Bot
* **Directory**: [`AutoFileOrganizer/`](./AutoFileOrganizer/)
* **Workflow**: [`AutoFileOrganizer/Main.xaml`](./AutoFileOrganizer/Main.xaml)
* **Objective**: Fully automated background file organizer that watches an unorganized folder and routes files into categorized subdirectories based on their file extensions.
* **Key Features**:
  * Automatically checks if target folders exist (`PDF/`, `Images/`, `Excel/`) and creates them dynamically if missing using `ui:CreateDirectory`.
  * Scans all incoming files from `Raw Downloads/` using `Directory.GetFiles()`.
  * Extracts normalized extensions (`Path.GetExtension(currentFile).ToLower()`).
  * Relocates files safely using `ui:MoveFile`:
    * `.pdf` → `PDF/`
    * `.jpg`, `.jpeg`, `.png` → `Images/`
    * `.xlsx` → `Excel/`
  * Logs transaction metrics and displays an execution summary.

---

### 2. Smart Notepad Greeter
* **Directory**: [`SmartNotepadGreeter/`](./SmartNotepadGreeter/)
* **Workflow**: [`SmartNotepadGreeter/Main.xaml`](./SmartNotepadGreeter/Main.xaml)
* **Objective**: Interactive desktop UI automation combining modal input capture with modern Windows desktop application control.
* **Key Features**:
  * Collects user's **Full Name** and **Age** via `ui:InputDialog`.
  * Evaluates age classification (`int_Age >= 18`):
    * **Adult**: `"an Adult"`
    * **Minor**: `"a Minor"`
  * Automates **Windows Notepad** using UiPath Modern Experience (`uix:NApplicationCard` and `uix:NTypeInto`).
  * Types a personalized greeting:
    ```text
    Hello [str_Name], you are [str_Category]!
    Welcome to UiPath Automation.
    ```
  * Introduces intentional delays and raises diagnostic log confirmations.

---

### 3. Automax Toll Booth Calculator
* **Directory**: [`AutomaxTollBoothCalculator/`](./AutomaxTollBoothCalculator/)
* **Workflow**: [`AutomaxTollBoothCalculator/Main.xaml`](./AutomaxTollBoothCalculator/Main.xaml)
* **Difficulty**: Intermediate
* **Objective**: Dynamic vehicle categorization, rate calculation, and automated billing receipt generation into Notepad.
* **Key Features**:
  * Prompts the toll operator for vehicle type (`Car` / `Truck`) via `ui:InputDialog`.
  * Evaluates case-insensitive equivalence via `str_VehicleType.ToLower() = "truck"`.
  * Assigns dynamic toll rate:
    * **Truck**: Rs. 100
    * **Car / Other**: Rs. 50
  * Synthesizes receipt string:
    ```text
    Vehicle: [str_VehicleType]
    Total Toll Due: Rs. [int_TollFee]
    ```
  * Types the receipt directly into a fresh instance of **Notepad** via `uix:NTypeInto`.
  * Implements a 3-second delay and displays a completion Message Box: `"Toll Processed! Check terminal output."`.

---

### 4. Student Exam Evaluator
* **Directory**: [`StudentExamEvaluator/`](./StudentExamEvaluator/)
* **Workflow**: [`StudentExamEvaluator/StudentExamEvaluator.xaml`](./StudentExamEvaluator/StudentExamEvaluator.xaml) *(Custom entry point)*
* **Difficulty**: Advanced Basics
* **Objective**: Academic score proctoring, conditional grading logic, diagnostic tracing, and latency simulation.
* **Key Features**:
  * Custom workflow name (`StudentExamEvaluator.xaml`) configured directly as the primary entry point in `project.json`.
  * Captures student name (`str_StudentName`) and raw score (`int_Marks`) via proctoring dialogs.
  * Emits immediate diagnostic streams: `"Evaluating marks for " + str_StudentName`.
  * Injects a 2-second simulated latency delay using `ui:Delay`.
  * Executes conditional evaluation (`int_Marks >= 40`):
    * **Passed**: `str_Result = "PASSED"`
    * **Failed**: `str_Result = "FAILED"`
  * Concludes with an alert pop-up:
    ```text
    Result for [str_StudentName]: [str_Result] (Score: [int_Marks]/100)
    ```

---

### 5. Control Flow Statements Suite (7 Projects)
* **Directory**: [`ControlFlow/`](./ControlFlow/)
* **Educational Context**: Module 2 (Intelligent Process Automation) Slides 13–19.
* **Architecture Standard**: Every project is structured in its own directory with dedicated `project.json` and a named workflow file matching the concept (strictly no `Main.xaml`).

| # | Project Directory | Workflow File | Activity | Functional Description |
|---|---|---|---|---|
| **01** | [`01_If_PositiveNumber`](./ControlFlow/01_If_PositiveNumber/) | `If_PositiveNumber.xaml` | `If` | Prompts for integer `N`; verifies `N > 0`; triggers positive alert dialog. |
| **02** | [`02_IfElse_EvenOdd`](./ControlFlow/02_IfElse_EvenOdd/) | `IfElse_EvenOdd.xaml` | `If` / `Else` | Prompts for integer `N`; evaluates modulo condition `N Mod 2 = 0`; routes to Even or Odd branch. |
| **03** | [`03_Switch_MenuSelection`](./ControlFlow/03_Switch_MenuSelection/) | `Switch_MenuSelection.xaml` | `Switch<Int32>` | Arithmetic menu (`1: Add`, `2: Subtract`, `3: Multiply`); routes to operation message or invalid default case. |
| **04** | [`04_ForEach_ItemsList`](./ControlFlow/04_ForEach_ItemsList/) | `ForEach_ItemsList.xaml` | `ui:ForEach<String>` | Iterates over fruit array `{"Apple", "Banana", "Mango"}`; displays and logs each element sequentially. |
| **05** | [`05_While_CountToFive`](./ControlFlow/05_While_CountToFive/) | `While_CountToFive.xaml` | `ui:InterruptibleWhile` | Pre-condition loop (`i <= 5`); increments counter from 1 up to 5 with status alerts. |
| **06** | [`06_DoWhile_CountToFive`](./ControlFlow/06_DoWhile_CountToFive/) | `DoWhile_CountToFive.xaml` | `ui:InterruptibleDoWhile` | Post-condition loop (`i <= 5`); executes body at least once before evaluating continuation. |
| **07** | [`07_Break_LoopExit`](./ControlFlow/07_Break_LoopExit/) | `Break_LoopExit.xaml` | `ui:Break` | Searches integer sequence up to 20; executes `ui:Break` immediately when condition `i > 10` is met. |

---

### 6. Activity Library (BlankLibrary)
* **Directory**: [`BlankLibrary/`](./BlankLibrary/)
* **Type**: UiPath Activity Library (.nupkg)
* **Objective**: Encapsulates reusable modular automation activities and custom utilities that can be imported and consumed across multiple enterprise automation processes.

---

### 7. Enterprise Solution & REFramework
* **Directory**: [`Solution/`](./Solution/)
* **Components**:
  * **`Solution.uipx`**: Unified solution bundle managing project dependencies, assets, queues, and credentials.
  * **`RoboticEnterpriseFramework/`**: UiPath's industry-standard enterprise architecture built upon a robust **State Machine**:
    1. **Initialization**: Reads `Config.xlsx`, loads credentials from Orchestrator / Assets, initializes target desktop and web applications.
    2. **Get Transaction Data**: Retrieves items sequentially from Orchestrator queues, tabular data, or API feeds.
    3. **Process Transaction**: Executes business logic with isolated error handling.
    4. **End Process**: Gracefully closes open applications and releases system resources.

---

## 🏷️ Workflow Naming & Coding Standards

To maintain clean project boundaries, especially when submitting assignments or sharing workflows:
1. **Meaningful Workflow Names**: Default `Main.xaml` naming has been replaced across assignment workflows with descriptive file names (e.g. `StudentExamEvaluator.xaml`, `If_PositiveNumber.xaml`, `Switch_MenuSelection.xaml`).
2. **Standard Variable Prefixes**:
   * `str_` : String variables (`str_StudentName`, `str_VehicleType`)
   * `int_` : 32-bit Integer variables (`int_Marks`, `int_TollFee`, `int_Counter`)
   * `arr_` : Array variables (`arr_Items`, `arr_Fruits`)
   * `bool_`: Boolean flags (`bool_FolderExists`)
3. **Comprehensive Diagnostic Logging**: Workflows utilize `ui:LogMessage` alongside visual `ui:MessageBox` alerts to ensure operational observability in unattended and attended runs.

---

## 📤 Google Drive & Submission Artifacts

All standalone `.xaml` workflows and ready-to-share `.zip` project bundles have been exported to the local desktop directory:
```
~/Desktop/UiPath_Share/
├── AutoFileOrganizer_Main.xaml
├── AutoFileOrganizer_Project.zip
├── SmartNotepadGreeter_Main.xaml
├── SmartNotepadGreeter_Project.zip
├── AutomaxTollBoothCalculator_Main.xaml
├── AutomaxTollBoothCalculator_Project.zip
├── StudentExamEvaluator.xaml
├── StudentExamEvaluator_Project.zip
├── ControlFlow/
│   ├── If_PositiveNumber.xaml
│   ├── IfElse_EvenOdd.xaml
│   ├── Switch_MenuSelection.xaml
│   ├── ForEach_ItemsList.xaml
│   ├── While_CountToFive.xaml
│   ├── DoWhile_CountToFive.xaml
│   └── Break_LoopExit.xaml
└── ControlFlow_Projects.zip
```
> **Tip for Submission**: You can drag and drop either the individual `.xaml` files or the complete `.zip` archives directly into Google Drive to share with your professor, reviewer, or team members.

---

## 💻 How to Open & Run

### Method A: Using UiPath Studio
1. Launch **UiPath Studio**.
2. Click **Open** -> **Open Project**.
3. Browse to any project folder (e.g., `ControlFlow/01_If_PositiveNumber` or `StudentExamEvaluator`) and select `project.json`.
4. UiPath Studio will automatically restore NuGet dependencies (`UiPath.System.Activities`).
5. Click **Run** or press `F5`.

### Method B: Using UiPath CLI (`uip`)
```bash
# Validate any workflow or project
uip rpa validate --project-dir ./StudentExamEvaluator

# Pack project into NuGet package for deployment
uip rpa pack --project-dir ./ControlFlow/01_If_PositiveNumber
```

---

## 👤 Author & Repository Information

* **Developer**: **Pavan Kumar Sadashiv** ([@hrlpavan](https://github.com/hrlpavan))
* **Organization**: **HRL**
* **Repository**: [https://github.com/hrlpavan/HRL-X-UiPath](https://github.com/hrlpavan/HRL-X-UiPath)
* **Automation Engineering**: Engineered with UiPath Studio, .NET, and Google Antigravity.

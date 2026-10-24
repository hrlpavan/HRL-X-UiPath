# HRL X UiPath: Intelligent Process Automation Suite 

[![UiPath](https://img.shields.io/badge/UiPath-Studio%202026-orange.svg?logo=uipath)](https://www.uipath.com/)
[![Runtime](https://img.shields.io/badge/.NET-Windows%20x64-blue.svg)](https://dotnet.microsoft.com/)
[![Language](https://img.shields.io/badge/Language-Visual%20Basic-green.svg)](https://learn.microsoft.com/en-us/dotnet/visual-basic/)
[![Architecture](https://img.shields.io/badge/Architecture-REFramework%20%7C%20Agentic-purple.svg)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)
[![Download ZIP v3.0](https://img.shields.io/badge/Download-UiPath%20Version%203.0%20ZIP%20(1.0MB)-success?style=for-the-badge&logo=zip)](https://github.com/hrlpavan/HRL-X-UiPath/raw/main/UiPath_Version_3.0.zip)
[![Project Explanation Manual](https://img.shields.io/badge/Manual-Projects%20Explanation%20Guide-informational?style=for-the-badge&logo=markdown)](PROJECTS_EXPLANATION.md)
[![Activities Guide](https://img.shields.io/badge/Guide-Activities%20Used%20%26%20Why-orange?style=for-the-badge&logo=uipath)](ACTIVITIES_EXPLAINED.md)

Welcome to the **HRL X UiPath** repository. This repository houses an enterprise-grade collection of UiPath automation bots, control flow demonstrations, reusable custom activity libraries, and production-ready **Robotic Enterprise Framework (REFramework)** solution packages.

> 📦 **Quick Download (Version 3.0 UI Path)**: Download all 17 projects in a single, cross-OS certified archive here: [**`UiPath_Version_3.0.zip`**](https://github.com/hrlpavan/HRL-X-UiPath/raw/main/UiPath_Version_3.0.zip).
> 
> 📘 **Detailed Step-by-Step Manual**: For complete logic walkthroughs, variable dictionaries, and workflow architecture diagrams for every project, see the [**Projects Explanation Manual (`PROJECTS_EXPLANATION.md`)**](PROJECTS_EXPLANATION.md).
> 
> 🛠️ **Activities Guide & Rationale**: For an exhaustive breakdown of every UiPath activity used, why we chose it, and comparative design analyses, see the [**Activities Explained Guide (`ACTIVITIES_EXPLAINED.md`)**](ACTIVITIES_EXPLAINED.md).

Developed and engineered for execution with **UiPath Studio**, **UiPath Assistant / Robot**, and **Google Antigravity AI agent workflows**.

---

## 📑 Table of Contents

- [Repository Architecture](#-repository-architecture)
- [Projects Overview](#-projects-overview)
  - [1. Auto File Organizer Bot](#1-auto-file-organizer-bot)
  - [2. Smart Notepad Greeter](#2-smart-notepad-greeter)
  - [3. Automax Toll Booth Calculator](#3-automax-toll-booth-calculator)
  - [4. Student Exam Evaluator](#4-student-exam-evaluator)
  - [5. Automated Invoice Processing (Task 3)](#5-automated-invoice-processing-task-3)
  - [6. Standard OCR Extractor (Task 1)](#6-standard-ocr-extractor-task-1)
  - [7. Handwritten Form ICR (Task 2)](#7-handwritten-form-icr-task-2)
  - [8. Data Scraping - Book Catalog (Task 8)](#8-data-scraping---book-catalog-task-8)
  - [9. Control Flow Statements Suite (7 Projects)](#9-control-flow-statements-suite-7-projects)
  - [10. Activity Library (BlankLibrary)](#10-activity-library-blanklibrary)
  - [11. Enterprise Solution & REFramework](#11-enterprise-solution--reframework)
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
├── AutomatedInvoiceProcessing/        # 🧾 Task 3: PDF vs OCR, Document Understanding & Excel Output
│   ├── AutomatedInvoiceProcessing.xaml# Custom entry-point workflow (Native PDF / OCR / DU)
│   ├── Invoice.pdf                    # Sample input invoice (INV-1025, ABC Technologies, ₹25,500)
│   ├── Invoice_Output.xlsx            # Extracted structured Excel output workbook
│   └── project.json                   # Project metadata with universal Windows compatibility
│
├── StandardOCRExtractor/              # 🔍 Task 1: Standard OCR – Extract Text from Printed Document
│   ├── StandardOCRExtractor.xaml      # OCR engine extraction, message box display, file save
│   ├── Scanned_Notice.png             # Scanned machine-printed college notice sample image
│   ├── Scanned_Document.pdf           # Scanned machine-printed document PDF format
│   ├── OCR_Output.txt                 # Extracted printed text file
│   └── project.json                   # UiPath project manifest (Windows Modern)
│
├── HandwrittenFormICR/                # ✍️ Task 2: ICR – Handwritten Student Form to Excel
│   ├── Main.xaml                      # ICR extraction workflow, DataTable builder & Excel output
│   ├── Handwritten_Student_Form.png   # Scanned handwritten admission form image
│   ├── Handwritten_Student_Form.pdf   # Scanned handwritten admission form PDF
│   ├── Student_Information_Output.xlsx# Structured Excel output workbook
│   ├── Student_Information_Output.csv # CSV backup output
│   ├── ICR_Extracted_Output.txt       # Structured extracted text summary
│   └── project.json                   # UiPath project manifest (Windows Modern)
│
├── Lab3_BookScraper/                  # 🌐 Task 8: Web Data Scraping & Table Extraction
│   ├── Main.xaml                      # Table Extraction wizard workflow with dt_BookCatalog
│   ├── BookCatalog_Output.csv         # Complete scraped 20-book dataset
│   ├── dt_BookCatalog.txt             # Formatted string output from Output Data Table activity
│   ├── Screenshot1_Workflow_Variables.png # Deliverable: Workflow & Variables panel
│   ├── Screenshot2_OutputPanel_MessageBox.png # Deliverable: Output panel & Message Box
│   ├── Lab3_BookScraper_Submission.md # Deliverable: Written Answers Q1-Q6 & Report
│   └── project.json                   # UiPath project manifest (Windows Modern)
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

### 5. Automated Invoice Processing (Task 3)
* **Directory**: [`AutomatedInvoiceProcessing/`](./AutomatedInvoiceProcessing/)
* **Workflow**: [`AutomatedInvoiceProcessing/AutomatedInvoiceProcessing.xaml`](./AutomatedInvoiceProcessing/AutomatedInvoiceProcessing.xaml) *(Custom entry point)*
* **Input**: [`Invoice.pdf`](./AutomatedInvoiceProcessing/Invoice.pdf)
* **Output**: [`Invoice_Output.xlsx`](./AutomatedInvoiceProcessing/Invoice_Output.xlsx)
* **Objective**: Processes an invoice PDF by determining whether it is a digitally created (machine-readable) PDF or a scanned document, extracts key invoice fields using the Document Understanding pipeline, validates the extracted fields, and stores them in `Invoice_Output.xlsx`.
* **Key Features**:
  * **Check PDF Type (`Digital PDF? Yes / No`)**: Evaluates if `Invoice.pdf` contains machine-readable text (`Yes` → **Native PDF Extraction / Read PDF Text**; `No` → **OCR Extraction**). Includes a Demo Preview selector so you can test both branches interactively.
  * **Step: Document Understanding & Classify as Invoice**: Identifies the document taxonomy as `Invoice`.
  * **Step: Extract Fields (Sub-steps)**: Extracts all 4 required fields:
    * **Invoice Number**: `INV-1025`
    * **Vendor Name**: `ABC Technologies`
    * **Invoice Date**: `06-10-2026`
    * **Total Amount**: `₹25,500`
  * **Step: Validate & Write to Excel**: Validates non-empty fields, writes structured data to `Invoice_Output.xlsx`, and displays a complete **Demo Preview Message Box**.

---

### 6. Standard OCR Extractor (Task 1)
* **Directory**: [`StandardOCRExtractor/`](./StandardOCRExtractor/)
* **Workflow**: [`StandardOCRExtractor/StandardOCRExtractor.xaml`](./StandardOCRExtractor/StandardOCRExtractor.xaml) *(Custom entry point)*
* **Input**: [`Scanned_Notice.png`](./StandardOCRExtractor/Scanned_Notice.png) / [`Scanned_Document.pdf`](./StandardOCRExtractor/Scanned_Document.pdf)
* **Output**: [`OCR_Output.txt`](./StandardOCRExtractor/OCR_Output.txt)
* **Objective**: Reads a scanned document containing machine-printed text using an Optical Character Recognition (OCR) engine (`UiPath Screen OCR`), extracts the complete printed text, displays the extracted text in an interactive Message Box, and saves it into `OCR_Output.txt` for later use.
* **Key Features**:
  * **Interactive Document Selection (`ui:InputDialog`)**: Prompts user for document selection with full fallback defaults to `Scanned_Notice.png` or `Scanned_Document.pdf`.
  * **High-Accuracy OCR Extraction Engine**: Extracts complete machine-printed text streams with automatic character counting and validation.
  * **Text File Persistence (`ui:WriteTextFile`)**: Persists extracted text to `OCR_Output.txt` with UTF-8 encoding.
  * **Interactive Visual Alert (`ui:MessageBox`)**: Renders a complete visual preview of the extracted document text directly to the user.
  * **Diagnostic Telemetry (`ui:LogMessage`)**: Complete Info-level audit logs for all pipeline steps.

---

### 7. Handwritten Form ICR (Task 2: HandwrittenFormICR)
* **Directory**: [`HandwrittenFormICR/`](./HandwrittenFormICR/)
* **Workflow**: [`HandwrittenFormICR/Main.xaml`](./HandwrittenFormICR/Main.xaml) *(Custom entry point)*
* **Input**: [`Handwritten_Student_Form.png`](./HandwrittenFormICR/Handwritten_Student_Form.png) / [`Handwritten_Student_Form.pdf`](./HandwrittenFormICR/Handwritten_Student_Form.pdf)
* **Output**: [`Student_Information_Output.xlsx`](./HandwrittenFormICR/Student_Information_Output.xlsx) & [`Student_Information_Output.csv`](./HandwrittenFormICR/Student_Information_Output.csv)
* **Objective**: Processes a scanned handwritten student admission form, applies Intelligent Character Recognition (ICR) / Document Understanding to extract 5 key fields (`Student Name`, `USN`, `Department`, `Phone Number`, and `Email ID`), structures them in an in-memory `DataTable`, exports them into Excel, and displays a modal verification dialog.
* **Key Features**:
  * **Interactive Form Selector (`ui:InputDialog`)**: Accepts image or PDF handwritten student forms with default fallback.
  * **Intelligent Character Recognition (ICR)**: High-confidence extraction of cursive/printed handwriting.
  * **Relational Storage (`ui:BuildDataTable` & `ui:AddDataRow`)**: Encapsulates extracted values into a strongly typed `DataTable`.
  * **Dual Output Persistence**: Writes structured records directly to `Student_Information_Output.xlsx` and `.csv`.
  * **Structured Alert Dialog (`ui:MessageBox`)**: Displays an aligned summary of all extracted student fields.

---

### 8. Data Scraping - Book Catalog (Task 8: Lab3_BookScraper)
* **Directory**: [`Lab3_BookScraper/`](./Lab3_BookScraper/)
* **Workflow**: [`Lab3_BookScraper/Main.xaml`](./Lab3_BookScraper/Main.xaml) *(Table Extraction & Data Scraping)*
* **Target Web Portal**: [http://books.toscrape.com/](http://books.toscrape.com/)
* **Deliverables**:
  * Scraped Dataset: [`BookCatalog_Output.csv`](./Lab3_BookScraper/BookCatalog_Output.csv) (20 Books)
  * Output String Dump: [`dt_BookCatalog.txt`](./Lab3_BookScraper/dt_BookCatalog.txt)
  * Workflow & Variable Panel Screenshot: [`Screenshot1_Workflow_Variables.png`](./Lab3_BookScraper/Screenshot1_Workflow_Variables.png)
  * Output Panel & Message Box Screenshot: [`Screenshot2_OutputPanel_MessageBox.png`](./Lab3_BookScraper/Screenshot2_OutputPanel_MessageBox.png)
  * Submission Report with Q1-Q6 Written Answers: [`Lab3_BookScraper_Submission.md`](./Lab3_BookScraper/Lab3_BookScraper_Submission.md)
* **Objective**: Automates web data scraping from `http://books.toscrape.com/` using the **Table Extraction Wizard**, captures 20 book titles, prices, and stock statuses into a `System.Data.DataTable` variable (`dt_BookCatalog`), serializes the data with `ui:OutputDataTable`, and presents the result in both the Output Panel and a modal `ui:MessageBox`.
* **Key Features**:
  * **DOM Pattern Recognition**: Matches correlated HTML elements (`article.product_pod`, `h3 a`, `.price_color`, `.instock.availability`).
  * **Data Table Pipeline**: In-memory relational storage in `dt_BookCatalog` (`System.Data.DataTable`).
  * **String Conversion**: `Output Data Table` (`ui:OutputDataTable`) transforms tabular data into readable format.
  * **Dual Presentation**: Displays results via Info-level `ui:LogMessage` and interactive `ui:MessageBox`.

---

### 9. Control Flow Statements Suite (7 Projects)
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

### 10. Activity Library (BlankLibrary)
* **Directory**: [`BlankLibrary/`](./BlankLibrary/)
* **Type**: UiPath Activity Library (.nupkg)
* **Objective**: Encapsulates reusable modular automation activities and custom utilities that can be imported and consumed across multiple enterprise automation processes.

---

### 11. Enterprise Solution & REFramework
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
1. **Meaningful Workflow Names**: Default `Main.xaml` naming has been replaced across assignment workflows with descriptive file names (e.g. `AutomatedInvoiceProcessing.xaml`, `StudentExamEvaluator.xaml`, `If_PositiveNumber.xaml`, `Switch_MenuSelection.xaml`).
2. **Standard Variable Prefixes**:
   * `str_` : String variables (`str_InvoiceNumber`, `str_VendorName`, `str_StudentName`)
   * `int_` : 32-bit Integer variables (`int_Marks`, `int_TollFee`, `int_Counter`)
   * `arr_` : Array variables (`arr_Items`, `arr_Fruits`)
   * `bool_`: Boolean flags (`bool_IsDigitalPDF`, `bool_IsValid`)
3. **Comprehensive Diagnostic Logging**: Workflows utilize `ui:LogMessage` alongside visual `ui:MessageBox` alerts to ensure operational observability in unattended and attended runs.

---

## 📤 Google Drive & Submission Artifacts

All standalone `.xaml` workflows and ready-to-share `.zip` project bundles have been exported to the local desktop directory:
```
~/Desktop/UiPath_Share/
├── HRL_X_UiPath_All_Projects.zip      # 📦 ALL projects bundled in one master archive
├── AutomatedInvoiceProcessing.xaml    # 🧾 Task 3: Automated Invoice Processing workflow
├── AutomatedInvoiceProcessing_Project.zip
├── Invoice.pdf                        # Sample Input Invoice PDF
├── Invoice_Output.xlsx                # Extracted Output Excel File
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
> **Tip for Submission**: 
> - **All-in-One Master Bundle**: Download or share [`HRL_X_UiPath_All_Projects.zip`](https://github.com/hrlpavan/HRL-X-UiPath/raw/main/HRL_X_UiPath_All_Projects.zip) (includes all bots, libraries, and control flow workflows).
> - You can also drag and drop individual `.xaml` files or modular `.zip` archives directly into Google Drive to share with your professor or reviewer.

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

### Method C: One-Command Auto-Sync & Cross-OS Packaging (`uipath-sync`)
Whenever you add or modify a UiPath project, run this single command:
```bash
# Run globally from anywhere:
uipath-sync

# Or locally from the repository root:
./sync-uipath.sh
```
This automated engine automatically:
1. Validates all `project.json` manifests and `.xaml` files.
2. Normalizes relative workflow invocations (`\` $\rightarrow$ `/`) for 100% cross-OS compatibility (Windows, macOS, Linux).
3. Packages the clean, organized bundle into `UiPath_Version_3.0.zip` and syncs `HRL_X_UiPath_All_Projects.zip`.


---

## 👤 Author & Repository Information

* **Developer**: **Pavan Kumar Sadashiv** ([@hrlpavan](https://github.com/hrlpavan))
* **Organization**: **HRL**
* **Repository**: [https://github.com/hrlpavan/HRL-X-UiPath](https://github.com/hrlpavan/HRL-X-UiPath)
* **Automation Engineering**: Engineered with UiPath Studio, .NET, and Google Antigravity.

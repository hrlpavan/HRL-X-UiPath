# HRL X UiPath Autofile Organizer 🤖

Welcome to the **HRL X UiPath** repository. This workspace contains modern enterprise UiPath automation bots, reusable libraries, and solution packages engineered for agentic execution with **Google Antigravity** and **UiPath Studio**.

---

## 📁 Repository Structure

```
HRL-X-UiPath/
├── AutoFileOrganizer/                 # Auto File Organizer Bot
│   ├── Main.xaml                      # Main file sorting workflow
│   ├── project.json                   # UiPath project definition (Portable)
│   ├── Raw Downloads/                 # Source input directory
│   ├── PDF/                           # Output directory for .pdf documents
│   ├── Images/                        # Output directory for .jpg, .jpeg, .png
│   └── Excel/                         # Output directory for .xlsx spreadsheets
│
├── SmartNotepadGreeter/                # Smart Notepad Greeter Bot
│   ├── Main.xaml                      # Interactive user input & Notepad UI automation
│   └── project.json                   # Project metadata & UIAutomation dependencies
│
├── AutomaxTollBoothCalculator/        # Automax Toll Booth Calculator Bot
│   ├── Main.xaml                      # String evaluation logic, rate calculation & Notepad receipt
│   └── project.json                   # Project metadata & dependencies
│
├── StudentExamEvaluator/              # The Student Exam Evaluator Bot
│   ├── StudentExamEvaluator.xaml      # Core grading workflow (custom entry-point)
│   └── project.json                   # Configured with StudentExamEvaluator.xaml as main
│
├── BlankLibrary/                      # Reusable Custom Activities Library
│   ├── NewActivity.xaml               # Custom activity implementation
│   ├── project.json                   # Library project definition
│   └── AGENTS.md / CLAUDE.md          # Coding agent guidelines
│
└── Solution/                          # UiPath Solution Package
    ├── Solution.uipx                  # Packaged solution archive
    ├── resources/                     # Shared tenant resources & assets
    └── RoboticEnterpriseFramework/   # Production-grade REFramework implementation
        ├── Main.xaml                  # State machine workflow
        ├── Framework/                 # Init, GetTransactionData, Process, SetTransactionStatus
        ├── Data/                      # Config.xlsx, Inputs, Temp
        └── project.json               # REFramework project metadata
```

---

## 🚀 Projects Overview

### 1. Auto File Organizer Bot (`AutoFileOrganizer/`)
An autonomous file sorter that checks and creates required destination directories and routes incoming files from `Raw Downloads/` into designated categorical folders based on file extensions:
* **PDF Files (`.pdf`)** → Routed to `PDF/`
* **Image Files (`.jpg`, `.jpeg`, `.png`)** → Routed to `Images/`
* **Spreadsheets (`.xlsx`)** → Routed to `Excel/`

### 2. Smart Notepad Greeter (`SmartNotepadGreeter/`)
An interactive desktop UI automation workflow that:
* Prompts the user for their **Name** and **Age** via `ui:InputDialog`.
* Evaluates age limit (`int_Age >= 18`) using conditional logic to categorize the user as **'an Adult'** or **'a Minor'**.
* Launches **Notepad** via modern UI Automation (`uix:NApplicationCard`).
* Types a personalized greeting message into the text editor (`uix:NTypeInto`).
* Pauses with a clean delay and logs completion message.

### 3. Automax Toll Booth Calculator (`AutomaxTollBoothCalculator/`)
An intermediate string evaluation automation workflow that:
* Prompts the user for their vehicle type (`Car` / `Truck`) via `ui:InputDialog`.
* Evaluates case-insensitive equivalence using `str_VehicleType.ToLower() = "truck"`.
* Computes dynamic toll rate:
  * **Truck**: Rs. 100
  * **Car / Other**: Rs. 50
* Consolidates receipt string:
  ```text
  Vehicle: [str_VehicleType]
  Total Toll Due: Rs. [int_TollFee]
  ```
* Types the formatted receipt into a fresh instance of **Notepad** via `uix:NTypeInto`.
* Executes a 3-second delay, outputs to terminal log, and raises a completion Message Box.

### 4. The Student Exam Evaluator (`StudentExamEvaluator/`)
An advanced-basics evaluation bot configured with `StudentExamEvaluator.xaml`:
* Collects student name (`str_StudentName`) and score (`int_Marks`) via proctoring input dialogs.
* Streams diagnostic output via `ui:LogMessage`: `"Evaluating marks for " + str_StudentName`.
* Simulates background processing latency using a 2-second Delay.
* Executes conditional grading logic (`int_Marks >= 40`):
  * **True**: `str_Result = "PASSED"`
  * **False**: `str_Result = "FAILED"`
* Generates pop-up alert via `ui:MessageBox`:
  ```text
  Result for [str_StudentName]: [str_Result] (Score: [int_Marks]/100)
  ```

### 5. Activity Library (`BlankLibrary/`)
A modular UiPath Library project designed to package reusable workflows and custom activities for distribution across enterprise automation pipelines.

### 6. Enterprise Solution (`Solution/`)
An end-to-end automation solution encapsulating:
* **`Solution.uipx`**: Deployable solution manifest linking packages, processes, and tenant resources.
* **`RoboticEnterpriseFramework`**: Transactional state-machine architecture following UiPath best practices (Initialization, Transaction Processing, Exception Handling, and Logging).

---

## 🔗 Google Antigravity & UiPath CLI Integration

This repository is designed to interface with **Google Antigravity** using:
* **`uip` CLI**: Command-line orchestration for testing, building, and publishing automations.
* **UiPath MCP Server**: Integrated via stdio (`uip mcp serve`) for direct AI tool invocation.
* **UiPath Agent Skills**: Pre-trained domain skills (`uipath-rpa`, `uipath-agents`, `uipath-platform`, `uipath-solution`).

---

## 👤 Author
* **Pavan Kumar Sadashiv** ([@hrlpavan](https://github.com/hrlpavan))
* Organization: **HRL**

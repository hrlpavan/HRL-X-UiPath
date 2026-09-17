# HRL X UiPath 🤖⚡

Welcome to the **HRL X UiPath** repository. This workspace contains modern, cross-platform enterprise UiPath automation bots, reusable libraries, and solution packages engineered for agentic execution with **Google Antigravity** and **UiPath Studio**.

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

#### Running via UiPath CLI:
```bash
uip rpa run --file-path Main.xaml --project-dir ./AutoFileOrganizer
```

### 2. Activity Library (`BlankLibrary/`)
A modular UiPath Library project designed to package reusable workflows and custom activities for distribution across enterprise automation pipelines.

### 3. Enterprise Solution (`Solution/`)
An end-to-end automation solution encapsulating:
* **`Solution.uipx`**: Deployable solution manifest linking packages, processes, and tenant resources.
* **`RoboticEnterpriseFramework`**: Transactional state-machine architecture following UiPath best practices (Initialization, Transaction Processing, Exception Handling, and Logging).

---

## 🔗 Google Antigravity & UiPath CLI Integration

This repository is designed to interface with **Google Antigravity** using:
* **`uip` CLI**: Command-line orchestration for testing, building, and publishing automations.
* **UiPath MCP Server**: Integrated via stdio (`uip mcp serve`) for direct AI tool invocation.
* **UiPath Agent Skills**: Pre-trained domain skills (`uipath-rpa`, `uipath-agents`, `uipath-platform`, `uipath-solution`).

### CLI Commands Reference

```bash
# Validate project diagnostics
uip rpa validate --project-dir ./AutoFileOrganizer

# Compile and build
uip rpa build --project-dir ./AutoFileOrganizer

# Run workflow locally
uip rpa run --file-path Main.xaml --project-dir ./AutoFileOrganizer

# Pack into NuGet package
uip rpa pack --project-dir ./AutoFileOrganizer
```

---

## 👤 Author
* **Pavan Kumar Sadashiv** ([@hrlpavan](https://github.com/hrlpavan))
* Organization: **HRL**

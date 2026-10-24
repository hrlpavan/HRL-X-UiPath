# Task 16: Customer Support Chatbot Using Google Dialogflow 🤖💬

**Agent Name**: `BankSupportBot`  
**Domain**: Banking Customer Support  
**Platform**: Google Dialogflow ES / CX & UiPath Conversational Automation  
**Deliverable Package**: [`BankSupportBot_Dialogflow_Export.zip`](./BankSupportBot_Dialogflow_Export.zip)  

---

## 📌 Problem Statement & Objective
A commercial bank aims to modernize its client communication channels by deploying an intelligent conversational AI chatbot (**BankSupportBot**) built with Google Dialogflow. The virtual assistant answers inquiries regarding:
1. **Account Balances** (`CheckBalance`)
2. **Funds Transfers** (`TransferMoney`) with automated entity extraction of transfer amounts via `@sys.number`
3. **Branch Working Hours** (`WorkingHours`)

---

## 🛠️ Step-by-Step Dialogflow Console Setup Guide

### Step 1: Create the Agent
1. Navigate to the [Google Dialogflow Console](https://dialogflow.cloud.google.com/).
2. Click **Create Agent** in the left menu.
3. Set **Agent Name**: `BankSupportBot`.
4. Set **Default Language**: `en - English`.
5. Set **Default Time Zone**: `(GMT+5:30) India Standard Time (Asia/Kolkata)`.
6. Click **Create**.

### Step 2: One-Click Import from ZIP (Restoration)
1. In the left navigation pane, click the **Settings ⚙️** gear icon next to `BankSupportBot`.
2. Click on the **Export and Import** tab.
3. Select **Restore from ZIP** (or *Import from ZIP*).
4. Choose the bundled package: [`BankSupportBot_Dialogflow_Export.zip`](./BankSupportBot_Dialogflow_Export.zip).
5. Type `RESTORE` in the confirmation box and click **Restore**.
6. The entire taxonomy—including all 3 required intents, training phrases, parameters, and responses—is restored instantly!

---

## 🧠 Intents & Entity Configuration Specifications

### 1. `CheckBalance` Intent
* **Intent Name**: `CheckBalance`
* **Action**: `check.balance`
* **Training Phrases**:
  * *"What is my account balance?"*
  * *"How much money do I have?"*
  * *"Check my balance"*
  * *"Show my account balance"*
  * *"What is my bank balance?"*
* **Configured Response**:
  > *"Your current savings account balance is ₹45,250.00 as of today."*

---

### 2. `TransferMoney` Intent (With Entity Extraction)
* **Intent Name**: `TransferMoney`
* **Action**: `transfer.money`
* **Parameter & Entity Mapping**:
  | Parameter Name | Entity Type | Value Reference | Mandatory | Prompt Question |
  |---|---|---|---|---|
  | `amount` | `@sys.number` | `$amount` | Yes | *"Please enter the amount you want to transfer."* |
* **Training Phrases (with `@sys.number` entity highlighting)**:
  * *"I want to transfer money"*
  * *"Transfer ₹@sys.number:amount[2000]"*
  * *"Transfer @sys.number:amount[5000] to my friend"*
  * *"Send @sys.number:amount[1000] rupees"*
  * *"Transfer @sys.number:amount[2,000]"*
* **Configured Response**:
  > *"I have initiated the transfer of ₹$amount. Please confirm the recipient's details to proceed."*

---

### 3. `WorkingHours` Intent
* **Intent Name**: `WorkingHours`
* **Action**: `check.hours`
* **Training Phrases**:
  * *"What are your working hours?"*
  * *"When is the bank open?"*
  * *"What are the branch working hours?"*
  * *"Are you open on Saturdays?"*
  * *"What are the bank timings?"*
* **Configured Response**:
  > *"Our branch working hours are Monday to Friday from 9:30 AM to 4:30 PM, and on working Saturdays from 9:30 AM to 1:30 PM. Net banking and ATM services are available 24/7."*

---

## 🧪 Comprehensive Testing & Verification Results

The agent was tested with distinct customer sentences across all target scenarios:

| # | User Test Input | Predicted Intent | Extracted Entity (`@sys.number`) | Chatbot Response | Status |
|---|---|---|:---:|---|:---:|
| **1** | *"What is my account balance?"* | `CheckBalance` | `N/A` | *"Your current savings account balance is ₹45,250.00 as of today."* | ✅ **MATCH** |
| **2** | *"Transfer ₹2,000."* | `TransferMoney` | `2000` | *"I have initiated the transfer of ₹2000. Please confirm the recipient's details to proceed."* | ✅ **MATCH** |
| **3** | *"What are your working hours?"* | `WorkingHours` | `N/A` | *"Our branch working hours are Monday to Friday from 9:30 AM to 4:30 PM..."* | ✅ **MATCH** |
| **4** | *"How much money do I have?"* | `CheckBalance` | `N/A` | *"Your current savings account balance is ₹45,250.00 as of today."* | ✅ **MATCH** |
| **5** | *"When is the bank open?"* | `WorkingHours` | `N/A` | *"Our branch working hours are Monday to Friday from 9:30 AM to 4:30 PM..."* | ✅ **MATCH** |

---

## 📂 Project Deliverables Summary
* **Dialogflow Agent JSONs**: [`dialogflow_agent/`](./dialogflow_agent/)
* **One-Click Import Archive**: [`BankSupportBot_Dialogflow_Export.zip`](./BankSupportBot_Dialogflow_Export.zip)
* **UiPath Test Automation Workflow**: [`Main.xaml`](./Main.xaml)
* **Testing Log Report**: [`Chatbot_Testing_Results.txt`](./Chatbot_Testing_Results.txt)
* **Tabular Datasets**: [`Chatbot_Testing_Results.csv`](./Chatbot_Testing_Results.csv) & [`Chatbot_Testing_Results.xlsx`](./Chatbot_Testing_Results.xlsx)

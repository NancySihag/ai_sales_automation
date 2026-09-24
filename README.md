# 🚀 AI Sales Automation & Financial Impact Engine

A Python-based sales automation and business analysis application that demonstrates how AI-style workflow analysis can identify operational bottlenecks, estimate automation opportunities, and calculate potential financial impact.

The project combines a Python backend engine with an interactive Streamlit dashboard to simulate an end-to-end business automation workflow.

> **Note:** This is a portfolio demonstration using simulated business data and configurable assumptions. The financial figures are estimates, not actual customer results or financial guarantees.

---

## 🌐 Live Demo

**Live Demo:** [Open the AI Sales Automation Dashboard](http://localhost:8501)

---

## 📌 Project Overview

Businesses often spend significant time on repetitive manual workflows.

This project demonstrates a workflow where business data is analyzed to identify:

- Operational bottlenecks
- Affected team size
- Estimated workload
- Potential automation rate
- Monthly hours that could be recovered
- Estimated monthly labor value
- Annualized financial impact
- Recommended automation strategy

The application turns these inputs into an interactive business-impact dashboard and downloadable executive report.

---

## ✨ Key Features

### 📊 Business Workflow Analysis

- Industry-based target selection
- Simulated business registry
- Operational bottleneck identification
- Affected workforce analysis

### 🤖 Automation Opportunity Analysis

- Configurable weekly hours lost
- Adjustable automation rate
- Estimated monthly workload
- Estimated recoverable hours
- Before/after workload comparison

### 💰 Financial Impact Modeling

The engine calculates:

- Monthly hours lost
- Hours recovered
- Monthly labor value
- Annualized financial impact

### 🧠 Executive Recommendation Engine

Generates an AI-style executive recommendation based on the selected automation rate.

The recommendation can suggest:

- Automation evaluation
- Phased automation
- Targeted workflow assessment

### 📄 Downloadable Executive Report

Users can generate and download a text-based executive analysis containing:

- Organization information
- Operational bottleneck
- Automation opportunity
- Financial impact
- Recommended action
- Business assumptions
- Disclaimer

### 🛡️ Input Validation

The backend validates:

- Negative headcount
- Negative hourly wage
- Negative workload assumptions
- Invalid automation rates

Invalid inputs raise clear `ValueError` exceptions.

### 🧪 Automated Testing

The backend includes automated tests covering:

- Industry pipeline filtering
- ROI calculations
- Zero automation
- Full automation
- Negative headcount
- Negative wage
- Invalid automation rate
- Executive recommendation generation

Current test status:

**8/8 tests passing**

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Dashboard
  │
  ├── Industry Selection
  ├── Business Assumptions
  ├── Automation Rate
  │
  ▼
AI Sales Automation Engine
  │
  ├── Target Registry
  ├── Workflow Analysis
  ├── ROI Calculation
  ├── Validation
  └── Executive Recommendation
  │
  ▼
Business Impact Dashboard
  │
  ├── Hours Recovered
  ├── Automation Potential
  ├── Monthly Impact
  └── Annualized Impact
  │
  ▼
Downloadable Executive Report

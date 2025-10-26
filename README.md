# 🧹 Cyber Hygiene Checklist Tool (v1.0)

A Python-based tool that performs basic **cyber hygiene and security checks** on your local system.  
Built with the goal of demonstrating real-world **cybersecurity automation**, **Python scripting**, and **OS command** interaction skills.

---

## 🔍 Overview

This tool automates several essential cybersecurity hygiene checks that professionals use to assess system security posture.

It checks:
- 🔐 **System Security:** Firewall and OS version checks  
- 🌐 **Network Configuration:** Hostname, IP, and open port listing  
- 🧩 **File Hygiene:** Scans for files with insecure keywords (e.g., `password`, `key`, `secret`)  
- 🧾 **Report Generation:** Outputs structured results in JSON format

---

## 🧰 Tech Stack

| Area | Technology |
|------|-------------|
| Language | Python 3 |
| Libraries | psutil, os, subprocess, platform |
| Environment | VS Code / CLI |
| OS Support | Windows, Linux (partial) |

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/VoidCodes-ux/cyber-hygiene-checklist-tool.git

cd cyber-hygiene-checklist-tool

# (Optional) Install psutil for advanced system checks
pip install psutil

# Run the tool from your terminal
python main.py --output reports/report.json

|The generated JSON report will be saved inside the /reports folder
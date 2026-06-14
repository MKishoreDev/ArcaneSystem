# Arcane System

<p align="center">
  <b>Telegram's Community Intelligence & Enforcement System</b>
  <br>
  Built for large communities, moderation teams, and public groups.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue">
  <img src="https://img.shields.io/badge/Pyrogram-Latest-green">
  <img src="https://img.shields.io/badge/MongoDB-Database-success">
  <img src="https://img.shields.io/badge/Status-Archived-red">
</p>

---

# ⚠️ Archive Notice

This repository contains the original **Arcane System** source code developed between **2022–2024**.

The project is no longer actively maintained and is preserved for historical, educational, and archival purposes.

Many ideas introduced in Arcane System later influenced moderation systems used across multiple Telegram communities.

---

# About

Arcane System was an experimental moderation and enforcement framework built for Telegram communities.

The project was originally inspired by the **Sibyl System** from the anime series Psycho-Pass — a fictional intelligence network capable of monitoring threats and maintaining public order.

While Arcane System was never intended to replicate the anime's concept literally, it borrowed the idea of centralized intelligence, automated enforcement, and community safety.

Instead of relying on traditional Telegram admin workflows, Arcane System introduced a structured moderation hierarchy and automated tools to help communities manage abuse, spam, and malicious actors at scale.

---

# Why Arcane System Was Created

Back in 2022, Telegram moderation tools were limited.

Most communities relied on:

* Manual moderation
* Basic anti-spam bots
* Fragmented admin tools
* No centralized reporting system
* No staff hierarchy
* Poor moderation analytics

Arcane System was created to solve those problems by providing a unified moderation ecosystem.

---

# Core Features

## Enforcement Framework

* Global enforcement actions
* User watchlists
* Staff investigation tools
* Escalation system
* Enforcement history tracking

## Inspector System

Inspectors were responsible for:

* Reviewing reports
* Investigating suspicious users
* Collecting evidence
* Forwarding cases to Enforcers

## Enforcer System

Enforcers had authority to:

* Issue punishments
* Remove malicious users
* Execute global actions
* Maintain community safety

## Reporting System

* User reports
* Evidence collection
* Case tracking
* Staff notifications

## Anti-Spam Protection

* Flood detection
* Automated actions
* Suspicious account detection
* Link filtering
* Pattern matching

## Logging System

* Administrative actions
* Enforcement records
* Report logs
* Audit trails

## Database Infrastructure

Powered by MongoDB:

* User records
* Staff records
* Enforcement history
* Report archives
* Configuration storage

## Utility Modules

* Group management tools
* Administrative utilities
* Moderation helpers
* Automated workflows

---

# Technology Stack

| Component          | Technology |
| ------------------ | ---------- |
| Language           | Python     |
| Telegram Framework | Pyrogram   |
| Database           | MongoDB    |
| Async Driver       | Motor      |
| API Library        | TgCrypto   |
| HTTP Client        | AioHTTP    |

---

# Project Structure

```text
Arcane/
│
├── plugins/
│   ├── add.py
│   ├── bots.py
│   ├── inspectors.py
│   ├── enforcers.py
│   ├── reports.py
│   └── moderation/
│
├── utils/
│   ├── db.py
│   ├── dbfunctions.py
│   ├── helpers.py
│   └── security.py
│
├── buttons.py
├── media.py
├── strings.py
├── ranks.py
└── __main__.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/MKishoreDev/ArcaneSystem.git
cd ArcaneSystem
```

## Install Requirements

```bash
pip install -r requirements.txt
```

## Configure Variables

```python
API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

MONGO_URI = ""

DEVS = []

INSPECTOR = []

ENFORCER = []

KAWAII_LOGS = -100xxxxxxxxxx
KAWAII_CHANNEL = -100xxxxxxxxxx
```

## Run

```bash
python -m Arcane
```

# Legacy

Arcane System represents one of the early attempts to create a structured moderation ecosystem for Telegram communities.

Although development has ended, the project remains an important milestone in our journey as developers and community builders.

---

# Contributors

<table>
<tr>

<td align="center">
<a href="https://github.com/MKishoreDev">
<img src="https://github.com/MKishoreDev.png" width="120px">
<br>
<b>MKishoreDev</b>
</a>
<br>
Founder • Lead Developer
</td>

<td align="center">
<a href="https://github.com/Thiruxd">
<img src="https://github.com/Thiruxd.png" width="120px">
<br>
<b>Thiruxd</b>
</a>
<br>
Founder • Lead Developer
</td>

<td align="center">
<a href="https://github.com/nandhxd">
<img src="https://github.com/nandhxd.png" width="120px">
<br>
<b>nandhxd</b>
</a>
<br>
Core Developer
</td>

</tr>
</table>

---

# Credits

* Pyrogram Team
* MongoDB Team
* Open Source Community
* Every moderator, tester, and contributor who helped shape Arcane System

---

# License

MIT License

---

<p align="center">
Built during the Telegram era of 2022.
<br>
Archived for history.
</p>

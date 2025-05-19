
---

# 🧠 Bootcamp Project Portfolio – Developer Learning Journey

Welcome to the official documentation of my **Bootcamp Journey**, where I explored and built practical solutions across essential areas of backend development, developer tooling, text processing, and data engineering. This bootcamp emphasized *hands-on learning*, *modular system design*, and *production readiness*.

---

## 📁 Project Structure

The bootcamp is organized into the following core modules:

1. [`tools`](#1-tools)
2. [`basics`](#2-basics)
3. [`doctools`](#3-doctools)
4. [`language-drills`](#4-language-drills)
5. [`dataflow-framework`](#5-dataflow-framework)
6. [`persistence-drills`](#6-persistence-drills)
7. [`figure-captions-extraction`](#7-figure-captions-extraction)

---

## 1. 🛠️ Tools

### ✅ What I Did:

* Explored developer tools and utilities for productivity, including command-line operations, scripting, and file manipulations.
* Practiced using Git efficiently with branching, merging, and PR workflows.
* Created basic automation scripts to enhance workflow reproducibility.

### 💡 What I Learned:

* Mastered Git workflows (e.g., rebase, stash, cherry-pick).
* Developed proficiency in shell scripting for task automation.
* Understood the importance of toolchains in developer environments.

---

## 2. 📦 Basics

### ✅ What I Did:

* Built foundational scripts to process files, handle inputs, and perform string operations.
* Developed simple parsers and output generators.
* Focused on code readability, structure, and versioning.

### 💡 What I Learned:

* Reinforced core programming concepts: conditionals, loops, file I/O, functions.
* Learned how to write maintainable, modular, and testable code.
* Understood how to structure a small codebase professionally.

---

## 3. 📝 Doctools

### ✅ What I Did:

* Created documentation and developer tooling to generate or parse structured text.
* Worked on markdown processors, document transformers, and auto-indexing utilities.

### 💡 What I Learned:

* Understood the role of documentation in production systems.
* Implemented document parsing and transformation pipelines.
* Designed CLI tools to generate summaries and document navigation aids.

---

## 4. 🧠 Language Drills

### ✅ What I Did:

* Built modules that focus on natural language understanding and manipulation.
* Developed simple tools for tokenization, lemmatization, and syntax handling.
* Practiced grammar analysis and text transformation logic.

### 💡 What I Learned:

* Gained insight into language parsing fundamentals.
* Understood how to manipulate raw text using regex, token rules, and data models.
* Learned about syntax trees and simple rule-based transformation systems.

---

## 5. 🔁 Dataflow Framework

### ✅ What I Did:

* Incrementally built a line-processing engine from scratch, evolving it through multiple abstraction levels:

  * From a simple line reader (Level 0)
  * To a fully dynamic, config-driven, stateful streaming system (Level 8)
* Created a DAG-based pipeline capable of routing and transforming real-time file input.

### 💡 What I Learned:

* How to design for scalability and modularity.
* Implemented a fully **configurable**, **observable**, and **fault-tolerant** data processing framework.
* Understood software evolution from scripts to structured systems.

---

## 6. 💾 Persistence Drills

### ✅ What I Did:

* Explored persistence methods including flat files, JSON, SQLite, and DuckDB.
* Built code to abstract storage mechanisms from logic.
* Implemented simple interfaces for reading, writing, and querying persistent data.

### 💡 What I Learned:

* Core concepts of storage models: row vs column stores, in-memory vs on-disk.
* Practical experience with **DuckDB**, a modern embedded analytical database.
* Designed pluggable persistence layers that decouple storage logic.

---

## 7. 🖼️ Figure Captions Extraction System

### ✅ What I Did:

* Developed a production-ready system for extracting **figure captions** and related metadata from scientific publications using PubMed APIs.
* Built features to:

  * Fetch paper structure using the [BioC PMC API](https://www.ncbi.nlm.nih.gov/research/bionlp/APIs/BioC-PMC/)
  * Extract entities from figure captions using [PubTator API](https://www.ncbi.nlm.nih.gov/research/pubtator3/api)
  * Persist data to DuckDB and expose a secure REST API for querying
* Included CLI, batch ingestion, folder watching, and Docker-based deployment support.

### 💡 What I Learned:

* How to build a **modular extraction pipeline** for scientific documents.
* Integrated multiple third-party APIs and structured the ingestion flow.
* Designed and implemented:

  * Secure REST APIs (API-key protected)
  * Config-driven ingestion jobs
  * Monitoring and logging for production visibility
* Learned how to write **clean, production-ready code** with extensibility in mind.

---

## 🚀 Skills Gained

| Category        | Skills                                                       |
| --------------- | ------------------------------------------------------------ |
| Programming     | Python, Bash, Regex, CLI Tools                               |
| API & Web       | REST APIs, Auth, HTTP clients, JSON/CSV data formats         |
| Storage         | DuckDB, SQLite, file-based storage                           |
| Architecture    | Modular system design, config-driven flows, DAGs             |
| Deployment      | Docker, Makefile, environment configs                        |
| Data Processing | Text parsing, streaming, batch processing, stateful routing  |
| Dev Practices   | Logging, testing, CLI design, documentation, version control |

---

## 📘 How to Use This Repository

Each folder is independently runnable and includes a `README.md` with setup and execution instructions. Start from simpler modules like `basics/` and follow through to more complex ones like `figure-captions-extraction/`.

To deploy any project:

```bash
# Build and run Docker (where applicable)
docker build -t <project> .
docker run <project>
```

For help:

```bash
python <script>.py --help
```

---

## 📌 Final Note

This bootcamp provided an in-depth, hands-on journey through backend development, data extraction, and system design. Each module built upon the previous, allowing me to develop confidence in building real-world systems with clarity, modularity, and long-term maintainability.

---


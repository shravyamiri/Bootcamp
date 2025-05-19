## 🗓️ Daily Log 

### ✅ Tools

#### 🔧 GitHub Setup
- Created a GitHub account and initialized a **monorepo named `bootcamp`**.
- Learned how to manage repositories using Git and GitHub.
- Understood the importance of publishing all work and maintaining traceability.

#### ☁️ Server Setup
- Set up a **Linux cloud server** (e.g., Azure VM via GitHub Student Pack).
- Learned about free DNS providers (e.g., `afraid.org`) for custom domains.
- Deployed a basic **web server** with my name and photo as proof of setup.
- Gained hands-on experience with public hosting and server access.

#### 🐳 Docker Basics
- Installed Docker on the server.
- Pulled a base **Python Docker image** from Docker Hub.
- Ran a test Python "Hello, World!" program inside Docker container.

#### 🖥️ Client Setup
- Configured **SSH keys** for:
  - GitHub push/pull without password.
  - Secure login into the cloud server.
- Learned how to use **`rsync`** for file transfer between local machine and server.

#### 🧰 IDE Recommendations
- Compared **PyCharm Community** vs **VSCode** for Python development.
- Understood limitations of LLM plugins (like Copilot) in IDEs currently.

#### 🤖 LLM Usage
- Chose ChatGPT, Claude, or Gemini as reliable LLM assistants.
- Learned the importance of **prompting effectively**, **validating output**, and **manually testing code**.

#### 🐍 Python Setup with `uv`
- Installed multiple Python versions: **3.13 (latest)** and **3.11 (stable)**.
- Used `uv` to:
  - Manage virtual environments.
  - Create a virtual environment named `bootcamp` in Python 3.13.
- Understood `uv` as the **recommended modern Python package manager**.

#### 🖥️ CLI Demo Tools
- Explored **Asciinema** for recording CLI demonstrations.
- Plan to use Asciinema links in future project `README.md` files for showcasing scripts and tools.

#### 📚 Further Reading
- Researched `uv` ecosystem, learned how it streamlines Python packaging and environment setup.
- Investigated best plugins for VSCode to support static typing and refactoring with Python.

---

### 🧠 Key Takeaways

- Set up GitHub, cloud server, Docker, and Python environments from scratch.
- Learned about SSH, rsync, web deployment, and modern dev tools.
- Gained foundational knowledge to run Python applications in containerized and remote environments.


---



#### 📅 Basics

---

### ✅ Tasks Completed:

####  **Project & Environment Setup**

* Initialized a Python project using `uv init`.
* Created and activated a virtual environment using `uv venv`.
* Configured my IDE (PyCharm/VSCode) to use the created virtual environment.
* Installed and used `uv` to manage dependencies and Python versions (Python 3.13 and 3.11).

#### **Basic Application Setup (`ex-basics-1`)**

* Created a module named `shravya-hello`.
* Wrote a function that prints "Hello, <name>" or defaults to "Hello, World!".
* Published the package on **TestPyPI** and added the link to the `README.md`.
* Enhanced the `README.md` for a clean, informative package page.

####  **Using External Libraries (`ex-basics-2`)**

* Installed the `rich` library using `uv`.
* Integrated `rich` to display colorful and formatted output.

####  **CLI Application (`ex-basics-3`)**

* Installed the `typer` module.
* Built a CLI application using `typer`.
* Configured `pyproject.toml` to expose the CLI on installation.
* Tested and demoed the CLI tool using `asciinema`.

####  **Typing & IDE Proficiency Drills**

* Practiced writing functions with proper **type annotations**.
* Explored **Optional**, **Union**, **Callable**, **TypedDict**, and **Any** types.
* Created and tested small applications to:

  * Catch type mismatches using IDE static analysis.
  * Use linting to clean up and format code.
  * Perform **code refactoring** like moving functions and renaming variables.
  * Use **navigation** and **auto-imports** features in IDE.
  * Write and view **docstrings** in the IDE.
  * Manage modules using `uv` and validate project structure.

---

### 📚 What I Learned:

####  Python Code Guidelines

* Importance of **type annotations** for readability and tooling support.
* Best practices for function size (≤ 25 lines), modular design, and clean naming.
* Managing configuration using `.env`, YAML, or a constants module instead of hardcoded values.
* Writing meaningful `docstrings` and using specific exceptions for better error handling.

####  Tools & Ecosystem

* Gained confidence using `uv` for Python project management, dependencies, and virtual environments.
* Published a Python package to **TestPyPI** and learned the packaging flow.
* Used **rich** for elegant terminal output and **typer** to build a CLI.
* Used `asciinema` to demo CLI applications, an efficient tool for CLI-based project showcases.

####  IDE Skills Improved

* Understood how to enable and use **linting**, **type checking**, and **auto-refactoring** in IDE.
* Practiced **moving code**, **navigating definitions**, and **auto-fixing suggestions**.
* Learned how to make the IDE recognize and properly use `uv` environments.
* Explored typing drills to become more comfortable with Python’s static typing.

---

> ✅ **Progress Summary:** Completed setup of development environment, published my first Python CLI package, and practiced Python typing, IDE features, and CLI packaging. Confident in proceeding with application development using clean code principles and tools like `uv`, `rich`, `typer`, and TestPyPI.

---

Here's an example `dailylog.md` entry based on your completion of the **Developer Documentation: Tools & Best Practices** training. You can copy and extend this daily log as you go through the training over multiple days:

---

### `dailylog.md`

#### 📅 Doctools


---

#### ✅ **What I Did**

* **Markdown Essentials**

  * Created a **Markdown Cheatsheet** with examples of headings, links, lists, code blocks, tables, and images.
  * Wrote a detailed **README.md** for a small Python project including install steps, usage, and troubleshooting.
  * Started maintaining this `dailylog.md` inside the monorepo.

* **Visual Thinking Tools**

  * Used **Mermaid.js** to create a **sequence diagram** for a login flow (user → frontend → backend → DB).
  * Designed a **block diagram** of a 3-tier architecture using **Draw\.io** (Client, API, DB) and exported it as PNG/SVG.
  * Created a **mind map in XMind** outlining sections of a design document: problem, goals, non-goals, options, risks.

* **MkDocs Setup**

  * Installed **MkDocs** and the **Material theme**.
  * Created a basic project structure with `docs/`, `mkdocs.yml`, and 3 content pages.
  * Verified `mkdocs serve` worked and added navigation structure, diagrams, and search functionality.

* **Collaboration with Google Docs**

  * Collaborated on a **feature proposal doc** with a peer. Added review comments, resolved suggestions, and exported it to Markdown.

* **GitHub Docs Structure**

  * Set up a sample repo with:

    * `README.md` explaining setup and usage.
    * `docs/` folder with architecture and developer guides.
    * Internal links across docs, verified no dead ends.

* **System Design Docs**

  * Wrote a one-pager **design doc** with problem statement, goals, trade-offs, and risks.
  * Created an **architecture doc** explaining system components, data flows, and constraints.
  * Produced a **system map diagram** using both Mermaid and Draw\.io.

* **Capstone**

  * Used MkDocs to publish all documentation as a **live documentation site**.
  * Verified that someone could understand and onboard into the project using only the published documentation.

---

####  **What I Learned**

* How to use **Markdown** effectively to create readable and professional developer documents.
* Importance of using **README.md** not just for setup, but also for explaining the "why" of a project.
* How to make technical flows **visual** with tools like Mermaid and Draw\.io.
* Why **mind maps and design documents** help clarify thinking before coding.
* How to install and configure **MkDocs + Material Theme** to create a beautiful documentation site.
* Writing documentation as an **iterative process** — starting simple, then improving structure and clarity.
* Using **visual + written** formats together increases clarity and speeds up onboarding.
* Importance of linking documentation with code (versioned together), and maintaining clean structure across folders.
* Practiced writing for other developers — not just for myself.
* Learned to **self-review** documentation using criteria like clarity, structure, usefulness, and navigability.

---

>  **Reflection**:
> Before this, I underestimated how powerful good documentation is. After going through this, I realize it’s not just a side-task — it’s core to good engineering. Writing docs also forced me to think deeply about the systems I build.

---

 Python Drills
Dsection1 – Core Python Proficiency
What I did:

Built helloworld module with say_hello(name) function.

Created a CLI using typer that calls this function.

Published to test PyPI.

What I used:

typer

setuptools, pyproject.toml, twine, dev-pypi

What I learned:

Modular structure helps with packaging.

Typer makes CLI creation intuitive with automatic help docs.

Publishing to dev-pypi helped test packaging end-to-end.

section 2 – Reusability + Config
What I did:

Created a new many-hellos CLI that imports from helloworld.

Added support for _config.yaml to set num_times for greetings.

Wrote config loader that checks: current directory → CONFIG_PATH → default file.

What I used:

yaml for config

os.environ, pathlib

Typer for CLI reuse

What I learned:

Keeping config separate from logic improves flexibility.

Layered config loading (cwd > env > fallback) is a useful pattern.

Importing code across projects improves reusability.

section 3 – Logging & Selective Debugging
What I did:

Added logging to both say_hello and config loader.

Enabled/disabled logging via CLI in many-hellos.

Selectively turned on logging for config only.

What I used:

Python logging module

Custom logger setup (__name__ scoped)

CLI flags to toggle debug mode

What I learned:

Logging is better than print for production tools.

Scoped loggers allow selective output — useful for debugging.

Good logging improves observability during CLI execution.

section 4,5,6 – Idioms, Object-Oriented, Functional
What I did:

Practiced Pythonic idioms like unpacking, list comprehensions, and context managers.

Refactored hello module to use OOP (HelloGreeter class with strategy pattern).

Used functools.partial and map for functional variations.

What I used:

with, enumerate, zip, partial, filter

OOP principles (encapsulation, abstraction)

What I learned:

Python has elegant, readable idioms — leverage them.

Combining OOP + functional leads to clean designs.

Small helpers (partial, lambda, etc.) simplify repetitive logic.

section 7 – Packaging + Validation
What I did:

Added input validation to CLI using pydantic.

Packaged the CLI tools as Python distributions.

Added test cases using pytest.

What I used:

pydantic for argument validation

setuptools and pyproject.toml

pytest for testing

What I learned:

Pydantic makes runtime validation easy and safe.

Tests make it easier to refactor confidently.

Publishing + testing completes the software loop.

-------------------------------------------------------------------------------------------------------------------------------------------------------

📅 Abstraction Through Streaming Line Processing
✅ What I Did
Started from a basic script that reads and processes a text file line by line (Level 0).

Gradually enhanced the script through multiple abstraction levels, creating folders like abstraction-level-1, abstraction-level-2, etc.

Added CLI support to allow dynamic input parameters (Level 1).

Refactored code into a modular structure with reusable components for line reading, processing, and output writing (Level 2).

Introduced config-driven pipelines where transformations are no longer hardcoded but read from external configs (Level 3).

Implemented streaming logic and state handling for real-time data processing (Level 4).

Built dynamic DAG-based routing, allowing different flows based on data or logic conditions (Level 5).

Added a state-based routing system where routing decisions depend on past inputs and maintained states (Level 6).

Introduced observability features, like debug logging, metrics, and internal state inspection (Level 7).

Developed an automated folder watcher to detect new files, recover from failures, and auto-restart interrupted jobs (Level 8).

Finalized the project into a real-time file processing system that is configurable, fault-tolerant, testable, and extensible.

📚 What I Learned
How to build software incrementally, starting from a script and evolving into a production-grade, modular system.

Importance of abstraction and separation of concerns — decoupling logic from configuration makes the system reusable and easier to maintain.

Gained experience in designing CLI tools and using libraries like argparse or typer for command-line interfaces.

Learned how to externalize logic using configs, enabling dynamic behavior without code changes.

Understood stream processing concepts — how to process unbounded data line-by-line in real-time scenarios.

Applied Directed Acyclic Graph (DAG) routing for flexible control flows in data processing pipelines.

Implemented stateful processing and routing, where current decisions depend on past inputs or context.

Learned about observability — adding logging, counters, and traceability features to make systems debuggable and monitorable.

Built an automated file watcher with recovery, enabling the system to process files as they arrive and restart from failures.

Overall, learned how to design for change, modularize systems, and handle complexity using clean architecture principles.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Persistence  Drills
This project is a comprehensive hands-on journey through data persistence in Python, covering both file-based serialization and relational database storage using SQLite and SQLAlchemy.

✅ What I Did
🔸 File-Based Persistence
Implemented serialization and deserialization of objects using:

Pickle: Binary serialization for Python objects.

JSON: Human-readable format for lightweight data exchange.

YAML: Flexible, readable serialization format.

Built custom serialization logic for:

Complex/nested objects

Cyclic references

Versioned objects

Custom collection types

Designed save/load mechanisms for application state and user data.

🔸 Database Persistence with SQLite
Created relational tables and performed CRUD operations manually using SQLite.

Wrote SQL queries for data manipulation and retrieval.

Normalized tables and established relationships using foreign keys.

🔸 ORM with SQLAlchemy
Defined models and schemas using declarative base.

Performed CRUD operations through ORM.

Implemented relationships (one-to-many, many-to-many).

Handled transactions and rollbacks.

Performed batch inserts and complex queries using SQLAlchemy.

🔸 Real-World Scenarios
Simulated mini-projects like:

Inventory and order tracking

Student grading system

Bookstore database

Flight reservation system

Used sessions, schema migrations, and exception handling.

📚 What I Learned
🧩 Serialization Techniques: How to persist Python objects using multiple formats and ensure compatibility, performance, and security.

🔄 Custom Serialization Logic: Managing complex object structures and handling special cases like cyclic references.

🛢️ Relational Databases: Schema design, normalization, indexing, and SQL operations in SQLite.

🧱 SQLAlchemy ORM: Translating Python objects to database tables, and managing relationships and sessions cleanly.

🔁 Transactions and Data Integrity: Ensuring atomicity and consistency using transactions and rollback mechanisms.

🛠️ Problem Solving with Persistence: Designing scalable solutions for real-world applications using persistent storage.

🛠️ Tech Stack
Python 3.x

SQLite

SQLAlchemy

Pickle, JSON, YAML
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Figure Caption Extraction and Access System
✅ What I Did
Studied the requirements and scope of the system including user roles: User, Admin, and Ops.

Explored the BioC-PMC API to understand how to retrieve paper structure (title, abstract, figure captions, URLs).

Investigated PubTator API to extract named biological entities (like genes) from figure captions.

Outlined the system architecture, ensuring modularity for future data sources beyond PubMed Central.

Planned out:

Ingestion pipeline for PMC/PMID IDs

REST API endpoints for querying and uploading

CLI interface for local and batch data submission

DuckDB as default local storage

Drafted the design document including:

Components and interactions

Justified use of DuckDB for fast local analytics

Initial thoughts on scalability and modularity

Listed required tools and technologies (Python, FastAPI, DuckDB, Docker, BioC API, PubTator, SQLModel/Pydantic).

Began writing the ingestion pipeline to extract and persist paper metadata and figure captions.

📚 What I Learned
How to structure a data pipeline that integrates third-party APIs (BioC, PubTator) with storage engines like DuckDB.

Practical usage of BioC-PMC and PubTator APIs for biomedical NLP and metadata extraction.

Gained clarity on how to build a production-grade system with RESTful APIs, CLI tools, and Dockerization.

Understood the importance of modular, configurable architecture to support:

API security via API keys

Configurable data sources and logging levels

Future extensibility without code rewrites

Learned the value of clean configuration management, making the system admin-friendly and deployment-ready.

Reinforced best practices in documenting, logging, and preparing systems for real-world ops and monitoring.







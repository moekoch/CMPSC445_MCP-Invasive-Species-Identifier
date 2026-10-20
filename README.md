# MCP Invasive Species Identifier



This repository is a local, lightweight Model Context Protocol (MCP) server that provides computer vision and regulatory lookup tools for plant species identification, invasive species risk assessment, and ecological removal protocols for the Wintergreen Gorge at Penn State Behrend.



> **Note:** This repository represents the **Phase 1: Architecture & Shell** release. It contains the project layout, database setup scripts, and mock MCP tool endpoints ready for model and database integration.



---



## 📅 Project Roadmap & Scope



| Phase | Description | Status |

| :--- | :--- | :---: |

| **Phase 1** | Repository structure, DB initialization, and FastMCP shell integration | 🚧 In Progress |

| **Phase 2** | Local Vision Transformer (PyTorch/ViT) inference pipeline setup | ⏳ Scheduled |

| **Phase 3** | Local SQLite regulatory lookup database for state/county invasive status | ⏳ Scheduled |

| **Phase 4** | Deterministic removal protocol rules engine & end-to-end testing | ⏳ Scheduled |



---



## 📂 Intended Repository Structure



```text

CMPSC445_MCP-Invasive-Species-Identifier/

├── README.txt                     # Project architecture and setup guide

├── requirements.txt               # Project dependencies (FastMCP, PyTorch, Transformers)

├── pyproject.toml                 # Build configuration

├── .gitignore                     # Git ignore rules

│

├── data/                          # Datasets and local databases (.gitignored)

│   ├── raw/                       # Sample images for testing

│   ├── models/                    # Cached model weights

│   └── db/                        # SQLite database storage

│       └── regulations.db

│

├── src/                           # Core source modules

│   └── invasive-identifier/

│       ├── __init__.py

│       ├── server.py              # Main FastMCP server entrypoint & tools

│       ├── vision/                # Computer vision inference engine

│       │   ├── __init__.py

│       │   └── classifier.py

│       ├── regulatory/            # Regulatory lookup module

│       │   ├── __init__.py

│       │   └── lookup.py

│       └── rules/                 # Eradication & mitigation logic

│           ├── __init__.py

│           └── protocols.py

│

├── tests/                         # Test suite

│   ├── __init__.py

│   └── test_tools.py

│

└── scripts/                       # Maintenance & testing utility scripts

    ├── init_db.py                 # SQLite database initialization script

    └── run_test_pipeline.py       # Standalone pipeline test runner

```



---



## 🛠️ MCP Tools Exposed



The MCP server will expose three main tools via `stdio` transport:



1. **`classify_botanical_image(image_path: str)`**

   * **Description:** Accepts a local image file path and returns predicted botanical species and confidence scores using a local Vision Transformer.

2. **`check_invasive_status(scientific_name: str, state_code: str = "PA")`**

   * **Description:** Queries the local regulatory database to determine if a species is listed as invasive or noxious in a given state.

3. **`generate_removal_protocol(scientific_name: str, severe_infestation: bool = False)`**

   * **Description:** Produces targeted mechanical, chemical, and disposal mitigation guidelines for invasive flora.



---



## 🚀 Quickstart & Environment Setup



### 1. Prerequisites

* Python 3.10+

* Virtual environment tool (`venv` or `conda`)



### 2. Installation



Clone the repository and set up a virtual environment:



```bash

# Clone repository

git clone https://github.com/moekoch/CMPSC445_MCP-Invasive-Species-Identifier.git

cd CMPSC445_MCP-Invasive-Species-Identifier



# Create and activate virtual environment

python -m venv .venv

source .venv/bin/activate  # On Windows: .venv\Scripts\activate



# Install dependencies

pip install -r requirements.txt

```



### 3. Initialize Local Database



Run the database setup script to generate the local SQLite database in `data/db/`:



```bash

python scripts/init_db.py

```



---



## 🧪 Testing



### Manual Pipeline Test (No MCP Overhead)

To test the core ML and regulatory execution flow during development without launching the transport protocol:



```bash

python scripts/run_test_pipeline.py

```



### Run MCP Tool Server

To start the FastMCP server for tool invocation:



```bash

python -m invasive-identifier.server

```



---
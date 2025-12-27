# 🚀 Technical Challenge - Technical Implementer | Kartado

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JSON](https://img.shields.io/badge/json-5E5E5E?style=for-the-badge&logo=json&logoColor=white)
![Cursor](https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white)
![Windsurf](https://img.shields.io/badge/Windsurf-4B0082?style=for-the-badge&logo=windsurf&logoColor=white)

This repository presents the solution developed for the Technical Implementer challenge at **Kartado**. The project focuses on dynamic data structure manipulation, JSON schema validation, and the implementation of calculation logic applied to infrastructure engineering.

## 🚀 The Project

The core objective was to create a robust solution for managing technical forms. The solution allows for the dynamic expansion of fields while ensuring data integrity and automating complex calculations through a systemic approach.

## 🧠 Technical Decisions & Systemic Vision

The solution's architecture was designed to be scalable and maintainable:

* **JSON Manipulation**: Utilizes Python's native library to ensure performance and compatibility.
* **Identifier Management (IDs)**: Implementation of dynamic auto-increment logic for new fields, based on the highest existing ID to prevent conflicts.
* **Business Logic (JSONLogic)**: The form is structured to support complex mathematical operations (such as Area and Volume calculations) integrated directly into the data schema, allowing the calculation intelligence to reside within the field definition.
* **Rigorous Validation**: The insertion function verifies the mandatory presence of critical attributes (`displayName`, `apiName`, and `dataType`) before any write operation.

## 🛠️ Tech Stack

* **Primary Language:** Python 3.x
* **Data Formats:** JSON / JSONLogic
* **IDE & AI Tools:** Cursor, Windsurf, and GitHub Copilot for code modularization and refactoring.
* **Standardization:** UTF-8 encoding to support special characters in display fields.

## 📂 Repository Structure

* **`/respostas-desafios`**: Contains the core technical solution.
    * `adicionar_campo.py`: Python script with form manipulation and validation logic.
    * `formulario.json`: Data structure representing a technical form with calculation logic.
* **`/documentos-importantes`**: Technical documentation detailing design decisions and data flows.

## ⚙️ How to Test the Solution

To validate the field addition function, ensure you have Python installed and follow these steps:

1.  Navigate to the challenge folder:
    ```bash
    cd respostas-desafios
    ```
2.  Run the test script:
    ```bash
    python adicionar_campo.py
    ```

The script will read `formulario.json`, validate the input data, and insert a new field at the beginning of the list while maintaining ID integrity.

## 🌟 Key Features Implemented

* **Modularization**: Clean code and single-responsibility functions.
* **Error Handling**: Type checking and key existence verification to prevent runtime failures.
* **Documentation**: Code documented with *docstrings* following professional standards.

---

## 📞 Contact

**Éverson Filipe Campos da Silva Moura**  
📧 [eversonfilipe124@gmail.com](mailto:eversonfilipe124@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/eversonfilipe-agile-products-ai/)

---
*This project was developed as part of the Kartado selection process, demonstrating technical skills in Python and systems analysis.*

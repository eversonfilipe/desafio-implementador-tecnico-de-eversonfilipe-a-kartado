# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to Semantic Versioning.

## [2.0.0] - Public Portfolio Release - 2025-12-27

This version marks the transition of the repository from a private submission environment to a Public Technical Solution Showcase. The main focus was compliance with data protection laws and the refinement of documentation for the tech community.

### Added
- **Bilingual Documentation:** Inclusion of `README-EN.md` for the international accessibility of the portfolio.
- **Tech Stack Badges:** Implementation of visual technology indicators in the documentation header.
- **Execution Guide:** Detailed "How to Test" section to facilitate peer review.

### Changed
- **README.md Refactoring:** Complete rewrite focusing on architectural decisions and systemic vision, removing the "candidate" tone and assuming a "problem solver" tone.
- **Code Comments:** Refinement of docstrings in `adicionar_campo.py` to follow professional technical documentation standards.

### Removed
- **Third-Party Intellectual Property Documentation:** Removal of the original instruction file (.docx) to respect the proponent company's copyrights.
- **Personally Identifiable Information (PII):** Removal of resumes, behavioral reports, and sensitive contacts that were present in the submission version.

### Security
- **Data Sanitization:** Complete sanitization of commit history to ensure that sensitive data (PII) and internal documents are not publicly accessible.
- **Repository Hardening:** Configuration of visibility and file auditing for compliance with public portfolio standards.

---

## [1.0.0] - Private Candidate Submission - 2025-08-11

Initial version submitted for technical evaluation.

### Added
- **Core Logic:** Implementation of the `adicionar_campo` function with ID auto-increment logic.
- **Data Structure:** Structuring of `formulario.json` with examples of calculations via JSONLogic.
- **Initial Setup:** Initial setup of the Python environment and UTF-8 file handling.

[2.0.0]: https://github.com/eversonfilipe/desafio-implementador-tecnico/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/eversonfilipe/desafio-implementador-tecnico/releases/tag/v1.0.0

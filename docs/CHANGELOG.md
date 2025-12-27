# Changelog

Todas as alterações notáveis neste projeto serão documentadas neste arquivo. O formato é baseado no [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) e este projeto adere ao versionamento semântico.

## [2.0.0] - Public Portfolio Release - 2025-12-27

Esta versão marca a transição do repositório de um ambiente de submissão privada para um Showcase Público de Solução Técnica. O foco principal foi a conformidade com leis de proteção de dados e o refinamento da documentação para a comunidade tech.

### Added
- **Documentação Bilíngue:** Inclusão do `README-EN.md` para acessibilidade internacional do portfólio.
- **Badges de Tech Stack:** Implementação de indicadores visuais de tecnologia no cabeçalho da documentação.
- **Guia de Execução:** Seção detalhada de "Como Testar" para facilitar a revisão por pares.

### Changed
- **Refatoração de README.md:** Reescrita completa focando em decisões arquiteturais e visão sistêmica, removendo o tom de "candidato" e assumindo o tom de "resolvedor de problemas".
- **Comentários de Código:** Refinamento das docstrings em `adicionar_campo.py` para seguir padrões de documentação técnica profissional.

### Removed
- **Documentação de Propriedade Intelectual de Terceiros:** Remoção do arquivo original de instruções (.docx) para respeitar os direitos autorais da empresa proponente.
- **Informações de Identificação Pessoal (PII):** Remoção de currículos, relatórios comportamentais e contatos sensíveis que estavam presentes na versão de submissão.

### Security
- **Higienização de Dados:** Sanitização completa do histórico de commits para garantir que dados sensíveis (PII) e documentos internos não estejam acessíveis publicamente.
- **Hardening de Repositório:** Configuração de visibilidade e auditoria de arquivos para conformidade com padrões de portfólio público.

---

## [1.0.0] - Private Candidate Submission - 2025-08-11

Versão inicial enviada para avaliação técnica.

### Added
- **Core Logic:** Implementação da função `adicionar_campo` com lógica de auto-incremento de ID.
- **Data Structure:** Estruturação do `formulario.json` com exemplos de cálculos via JSONLogic.
- **Initial Setup:** Configuração inicial do ambiente Python e manipulação de arquivos UTF-8.

[2.0.0]: https://github.com/eversonfilipe/desafio-implementador-tecnico/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/eversonfilipe/desafio-implementador-tecnico/releases/tag/v1.0.0

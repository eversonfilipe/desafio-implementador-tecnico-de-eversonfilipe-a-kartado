# 🚀 Desafio Técnico - Implementador Técnico | Kartado

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JSON](https://img.shields.io/badge/json-5E5E5E?style=for-the-badge&logo=json&logoColor=white)
![Cursor](https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white)
![Windsurf](https://img.shields.io/badge/Windsurf-4B0082?style=for-the-badge&logo=windsurf&logoColor=white)

Este repositório apresenta a solução desenvolvida para o desafio técnico de Implementador Técnico na **Kartado**. O projeto foca na manipulação de estruturas de dados dinâmicas, validação de esquemas JSON e implementação de lógicas de cálculo aplicadas à engenharia de infraestrutura.

## 🚀 O Projeto

O objetivo central foi criar uma solução robusta para a gestão de formulários técnicos. A solução permite a expansão dinâmica de campos, garantindo a integridade dos dados e a automação de cálculos complexos através de uma abordagem sistêmica.

## 🧠 Decisões Técnicas & Visão Sistêmica

A arquitetura da solução foi pensada para ser escalável e de fácil manutenção:

* **Manipulação de JSON**: Utilização da biblioteca nativa do Python para garantir performance e compatibilidade.
* **Gestão de Identificadores (IDs)**: Implementação de lógica de auto-incremento dinâmico para novos campos, baseando-se no maior ID existente para evitar conflitos.
* **Lógica de Negócio (JSONLogic)**: O formulário foi estruturado para suportar operações matemáticas complexas (como cálculos de Área e Volume) integradas diretamente no esquema do dado, permitindo que a inteligência do cálculo resida na definição do campo.
* **Validação Rigorosa**: A função de inserção verifica a presença obrigatória de atributos críticos (`displayName`, `apiName` e `dataType`) antes de qualquer operação de escrita.

## 🛠️ Tech Stack

* **Linguagem Principal:** Python 3.x
* **Formatos de Dados:** JSON / JSONLogic
* **IDE & Ferramentas de IA:** Cursor, Windsurf e GitHub Copilot para modularização e refatoração de código.
* **Padronização:** Codificação UTF-8 para suporte a caracteres especiais em campos de exibição.

## 📂 Estrutura do Repositório

* **`/respostas-desafios`**: Contém o núcleo da solução técnica.
    * `adicionar_campo.py`: Script Python com a lógica de manipulação e validação de formulários.
    * `formulario.json`: Estrutura de dados representando um formulário técnico com lógicas de cálculo.
* **`/documentos-importantes`**: Documentação técnica detalhando as decisões de design e fluxos de dados.

## ⚙️ Como Testar a Solução

Para validar a função de adição de campos, certifique-se de ter o Python instalado e siga os passos:

1.  Navegue até a pasta de desafios:
    ```bash
    cd respostas-desafios
    ```
2.  Execute o script de teste:
    ```bash
    python adicionar_campo.py
    ```

O script realizará a leitura do `formulario.json`, validará os dados de entrada e inserirá um novo campo no início da lista, mantendo a integridade dos IDs.

## 🌟 Diferenciais Implementados

* **Modularização**: Código limpo e funções com responsabilidade única.
* **Tratamento de Erros**: Verificações de tipo e existência de chaves para prevenir falhas em tempo de execução.
* **Documentação**: Código documentado com *docstrings* seguindo padrões profissionais.

---

## 📞 Contato

**Éverson Filipe Campos da Silva Moura** 📧 [eversonfilipe124@gmail.com](mailto:eversonfilipe124@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/eversonfilipe-agile-products-ai/)

---
*Este projeto foi desenvolvido como parte do processo seletivo da Kartado, demonstrando competências técnicas em Python e parametrização de sistemas.*

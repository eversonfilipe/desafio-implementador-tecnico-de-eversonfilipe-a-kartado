import json

with open("formulario.json", "r") as file:
    formulario_existente = json.load(file)

def adicionar_campo(formulario_existente, campo_novo):
    """
    Adiciona um novo campo ao formulário JSON conforme especificado no desafio.
    
    Parâmetros:
    - formulario_existente: dict, formato {"formulario": [lista_de_campos]}.
    - campo_novo: dict, deve conter "displayName", "apiName", e "dataType".
    
    Retorna:
    - dict: Formulário atualizado com o novo campo no início da lista.
    """
    
    # Validação básica dos parâmetros
    if not isinstance(formulario_existente, dict) or "formulario" not in formulario_existente:
        raise ValueError("O formulário existente deve ser um dicionário com a chave 'formulario'.")
    
    if not all(key in campo_novo for key in ["displayName", "apiName", "dataType"]):
        raise ValueError("O campo novo deve conter 'displayName', 'apiName' e 'dataType'.")
    
    # Obtém a lista de campos e calcula o próximo ID
    lista_campos = formulario_existente["formulario"]
    novo_id = 1 if not lista_campos else max(campo["id"] for campo in lista_campos) + 1
    
    # Cria o campo com ID e insere no início da lista
    campo_com_id = {"id": novo_id, **campo_novo}
    lista_campos.insert(0, campo_com_id)
    
    return {"formulario": lista_campos}


# Exemplo de uso (para testes)
if __name__ == "__main__":
    # Exemplo de formulário existente (Parte 1)
    formulario_exemplo = {
        "formulario": [
            {"id": 2, "displayName": "Comprimento", "apiName": "comprimento", "dataType": "float"},
            {"id": 3, "displayName": "Largura", "apiName": "largura", "dataType": "float"}
        ]
    }
    
    # Novo campo a ser adicionado
    novo_campo = {
        "displayName": "Material",
        "apiName": "material",
        "dataType": "string"
    }
    
    # Chama a função e imprime o resultado
    formulario_atualizado = adicionar_campo(formulario_exemplo, novo_campo)
    print(formulario_atualizado)

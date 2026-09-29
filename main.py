import time

# --- ESTRUTURA DE DADOS ---
pecas_aprovadas = []
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []
LIMITE_CAIXA = 10

# --- FUNÇÕES LÓGICAS ---
def avaliar_peca(peso, cor, comprimento):
    """Avalia a peça com base nas regras de negócio da indústria."""
    motivos = []
    
    if not (95 <= peso <= 105):
        motivos.append("Peso fora do padrão (95g - 105g)")
    if cor.lower() not in ['azul', 'verde']:
        motivos.append("Cor inválida (Apenas Azul ou Verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do padrão (10cm - 20cm)")
        
    # Retorna True se aprovada (lista vazia de motivos), e a lista de motivos
    return len(motivos) == 0, motivos

def cadastrar_peca():
    global caixa_atual
    print("\n--- Cadastro de Nova Peça ---")
    try:
        id_peca = input("ID da Peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor (Ex: Azul, Verde): ").strip()
        comprimento = float(input("Comprimento (cm): "))
        
        aprovada, motivos = avaliar_peca(peso, cor, comprimento)
        
        if aprovada:
            peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
            pecas_aprovadas.append(peca)
            caixa_atual.append(peca)
            print("✅ Resultado: Peça APROVADA e adicionada à caixa atual.")
            
            # Regra de negócio: Fechar caixa ao atingir 10 unidades
            if len(caixa_atual) == LIMITE_CAIXA:
                caixas_fechadas.append(caixa_atual.copy())
                caixa_atual.clear()
                print(f"📦 ALERTA: Caixa fechada! Limite de {LIMITE_CAIXA} atingido. Nova caixa iniciada.")
        else:
            peca = {"id": id_peca, "motivos": motivos}
            pecas_reprovadas.append(peca)
            print("❌ Resultado: Peça REPROVADA.")
            print(f"Motivo(s): {', '.join(motivos)}")
            
    except ValueError:
        print("⚠️ Erro: Entrada de dados inválida. Utilize apenas números para peso e comprimento.")

def listar_pecas():
    print("\n--- Lista de Peças Processadas ---")
    print(f"\n✅ APROVADAS ({len(pecas_aprovadas)} total):")
    for p in pecas_aprovadas:
        print(f" - ID: {p['id']} | {p['peso']}g | {p['cor']} | {p['comprimento']}cm")
        
    print(f"\n❌ REPROVADAS ({len(pecas_reprovadas)} total):")
    for p in pecas_reprovadas:
        print(f" - ID: {p['id']} | Motivos: {', '.join(p['motivos'])}")

def remover_peca():
    print("\n--- Remover Peça Cadastrada ---")
    id_remocao = input("Digite o ID da peça que deseja remover: ")
    
    # Tenta remover de aprovadas
    for peca in pecas_aprovadas:
        if peca["id"] == id_remocao:
            pecas_aprovadas.remove(peca)
            # Tenta remover da caixa atual aberta
            if peca in caixa_atual:
                caixa_atual.remove(peca)
            # Tenta remover de caixas fechadas
            for caixa in caixas_fechadas:
                if peca in caixa:
                    caixa.remove(peca)
            print(f"✅ Peça aprovada {id_remocao} removida do sistema com sucesso.")
            return

    # Tenta remover de reprovadas
    for peca in pecas_reprovadas:
        if peca["id"] == id_remocao:
            pecas_reprovadas.remove(peca)
            print(f"✅ Peça reprovada {id_remocao} removida do sistema com sucesso.")
            return
            
    print("⚠️ Peça não encontrada no sistema.")

def listar_caixas():
    print("\n--- Relatório de Caixas de Armazenamento ---")
    print(f"Caixas prontas para expedição (Fechadas): {len(caixas_fechadas)}")
    for i, caixa in enumerate(caixas_fechadas, 1):
        ids = [p['id'] for p in caixa]
        print(f" 📦 Caixa {i}: {len(caixa)} peças. IDs: {ids}")
        
    print(f"\nCaixa atual (em aberto): {len(caixa_atual)}/{LIMITE_CAIXA} peças alocadas.")

def gerar_relatorio_final():
    print("\n" + "="*40)
    print("📊 RELATÓRIO FINAL CONSOLIDADO")
    print("="*40)
    print(f"Total de Peças Aprovadas: {len(pecas_aprovadas)}")
    print(f"Total de Peças Reprovadas: {len(pecas_reprovadas)}")
    
    print("\n--- Detalhamento de Reprovações ---")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada no turno.")
    for p in pecas_reprovadas:
        print(f"Peça {p['id']}: {', '.join(p['motivos'])}")
        
    print(f"\n--- Armazenamento ---")
    print(f"Quantidade total de caixas fechadas utilizadas: {len(caixas_fechadas)}")
    if len(caixa_atual) > 0:
        print(f"Existe 1 caixa incompleta na linha contendo {len(caixa_atual)} peça(s).")
    print("="*40)

# --- MENU INTERATIVO ---
def menu():
    while True:
        print("\n" + "-"*35)
        print("🏭 SISTEMA DE GESTÃO DE QUALIDADE")
        print("-"*35)
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final (Sair)")
        
        opcao = input("\nEscolha uma opção (1-5): ")
        
        if opcao == '1':
            cadastrar_peca()
        elif opcao == '2':
            listar_pecas()
        elif opcao == '3':
            remover_peca()
        elif opcao == '4':
            listar_caixas()
        elif opcao == '5':
            gerar_relatorio_final()
            print("\nEncerrando o sistema... Turno finalizado. 👋")
            time.sleep(1)
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

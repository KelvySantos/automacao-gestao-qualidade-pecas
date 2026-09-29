# Desafio de Automação Digital: Gestão de Qualidade 🏭

Protótipo em Python desenvolvido para automatizar a triagem, aprovação e empacotamento de peças em uma linha de montagem industrial.

## 🚀 O Problema
Atualmente, inspeções de peças em fábricas são feitas de forma manual, causando gargalos logísticos, fadiga e erros de contagem. Este sistema substitui a validação subjetiva por um script lógico, garantindo que 100% da produção seja inspecionada contra parâmetros estritos.

## ⚙️ Funcionalidades
1. **Inspeção Automática:** Valida cada peça considerando peso (95g a 105g), cor (Azul/Verde) e comprimento (10cm a 20cm).
2. **Empacotamento Inteligente:** Agrupa peças aprovadas. Fecha caixas automaticamente ao atingir o limite de 10 unidades.
3. **Gestão de Inventário:** Permite listagem, adição e remoção de peças do sistema.
4. **Relatórios:** Gera log consolidado de produção, incluindo motivos específicos de reprovação.

## 💻 Como Rodar o Projeto

**Pré-requisitos:**
* Ter o [Python](https://www.python.org/downloads/) (versão 3.x) instalado em sua máquina.

**Passo a passo:**
1. Faça o clone deste repositório ou baixe o arquivo `main.py`.
2. Abra o terminal (Prompt de Comando, PowerShell ou Terminal do Linux/Mac).
3. Navegue até a pasta onde o arquivo está salvo: `cd caminho/para/a/pasta`
4. Execute o script com o comando:
   ```bash
   python main.py
   ```

## 📋 Menu do Sistema

O sistema oferece as seguintes opções:

1. **Cadastrar nova peça** - Insira ID, peso, cor e comprimento para validação automática
2. **Listar peças aprovadas/reprovadas** - Visualize todas as peças processadas
3. **Remover peça cadastrada** - Delete uma peça do sistema pelo ID
4. **Listar caixas fechadas** - Veja as caixas prontas para expedição
5. **Gerar relatório final** - Encerre o turno com relatório consolidado

## 🎯 Critérios de Qualidade

Para uma peça ser **APROVADA**, deve atender aos seguintes critérios:

| Critério | Valor Aceito |
|----------|-------------|
| Peso | 95g a 105g |
| Cor | Azul ou Verde |
| Comprimento | 10cm a 20cm |

## 📊 Exemplo de Uso

### Entrada:
```text
ID da Peça: P001
Peso (g): 100
Cor (Ex: Azul, Verde): Azul
Comprimento (cm): 15
```

### Saída:
```text
✅ Resultado: Peça APROVADA e adicionada à caixa atual.
```

### Exemplo de Reprovação:
```text
ID da Peça: P002
Peso (g): 110
Cor (Ex: Azul, Verde): Vermelho
Comprimento (cm): 25
```

### Saída:
```text
❌ Resultado: Peça REPROVADA.
Motivo(s): Peso fora do padrão (95g - 105g), Cor inválida (Apenas Azul ou Verde), Comprimento fora do padrão (10cm - 20cm)
```

## 📦 Relatório Final

Ao finalizar o sistema, você receberá um relatório consolidado contendo:
- Total de peças aprovadas
- Total de peças reprovadas com detalhamento dos motivos
- Quantidade de caixas utilizadas
- Status da caixa em aberto (se houver)

## 🛠️ Estrutura do Código

- **Estrutura de Dados:** Listas globais para armazenar peças aprovadas, reprovadas, caixas fechadas e caixa atual
- **Funções Lógicas:**
  - `avaliar_peca()` - Valida critérios de qualidade
  - `cadastrar_peca()` - Recebe dados e processa nova peça
  - `listar_pecas()` - Exibe peças aprovadas e reprovadas
  - `remover_peca()` - Remove peça do sistema
  - `listar_caixas()` - Mostra status das caixas
  - `gerar_relatorio_final()` - Gera relatório consolidado
  - `menu()` - Loop interativo do sistema

## 💡 Benefícios da Solução

✅ Redução de erros de inspeção manual
✅ Aumento na velocidade de processamento
✅ Rastreabilidade completa de cada peça
✅ Redução de custos operacionais
✅ Fácil manutenção e expansão do sistema

## 🚀 Possíveis Expansões Futuras

- Integração com sensores IoT em tempo real
- Implementação de Machine Learning para detecção de anomalias
- Integração com banco de dados para persistência de dados
- Dashboard web para visualização de métricas
- API REST para integração com sistemas ERP
- Relatórios em PDF/Excel

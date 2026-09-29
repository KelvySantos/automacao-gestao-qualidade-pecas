# Desafio de Automação Digital: Gestão de Qualidade 🏭

Protótipo em Python desenvolvido para automatizar a triagem, aprovação e empacotamento de peças em uma linha de montagem industrial.

## 🚀 Visão Geral

Este projeto combina duas interfaces complementares:

- CLI em Python (`main.py`): solução local, interativa e simples para controle de qualidade em terminal.
- Aplicativo web complementar: solução visual para acompanhamento do processo de qualidade e gerenciamento de caixas.

A aplicação web disponível em:

- https://quality-box-manager--kelvysantosdev.replit.app/controle-qualidade/

## 🧩 Problema resolvido

Atualmente, inspeções de peças em fábricas costumam ser feitas de forma manual, gerando gargalos logísticos, fadiga operacional e erros de contagem. Este sistema substitui a validação subjetiva por uma rotina automatizada que:

- valida cada peça por critérios técnicos;
- separa peças aprovadas e reprovadas;
- organiza as peças em caixas;
- gera relatórios finais do turno.

## ⚙️ Funcionalidades

1. **Inspeção Automática:** Valida cada peça considerando peso (95g a 105g), cor (Azul/Verde) e comprimento (10cm a 20cm).
2. **Empacotamento Inteligente:** Agrupa peças aprovadas. Fecha caixas automaticamente ao atingir o limite de 10 unidades.
3. **Gestão de Inventário:** Permite listagem, adição e remoção de peças do sistema.
4. **Relatórios:** Gera log consolidado de produção, incluindo motivos específicos de reprovação.
5. **Interface Web Complementar:** Permite visualização e acompanhamento do processo de forma mais amigável e operacional.

## 💻 Como rodar o projeto

### Pré-requisitos

- Ter o Python 3.x instalado em sua máquina.

### Executando a versão CLI

1. Clone este repositório.
2. Abra o terminal.
3. Navegue até a pasta do projeto.
4. Execute:

```bash
python main.py
```

### Executando a versão web

A aplicação web está disponível online no link abaixo:

- https://quality-box-manager--kelvysantosdev.replit.app/controle-qualidade/

## 📋 Menu do sistema CLI

O sistema oferece as seguintes opções:

1. **Cadastrar nova peça** - Insira ID, peso, cor e comprimento para validação automática.
2. **Listar peças aprovadas/reprovadas** - Visualize todas as peças processadas.
3. **Remover peça cadastrada** - Delete uma peça do sistema pelo ID.
4. **Listar caixas fechadas** - Veja as caixas prontas para expedição.
5. **Gerar relatório final** - Encerre o turno com relatório consolidado.

## 🎯 Critérios de qualidade

Para uma peça ser **APROVADA**, deve atender aos seguintes critérios:

| Critério | Valor aceito |
|----------|--------------|
| Peso | 95g a 105g |
| Cor | Azul ou Verde |
| Comprimento | 10cm a 20cm |

## 📊 Exemplo de uso

### Entrada

```text
ID da Peça: P001
Peso (g): 100
Cor (Ex: Azul, Verde): Azul
Comprimento (cm): 15
```

### Saída

```text
✅ Resultado: Peça APROVADA e adicionada à caixa atual.
```

### Reprovação

```text
ID da Peça: P002
Peso (g): 110
Cor (Ex: Azul, Verde): Vermelho
Comprimento (cm): 25
```

### Saída

```text
❌ Resultado: Peça REPROVADA.
Motivo(s): Peso fora do padrão (95g - 105g), Cor inválida (Apenas Azul ou Verde), Comprimento fora do padrão (10cm - 20cm)
```

## 📦 Relatório final

Ao finalizar o sistema, você receberá um relatório consolidado contendo:

- Total de peças aprovadas;
- Total de peças reprovadas com detalhamento dos motivos;
- Quantidade de caixas utilizadas;
- Status da caixa em aberto, se houver.

## 🛠️ Estrutura do código

- **Estrutura de Dados:** Listas globais para armazenar peças aprovadas, reprovadas, caixas fechadas e caixa atual.
- **Funções lógicas:**
  - `avaliar_peca()` - Valida critérios de qualidade.
  - `cadastrar_peca()` - Recebe dados e processa nova peça.
  - `listar_pecas()` - Exibe peças aprovadas e reprovadas.
  - `remover_peca()` - Remove peça do sistema.
  - `listar_caixas()` - Mostra status das caixas.
  - `gerar_relatorio_final()` - Gera relatório consolidado.
  - `menu()` - Loop interativo do sistema.

## 💡 Benefícios da solução

✅ Redução de erros de inspeção manual
✅ Aumento na velocidade de processamento
✅ Rastreabilidade completa de cada peça
✅ Redução de custos operacionais
✅ Fácil manutenção e expansão do sistema

## 🚀 Possíveis expansões futuras

- Integração com sensores IoT em tempo real;
- Implementação de Machine Learning para detecção de anomalias;
- Integração com banco de dados para persistência dos dados;
- Dashboard web para visualização de métricas;
- API REST para integração com sistemas ERP;
- Relatórios em PDF/Excel.

## 📌 Observação

Este repositório concentra a base lógica do projeto em Python. A interface web funciona como complemento operacional para a solução principal, oferecendo uma experiência mais visual e prática para o acompanhamento da qualidade em linha.

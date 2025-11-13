# Security-Headers-Analysis-Tool
Um script em Python para verificar rapidamente a presença de headers de segurança HTTP em qualquer website.

## **Descrição:**
Esta é uma ferramenta de linha de comando (CLI) desenvolvida para auditar a presença de headers de segurança essenciais. O script aceita uma URL como argumento, simula uma requisição de navegador e analisa a resposta HTTP, exibindo um relatório colorido no terminal que indica quais headers estão presentes ou ausentes.

## **Funcionalidades:**
Análise Rápida: Verifica alguns headers de segurança fundamentais;
Feedback Visual: Usa cores (verde ✅ e vermelho ❌) para um feedback claro e imediato;
Simulação de Navegador: Define um User-Agent para simular uma requisição de um usuário comum;
Tratamento de Erros: Lida com falhas de conexão, timeouts e uso incorreto do comando.

## **Tecnologias Utilizadas:**
Python;
requests: Para realizar as requisições HTTP;
colorama: Para adicionar cores ao output no terminal;

## **Como Usar:**
### **1. Pré-requisitos:**
Python 3
pip (geralmente incluído no Python)

### **2. Instalação**
Clone este repositório (ou apenas salve o arquivo Check_headers.py) e instale as dependências:
pip install requests colorama

### **4. Execução**
Execute o script a partir do seu terminal, passando a URL do site que deseja verificar como argumento.
python Check_headers.py <website_url>

### **Exemplos:**
python Check_headers.py google.com

python Check_headers.py https://github.com
(O script adiciona https:// automaticamente se nenhum protocolo (http/https) for fornecido.)

### **Exemplo de Saída**
C:\Users\User\Project> python Check_headers.py google.com

Strict-Transport-Security ✅ 1/7

Content-Security-Policy ❌ 1/7

X-Frame-Options ✅ 2/7

X-Content-Type-Options ✅ 3/7

Clear-Site-Data ❌ 3/7

Permissions-Policy ✅ 4/7

Cross-Origin-Opener-Policy ✅ 5/7

## **Observações Importantes**
**Contexto da Resposta:** A ferramenta analisa apenas a resposta específica recebida para a URL exata que foi testada.

**Resultados Condicionais:** Um ❌ (ausente) não significa que aquele site não tem o header, mas sim que o cabeçalho não estava presente naquela transação específica. É importante notar que um servidor pode ter um header configurado, mas não enviá-lo em todas as respostas (por exemplo, pode enviá-lo apenas em páginas de login, apenas em conexões HTTPS, ou não enviá-lo para arquivos de imagem ou CSS).

## **Headers Verificados**
A ferramenta verifica a presença dos seguintes headers:

Strict-Transport-Security,
Content-Security-Policy,
X-Frame-Options,
X-Content-Type-Options,
Clear-Site-Data,
Permissions-Policy,
Cross-Origin-Opener-Policy

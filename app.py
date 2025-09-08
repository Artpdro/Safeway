from flask import Flask, render_template_string, redirect, url_for
import os

app = Flask(__name__, static_folder='frontend/dist')

# Template HTML para a página de documentação
DOCUMENTATION_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Safeway - Documentação</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }
        
        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .content {
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        
        .section {
            margin-bottom: 40px;
        }
        
        .section h2 {
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-bottom: 20px;
            font-size: 2rem;
        }
        
        .section h3 {
            color: #764ba2;
            margin-bottom: 15px;
            font-size: 1.5rem;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        
        .feature-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        
        .feature-card h4 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .btn {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 25px;
            font-weight: bold;
            transition: transform 0.3s ease;
            margin: 10px;
        }
        
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .code-block {
            background: #2d3748;
            color: #e2e8f0;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
        }
        
        .api-endpoint {
            background: #e8f5e8;
            border: 1px solid #4caf50;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            font-family: monospace;
        }
        
        .warning {
            background: #fff3cd;
            border: 1px solid #ffc107;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }
        
        .footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚗 Safeway</h1>
            <p>Sistema de Análise de Acidentes de Trânsito</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📋 Visão Geral</h2>
                <p>O Safeway é uma plataforma completa para análise de dados de acidentes de trânsito no Brasil. 
                O sistema combina dados do DATATRAN e IBGE para fornecer insights valiosos sobre segurança viária.</p>
                
                <div class="feature-grid">
                    <div class="feature-card">
                        <h4>📊 Dashboard Interativo</h4>
                        <p>Visualizações dinâmicas com gráficos e mapas de calor para análise de acidentes.</p>
                    </div>
                    <div class="feature-card">
                        <h4>🗺️ Mapas de Densidade</h4>
                        <p>Identificação de trechos críticos e zonas de alto risco de acidentes.</p>
                    </div>
                    <div class="feature-card">
                        <h4>🤖 Integração com IA</h4>
                        <p>Chat inteligente para consultas sobre os dados usando Ollama/LLM.</p>
                    </div>
                    <div class="feature-card">
                        <h4>📈 Análise Temporal</h4>
                        <p>Análise de padrões por horário, dia da semana e condições meteorológicas.</p>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>🚀 Como Usar</h2>
                
                <h3>1. Acesso ao Dashboard</h3>
                <p>Para acessar o dashboard principal de análise de acidentes:</p>
                <a href="/dashboard" class="btn">🎯 Acessar Dashboard</a>
                
                <h3>2. Estrutura do Projeto</h3>
                <div class="code-block">
Safeway/
├── app.py                 # Servidor Flask (Documentação)
├── app_optimized.py       # Dashboard Streamlit
├── auth.py               # Sistema de autenticação
├── frontend/             # Interface React
├── core/                 # Módulos principais
├── data/                 # Dados processados
└── pages/                # Páginas adicionais
                </div>
                
                <h3>3. Instalação e Configuração</h3>
                <div class="code-block">
# Clone o repositório
git clone https://github.com/Artpdro/Safeway.git
cd Safeway

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor Flask (documentação)
python app.py

# Execute o dashboard Streamlit (em outro terminal)
streamlit run app_optimized.py
                </div>
            </div>
            
            <div class="section">
                <h2>🔧 API Endpoints</h2>
                
                <h3>Rotas Principais</h3>
                <div class="api-endpoint">
                    <strong>GET /</strong> - Página de documentação (esta página)
                </div>
                <div class="api-endpoint">
                    <strong>GET /dashboard</strong> - Redireciona para o dashboard Streamlit
                </div>
                <div class="api-endpoint">
                    <strong>GET /run_streamlit</strong> - Inicia o servidor Streamlit
                </div>
                
                <div class="warning">
                    <strong>⚠️ Nota:</strong> O dashboard Streamlit roda na porta 8501. 
                    Certifique-se de que esta porta esteja disponível.
                </div>
            </div>
            
            <div class="section">
                <h2>📊 Funcionalidades do Dashboard</h2>
                
                <h3>Visualizações Disponíveis</h3>
                <ul style="margin-left: 20px;">
                    <li><strong>Mapa de Calor:</strong> Acidentes por UF e tipo</li>
                    <li><strong>Análise Temporal:</strong> Risco por horário do dia</li>
                    <li><strong>Principais Causas:</strong> Top 10 causas de acidentes</li>
                    <li><strong>Distribuição Semanal:</strong> Acidentes por dia da semana</li>
                    <li><strong>Condições Meteorológicas:</strong> Impacto do clima nos acidentes</li>
                    <li><strong>Mapa de Densidade:</strong> Localização geográfica dos acidentes</li>
                </ul>
                
                <h3>Dados Suportados</h3>
                <ul style="margin-left: 20px;">
                    <li>DATATRAN (2020-2025)</li>
                    <li>Dados IBGE agregados</li>
                    <li>Coordenadas geográficas</li>
                    <li>Informações meteorológicas</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>🤖 Integração com IA</h2>
                <p>O sistema inclui integração com Ollama para consultas inteligentes sobre os dados:</p>
                
                <div class="code-block">
# Instalar Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Baixar modelo
ollama pull llama3.1

# O chat estará disponível no dashboard
                </div>
            </div>
            
            <div class="section">
                <h2>👥 Equipe de Desenvolvimento</h2>
                <p>Este projeto foi desenvolvido por:</p>
                <ul style="margin-left: 20px;">
                    <li><strong>Arthur Pedro</strong> - Desenvolvimento Backend e Análise de Dados</li>
                    <li><strong>Pedro Lacerda</strong> - Desenvolvimento Frontend e Visualizações</li>
                </ul>
            </div>
        </div>
        
        <div class="footer">
            <p>&copy; 2024 Safeway - Sistema de Análise de Acidentes de Trânsito</p>
            <p>Desenvolvido com ❤️ para um trânsito mais seguro</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def documentation():
    """Página principal com documentação do sistema"""
    return render_template_string(DOCUMENTATION_TEMPLATE)

@app.route('/dashboard')
def dashboard():
    """Redireciona para o dashboard Streamlit"""
    return redirect('http://localhost:8501')

@app.route('/run_streamlit')
def run_streamlit():
    """Inicia o servidor Streamlit"""
    import subprocess
    import time
    
    try:
        # Verifica se o Streamlit já está rodando
        import requests
        try:
            response = requests.get('http://localhost:8501', timeout=2)
            if response.status_code == 200:
                return 'Streamlit já está rodando na porta 8501. <a href="http://localhost:8501">Clique aqui para acessar</a>'
        except:
            pass
        
        # Inicia o Streamlit em segundo plano
        subprocess.Popen([
            'streamlit', 'run', 'app_optimized.py', 
            '--server.port', '8501', 
            '--server.headless', 'true',
            '--server.address', '0.0.0.0'
        ])
        
        # Aguarda alguns segundos para o servidor iniciar
        time.sleep(3)
        
        return '''
        <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h2>🚀 Streamlit Dashboard Iniciado!</h2>
            <p>O dashboard está sendo iniciado na porta 8501...</p>
            <p><a href="http://localhost:8501" style="background: #667eea; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Acessar Dashboard</a></p>
            <p><a href="/" style="color: #667eea;">← Voltar para Documentação</a></p>
        </div>
        '''
    except Exception as e:
        return f'''
        <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h2>❌ Erro ao Iniciar Streamlit</h2>
            <p>Erro: {e}</p>
            <p>Certifique-se de que o Streamlit está instalado:</p>
            <code>pip install streamlit</code>
            <p><a href="/" style="color: #667eea;">← Voltar para Documentação</a></p>
        </div>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


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
            <p>Traffic Accident Analysis System</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📋 Overview</h2>
                <p>Safeway is a comprehensive platform for analyzing traffic accident data in Brazil.
The system combines data from DATATRAN and IBGE to provide valuable insights into road safety.</p>
                
                <div class="feature-grid">
                    <div class="feature-card">
                        <h4>📊 Interactive Dashboard</h4>
                        <p>Dynamic visualizations with graphs and heat maps for accident analysis.</p>
                    </div>
                    <div class="feature-card">
                        <h4>🗺️ Density Maps</h4>
                        <p>Identification of critical sections and high-risk accident zones.</p>
                    </div>
                    <div class="feature-card">
                        <h4>🤖 AI integration</h4>
                        <p>Smart chat for data queries using Ollama/LLM.</p>
                    </div>
                    <div class="feature-card">
                        <h4>📈 Temporal Analysis</h4>
                        <p>Pattern analysis by time, day of the week and weather conditions.</p>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>🚀 How to Use</h2>
                
                <h3>1. Access the Dashboard</h3>
                <p>To access the main accident analysis dashboard:</p>
                <a href="/dashboard" class="btn">🎯 Access Dashboard</a>
                
                <h3>2. Project Structure</h3>
                <div class="code-block">
Safeway/
├── app.py                 # Flask Server (Documentation)
├── app_optimized.py       # Streamlit Dashboard
├── auth.py               # Authentication system
├── frontend/             # React interface
├── core/                 # Main modules
├── data/                 # Processed data
└── pages/                # Additional pages
                </div>
                
                <h3>3. Installation and Configuration</h3>
                <div class="code-block">
# Clone the repository
git clone https://github.com/Artpdro/Safeway.git
cd Safeway

# Install dependencies
pip install -r requirements.txt

# Run the Flask server (documentation)
python app.py

# ERun the Streamlit dashboard (in another terminal)
streamlit run app_optimized.py
                </div>
            </div>
            
            <div class="section">
                <h2>🔧 API Endpoints</h2>
                
                <h3>Main Routes</h3>
                <div class="api-endpoint">
                    <strong>GET /</strong> - Documentation page (this page)
                </div>
                <div class="api-endpoint">
                    <strong>GET /dashboard</strong> - Redirects to the Streamlit dashboard
                </div>
                <div class="api-endpoint">
                    <strong>GET /run_streamlit</strong> - Start the Streamlit server
                </div>
                
                <div class="warning">
                    <strong>⚠️ Notice:</strong> The Streamlit dashboard run on port 8501. 
                    Make sure this port is available.
                </div>
            </div>
            
            <div class="section">
                <h2>📊 Supported Data</h2>
                
                <h3>Available Views</h3>
                <ul style="margin-left: 20px;">
                    <li><strong>Heat Map:</strong> Accidents by State and Type</li>
                    <li><strong>Temporal Analysis:</strong> Risk by time of day</li>
                    <li><strong>Main Causes:</strong> Top 10 causes of accidents</li>
                    <li><strong>Weekly Distribution:</strong> Accidents by day of the week</li>
                    <li><strong>Weather Conditions:</strong> Impact of climate on accidents</li>
                    <li><strong>Density Map:</strong> Geographic location of accidents</li>
                </ul>
                
                <h3>Supported Data</h3>
                <ul style="margin-left: 20px;">
                    <li>DATATRAN (2020-2025)</li>
                    <li>Aggregated IBGE data</li>
                    <li>Geographic coordinates</li>
                    <li>Weather information</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>🤖 AI integration</h2>
                <p>The system includes integration with Ollama for intelligent queries on the data:</p>
                
                <div class="code-block">
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Dowload model
ollama pull llama3.1

# The chat will be available on the dashboard
                </div>
            </div>
            
            <div class="section">
                <h2>👥 Development Team</h2>
                <p>This project was developed by:</p>
                <ul style="margin-left: 20px;">
                    <li><strong>Arthur Pedro</strong> - Backend Development and Data Analysis</li>
                    <li><strong>Pedro Lacerda</strong> - Frontend Development and Visualizations</li>
                </ul>
            </div>
        </div>
        
        <div class="footer">
            <p>&copy; 2024 Safeway - Traffic Accident Analysis System</p>
            <p>Developed with ❤️ by a safer traffic</p>
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


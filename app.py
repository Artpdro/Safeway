from flask import Flask, send_from_directory
import os
import subprocess

app = Flask(__name__, static_folder='frontend/dist')

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/run_streamlit')
def run_streamlit():
    # Isso é uma simplificação. Em um ambiente de produção, você não executaria o Streamlit assim.
    # O ideal seria ter o Streamlit rodando em uma porta separada e o Flask atuando como um proxy ou API gateway.
    # Para este exercício, vamos apenas indicar que o Streamlit seria iniciado.
    try:
        # Inicia o Streamlit em segundo plano. Isso pode não funcionar como esperado em todos os ambientes.
        # É mais uma demonstração de intenção do que uma solução robusta.
        subprocess.Popen(['streamlit', 'run', 'app_optimized.py', '--server.port', '8501', '--server.headless', 'true'])
        return 'Streamlit app is starting on port 8501...'
    except Exception as e:
        return f'Error starting Streamlit: {e}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



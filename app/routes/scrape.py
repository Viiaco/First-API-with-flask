from app import app, auth
import requests
from bs4 import BeautifulSoup
from flask import jsonify, Response
import pandas as pd

# Define the URL at the top
url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02'

@app.route('/scrape/producao', methods=['GET'])
@auth.login_required
def scrape_producao():
    """ 
    Rota para obter dados de produção de uma URL especificada.
    Método: GET 
    Autenticação: Requer autenticação HTTP Basic. 
    Retorna: 
    - JSON contendo os dados da tabela convertidos em registros, se os dados forem obtidos com sucesso. 
    - JSON contendo uma mensagem de erro, se houver problemas na obtenção dos dados. 
    Erros possíveis: {"error": "Erro ao obter dados da tabela"}: Se a tabela não for encontrada ou se houver problemas ao acessar a URL.
    """
    data = get_table_data(url)
    if data:
        df = pd.DataFrame(data[1:], columns=data[0])
        return df.to_json(orient='records')
    else:
        return jsonify({"error": "Erro ao obter dados da tabela"})

def get_table_data(url):
    """ 
    Função auxiliar para extrair dados de uma tabela HTML de uma URL especificada. 
    Parâmetros: url : str A URL da página da web que contém a tabela a ser extraída. 
    Retorna: 
    - Lista de listas contendo os dados da tabela, se a tabela for encontrada. 
    - None, se a tabela não for encontrada ou se houver problemas ao acessar a URL. 
    Erros possíveis:
    - "Tabela não encontrada na página.": Se a tabela especificada não for encontrada na página. 
    - f"Erro ao acessar a página: {response.status_code}": Se houver problemas ao acessar a URL, com o código de status HTTP correspondente.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'tb_base tb_dados'})
        if table:
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cells = row.find_all(['th', 'td'])
                cells_text = [cell.get_text(strip=True) for cell in cells]
                data.append(cells_text)
            return data
        else:
            print("Tabela não encontrada na página.")
            return None
    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None
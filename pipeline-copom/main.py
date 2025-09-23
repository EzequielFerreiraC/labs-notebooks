import requests

URL_BACEN = 'https://www.bcb.gov.br'
API_REPORT_LISTS = "/api/servico/sitebcb/copom/atas?quantidade="
API_REPORT_DETAILS = "/api/servico/sitebcb/copom/atas_detalhes?nro_reuniao="

QTD_REPORTS = 1000

# response = requests.get(f"{URL_BACEN}{API_REPORT_LISTS}{QTD_REPORTS}")

response = requests.get(f"{URL_BACEN}{API_REPORT_DETAILS}272")
data = response.json()

def check_api_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return True
    except requests.RequestException as e:
        print("Erro ao acessar a API:", e)
        return False
    
def get_lists_reports(url):
    if check_api_status(url):
        response = requests.get(url)
        data = response.json()
        items = data.get("conteudo", [])
        print(len(items))

# related to PDF
def get_url_reports(url):
    return False

resultado = get_lists_reports(f"{URL_BACEN}{API_REPORT_LISTS}")
print(resultado)
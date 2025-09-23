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
        print(f"Total de itens encontrados: {len(items)}")


        for item in items:
            nro_reuniao = item["nroReuniao"]
            print("Reunião: ", nro_reuniao)
            get_url_reports(f"{URL_BACEN}{API_REPORT_DETAILS}{nro_reuniao}")

# related to PDF
def get_url_reports(url):
    if check_api_status(url):
        response = requests.get(url)
        data = response.json()

        content = data["conteudo"][0]
        url_report = content.get("urlPdfAta")
        print("urlPdfAta:", url_report)


get_lists_reports(f"{URL_BACEN}{API_REPORT_LISTS}{QTD_REPORTS}")

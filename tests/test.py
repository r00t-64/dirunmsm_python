import requests
url = "http://biblioteca.unmsm.edu.pe/scudirectorio/resultado.asp"
params = {
    "pag": "1",
    "inicio": "SI",
    "Pat": "apellido1",
    "Mat": "apellido2",
    "Nom": "name1"
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.text
    # Process the data as per your requirements
    print(data)
else:
    print("Error occurred while accessing the API.")
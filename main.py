from api.api_client import APIClient
def main():
    base_url = "http://biblioteca.unmsm.edu.pe/scudirectorio/resultado.asp"
    headers = {
        "Content-Type": "application/json",
    }

    # Get user input for parameters
    p_lastname = input("Ingrese apellido paterno : ")
    m_lastname = input("Ingrese apellido materno: ")
    first_name = input("Ingrese nombre: ")

    params = {
        "pag": "1",
        "inicio": "SI",
        "Pat": p_lastname,
        "Mat": m_lastname,
        "Nom": first_name
    }

    api_client = APIClient(base_url, headers=headers)
    
    data = api_client.get_data(params=params)
    
    if data:
        # Process the retrieved data as per your requirements
        print(data)
if __name__ == "__main__":
    main()
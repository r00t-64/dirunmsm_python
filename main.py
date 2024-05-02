import sys
from api.api_client import APIClient
def main():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py find_stundent|get_data")
        return
    
    method = sys.argv[1]

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

    api_client = APIClient(base_url, headers=headers, params=params)
    
    if method == "get_data":
        api_client.get_data()
        return
    
    if method == "find_student":
        data = api_client.retrieve_all_students()
        
        if data:
            # Process the retrieved data as per your requirements
            print(data)

if __name__ == "__main__":
    main()
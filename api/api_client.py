import requests
from bs4 import BeautifulSoup
import json 

class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def get_data(self, params=None):
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)
            response.raise_for_status()

            # Parse the HTML response using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            td_elements = soup.find_all('td', class_='valor')

            # New Algorythm
            extracted_data = []  
            student_td_groups = []
            current_student_tds = [] 

            # Stundent array of td_elements creation
            for td_element in td_elements:
                if td_element.has_attr('width') and td_element['width'] == '70%' and 'valor' in td_element['class']:
                    if current_student_tds:
                        student_td_groups.append(current_student_tds)  
                        current_student_tds = []  
                current_student_tds.append(td_element)
            
            
            if current_student_tds:
                student_td_groups.append(current_student_tds)

            for group in student_td_groups:
                # Check the length of the group
                if len(group) == 7:
                    # Extract data from <td> elements and construct the JSON format
                    student_data = {
                        'name': group[0].text.strip(),
                        'email': group[1].text.strip().split(' ')[0],
                        'career': {
                            'student_id': group[2].text.strip(),
                            'program': group[3].text.strip(),
                            'department': group[4].text.strip(),
                            'type': group[5].text.strip(),
                            'status': group[6].text.strip()
                        }
                    }
                    # Append the student data to the list
                    extracted_data.append(student_data)
                else:
                    name = group[0].text.strip()
                    email = group[1].text.strip().split(' ')[0]
                    careers = []
                    for i in range(2, len(group), 5):
                        career_data = {
                            'student_id': group[i].text.strip(),
                            'program': group[i + 1].text.strip(),
                            'department': group[i + 2].text.strip(),
                            'type': group[i + 3].text.strip(),
                            'status': group[i + 4].text.strip()
                        }
                        careers.append(career_data)
                    # Construct the student data and append to extracted_data
                    student_data = {'name': name, 'email': email, 'careers': careers}
                    extracted_data.append(student_data)
                
            json_data = json.dumps(extracted_data, ensure_ascii=False)
            return json_data
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None


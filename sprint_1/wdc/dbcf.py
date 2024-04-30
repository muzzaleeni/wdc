import requests

class DatabaseConnection:
    def __init__(self, server_url):
        self.server_url = server_url

    def execute_query(self, query, output_file=None):
        """Executing WCPS query and save the output to a files """

        response = requests.post(self.server_url, data={'query': query})
        
        if response.status_code == 200:
            if output_file:
                with open(output_file, 'wb') as file:
                    file.write(response.content)
                print(f"Output saved in {output_file}")
            else:
                return response.content
        else:
            print("Fail !!!", response.status_code, response.text)

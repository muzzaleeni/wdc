#importing all the neccessary dependencies and libraries
import os
from PIL import Image
from io import BytesIO
import requests
from  dbc import *
import json

connection=DatabaseConnection
#datacube object which connect to the database conection object
class Datacube:
    def __init__(self):
        self.database_connection = DatabaseConnection("https://ows.rasdaman.org/rasdaman/ows")
        self.base_wcs_url = self.database_connection.base_wcs_url

    def execute_query(self, query):
        response = requests.post(self.base_wcs_url, params={"query": query})
        return response

datacube = Datacube()

#dictionary to keep the responses from the server also in a json file
all_responses = {}

def run_query(query):
    # executing query
    response = datacube.execute_query(query)
    print(response.status_code)

    if response.status_code != 200:
        if response.status_code==500:
            print("the server encountered an unexpected condition that prevented it from fulfilling the request")

    # checking response status and content
    if response.status_code == 200 and response.content:
        # processing response content as needed
        content_type = response.headers.get("Content-Type")
        print("Content-Type:", content_type)

        if content_type == "image/jpeg":
            img = Image.open(BytesIO(response.content))
            img.save("lazyuser/outputs/subset_image.jpg")
            print("Image saved successfully.")

        elif content_type == "image/png":
            img = Image.open(BytesIO(response.content))

            # Specify the filename for the results image
            results_filename = "lazyuser/outputs/results.png"

            # Check if the results image exists
            if os.path.exists(results_filename):
                # Open the existing results image
                results_img = Image.open(results_filename)

                # Create a new image with RGBA mode
                new_img = Image.new("RGBA", (max(img.width, results_img.width), img.height + results_img.height))

                # Paste the existing results image onto the new image
                new_img.paste(results_img, (0, 0))

                # Paste the new image onto the existing results image
                new_img.paste(img, (0, results_img.height))

                # Save the updated results image
                new_img.save(results_filename)
                new_img.close()
                print("Image saved successfully.")

            else:
                # If the results image doesn't exist, save the current image as the results image
                img.save(results_filename)


        elif content_type == "text/csv":
            decoded_content = response.content.decode("utf-8")
            all_responses["text"] = decoded_content
            with open("lazyuser/outputs/outputs.csv", "a", newline="") as csvfile:
            # Write the decoded content to the CSV file
                csvfile.write(decoded_content)
                print("Result saved successfully.")
            
        else:
            print("Can't identify the reponse type")
            decoded_content = response.content.decode("utf-8")
            all_responses["other"] = decoded_content
        with open("lazyuser/outputs/responses.json", "a") as json_file:
            json.dump(all_responses, json_file)
            #nor printing a newline
            json_file.write("\n")
    else:
        print("Query failed.")

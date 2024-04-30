from IPython.display import Image
from wdc.datacube_object import Datacube
from wdc.database_connection import DatabaseConnection
import matplotlib.pyplot as plt
import io

dbc = DatabaseConnection()

dco = Datacube(dbc, coverage_id='AvgTemperatureColorScaled', encode='image/png')


data = dco.get('2014-07')
# Image(data)

# Convert the image data to a format compatible with Matplotlib
image = plt.imread(io.BytesIO(data))
# Display the image using Matplotlib
plt.imshow(image)
plt.axis('off')  # Optional: Turn off axis
plt.show()

#modifying functionalities
modif_ans1 = {"ansi": "2000-02-01"}

subset_dc = dco.subset(modif_ans1)
data1 = subset_dc.execute()
# Image(data)
image1 = plt.imread(io.BytesIO(data1))
# Display the image using Matplotlib
plt.imshow(image1)
plt.axis('off')  # Optional: Turn off axis
plt.show()




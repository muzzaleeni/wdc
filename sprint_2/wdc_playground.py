from IPython.display import Image
from wdc.dco import Datacube
from wdc.dbc import DatabaseConnection
import matplotlib.pyplot as plt
import io

dbc = DatabaseConnection()

dco = Datacube(dbc, coverage_id='AvgTemperatureColorScaled', encode='image/png')

#modifying functionalities
dco1 = Datacube(dbc, coverage_id='AvgTemperatureColorScaled', encode='image/png')
modif_ans2 = {"ansi": "2000-04"}

subset_dc1 = dco1.slice(modif_ans2)
data2 = subset_dc1.execute()
# Image(data)
image2 = plt.imread(io.BytesIO(data2))
# Display the image using Matplotlib
plt.imshow(image2)
plt.axis('off')  # Optional: Turn off axis
plt.show()


dco_2 = Datacube(dbc, coverage_id='AvgLandTemp', encode='text/csv')
subset = {"ansi": ("2014-01", "2014-12"), "Lat": (53.08), "Lon": (8.80)}
dco_1D = dco_2.slice(subset)
data_bytes = dco_1D.execute()
data_str = data_bytes.decode('utf-8')
y_values = [float(val) for val in data_str.split(',')]

x_values = range(len(y_values))

plt.plot(x_values, y_values)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title(f'{dco_1D.coverage_id}')
plt.grid(True)
plt.show()

data = dco.get('2014-07')
Image(data)

# Convert the image data to a format compatible with Matplotlib
image = plt.imread(io.BytesIO(data))
# Display the image using Matplotlib
plt.imshow(image)
plt.axis('off')  # Optional: Turn off axis
plt.show()

#modifying functionalities
modif_ans1 = {"ansi": "2000-02-01"}

subset_dc = dco.slice(modif_ans1)
data1 = subset_dc.execute()
Image(data)
image1 = plt.imread(io.BytesIO(data1))
# Display the image using Matplotlib
plt.imshow(image1)
plt.axis('off')  # Optional: Turn off axis
plt.show()



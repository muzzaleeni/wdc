from IPython.display import Image
from wdc.dco import Datacube
from wdc.dbc import DatabaseConnection
import matplotlib.pyplot as plt
import io

dbc = DatabaseConnection()

dco = Datacube(dbc, coverage_id='AvgTemperatureColorScaled', encode='image/png')
#---------------------------- 1 -----------------------------#
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
#---------------------------- 2 -----------------------------#
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
# plt.show()

#---------------------------- 3 -----------------------------#
data = dco.get('2014-07')
# Image(data)

# Convert the image data to a format compatible with Matplotlib
image = plt.imread(io.BytesIO(data))
# Display the image using Matplotlib
plt.imshow(image)
plt.axis('off')  # Optional: Turn off axis
# plt.show()

#---------------------------- 4 -----------------------------#
#modifying functionalities
modif_ans1 = {"ansi": "2000-02-01"}

subset_dc = dco.slice(modif_ans1)
data1 = subset_dc.execute()
# Image(data)
image1 = plt.imread(io.BytesIO(data1))
# Display the image using Matplotlib
plt.imshow(image1)
plt.axis('off')  # Optional: Turn off axis
# plt.show()




#---------------------------- 6 -----------------------------#
#Failing cannot be covered by the server
 # raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error:  for url: https://ows.rasdaman.org/rasdaman/ows?service=WCS&version=2.1.0&request=ProcessCoverage&query=for%20%24c%20in%20%28AvgLandTemp%29%20return%20encode%28%24c%5Bansi%28%222014-01%22%3A%222015-10%22%29%2C%20Lat%2853.08%29%2C%20Lon%288.8%29%5D%2C%20%22text/csv%22%29

#UNCOMENT THE CODE WHEN YOU PASTE IT IN JUPYTER
# dco3 = Datacube(dbc, coverage_id='AvgLandTemp', encode='text/csv')
# subset1 = {"ansi": ("2014-01", "2015-10"), "Lat": (53.08), "Lon": (8.80)}
# dco_1D1 = dco3.slice(subset1)
# data_bytes1 = dco_1D1.execute()
# data_str1 = data_bytes1.decode('utf-8')
# y_valuess = [float(val) for val in data_str1.split(',')]
#
# x_valuess = range(len(y_valuess))
#
# plt.plot(x_valuess, y_valuess)
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.title(f'{dco_1D1.coverage_id}')
# plt.grid(True)
# # plt.show()
#
#
#

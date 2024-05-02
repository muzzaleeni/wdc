from IPython.display import Image
from wdc.dco import Datacube
from wdc.dbc import DatabaseConnection
import matplotlib.pyplot as plt
import io



con = DatabaseConnection()


#---------------------------- 1 -----------------------------#
#modifying functionalities
datacube = Datacube(con, coverage_id='AvgTemperatureColorScaled', encode='image/png')
modify_ans = {"ansi": "2000-04"}
slice_datacube = datacube.slice(modify_ans)
datat = slice_datacube.execute()
# Image(data)
image2 = plt.imread(io.BytesIO(datat))
# Display the image using Matplotlib
plt.imshow(image2)
plt.axis('off')  # Optional: Turn off axis
plt.show()


#---------------------------- 2 -----------------------------#
datacube1 = Datacube(con, coverage_id='AvgLandTemp', encode='text/csv')
subset = {"ansi": ("2014-01", "2014-12"), "Lat": (53.08), "Lon": (8.80)}
slice_datacube1 = datacube1.slice(subset)
data_bytes = slice_datacube1.execute()
data_str = data_bytes.decode('utf-8')
y_values = [float(val) for val in data_str.split(',')]

x_values = range(len(y_values))

plt.plot(x_values, y_values)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title(f'{slice_datacube1.coverage_id}')
plt.grid(True)
plt.show()

#---------------------------- 3 -----------------------------#
datacube2 = Datacube(con, coverage_id='AvgTemperatureColorScaled', encode='image/png')
datat1 = datacube2.get('2014-07')
Image(datat1)
# Convert the image data to a format compatible with Matplotlib
image = plt.imread(io.BytesIO(datat1))
# Display the image using Matplotlib
plt.imshow(image)
plt.axis('off')  # Optional: Turn off axis
plt.show()

#---------------------------- 4 -----------------------------#
#modifying functionalities of datacube2
modify_ans1 = {"ansi": "2000-02-01"}
subset_dc = datacube2.slice(modify_ans1)
data1 = subset_dc.execute()
Image(data1)
image1 = plt.imread(io.BytesIO(data1))
# Display the image using Matplotlib
plt.imshow(image1)
plt.axis('off')  # Optional: Turn off axis
plt.show()

#---------------------------- 5 -----------------------------#
datacube1 = Datacube(con, coverage_id='AvgLandTemp', encode='text/csv')
subset = {"ansi": ("2014-01", "2016-12"), "Lat": (53.08), "Lon": (8.80)}
slice_datacube1 = datacube1.slice(subset)
data_bytes = slice_datacube1.execute()
data_str = data_bytes.decode('utf-8')
y_values = [float(val) for val in data_str.split(',')]

x_values = range(len(y_values))

plt.plot(x_values, y_values)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title(f'{slice_datacube1.coverage_id}')
plt.grid(True)
plt.show()
#  raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error:  for url: https://ows.rasdaman.org/rasdaman/ows?service=WCS&version=2.1.0&request=ProcessCoverage&query=for%20%24c%20in%20%28AvgLandTemp%29%20return%20encode%28%24c%5Bansi%28%222014-01%22%3A%222016-12%22%29%2C%20Lat%2853.08%29%2C%20Lon%288.8%29%5D%2C%20%22text/csv%22%29


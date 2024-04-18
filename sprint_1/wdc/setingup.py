from wdc import Datacube, DatabaseConnection

def main():
    server_url = 'https://ows.rasdaman.org/rasdaman/ows'
    dbcf = DatabaseConnection(server_url)
    dcof = Datacube(dbcf)

    query = 'for c in (mean_summer_airtemp) return encode(c, "png")'
    dcof.fetch_png_image(query, 'output.png')

if __name__ == '__main__':
    main()

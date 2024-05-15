# from ../datacube_obj1.py import Datacube
from .lazyuserdco import run_query



# -------------------AvgLandTemp Query-------------------------------
query1 = '''
for $c in ( AvgLandTemp )
 return encode(
            $c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")]
        , "text/csv")
'''

query2='''
for $c in ( AvgLandTemp ) 
return encode(
    switch 
            case $c[ansi("2014-07"), Lat(35:75), Long(-20:40)] = 99999 
                return {red: 255; green: 255; blue: 255} 
            case 18 > $c[ansi("2014-07"), Lat(35:75), Long(-20:40)] 
                return {red: 0; green: 0; blue: 255} 
            case 23 > $c[ansi("2014-07"), Lat(35:75), Long(-20:40)] 
                return {red: 255; green: 255; blue: 0} 
            case 30 > $c[ansi("2014-07"), Lat(35:75), Long(-20:40)]  
                return {red: 255; green: 140; blue: 0} 
            default return {red: 255; green: 0; blue: 0}
        , "image/png")
'''

query3='''
for $c in ( AvgLandTemp ) 
 return encode(
                $c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")] 
                + 273.15
        , "text/csv")
'''
query4='''
for $c in (AvgLandTemp) 
return 
    min($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

query5='''
for $c in (AvgLandTemp)
return 
    max($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

query6='''
for $c in (AvgLandTemp)
return count(
                $c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")]
            > 15)
'''
query7='''
for $c in ( AvgLandTemp ) 
return encode(
                coverage myCoverage
                over $p x(0:200),
                     $q y(0:200)
                values $p + $q
    , "image/png")
'''
# -------------------------AvgTemperatureColor Query---------------------------------
query8= '''
image>>for $c in ( AvgTemperatureColor )
 return encode(
               $c[ansi("2014-07")]
        , "image/png")
'''

query9= ''' 
for $c in (AvgTemperatureColor) 
return 
    min($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

query10= '''
for $c in (AvgTemperatureColor)
return 
    max($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

query11= '''
for $c in (AvgTemperatureColor)
return 
    avg($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

query12='''
image>>for $c in ( AvgTemperatureColor ) 
return encode(
                coverage myCoverage
                over $p x(0:200),
                     $q y(0:200)
                values $p + $q
    , "image/png")
'''

# -------------------C3S_satellite_soil_moisture_active_daily_sensor Query--------------------------
query13= '''
image>>for $c in ( C3S_satellite_soil_moisture_active_daily_sensor ) 
return encode(
                coverage myCoverage
                over $p x(0:200),
                     $q y(0:200)
                values $p + $q
    , "image/png")
'''

query14='''
for $c in (C3S_satellite_soil_moisture_active_daily_sensor) 
return 
    min($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

query15='''
for $c in (C3S_satellite_soil_moisture_active_daily_sensor)
return 
    max($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

query16= '''
diagram>>for $c in ( C3S_satellite_soil_moisture_active_daily_sensor )
 return encode(
            $c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-09")]
        , "text/csv")
'''

query17= '''
for $c in (C3S_satellite_soil_moisture_active_daily_sensor)
return 
    avg($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''

# -----------------------RadianceColorScaled Query ----------------------------------

query18= '''
image>>for $c in ( RadianceColorScaled )
 return encode(
               $c[ansi("2014-07")]
        , "image/png")
'''

query19= '''
for $c in (RadianceColorScaled)
return 
    avg($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''
query20='''
for $c in (RadianceColorScaled)
return 
    max($c[Lat(53.08), Long(8.80), ansi("2014-01":"2014-12")])
'''
#-----------------------------------Others--------------------------

query='''
for $c in (S2_L2A_32631_B12_20m),
    $d in (S2_L2A_32631_B08_10m),
    $e in (S2_L2A_32631_B03_10m)
let $cutOut := [ ansi( "2021-04-09" ), E( 670000:730000 ), N( 4990220:5015220 ) ]
return
    encode( { red: $c[ $cutOut ]; green: $d[ $cutOut ]; blue: $e[ $cutOut ] } / 15.0,
            "image/png"
)'''
# Run the query
''' run_query(query)
run_query(query1)
run_query(query_not_working)
run_query(query2)
run_query(query3)
run_query(query4)
run_query(query5) '''

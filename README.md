## !!Must read!!

    The first sprint was hadcoding one query, the one in example on Teams channel, so the only functions we could make use of were the DataBaseConnection and some code from the Datacube object
    The parameters of the __init__ function of the CoverageQuery class from the sprint_1/wdc/connectionras.py have been integrated in sprint_2/wdc/wrapper/coverages.py classes and functions

- connectionras.py/class CoverageQuery:
  self.base_wcs_url = base_wcs_url
  self.base_wcps_url = base_wcps_url
  self.coverage_id = coverage_id
  self.time_subset = None
  self.spatial_subset_e = None
  self.spatial_subset_n = None
  self.format = "image/jpeg"

- wrapper/Coverages:
  request_url = f"{self.base_wcs_url}&request=GetCoverage&coverageId={self.coverage_id}&FORMAT={self.output_format}
  self.connection = connection
  self.coverage_id = coverage_id
  self.subset = subset
  self.output_format = output_format

-

## points

-
-
-

twice ##, three times "normal"

# Jubgiu

## jhvj

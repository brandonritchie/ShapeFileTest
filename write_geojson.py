import requests
from geojson import dump

def write_geojson(url, file_name):
    r = requests.get(url)
    with open(f'C:\\Users\\britchie\\OneDrive - AgReserves, Inc\\Documents\\ShapeFileTest\\{file_name}.geojson', 'w') as f:
        dump(r.json(), f)

if __name__ == "__main__":
    url = 'https://hdqgisweb2.agreserves.com/arcgis/rest/services/TEST/NavasotaRanchKML/MapServer/14/query?where=1%3D1&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=*&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=geojson'
    file_name = 'NavasotaShape'
    write_geojson(url, file_name)
    print(f"{file_name}.geojson saved at ShapeFileTest\{file_name}.geojson")

#Test
@echo off
"C:\Users\britchie\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\Python 3.10 (64-bit).lnk" "C:\Users\britchie\OneDrive - AgReserves, Inc\Documents\ShapeFileTest\write_geojson.py"

cd C:\Users\britchie\OneDrive - AgReserves, Inc\Documents\ShapeFileTest
git add .
git commit -am "Shape data changes"
git push
echo Press Enter...
read
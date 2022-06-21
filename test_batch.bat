@echo off
"C:\Users\britchie\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\Python 3.10 (64-bit).lnk" "C:\Users\britchie\OneDrive - AgReserves, Inc\Documents\ShapeFileTest\write_geojson.py"

pause

#!/bin/sh
cd C:\Users\britchie\OneDrive - AgReserves, Inc\Documents\ShapeFileTest
git add .
git commit -am "made changes"
git push
echo Press Enter...
read
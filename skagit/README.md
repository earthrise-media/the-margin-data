# Skagit

## Rivers
River shapefiles come from the National Weather Service: https://www.weather.gov/gis/Rivers accessed September 20, 2022. `skagit-river.geojson` contains geometry for the Skagit River in GeoJSON format. 

## Dams
Dam Data comes from the US Army's National Inventory of Dams: https://nid.usace.army.mil/#/ accessed September 20, 2022. Hydroelectric dams were identified by filtering on Dams whose `Primary Purpose` was `Hydroelectric`. `hydroelectric-dams.geojson` contains the 2,136 points in whose primary purpose is Hydroelectric. 

The Hydroelectric Dam animation was created in Observable, you can view and fork the code here: https://observablehq.com/@ejfox/hydroelectric-dam-animation
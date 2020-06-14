import overpy
import geopandas as gpd
import pandas as pd
import json
import time
from shapely.geometry import Point


class Poi:

    """This class fetch PoIs from Overpass Api for a specific area."""
    
    tags = {'tourism', 'shop', 'office', 'historic', 'craft', 'emergency', 'station', 'public_transport', 'amenity'}

    __lastcall = 0
    
    def __init__(self, city):
        self.city = city
        self.__init_overpass_api()

    def __init_overpass_api(self):

        self.__api = overpy.Overpass()

        nodes = pd.DataFrame(columns = ["Latitude","Longitude","Tag"])
        result = self.__query_overpass_api(self.tags)
        for node in result.nodes:
            for tag in node.tags.keys():
                if(tag in self.tags):
                    nodes.loc[len(nodes)] = [node.lat,node.lon,tag]

        gdf = gpd.GeoDataFrame(
            nodes, geometry=gpd.points_from_xy(nodes.Longitude, nodes.Latitude), crs = 'EPSG:4326')

        self.gdf = gdf.drop(columns=['Latitude','Longitude']).to_crs('EPSG:2163')

    def __query_overpass_api(self, tags):
        self.__lastcall = time.time()
        
        query_string = ''
        
        for tag in tags:
            query_string += 'area[name="'+ self.city + '"]; ('
            query_string += 'node["'+ tag +'"](area);'            
            query_string += '); out;'
        
        return self.__api.query(query_string)

       
    def closest(self, lon, lat, distance = 5):
        """Find closest PoI near the point"""
        gpdBuffer = gpd.GeoDataFrame(geometry = [Point(lon,lat)], crs = 'EPSG:4326').to_crs('EPSG:2163')
        buffer_length_in_km = (distance * 1000)
        gpdBuffer = gpdBuffer.buffer(buffer_length_in_km)
        
        tmp = self.gdf[self.gdf.geometry.intersects(gpdBuffer.loc[0])]
        result = pd.DataFrame(columns=self.tags)
        for tag in self.tags:
            result[tag] = tmp[tmp['Tag'] == tag].count()    
        result = result.drop('geometry', axis = 0)
        
        return result

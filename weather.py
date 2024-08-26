import requests

class IPGeo: 

    data = None
    lat = None
    lon = None

    def __init__(self): 
        self.geo()

    def geo(self): 
        """
        Poke the Internet and geolocate the source (first routable) IP 
        """

        # Techniknews.net free IP geolocation API, this URI maps your routable Internet address to the 
        # lat/long of its owner
        ip_geo_url='https://api.techniknews.net/ipgeo'

        response = requests.get(ip_geo_url)
        if response.ok: 
            try: 
                self.data = response.json()
                self.lat = self.data['lat']
                self.lon = self.data['lon']
            except KeyError as k:
                print('Failed to unpack IP geolocation response')

class Forecast: 
    
    data = None    
    forecast_url = None
    station = None
    location = None
    forecast = None

    def __init__(self): 
        pass

    def resolve_location(self, lat, lon): 
        """
        retrieve a US forecast given a lat/lon pair
        """
        
        # Resolve our location ... e.g. https://api.weather.gov/points/39.7456,-97.0892
        points_base_url = "https://api.weather.gov/points/"
        points_url = points_base_url + str(lat) + ',' + str(lon)

        response = requests.get(points_url)
        if response.status_code == 200: 
            self.data = response.json()['properties']
            
            self.forecast_url = self.data['forecast']
            self.station = self.data['cwa']

            loc = self.data['relativeLocation']['properties']
            self.location = loc['city'] + ', ' + loc['state']

    def update_forecast(self):
        """
        grab the forecast, requires location resolution be updated prior
        """
        if self.forecast_url: 
            
            response = requests.get(self.forecast_url) 
            if response.status_code == 200: 
                
                self.forecast = []
                
                for period in response.json()['properties']['periods']: 
                    if period['number'] <= 7:
                        self.forecast.append(
                            "Day " 
                            + str(period['number']) 
                            + ": " 
                            + period['detailedForecast']
                        )
            else: 
                raise Exception("Forecast URL (" + self.forecast_url + ") returned unexpected code: " + str(response.status_code))

        else: 
            raise Exception("No forecast URL found!")

class Precipitation(): 

    def __init__(self): 
        pass

    def get_precipitation(self): 

        noaa_token='HGSaAdFuTwXNcAgyrbysQlUXxBTTxsjY'
        noaa_url='https://www.ncei.noaa.gov/cdo-web/api/v2/datasets/PRECIP_HLY'

        # Datasets are at, https://www.ncei.noaa.gov/cdo-web/api/v2/datasets/  A query to this endpoint
        # returns the full list, we care bsaout the hourly precip data: 
        #   {'uid': 'gov.noaa.ncdc:C00313',
        #    'mindate': '1900-01-01',
        #    'maxdate': '2014-01-01',
        #    'name': 'Precipitation Hourly',
        #    'datacoverage': 1,
        #    'id': 'PRECIP_HLY'}]}
        headers = { 'token' : noaa_token }

        response = requests.get(noaa_url, headers=headers)

        print(response.json())


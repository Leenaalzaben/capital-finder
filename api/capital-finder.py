from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    api_path = self.path 
    url_components = parse.urlsplit(api_path)
    query_list = parse.parse_qsl(url_components.query)
    my_dictionary = dict(query_list)
    
    country = my_dictionary.get('country')
    capital = my_dictionary.get('capital')
    display = ''

    if country:
       url = 'https://restcountries.com/v3.1/name/'
       country_name = requests.get(url + country)
       json_file = country_name.json()
       for country_info in json_file:
           show = country_info['capital'][0]
           display = f"The capital of {country} is {show}"

    elif capital:
        url = 'https://restcountries.com/v3.1/capital/'
        r = requests.get(url + capital)
        json_file = r.json()
        for country_info in json_file:
            show = country_info['name']['common']
            display = f"{capital} is the capital of {show}."
    
    self.wfile.write(str(display).encode())
    print(display)

    return

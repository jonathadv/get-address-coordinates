# get-address-coordinates
Script to retrieve addresses' coordinates in bulk from GoogleMaps API and save the information as JSON.


**Requires:**
* Python3
* python-requests (http://docs.python-requests.org)

**Usage:** `./get_address_coordinates.py`


This script expects a file called *addresses.text* formatted as explained below.

---

### addresses.txt file format
```
#CityName1
Address1
Address2
Address3
Address4

#CityName2
Address5
Address6
Address7
Address8
```

### Sample
```
#Porto Alegre
Avenida Cristóvão Colombo, 1824
Rua Landel Moura, 551
Avenida Protásio Alves, 555
Avenida Cristóvão Colombo, 545
Rua Barão Tramandai, 246
Avenida Mostardeiro,, 597
Avenida Avenida, 768 204
Avenida Forte Do, 1353
Rua Miguel Tostes, 941
Avenida Juca Batista, 665
Avenida Protásio Alves, 555
Rua Doutor  Flores, 27
```

---

### Console Output
```
Setting city as Porto Alegre
[GET to Maps API] - Address: (Avenida Cristóvão Colombo, 1824 Porto Alegre)
addressObject: address = [Av. Cristóvão Colombo, 1824 - Floresta, Porto Alegre - RS, 90560-002, Brazil], latitude = [-30.0181229], longitude = [-51.2028571]
[GET to Maps API] - Address: (Rua Landel Moura, 551 Porto Alegre)
addressObject: address = [R. Landel de Moura, 551 - Tristeza, Porto Alegre - RS, 91920-150, Brazil], latitude = [-30.1161201], longitude = [-51.2547028]
[GET to Maps API] - Address: (Avenida Protásio Alves, 555 Porto Alegre)
addressObject: address = [Av. Protásio Alves, 555 - Alto Petrópolis, Porto Alegre - RS, Brazil], latitude = [-30.038557], longitude = [-51.2026718]
[GET to Maps API] - Address: (Avenida Cristóvão Colombo, 545 Porto Alegre)
addressObject: address = [Av. Cristóvão Colombo, 545 - Floresta, Porto Alegre - RS, 90560-003, Brazil], latitude = [-30.0255108], longitude = [-51.2123441]
[GET to Maps API] - Address: (Rua Barão Tramandai, 246 Porto Alegre)
addressObject: address = [R. Barão de Tramandaí, 246 - Passo d'Areia, Porto Alegre - RS, 91030-380, Brazil], latitude = [-30.008439], longitude = [-51.1705036]
[GET to Maps API] - Address: (Avenida Mostardeiro,, 597 Porto Alegre)
addressObject: address = [R. Mostardeiro, 597 - Moinhos de Vento, Porto Alegre - RS, 90430-000, Brazil], latitude = [-30.0286244], longitude = [-51.2010288]
[GET to Maps API] - Address: (Avenida Avenida, 768 204 Porto Alegre)
addressObject: address = [Avenida Assis Brasil, Porto Alegre - RS, Brazil], latitude = [-29.9730133], longitude = [-51.1245677]
[GET to Maps API] - Address: (Avenida Forte Do, 1353 Porto Alegre)
addressObject: address = [Av. do Forte, 1353 - Vila Ipiranga, Porto Alegre - RS, Brazil], latitude = [-30.0226412], longitude = [-51.1515332]
[GET to Maps API] - Address: (Rua Miguel Tostes, 941 Porto Alegre)
addressObject: address = [R. Miguel Tostes, 941 - Rio Branco, Porto Alegre - RS, 90430-061, Brazil], latitude = [-30.0365668], longitude = [-51.2058782]
[GET to Maps API] - Address: (Avenida Juca Batista, 665 Porto Alegre)
addressObject: address = [Av. Juca Batista, 665 - Ipanema, Porto Alegre - RS, 91770-000, Brazil], latitude = [-30.1398443], longitude = [-51.2205277]
[GET to Maps API] - Address: (Avenida Protásio Alves, 555 Porto Alegre)
addressObject: address = [Av. Protásio Alves, 555 - Alto Petrópolis, Porto Alegre - RS, Brazil], latitude = [-30.038557], longitude = [-51.2026718]
[GET to Maps API] - Address: (Rua Doutor  Flores, 27 Porto Alegre)
addressObject: address = [R. Dr. Flores, 27 - Centro Histórico, Porto Alegre - RS, Brazil], latitude = [-30.0273365], longitude = [-51.2246625]
File addresses.json save!
File addresses_fail.txt save!
```

---


### File output

***addresses.json***

A file with the retrieved addresses in JSON format.

```json
{ "address": "Av. Cristóvão Colombo, 1824 - Floresta, Porto Alegre - RS, 90560-002, Brazil", "latitude": -30.0181229, "longitude": -51.2028571 }
{ "address": "R. Landel de Moura, 551 - Tristeza, Porto Alegre - RS, 91920-150, Brazil", "latitude": -30.1161201, "longitude": -51.2547028 }
{ "address": "Av. Protásio Alves, 555 - Alto Petrópolis, Porto Alegre - RS, Brazil", "latitude": -30.038557, "longitude": -51.2026718 }
{ "address": "Av. Cristóvão Colombo, 545 - Floresta, Porto Alegre - RS, 90560-003, Brazil", "latitude": -30.0255108, "longitude": -51.2123441 }
{ "address": "R. Barão de Tramandaí, 246 - Passo d'Areia, Porto Alegre - RS, 91030-380, Brazil", "latitude": -30.008439, "longitude": -51.1705036 }
{ "address": "R. Mostardeiro, 597 - Moinhos de Vento, Porto Alegre - RS, 90430-000, Brazil", "latitude": -30.0286244, "longitude": -51.2010288 }
{ "address": "Avenida Assis Brasil, Porto Alegre - RS, Brazil", "latitude": -29.9730133, "longitude": -51.1245677 }
{ "address": "Av. do Forte, 1353 - Vila Ipiranga, Porto Alegre - RS, Brazil", "latitude": -30.0226412, "longitude": -51.1515332 }
{ "address": "R. Miguel Tostes, 941 - Rio Branco, Porto Alegre - RS, 90430-061, Brazil", "latitude": -30.0365668, "longitude": -51.2058782 }
{ "address": "Av. Juca Batista, 665 - Ipanema, Porto Alegre - RS, 91770-000, Brazil", "latitude": -30.1398443, "longitude": -51.2205277 }
{ "address": "Av. Protásio Alves, 555 - Alto Petrópolis, Porto Alegre - RS, Brazil", "latitude": -30.038557, "longitude": -51.2026718 }
{ "address": "R. Dr. Flores, 27 - Centro Histórico, Porto Alegre - RS, Brazil", "latitude": -30.0273365, "longitude": -51.2246625 }

```

***addresses_fail.txt***

A file with the list of address the script failed to retrieve.

```
A non-existent address 1
A non-existent address 2
A non-existent address 3
```

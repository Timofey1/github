import xml.dom.minidom as minidom

doc = minidom.parse("map.xml")
# node = doc.documentElement
nodes = doc.getElementsByTagName("node")
print(len(nodes))
print(nodes[0].attributes["id"].value)

DATA = []
for node in nodes:
    id = node.attributes['id'].value
    lat = node.attributes['lat'].value
    lon = node.attributes['lon'].value
    print(id,lat,lon)
    DATA.append(dict(id=id,lat=lat,lon=lon))
print(DATA)


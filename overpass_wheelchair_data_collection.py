import overpy

api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
    area[name="Москва"];
    node[wheelchair=yes](area);
    out body;
    """)

for node in result.nodes:
    print("Name: %s" % node.tags.get("name", "n/a"))
    print("wheelchair: %s" % node.tags.get("wheelchair", "n/a"))
    # print("  Nodes:")
    # for node in way.nodes:
    #     print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
import xml.etree.ElementTree as ET
tree = ET.parse('CDcatalog.xml')
catalog = tree.getroot()

# Iterating through the children of root
for cd in catalog:
    for title in cd.findall("title"):
        print(title.text)

# This does the same but using XPath
# All 'title' grand-children of 'book' children of the top-level elements
print("******* Using XPath *******")
for artist in catalog.findall("./CD/title/artist"):
    print(artist.text)

# Accessing particular elements
print(catalog[0][1].get('lang'))

# Nodes with category='fantasy' that have a 'published' child
print(catalog.findall(".//published/..[@category='fantasy']"))

# 'published' nodes that are children of nodes with category='fantasy'
print(catalog.findall(".//*[@category='fantasy']/published"))
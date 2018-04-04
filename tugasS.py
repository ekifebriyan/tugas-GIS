import mapnik
m = mapnik.Map(3840,2160)
m.background = mapnik.Color('steelblue')
# MAP 1 INDO DESA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFF00')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('EKI',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_desa/Indo_Desa_region.shp")
layer = mapnik.Layer('desa')
layer.datasource = ds
layer.styles.append('EKI')
m.layers.append(layer)
# INDO DESA

# MAP 2 INDO KABUPATEN
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#D2691E')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('EKI',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_kabupaten/INDONESIA_KAB.shp")
layer = mapnik.Layer('kabupaten')
layer.datasource = ds
layer.styles.append('EKI')
m.layers.append(layer)
# INDO KABUPATEN

# MAP 3 INDO KECAMATAN
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#00FFFF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('EKI',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_kecamatan/INDONESIA_KEC.shp")
layer = mapnik.Layer('kecamatan')
layer.datasource = ds
layer.styles.append('EKI')
m.layers.append(layer)
# BATAS KECAMATAN

# MAP 4 JAWA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF0000')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('EKI',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_provinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('provinsi')
layer.datasource = ds
layer.styles.append('EKI')
m.layers.append(layer)
# BATAS PROVBINSI

# MAP 5 JAWA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF00FF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('EKI',s)
ds = mapnik.Shapefile(file="SHP_Indonesia_Kota/IND_KOT_text.shp")
layer = mapnik.Layer('kota')
layer.datasource = ds
layer.styles.append('EKI')
m.layers.append(layer)
# BATAS JALAN UTAMA

m.zoom_all()
mapnik.render_to_file(m,'tugasS.pdf','pdf')
print "rendered image to 'tugasS.pdf '"
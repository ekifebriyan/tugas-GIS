import mapnik
m = mapnik.Map(1320,640)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#cc0099')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')


r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('eki',s)
ds = mapnik.Shapefile(file="eki gis/shp kecamatan/batas_kecamatan.shp")
layer = mapnik.Layer('kecamatan')
layer.datasource = ds 
layer.styles.append('eki')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'kecamatan.png', 'png')
print "rendered image to 'kecamatan.png'"

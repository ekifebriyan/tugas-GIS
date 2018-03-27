import mapnik
m = mapnik.Map(1220,440)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#996633')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')


r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('eki',s)
ds = mapnik.Shapefile(file="eki gis/shp kabupaten/batas_kab.shp")
layer = mapnik.Layer('kabupaten')
layer.datasource = ds 
layer.styles.append('eki')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'kabupaten.pdf', 'pdf')
print "rendered image to 'kabupaten.pdf'"

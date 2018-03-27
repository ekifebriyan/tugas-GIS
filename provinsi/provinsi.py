import mapnik
m = mapnik.Map(1220,740)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#009900')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')


r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('eki',s)
ds = mapnik.Shapefile(file="eki gis/shp provinsi/batas_prov.shp")
layer = mapnik.Layer('provinsi')
layer.datasource = ds 
layer.styles.append('eki')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'provinsi.pdf', 'pdf')
print "rendered image to 'provinsi.pdf'"

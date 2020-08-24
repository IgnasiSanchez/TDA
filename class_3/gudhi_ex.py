import gudhi as gd

cplx = gd.RipsComplex(points=[[0,0], [1,2], [2,1], [4,3], [4,-3]])
stree = cplx.create_simplex_tree(max_dimension=5)

for x in stree.get_filtration():
	print(x)

diag = stree.persistence(min_persistence=0.01)
plot = gd.plot_persistence_barcode(diag)
plot.show()
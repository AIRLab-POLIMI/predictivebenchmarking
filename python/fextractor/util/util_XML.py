import numpy as np
import xml.etree.cElementTree as ET
from xml.etree import ElementTree


def crea_xml(nome_xml_segmentato,spazi):
	'''
	Creo xml delle stanze segmentate.
	'''
	#------------------CREO XML--------------------------------------------------------------------

	import uuid
	id_stanze = []
	for s in spazi:
		id_stanze.append(uuid.uuid1())


	xml = open(nome_xml_segmentato, "w")
	xml_id = uuid.uuid1()
	xml.write('<building id="'+str(xml_id)+'">\n<name>'+str(nome_xml_segmentato)+'</name>\n<scale>\n<represented_distance>\n<value>10</value>\n<um>pixel</um>\n</represented_distance>\n<real_distance>\n<value>90</value>\n<um>cm</um>\n</real_distance>\n</scale>\n<Info>Inserire informazioni sull\'edificio</Info>\n<building_type>\n<main_type>SCHOOL</main_type>\n</building_type>\n<floor>\n<spaces>\n')
	for i,s in enumerate(spazi):
		#indice_gt_corrisp = indici_gt_corrispondenti_fwd[i]
		xml.write('<space id="'+str(id_stanze[i])+'">\n')	
		xml.write('<partial_room>\n<parziale ="'+str(s.parziale)+'"/>\n</partial_room>\n')	
	

		xml.write('<centroid>\n<point x="'+str(int(s.spazio.centroid.x))+'" y="'+str(int(s.spazio.centroid.x))+'" />\n</centroid>\n<bounding_box>\n<maxx>\n<point x="'+str(int(s.spazio.bounds[2]))+'" y="'+str(int(s.spazio.bounds[3]))+'" />\n</maxx>\n<maxy>\n<point x="'+str(int(s.spazio.bounds[2]))+'" y="'+str(int(s.spazio.bounds[3]))+'" />\n</maxy>\n<minx>\n<point x="'+str(int(s.spazio.bounds[0]))+'" y="'+str(int(s.spazio.bounds[1]))+'" />\n</minx>\n<miny>\n<point x="'+str(int(s.spazio.bounds[0]))+'" y="'+str(int(s.spazio.bounds[1]))+'" />\n</miny>\n</bounding_box>\n<bounding_polygon>\n')
		if s.spazio.boundary.type is 'MultiLineString':
			for l in s.spazio.boundary:
				b = l.coords.xy
				for n in xrange(0,len(b[0])):
					xml.write('<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n')
		
			xml.write('</bounding_polygon>\n<space_representation>\n')
			for l in s.spazio.boundary:
				b = l.coords.xy
				for n in xrange(0,len(b[0])-1):
					xml.write('<linesegment id="'+str(uuid.uuid1())+'">\n<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n<point x="'+str(int(b[0][n+1]))+'" y="'+str(int(b[1][n+1]))+'" />\n<class>WALL</class>\n<type>EXPLICIT</type>\n<features>NORMAL</features>\n</linesegment>\n')
	
		else:	
			b = s.spazio.boundary.coords.xy
			for n in xrange(0,len(b[0])):
				xml.write('<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n')

			xml.write('</bounding_polygon>\n<space_representation>\n')
			for n in xrange(0,len(b[0])-1):
				xml.write('<linesegment id="'+str(uuid.uuid1())+'">\n<point x="'+str(int(b[0][n]))+'" y="'+str(int(b[1][n]))+'" />\n<point x="'+str(int(b[0][n+1]))+'" y="'+str(int(b[1][n+1]))+'" />\n<class>WALL</class>\n<type>EXPLICIT</type>\n<features>NORMAL</features>\n</linesegment>\n')

		
		xml.write('</space_representation>\n')
	
		xml.write('</space>\n')

	xml.write('</spaces>\n</floor>\n</building>')
	xml.close()
	
	return id_stanze

data_format = (('Lot','Artist','Nationality'), ('Low','High','Sale'), ('Height','Width'), ('Date','DateProvided','DateSigned'))


# First data set: 19th Century European Paintings
# 24 May 2018, 2:00 PM BST, London
# Prices in GBP
#
set1 = [ (( 1,'Giovanni Boldini','Italian'), (50000,70000,0), (14,23.5), (1876,True,False)),  # date in catalog
         (( 2,'Federico del Campo','Peruvian'), (150000,200000,0), (36,60), (1899,True,True)),
         (( 3,'Jean-Baptiste-Camille Corot','French'), (200000,300000,249000), (43,62), (1865,True,False)),
         (( 4,'Emile Claus','Belgian'), (100000,150000,0), (49,65), (1881,True,False)),  # date is my guess from materials...they say "early 1880s"
         (( 5,'Anders Zorn','Swedish'), (200000,300000,0), (180,100), (1916,True,True)),
         (( 6,'Peder Severin Krøyer','Danish'), (400000,600000,0), (86,66), (1896,True,True)),
         (( 7,'Helene Schjerfbeck','Finnish'), (70000,100000,0), (29,33), (1942,True,False)),
         (( 8,'Anders Zorn','Swedish'), (400000,600000,429000), (98.5,62.5), (1918,True,True)),
         (( 9,'Joaquín Sorolla','Spanish'), (100000,150000,112500), (15.5,22), (1906,True,True)),
         ((10,'Eliseo Meifrén','Spanish'), (25000,35000,25000), (80,100), (1900,False,False)),  # date is artist life midpoinnt
         ((11,'Joaquín Sorolla','Spanish'), (60000,80000,0), (19,24), (1919,True,False)),
         ((12,'Joaquín Sorolla','Spanish'), (50000,70000,0), (50,39.5), (1903,True,True)),
         ((13,'Darío de Regoyos','Spanish'), (15000,20000,18750), (48,30), (1882,True,False)),
         ((14,'Hermenegildo Anglada-Camarasa','Spanish'), (40000,60000,0), (40,74.5), (1915,False,False)),  # life midpoint
         ((15,'Ignacio Zuloaga','Spanish'), (60000,80000,62500), (190,120), (1915,True,True)),
         ((16,'Raimundo de Madrazo','Spanish'), (50000,70000,62500), (75,55), (1880,False,False)),  # life midpoint
         ((17,'Jean-Baptiste-Camille Corot','French'), (60000,80000,68750), (40.5,55.5), (1835,False,False)),  # life midpoint
         ((18,'Isaac Israels','Dutch'), (70000,100000,150000), (91.5,72), (1900,False,False)),  # life midpoint
         ((19,'Marie-François Firmin-Girard','French'), (12000,18000,0), (65.5,50), (1880,False,False)),   # life midpoint
         ((20,'Marie-François Firmin-Girard','French'), (8000,12000,8750), (46.5,32.5), (1882,True,False)),
         ((21,'Marie-François Firmin-Girard','French'), (40000,60000,52500), (38,54), (1900,True,False)),  # circa
         ((22,'Isaac Israels','Dutch'), (50000,70000,62500), (46,61), (1902,True,False)),  # circa
         ((23,'Giovanni Battista Torriglia','Italian'), (20000,30000,23750), (51,75), (1897,False,False)),  # life midpoint
         ((24,'Luigi Bechi','Italian'), (40000,60000,0), (138,100), (1897,False,False)),  # life midpoint
         ((25,'Jan Jacob Spohler','Dutch'), (5000,7000,0), (27.5,40.5), (1838,False,False)),  # life midpoint
         ((26,'Cornelis Springer','Dutch'), (8000,12000,7250), (40.6,30.5), (1890,True,True)),
         ((27,'Andreas Schelfhout','Dutch'), (40000,60000,0), (38.5,55), (1866,True,True)),
         ((28,'George Willem Opdenhoff','Dutch'), (8000,12000,0), (48,68.5), (1840,False,False)),  # life midpoint
         ((29,'Johannes Franciscus Spohler','Dutch'), (6000,8000,5000), (44,35), (1873,False,False)),  # life midpoint
         ((30,'Charles Leickert','Belgian'), (40000,60000,0), (81,122), (1861,False,False)),  # life midpoint; "signed and indistinctly dated"
         ((31,'Jan Jacob Spohler','Dutch'), (8000,12000,0), (40,53.5), (1861,True,True)),
         ((32,'Charles Leickert','Belgian'), (15000,20000,17500), (51,59), (1853,True,True)),
         ((33,'Hendrik Reekers','Dutch'), (4000,6000,10625), (40.5,34), (1839,True,True)),
         ((34,'Anton Weiss','German'), (10000,15000,21250), (91,77), (1840,True,True)),
         ((35,'Adriana Haanen','Dutch'), (15000,20000,21250), (71,55), (1848,True,True)),
         ((36,'Franz Richard Unterberger','Austrian'), (80000,120000,81250), (78.5,119.5), (1869,False,False)),  # life midpoint
         ((37,'Antonio Reyna','Spanish'), (8000,12000,10000), (35.5,75), (1898,False,False)),  # life midpoint
         ((38,'Pablo Salinas','Spanish'), (10000,15000,26250), (45.5,75.5), (1908,False,False)),  # life midpoint
         ((39,'Antonietta Brandeis','Czech'), (8000,12000,15000), (21.5,12), (1884,False,False)),   # **pair! same dimensions but portrait vs landscape...using the latter; life midpoint
         ((40,'Georgios Jakobides','Greek'), (30000,50000,31250), (94,63), (1882,True,False)),
         ((41,'Paul Emil Jacobs','German'), (80000,120000,112500), (134,118), (1841,True,True)),
         ((42,'Hoca Ali Riza','NA'), (4000,6000,10000), (15,22.5), (1894,False,False)),  # life midpoint **lifespan not given! from Wikipedia
         ((43,'Halid Naci','Turkish'), (8000,12000,0), (18,30), (1901,False,False)),  # life midpoint
         ((44,'Alberto Pasini','Italian'), (30000,50000,0), (37.5,29.5), (1868,True,False)),  # circa
         ((45,'August von Siegen','German'), (8000,12000,10000), (99,143), (1880,False,False)),  # total guess: birth year + 30 (no death year given)
         ((46,'Gyula Tornai','Hungarian'), (20000,30000,0), (127,74), (1894,False,False)),  # life midpoint
         ((47,'Eugène Giraud','French'), (10000,15000,17500), (51,74), (1843,False,False)),  # life midpoint
         ((48,'Rudolf Swoboda','Austrian'), (15000,25000,18750), (59,36), (1886,False,False)),  # life midpoint
         ((49,'Alfons Leopold Mielich','German'), (30000,50000,31250), (58,46), (1896,False,False)),  # life midpoint
         ((50,'Léon Comerre','French'), (4000,6000,5000), (49,26.5), (1883,False,False)),  # life midpoint
         ((51,'Luis Ricardo Falero','Spanish'), (10000,15000,15000), (75,40.5), (1895,True,True)),
         ((52,'Fabio Fabbi','Italian'), (8000,12000,26250), (30.5,45), (1903,False,False)),  # life midpoint
         ((53,'Emile Claus','Belgian'), (8000,12000,27500), (51,41), (1878,True,False)),  # circa
         ((54,'Edouard Cortès','French'), (25000,35000,27500), (40,66), (1925,False,False)),  # life midpoint
         ((55,'Edouard Hamman','Belgian'), (15000,20000,27500), (55,73), (1872,True,True)),
         ((56,'Vittorio Corcos','Italian'), (30000,50000,60000), (96,54.5), (1888,True,True)),
         ((57,'Wilhelm Kuhnert','German'), (40000,60000,75000), (50,65), (1917,True,True)),
         ((58,'Walter Leistikow','German'), (6000,8000,0), (131,97), (1886,False,False))]  # life midpoint


# Second data set: 19th Century European Paintings
# 13 Dec 2017, 2:30 PM BST, London
# Prices in GBP
#
set2 = [ (( 1,'Paolo Sala','Italian'), (25000,35000,31250), (27,22), (1899,True,True)),
         (( 2,'Emile Claus','Belgian'), (35000,55000,0), (43,46), (1916,True,False)),  # circa
         (( 3,'Isaac Israels','Dutch'), (100000,150000,0), (46,61), (1902,True,False)),  # circa
         (( 4,'Jean-Baptiste-Camille Corot','French'), (300000,500000,453000), (64.5,49), (1845,True,False)),  # 1840-50
         (( 5,'Gustave Moreau','French'), (350000,500000,513000), (52,25), (1895,True,False)),  # circa
         (( 7,'Jean-Baptiste-Camille Corot','French'), (200000,300000,297000), (47,58), (1867,True,False)),  #1865-70;  lot #6 not shown
         (( 8,'Isaac Israels','Dutch'), (80000,120000,75000), (43.5,60), (1905,True,False)),  # circa
         (( 9,'Akseli Gallen-Kallela','Finnish'), (70000,100000,187500), (68,55.5), (1916,True,True)),
         ((10,'Vilhelm Hammershøi','Danish'), (400000,600000,465000), (46,38.5), (1906,True,False)),
         ((11,'Eero Järnefelt','Finnish'), (150000,200000,0), (74,47), (1894,True,True)),
         ((12,'Vilhelm Hammershøi','Danish'), (200000,300000,249000), (45,40), (1913,True,False)),
         ((13,'Helene Schjerfbeck','Finnish'), (150000,200000,0), (44.5,35), (1927,True,False)),  # circa
         ((14,'Ernst Josephson','Swedish'), (400000,600000,0), (90,119), (1883,True,True)),
         ((15,'Nikolai Astrup','Norwegian'), (40000,60000,50000), (30.5,41.5), (1909,True,False)),  # circa
         ((16,'Helene Schjerfbeck','Finnish'), (200000,300000,249000), (35,31), (1934,True,False)),  # circa
         ((17,'Anders Zorn','Swedish'), (150000,200000,162500), (55,74), (1910,True,True)),
         ((18,'Santiago Rusiñol','Spanish'), (80000,120000,85000), (96,87), (1894,True,False)),
         ((19,'Joaquín Sorolla','Spanish'), (500000,700000,525000), (48,78), (1904,True,True)),
         ((20,'Joaquín Sorolla','Spanish'), (200000,300000,218750), (65,98), (1904,True,True)),
         ((21,'Darío de Regoyos','Spanish'), (30000,50000,90000), (60,51), (1905,True,False)),
         ((22,'Hermenigildo Anglada-Camarasa','Spanish'), (40000,60000,50000), (51,44), (1938,True,False)),
         ((23,'Joaquín Sorolla','Spanish'), (70000,90000,137500), (85,59), (1917,True,True)),
         ((24,'Joaquín Sorolla','Spanish'), (100000,150000,125000), (34.5,50.5), (1916,True,False)),
         ((25,'Giovanni Boldini','Italian'), (150000,200000,393000), (31.5,24.75), (1873,True,True)),
         ((26,'Wladislaw Czachorski','Polish'), (15000,20000,30000), (39,17.5), (1880,False,False)),  # life midpoint
         ((27,'Joaquín Agrasot','Spanish'), (15000,20000,0), (85,147), (1878,True,True)),
         ((28,'Henri Gervex','French'), (80000,120000,87500), (41.5,34), (1878,True,False)),  # this is a sketch, date is for final painting
         ((29,'Manfred Lindemann-Frommel','German'), (10000,15000,0), (59,73.5), (1891,True,True)),
         ((30,'Vittorio Corcos','Italian'), (30000,50000,31250), (55,41.5), (1886,True,False)),  # circa
         ((31,'Guglielmo Ciardi','Italian'), (30000,50000,31250), (57.5,101), (1904,True,False)),  # relates to a similar composition of 1904
         ((32,'Félix Ziem','French'), (40000,60000,50000), (54,85), (1866,False,False)),  # life midpoint
         ((33,'Raimundo de Madrazo','Spanish'), (50000,70000,50000), (73.5,59.5), (1880,False,False)),  # life midpoint;  lot #34 not shown
         ((35,'Adrianus Eversen','Dutch'), (8000,12000,12500), (53,46), (1857,False,False)),  # life midpoint
         ((36,'Cornelis Springer','Dutch'), (40000,60000,0), (62,48), (1879,True,True)),
         ((37,'Andreas Schelfhout','Dutch'), (10000,15000,0), (53,68.5), (1815,True,True)),
         ((38,'Andreas Schelfhout','Dutch'), (60000,80000,0), (38.5,55), (1866,True,True)),
         ((39,'Adriana Haanen','Dutch'), (8000,12000,8750), (77,66), (1850,True,True)),
         ((40,'Petrus van Schendel','Dutch'), (30000,50000,32500), (62,78), (1852,True,False)),  # circa
         ((41,'Georgios Jakobides','Greek'), (100000,150000,206250), (103,129), (1883,True,False)), # 1883-1884
         ((42,'Heinrich Bürkel','German'), (7000,10000,0), (35,49.5), (1855,True,False)),  # circa
         ((43,'Heinrich Bürkel','German'), (6000,9000,7500), (26.5,38), (1855,True,False)),  # circa
         ((44,'Heinrich Bürkel','German'), (7000,10000,0), (27,39.5), (1864,True,False)), # circa
         ((45,'Walter Leistikow','German'), (12000,18000,0), (131,97), (1886,False,False)),  # life midpoint
         ((46,'Heinrich Bürkel','German'), (10000,15000,0), (44,64), (1835,False,False)),  # life midpoint
         ((47,'Hans Thoma','German'), (12000,18000,32500), (90,120), (1910,True,True)),
         ((48,'Otto Scholderer','German'), (8000,12000,7500), (22,37), (1891,True,False)),  # circa
         ((49,'Raimundo de Madrazo','Spanish'), (7000,9000,6250), (84,67), (1892,True,True)),
         ((50,'Nikolaos Gyzis','Greek'), (15000,20000,50000), (50,40), (1871,False,False)),  # life midpoint
         ((51,'Adolph von Menzel','German'), (15000,20000,18750), (17.5,10.5), (1884,True,True)),
         ((52,'Léon Lhermitte','French'), (12000,18000,21250), (51,40), (1884,False,False)), # life midpoint
         ((53,'Fausto Zonaro','Italian'), (40000,60000,62500), (38,62), (1891,False,False)),  # life midpoint
         ((55,'Fausto Zonaro','Italian'), (60000,80000,68750), (39,61), (1891,False,False)),   # life midpoint;  lot #54 not shown
         ((56,'Edward Cucuel','American'), (20000,30000,47500), (80,65), (1914,False,False)),   # life midpoint
         ((57,'Kuroda Seiki','Japanese'), (12000,18000,15000), (26.5,35), (1895,False,False)),  # life midpoint
         ((58,'Paul Fischer','Danish'), (10000,15000,0), (55.5,39.5), (1897,False,False)),  # life midpoint
         ((59,'Carl Holsøe','Danish'), (25000,35000,0), (65,55), (1899,False,False)),  # life midpoint
         ((60,'Ulpiano Checa','Spanish'), (8000,12000,27500), (65,110), (1888,False,False)),  # life midpoint
         ((61,'Alfred Stevens','Belgian'), (15000,20000,16875), (124,46.5), (1864,False,False)),  # life midpoint
         ((62,'Vittorio Reggianini','Italian'), (25000,35000,0), (56,71), (1898,False,False)),  # life midpoint
         ((63,'Giovanni Battista Torriglia','Italian'), (30000,50000,62500), (72,109), (1897,False,False)),  # life midpoint
         ((64,'Edouard Cortès','French'), (6000,8000,20000), (46,56), (1925,False,False)),  # life midpoint
         ((65,'Edouard Cortès','French'), (10000,15000,20000), (33,46), (1925,False,False)),  # life midpoint
         ((66,'Edouard Cortès','French'), (10000,15000,18750), (33,46), (1925,False,False)),  # life midpoint
         ((67,'Gustav Richter','German'), (4000,6000,15000), (346,127), (1878,True,True)),
         ((68,'Jacques-Louis-Jules David','French'), (25000,35000,25000), (148,96), (1860,True,True)),
         ((69,'Blas Olleros Quintana','Spanish'), (8000,12000,16250), (123.5,92), (1885,False,False)),  # life midpoint
         ((70,'Guillaume Seignac','French'), (7000,10000,0), (55.5,46.5), (1897,False,False)),  # life midpoint
         ((71,'Charles Landelle','French'), (12000,18000,0), (55.5,38.5), (1864,False,False)),  # life midpoint
         ((72,'Emile Cambiaggio','Italian'), (20000,30000,0), (141,204), (1887,False,False)),  # exhibition date
         ((73,'Adolphe-Alexandre Lesrel','French'), (10000,15000,11875), (176,161), (1866,False,False)),  # possible exhibition date
         ((74,'Frederick Arthur Bridgman','American'), (5000,7000,6250), (18.5,23.5), (1922,True,True)),
         ((75,'Paul Philippoteaux','French'), (5000,7000,6250), (56,68.5), (1884,False,False)),  # life midpoint
         ((76,'Adolf Schreyer','German'), (10000,15000,20000), (79,126), (1869,True,True)),
         ((77,'Victor Huguet','French'), (10000,15000,12500), (65,92), (1868,False,False)) ]  # life midpoint

# Third data set: 19th Century European Paintings
# 06 June 2017, 2:30 PM BST, London
# Prices in GBP
#
set3 = [ (( 1,'Johan Christian Dahl','Norwegian'), (12000,18000,37500), (13.5,21.5), (1832,True,True)),
         (( 2,'Vilhelm Hammershøi','Danish'), (400000,600000,1448750), (39.5,42.5), (1899,True,False)),
         (( 3,'Federico Zandomeneghi','Italian'), (150000,200000,248750), (46,37), (1894,False,False)),  # female figure became prominent in his work in 1894
         (( 4,'Jean-Baptiste-Camille Corot','French'), (100000,150000,0), (33.5,47.5), (1851,True,True)),
         (( 5,'Luigi Loir','French'), (120000,180000,224750), (150,300), (1900,True,True)),  # indistinct 190(?)
         (( 6,'Giuseppe De Nittis','Italian'), (500000,700000,548750), (53,40.5), (1875,True,True)),
         (( 7,'Edmond Grandjean','French'), (200000,300000,236750), (77,126), (1876,True,True)),
         (( 8,'Edmond Grandjean','French'), (40000,60000,0), (40,64.5), (1889,True,True)),
         (( 9,'Roger Jourdain','French'), (30000,50000,0), (81,111), (1881,False,False)),  # life midpoint
         ((10,'Emile Claus','Belgian'), (80000,120000,87500), (92,92), (1916,True,True)),
         ((11,'Joaquín Sorolla','Spanish'), (700000,1000000,629750), (188.5,175.5), (1895,True,True)),
         ((12,'Hermenegildo Anglada-Camarasa','Spanish'), (80000,120000,100000), (38,49), (1900,True,False)),
         ((13,'Hermenegildo Anglada-Camarasa','Spanish'), (70000,90000,106250), (59.5,49), (1951,True,True)),
         ((14,'Hermenegildo Anglada-Camarasa','Spanish'), (150000,200000,0), (23.5,33), (1898,True,False)),  # dated approx from old catalog
         ((15,'Helene Schjerfbeck','Finnish'), (200000,300000,212500), (55.5,48.5), (1943,True,False)),
         ((16,'Albert Edelfelt','Finnish'), (80000,120000,0), (41,33), (1883,True,True)),
         ((17,'Jean-Léon Gérôme','French'), (500000,700000,488750), (60.5,100), (1889,True,False)),
         ((18,'Leo Putz','German'), (60000,80000,0), (69,76.5), (1904,False,False)),  # life midpoint
         ((19,'Edward Cucuel','American'), (25000,35000,45000), (80,80), (1914,False,False)),  # life midpoint
         ((20,'Leo Putz','German'), (120000,180000,0), (123,160), (1921,True,False)),
         ((21,'Lovis Corinth','German'), (80000,120000,0), (119,95), (1913,True,True)),
         ((22,'Veronika Maria Herwegen-Manini','German'), (40000,60000,0), (82,136), (1886,True,True)),
         ((23,'Guglielmo Ciardi','Italian'), (60000,80000,212500), (62,102), (1879,False,False)),  # life midpoint
         ((24,'Ludwig Richter','German'), (80000,120000,0), (34,43.5), (1830,True,True)),
         ((25,'Giuseppe Canella','Italian'), (6000,8000,0), (9,12.5), (1817,False,False)),  # life midpoint; two same-sized paintings
         ((26,'Rudolf von Alt','Austrian'), (30000,50000,35000), (40,50), (1864,False,False)),  # exhibition date
         ((27,'Jan Weissenbruch','Dutch'), (12000,18000,0), (48,67), (1850,True,True)),
         ((28,'Andreas Schelfhout','Dutch'), (50000,70000,90000), (33.5,46), (1856,True,True)),
         ((29,'Constantinos Volanakis','Greek'), (60000,80000,0), (104,174), (1872,False,False)),  # life midpoint
         ((30,'Julio Romero de Torres','Spanish'), (25000,35000,31250), (75,55), (1897,True,False)),  # circa
         ((31,'Henri Martin','French'), (50000,70000,60000), (146,89.5), (1900,True,False)),  # circa
         ((32,'Adolph Hirémy-Hirschl','Hungarian'), (15000,20000,52500), (109,274), (1896,False,False)),  # life midpoint
         ((33,'Ludwig Knaus','German'), (12000,18000,35000), (346,127), (1892,False,False)),  # exhibited
         ((34,'Ludwig von Hofmann','German'), (20000,30000,0), (126,93.5), (1928,True,True)),
         ((35,'Pierre Amédée Marcel-Beronneau','French'), (8000,12000,11875), (185.5,122.5), (1903,False,False)),  # life midpoint
         ((36,'Francisco Miralles','Spanish'), (20000,30000,21250), (33,53.5), (1874,False,False)),  # life midpoint
         ((37,'Manuel García Rodríguez','Spanish'), (15000,20000,27500), (41,30), (1913,True,True)),
         ((38,'Frank Myers Boggs','American'), (25000,35000,18750), (55,38), (1890,False,False)),   # life midpoint
         ((39,'Gustave Maincent','French'), (5000,8000,10000), (57,91), (1868,False,False)),  # life midpoint
         ((40,'Olga Wisinger-Florian','Austrian'), (8000,12000,10000), (36,46.5), (1894,False,False)),  # diary entry date of sketch
         ((41,'Carl Moll','Austrian'), (30000,50000,0), (190,151), (1897,True,True)),
         ((42,'Eugène Galien-Laloue','French'), (6000,8000,8125), (19,31), (1902,True,False)),  # circa
         ((43,'Otto Dill','German'), (8000,12000,0), (60,80), (1920,False,False)),  # life midpoint
         ((44,'Otto Dill','German'), (6000,8000,0), (34.8,49.8), (1920,False,False)),  # life midpoint
         ((45,'Emile Claus','Belgian'), (15000,20000,12500), (73,113), (1886,False,False)),  # life midpoint
         ((46,'Bernhard Mühlig','German'), (3000,5000,5000), (16.5,26.5), (1869,False,False)),  # life midpoint
         ((47,'Emile Claus','Belgian'), (15000,20000,70000), (43.5,34), (1886,False,False)),  # life midpoint
         ((48,'Albert Lynch','Peruvian'), (15000,20000,18750), (92.5,70), (1881,False,False)),  # life midpoint
         ((49,'Albert Lynch','Peruvian'), (10000,15000,10000), (61.5,46.5), (1881,False,False)),  # life midpoint
         ((50,'Georgius Jacobus Johannes van Os','Dutch'), (8000,12000,10000), (50,39), (1821,False,False)),  # life midpoint; two similar-sized paintings
         ((51,'Mihály Munkácsy','Hungarian'), (10000,15000,27500), (42,31), (1872,False,False)),  # life midpoint
         ((52,'Severin Roesen','American'), (15000,25000,0), (74,101), (1843,False,False)),  # life midpoint
         ((53,'Petrus van Schendel','Dutch'), (10000,15000,30000), (94.5,69), (1844,True,True)),
         ((54,'Giovanni Boldini','Italian'), (20000,30000,0), (70,59), (1865,True,False)),  # circa; two ovals  
         ((55,'Johan Vilhelm Gertner','Danish'), (5000,7000,5625), (26.5,20.5), (1868,True,True)),
         ((56,'Julius LeBlanc Stewart','American'), (8000,12000,15000), (55,39), (1887,False,False)),  # life midpoint
         ((57,'Paolo Sala','Italian'), (2000,3000,1875), (66,97), (1891,False,False)),  # life midpoint
         ((58,'Carl Holsøe','Danish'), (6000,8000,11875), (30,17.5), (1899,False,False)),  # life midpoint
         ((59,'Delphin Enjolras','French'), (10000,15000,0), (73,54), (1901,False,False)),  # life midpoint
         ((60,'Henri Evenepoel','Belgian'), (15000,25000,12500), (82,54), (1894,True,False)),  # circa
         ((61,'Paul Fischer','Danish'), (20000,30000,31250), (59,76), (1897,False,False)),  # life midpoint
         ((62,'Paul Fischer','Danish'), (10000,15000,17500), (63,38), (1909,True,True)),
         ((63,'Guillaume Seignac',''), (15000,20000,0), (55,46.6), (1897,False,False)),  # life midpoint; **repeated in later auction for lower price!
         ((64,'Daniel Israel','Austrian'), (5000,7000,6250), (23.5,18), (1880,False,False)),  # life midpoint
         ((65,'Daniel Israel','Austrian'), (5000,7000,6250), (27,19), (1880,False,False)),  # life midpoint
         ((66,'Georges Rochegrosse','French'), (10000,15000,30000), (54,65), (1898,False,False)),  # life midpoint
         ((67,'Fabio Fabbi','Italian'), (8000,12000,18750), (70,40), (1903,False,False)),  # life midpoint
         ((68,'Tadeusz Ajdukiewicz','Polish'), (8000,12000,27500), (45,54), (1884,True,True)),
         ((69,'Ricardo Villegas Cordero','Spanish'), (8000,12000,18750), (58,41), (1881,True,True)),
         ((70,'Géza Vastagh','Hungarian'), (8000,12000,21250), (53,113), (1892,False,False)) ]  # life midpoint


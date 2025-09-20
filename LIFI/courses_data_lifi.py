base_lifi_courses = [
    # ===== Semestre I =====
    {"id":"I5989","code":"I5989","name":"METODOLOGIA EXPERIMENTAL","credits":3, "hours": 2,"semester":1,"order":1,"area":"metodo","prereqs":[]},
    {"id":"I5988","code":"I5988","name":"LABORATORIO DE MECANICA","credits":2,"hours": 2,"semester":1,"order":2,"area":"lab","prereqs":[]},
    {"id":"I5304","code":"I5304","name":"MECANICA","credits":5,"hours": 2,"semester":1,"order":3,"area":"fis","prereqs":[]},
    {"id":"I5987","code":"I5987","name":"TALLER DE RESOLUCION DE PROBLEMAS DE MECANICA","credits":2,"hours": 2,"semester":1,"order":4,"area":"fis","prereqs":[]},
    {"id":"I5991","code":"I5991","name":"ALGEBRA LINEAL I","credits":10,"hours": 6,"semester":1,"order":5,"area":"mate","prereqs":[]},
    {"id":"I5990","code":"I5990","name":"CALCULO DIFERENCIAL E INTEGRAL I","credits":10,"hours": 6,"semester":1,"order":6,"area":"mate","prereqs":[]},
    {"id":"I5992","code":"I5992","name":"COMPUTO CIENTIFICO I","credits":5,"hours": 4,"semester":1,"order":7,"area":"progra","prereqs":[]},
    {"id":"SPC-I-08", "semester":1, "order":8, "kind":"spacer", "rows":1},
    {"id":"I6032","code":"I6032","name":"CLINICIA TUTORIAL I","credits":2,"hours": 2,"semester":1,"order":8,"area":"metodo","prereqs":[]},

    # ===== Semestre II =====
    {"id":"SPC-II-01", "semester":2, "order":9, "kind":"spacer", "rows":1},
    {"id":"I5995","code":"I5995","name":"LABORATORIO DE ELECTROMAGNETISMO","credits":3,"hours": 3,"semester":2,"order":9,"area":"lab","prereqs":[]},
    {"id":"I5993","code":"I5993","name":"ELECTROMAGNETISMO","credits":5,"hours": 2,"semester":2,"order":10,"area":"fis","prereqs":[]},
    {"id":"I5994","code":"I5994","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ELECTROMAGNETISMO","credits":2,"hours": 2,"semester":2,"order":11,"area":"fis","prereqs":[]},
    {"id":"I6000","code":"I6000","name":"ALGEBRA LINEAL II","credits":7,"hours": 4,"semester":2,"order":12,"area":"mate","prereqs":[]},
    {"id":"I5999","code":"I5999","name":"CALCULO DIFERENCIAL E INTEGRAL II","credits":7,"hours": 4,"semester":2,"order":13,"area":"mate","prereqs":[]},
    {"id":"SPC-II-07", "semester":2, "order":14, "kind":"spacer", "rows":1},
    {"id":"I6008","code":"I6008","name":"TEORIA DE LA PROBABILIDAD Y ESTADISTICA MATEMATICA","credits":7,"hours": 4,"semester":2,"order":14,"area":"mate","prereqs":[]},
    {"id":"I6033","code":"I6033","name":"CLINICA TUTORIAL II","credits":2,"hours": 2,"semester":2,"order":15,"area":"metodo","prereqs":["I6032"]},

    # ===== Semestre III =====
    {"id":"SPC-III-01", "semester":3, "order":16, "kind":"spacer", "rows":1},
    {"id":"I5998","code":"I5998","name":"LABORATORIO DE ONDAS, FLUIDOS Y FISICA MOLECULAR ","credits":2,"hours": 2,"semester":3,"order":16,"area":"lab","prereqs":[]},
    {"id":"I5996","code":"I5996","name":"ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":5,"hours": 2,"semester":3,"order":17,"area":"fis","prereqs":[]},
    {"id":"I5997","code":"I5997","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":2,"hours": 2,"semester":3,"order":18,"area":"fis","prereqs":[]},
    {"id":"I6010","code":"I6010","name":"ECUACIONES DIFERENCIALES ORDINARIAS Y MODELACION DE SISTEMAS","credits":7,"hours": 4,"semester":3,"order":19,"area":"mate","prereqs":[]},
    {"id":"I6009","code":"I6009","name":"CALCULO AVANZADO PARA FISICA","credits":7,"hours": 4,"semester":3,"order":20,"area":"mate","prereqs":[]},
    {"id":"I6011","code":"I6011","name":"SEMINARIO DE INVESTIGACION ","credits":3,"hours": 2,"semester":3,"order":21,"area":"metodo","prereqs":[]},
    {"id":"I6014","code":"I6014","name":"VARIABLE COMPLEJA","credits":7,"hours": 4,"semester":3,"order":22,"area":"mate","prereqs":[]},
    {"id":"I6001","code":"I6001","name":"CLINICA DE HABILIDADES BASICAS","credits":5,"hours": 4,"semester":3,"order":23,"area":"metodo","prereqs":[]},

    # ===== Semestre IV =====
    {"id":"SPC-IV-01", "semester":4, "order":24, "kind":"spacer", "rows":1},
    {"id":"I6004","code":"I6004","name":"LABORATORIO DE FISICA MODERNA","credits":2,"hours": 2,"semester":4,"order":24,"area":"lab","prereqs":[]},
    {"id":"I6002","code":"I6002","name":"FISICA MODERNA","credits":5,"hours": 2,"semester":4,"order":25,"area":"fis","prereqs":[]},
    {"id":"I6003","code":"I6003","name":"TALLER DE RESOLUCION DE PROBLEMAS DE FISICA MODERNA ","credits":2,"hours": 2,"semester":4,"order":26,"area":"fis","prereqs":[]},
    {"id":"I6030","code":"I6030","name":"ALGEBRA MULTILINEAL","credits":7,"hours": 4,"semester":4,"order":27,"area":"mate","prereqs":[]},
    {"id":"I6012","code":"I6012","name":"MECANICA TEORICA","credits":10,"hours": 6,"semester":4,"order":28,"area":"fis","prereqs":[]},
    {"id":"I6007","code":"I6007","name":"COMPUTO CIENTIFICO II","credits":5,"hours": 4,"semester":4,"order":29,"area":"progra","prereqs":[]},
    
    # ===== Semestre V =====
    {"id":"I6006","code":"I6006","name":"LABORATORIO DE ELECTRONICA BASICA","credits":3,"hours": 3,"semester":5,"order":32,"area":"lab","prereqs":[]},
    {"id":"SPC-V-02", "semester":5, "order":33, "kind":"spacer", "rows":1},
    {"id":"I6013","code":"I6013","name":"ELECTRODINAMICA","credits":10,"hours": 6,"semester":5,"order":33,"area":"fis","prereqs":[]},
    {"id":"I6018","code":"I6018","name":"TERMODINAMICA","credits":7,"hours": 4,"semester":5,"order":34,"area":"fis","prereqs":[]},
    {"id":"I6015","code":"I6015","name":"ECUACIONES DIFERENCIALES PARCIALES Y FUNCIONES ESPECIALES","credits":8,"hours": 5,"semester":5,"order":35,"area":"mate","prereqs":[]},
    {"id":"SPC-V-06", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"SPC-V-07", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"SPC-V-08", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"I6034","code":"I6034","name":"CLINICA TUTORIAL III","credits":2,"hours": 2,"semester":5,"order":36,"area":"metodo","prereqs":["I6033"]},
   
    # ===== Semestre VI =====
    {"id":"I6016","code":"I6016","name":"LABORATORIO DE FISICA I","credits":2,"hours": 2,"semester":6,"order":37,"area":"fis","prereqs":[]},
    {"id":"SPC-VI-02", "semester":6, "order":38, "kind":"spacer", "rows":1},
    {"id":"I6019","code":"I6019","name":"OPTICA","credits":7,"hours": 4,"semester":6,"order":38,"area":"fis","prereqs":[]},
    {"id":"I6020","code":"I6020","name":"FISICA RELATIVISTA","credits":7,"hours": 4,"semester":6,"order":39,"area":"fis","prereqs":[]},
    {"id":"I5803","code":"I5803","name":"QUIMICA GENERAL I","credits":9,"hours": 5,"semester":6,"order":40,"area":"quim","prereqs":[]},
    {"id":"I6922","code":"I6922","name":"LABORATORIO DE QUIMICA GENERAL I","credits":3,"hours": 3,"semester":6,"order":41,"area":"quim","prereqs":[]},
    {"id":"SPC-VI-07", "semester":6, "order":42, "kind":"spacer", "rows":1},
    {"id":"SPC-VI-08", "semester":6, "order":42, "kind":"spacer", "rows":1},
    {"id":"I6025","code":"I6025","name":"CLINICA DE FORMACION FUNDAMENTAL","credits":5,"hours": 4,"semester":6,"order":42,"area":"metodo","prereqs":["I6001"]},

    # ===== Semestre VII =====
    {"id":"I6024","code":"I6024","name":"LABORATORIO DE FISICA II","credits":2,"hours": 2,"semester":7,"order":43,"area":"fis","prereqs":[]},
    {"id":"SPC-VII-02", "semester":7, "order":44, "kind":"spacer", "rows":1},
    {"id":"SPC-VII-03", "semester":7, "order":44, "kind":"spacer", "rows":1},    
    {"id":"I6028","code":"I6028","name":"MECANICA DEL MEDIO CONTINUO","credits":10,"hours": 6,"semester":7,"order":44,"area":"fis","prereqs":[]},
    {"id":"I6026","code":"I6026","name":"MECANICA CUANTICA","credits":10,"hours": 6,"semester":7,"order":45,"area":"fis","prereqs":[]},
    {"id":"I6023","code":"I6023","name":"METODOS MATEMATICOS DE LA FISICA","credits":7,"hours": 0,"semester":7,"order":46,"area":"mate","prereqs":[]},
    {"id":"SPC-VII-07", "semester":7, "order":47, "kind":"spacer", "rows":1},    
    {"id":"OPTA1","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":7,"order":47,"area":"extra","prereqs":[]},

    # ===== Semestre VIII =====
    {"id":"SPC-VIII-01", "semester":8, "order":48, "kind":"spacer", "rows":1},
    {"id":"SPC-VIII-02", "semester":8, "order":48, "kind":"spacer", "rows":1},    
    {"id":"I6027","code":"I6027","name":"FISICA ESTADISTICA","credits":10,"hours": 6,"semester":8,"order":48,"area":"fis","prereqs":[]},
    {"id":"I6031","code":"I6031","name":"FISICA DE MATERIA CONDENSADA ","credits":7,"hours": 4,"semester":8,"order":49,"area":"fis","prereqs":[]},
    {"id":"I6022","code":"I6022","name":"HISTORIA Y FILOSOFIA DE LA FISICA","credits":7,"hours": 4,"semester":8,"order":50,"area":"educ","prereqs":[]},
    {"id":"SPC-VIII-07", "semester":8, "order":51, "kind":"spacer", "rows":1},
    {"id":"SPC-VIII-07", "semester":8, "order":51, "kind":"spacer", "rows":1},
    {"id":"OPTA2","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":8,"order":51,"area":"extra","prereqs":[]},
    {"id":"I6035","code":"I6035","name":"CLINICA TUTORIAL IV","credits":2,"hours": 2,"semester":8,"order":52,"area":"metodo","prereqs":["I6034"]},

    # ===== Semestre IX =====
    {"id":"I6029","code":"I6029","name":"LABORATORIO DE FISICA III","credits":2,"hours": 2,"semester":9,"order":53,"area":"fis","prereqs":[]},
    {"id":"SPC-IX-06", "semester":9, "order":54, "kind":"spacer", "rows":1},
    {"id":"SPC-IX-06", "semester":9, "order":54, "kind":"spacer", "rows":1},
    {"id":"I6021","code":"I6021","name":"DISEÑO Y EVALUACION DE RECURSOS EDUCATIVOS","credits":7,"hours": 4,"semester":9,"order":54,"area":"educ","prereqs":[]},
    {"id":"I6040","code":"I6040","name":"CLINICA DE FORMACION ESPECIALIZANTE","credits":5,"hours": 4,"semester":9,"order":55,"area":"metodo","prereqs":["I6025"]},
    {"id":"I6041","code":"I6041","name":"CLINICA DE FORMACION INTER O MULTIDSCIPLINAR","credits":5,"hours": 4,"semester":9,"order":56,"area":"metodo","prereqs":["I6025"]},
    {"id":"I6017","code":"I6017","name":"SIMULACION DE PROCESOS FISICOS","credits":5,"hours": 4,"semester":9,"order":57,"area":"progra","prereqs":[]},
    {"id":"OPTA3","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":9,"order":58,"area":"extra","prereqs":[]},
    {"id":"I6036","code":"I6036","name":"CLINICA TUTORIAL V","credits":2,"hours": 2,"semester":9,"order":59,"area":"metodo","prereqs":["I6035"]}

]

real_lifi_courses = [
    # ===== Semestre I =====
    {"id":"I5989","code":"I5989","name":"METODOLOGIA EXPERIMENTAL","credits":3, "hours": 2,"semester":1,"order":1,"area":"metodo","prereqs":[]},
    {"id":"SPC-I-02", "semester":1, "order":2, "kind":"spacer", "rows":1},
    {"id":"IB121","code":"IB121","name":"INTRODUCCION A LA FISICA","credits":0, "hours": 4,"semester":1,"order":2,"area":"metodo","prereqs":[]},
    {"id":"SPC-I-04", "semester":1, "order":3, "kind":"spacer", "rows":1},
    {"id":"I5991","code":"I5991","name":"ALGEBRA LINEAL I","credits":10,"hours": 6,"semester":1,"order":3,"area":"mate","prereqs":[]},
    {"id":"IB120","code":"IB120","name":"PRECALCULO","credits":0,"hours": 6,"semester":1,"order":4,"area":"mate","prereqs":[]},
    {"id":"I5992","code":"I5992","name":"COMPUTO CIENTIFICO I","credits":5,"hours": 4,"semester":1,"order":5,"area":"progra","prereqs":[]},
    {"id":"SPC-I-08", "semester":1, "order":6, "kind":"spacer", "rows":1},
    {"id":"I6032","code":"I6032","name":"CLINICIA TUTORIAL I","credits":2,"hours": 2,"semester":1,"order":6,"area":"metodo","prereqs":[]},

    # ===== Semestre II =====
    {"id":"SPC-II-01", "semester":2, "order":7, "kind":"spacer", "rows":1},
    {"id":"I5988","code":"I5988","name":"LABORATORIO DE MECANICA","credits":2,"hours": 2,"semester":2,"order":7,"area":"lab","prereqs":[]},
    {"id":"I5304","code":"I5304","name":"MECANICA","credits":5,"hours": 2,"semester":2,"order":8,"area":"fis","prereqs":[]},
    {"id":"I5987","code":"I5987","name":"TALLER DE RESOLUCION DE PROBLEMAS DE MECANICA","credits":2,"hours": 2,"semester":2,"order":9,"area":"fis","prereqs":[]},
    {"id":"I6000","code":"I6000","name":"ALGEBRA LINEAL II","credits":7,"hours": 4,"semester":2,"order":10,"area":"mate","prereqs":[]},
    {"id":"I5990","code":"I5990","name":"CALCULO DIFERENCIAL E INTEGRAL I","credits":10,"hours": 6,"semester":2,"order":11,"area":"mate","prereqs":[]},
    {"id":"SPC-II-07", "semester":2, "order":12, "kind":"spacer", "rows":1},
    {"id":"I6008","code":"I6008","name":"TEORIA DE LA PROBABILIDAD Y ESTADISTICA MATEMATICA","credits":7,"hours": 4,"semester":2,"order":12,"area":"mate","prereqs":[]},
    {"id":"I6033","code":"I6033","name":"CLINICA TUTORIAL II","credits":2,"hours": 2,"semester":2,"order":13,"area":"metodo","prereqs":["I6032"]},

    # ===== Semestre III =====
    {"id":"SPC-III-01", "semester":3, "order":14, "kind":"spacer", "rows":1},
    {"id":"I5995","code":"I5995","name":"LABORATORIO DE ELECTROMAGNETISMO","credits":3,"hours": 3,"semester":3,"order":14,"area":"lab","prereqs":[]},
    {"id":"I5993","code":"I5993","name":"ELECTROMAGNETISMO","credits":5,"hours": 2,"semester":3,"order":15,"area":"fis","prereqs":[]},
    {"id":"I5994","code":"I5994","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ELECTROMAGNETISMO","credits":2,"hours": 2,"semester":3,"order":16,"area":"fis","prereqs":[]},
    {"id":"I6010","code":"I6010","name":"ECUACIONES DIFERENCIALES ORDINARIAS Y MODELACION DE SISTEMAS","credits":7,"hours": 4,"semester":3,"order":17,"area":"mate","prereqs":[]},
    {"id":"I5999","code":"I5999","name":"CALCULO DIFERENCIAL E INTEGRAL II","credits":7,"hours": 4,"semester":3,"order":18,"area":"mate","prereqs":[]},
    {"id":"I6011","code":"I6011","name":"SEMINARIO DE INVESTIGACION ","credits":3,"hours": 2,"semester":3,"order":19,"area":"metodo","prereqs":[]},
    {"id":"SPC-III-08", "semester":3, "order":20, "kind":"spacer", "rows":1},
    {"id":"I6001","code":"I6001","name":"CLINICA DE HABILIDADES BASICAS","credits":5,"hours": 4,"semester":3,"order":21,"area":"metodo","prereqs":[]},

    # ===== Semestre IV =====
    {"id":"SPC-IV-01", "semester":4, "order":22, "kind":"spacer", "rows":1},
    {"id":"I5998","code":"I5998","name":"LABORATORIO DE ONDAS, FLUIDOS Y FISICA MOLECULAR ","credits":2,"hours": 2,"semester":4,"order":22,"area":"lab","prereqs":[]},
    {"id":"I5996","code":"I5996","name":"ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":5,"hours": 2,"semester":4,"order":23,"area":"fis","prereqs":[]},
    {"id":"I5997","code":"I5997","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":2,"hours": 2,"semester":4,"order":24,"area":"fis","prereqs":[]},
    {"id":"I6030","code":"I6030","name":"ALGEBRA MULTILINEAL","credits":7,"hours": 4,"semester":4,"order":25,"area":"mate","prereqs":[]},
    {"id":"I6009","code":"I6009","name":"CALCULO AVANZADO PARA FISICA","credits":7,"hours": 4,"semester":4,"order":26,"area":"mate","prereqs":[]},
    {"id":"I6014","code":"I6014","name":"VARIABLE COMPLEJA","credits":7,"hours": 4,"semester":4,"order":27,"area":"mate","prereqs":[]},
    {"id":"SPC-IV-08", "semester":4, "order":28, "kind":"spacer", "rows":1},
    {"id":"I6007","code":"I6007","name":"COMPUTO CIENTIFICO II","credits":5,"hours": 4,"semester":4,"order":28,"area":"progra","prereqs":[]},
    
    # ===== Semestre V =====
    {"id":"I6006","code":"I6006","name":"LABORATORIO DE ELECTRONICA BASICA","credits":3,"hours": 3,"semester":5,"order":29,"area":"lab","prereqs":[]},
    {"id":"I6004","code":"I6004","name":"LABORATORIO DE FISICA MODERNA","credits":2,"hours": 2,"semester":5,"order":30,"area":"lab","prereqs":[]},
    {"id":"I6002","code":"I6002","name":"FISICA MODERNA","credits":5,"hours": 2,"semester":5,"order":31,"area":"fis","prereqs":[]},
    {"id":"I6003","code":"I6003","name":"TALLER DE RESOLUCION DE PROBLEMAS DE FISICA MODERNA ","credits":2,"hours": 2,"semester":5,"order":32,"area":"fis","prereqs":[]},
    {"id":"I6013","code":"I6013","name":"ELECTRODINAMICA","credits":10,"hours": 6,"semester":5,"order":33,"area":"fis","prereqs":[]},
    {"id":"I6018","code":"I6018","name":"TERMODINAMICA","credits":7,"hours": 4,"semester":5,"order":34,"area":"fis","prereqs":[]},
    {"id":"I6015","code":"I6015","name":"ECUACIONES DIFERENCIALES PARCIALES Y FUNCIONES ESPECIALES","credits":8,"hours": 5,"semester":5,"order":35,"area":"mate","prereqs":[]},
    {"id":"I6012","code":"I6012","name":"MECANICA TEORICA","credits":10,"hours": 6,"semester":5,"order":36,"area":"fis","prereqs":[]},
    {"id":"I6034","code":"I6034","name":"CLINICA TUTORIAL III","credits":2,"hours": 2,"semester":5,"order":37,"area":"metodo","prereqs":["I6033"]},
   
    # ===== Semestre VI =====
    {"id":"I6016","code":"I6016","name":"LABORATORIO DE FISICA I","credits":2,"hours": 2,"semester":6,"order":38,"area":"fis","prereqs":[]},
    {"id":"SPC-VI-02", "semester":6, "order":38, "kind":"spacer", "rows":1},
    {"id":"I6019","code":"I6019","name":"OPTICA","credits":7,"hours": 4,"semester":6,"order":39,"area":"fis","prereqs":[]},
    {"id":"I6020","code":"I6020","name":"FISICA RELATIVISTA","credits":7,"hours": 4,"semester":6,"order":40,"area":"fis","prereqs":[]},
    {"id":"I5803","code":"I5803","name":"QUIMICA GENERAL I","credits":9,"hours": 5,"semester":6,"order":41,"area":"quim","prereqs":[]},
    {"id":"I6922","code":"I6922","name":"LABORATORIO DE QUIMICA GENERAL I","credits":3,"hours": 3,"semester":6,"order":42,"area":"quim","prereqs":[]},
    {"id":"SPC-VI-07", "semester":6, "order":43, "kind":"spacer", "rows":1},
    {"id":"SPC-VI-08", "semester":6, "order":43, "kind":"spacer", "rows":1},
    {"id":"I6025","code":"I6025","name":"CLINICA DE FORMACION FUNDAMENTAL","credits":5,"hours": 4,"semester":6,"order":43,"area":"metodo","prereqs":["I6001"]},

    # ===== Semestre VII =====
    {"id":"I6024","code":"I6024","name":"LABORATORIO DE FISICA II","credits":2,"hours": 2,"semester":7,"order":44,"area":"fis","prereqs":[]},
    {"id":"SPC-VII-02", "semester":7, "order":45, "kind":"spacer", "rows":1},
    {"id":"SPC-VII-03", "semester":7, "order":45, "kind":"spacer", "rows":1},    
    {"id":"I6028","code":"I6028","name":"MECANICA DEL MEDIO CONTINUO","credits":10,"hours": 6,"semester":7,"order":45,"area":"fis","prereqs":[]},
    {"id":"I6026","code":"I6026","name":"MECANICA CUANTICA","credits":10,"hours": 6,"semester":7,"order":46,"area":"fis","prereqs":[]},
    {"id":"I6023","code":"I6023","name":"METODOS MATEMATICOS DE LA FISICA","credits":7,"hours": 0,"semester":7,"order":47,"area":"mate","prereqs":[]},
    {"id":"SPC-VII-07", "semester":7, "order":48, "kind":"spacer", "rows":1},    
    {"id":"OPTA1","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":7,"order":48,"area":"extra","prereqs":[]},

    # ===== Semestre VIII =====
    {"id":"SPC-VIII-01", "semester":8, "order":49, "kind":"spacer", "rows":1},
    {"id":"SPC-VIII-02", "semester":8, "order":49, "kind":"spacer", "rows":1},    
    {"id":"I6027","code":"I6027","name":"FISICA ESTADISTICA","credits":10,"hours": 6,"semester":8,"order":49,"area":"fis","prereqs":[]},
    {"id":"I6031","code":"I6031","name":"FISICA DE MATERIA CONDENSADA ","credits":7,"hours": 4,"semester":8,"order":50,"area":"fis","prereqs":[]},
    {"id":"I6022","code":"I6022","name":"HISTORIA Y FILOSOFIA DE LA FISICA","credits":7,"hours": 4,"semester":8,"order":51,"area":"educ","prereqs":[]},
    {"id":"SPC-VIII-07", "semester":8, "order":52, "kind":"spacer", "rows":1},
    {"id":"SPC-VIII-07", "semester":8, "order":52, "kind":"spacer", "rows":1},
    {"id":"OPTA2","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":8,"order":52,"area":"extra","prereqs":[]},
    {"id":"I6035","code":"I6035","name":"CLINICA TUTORIAL IV","credits":2,"hours": 2,"semester":8,"order":53,"area":"metodo","prereqs":["I6034"]},

    # ===== Semestre IX =====
    {"id":"I6029","code":"I6029","name":"LABORATORIO DE FISICA III","credits":2,"hours": 2,"semester":9,"order":54,"area":"fis","prereqs":["I6004"]},
    {"id":"SPC-IX-06", "semester":9, "order":55, "kind":"spacer", "rows":1},
    {"id":"SPC-IX-06", "semester":9, "order":55, "kind":"spacer", "rows":1},
    {"id":"I6021","code":"I6021","name":"DISEÑO Y EVALUACION DE RECURSOS EDUCATIVOS","credits":7,"hours": 4,"semester":9,"order":55,"area":"educ","prereqs":[]},
    {"id":"I6040","code":"I6040","name":"CLINICA DE FORMACION ESPECIALIZANTE","credits":5,"hours": 4,"semester":9,"order":56,"area":"metodo","prereqs":["I6025"]},
    {"id":"I6041","code":"I6041","name":"CLINICA DE FORMACION INTER O MULTIDSCIPLINAR","credits":5,"hours": 4,"semester":9,"order":57,"area":"metodo","prereqs":["I6025"]},
    {"id":"I6017","code":"I6017","name":"SIMULACION DE PROCESOS FISICOS","credits":5,"hours": 4,"semester":9,"order":58,"area":"progra","prereqs":[]},
    {"id":"OPTA3","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":9,"order":59,"area":"extra","prereqs":[]},
    {"id":"I6036","code":"I6036","name":"CLINICA TUTORIAL V","credits":2,"hours": 2,"semester":9,"order":60,"area":"metodo","prereqs":["I6035"]}
]


mod_lifi_courses = [
    # ===== Semestre I =====
    {"id":"I5989","code":"I5989","name":"METODOLOGIA EXPERIMENTAL","credits":3, "hours": 2,"semester":1,"order":1,"area":"metodo","prereqs":[]},
    {"id":"I5988","code":"I5988","name":"LABORATORIO DE MECANICA","credits":2,"hours": 2,"semester":1,"order":2,"area":"lab","prereqs":[]},
    {"id":"I5304","code":"I5304","name":"MECANICA","credits":5,"hours": 2,"semester":1,"order":3,"area":"fis","prereqs":[]},
    {"id":"I5987","code":"I5987","name":"TALLER DE RESOLUCION DE PROBLEMAS DE MECANICA","credits":2,"hours": 2,"semester":1,"order":4,"area":"fis","prereqs":[]},
    {"id":"I5991","code":"I5991","name":"ALGEBRA LINEAL I","credits":10,"hours": 6,"semester":1,"order":5,"area":"mate","prereqs":[]},
    {"id":"I5990","code":"I5990","name":"CALCULO DIFERENCIAL E INTEGRAL I","credits":10,"hours": 6,"semester":1,"order":6,"area":"mate","prereqs":[]},
    {"id":"I5992","code":"I5992","name":"COMPUTO CIENTIFICO I","credits":5,"hours": 4,"semester":1,"order":7,"area":"progra","prereqs":[]},
    {"id":"I6032","code":"I6032","name":"CLINICIA TUTORIAL I","credits":2,"hours": 2,"semester":1,"order":8,"area":"metodo","prereqs":[]},

    # ===== Semestre II =====
    {"id":"I6008","code":"I6008","name":"TEORIA DE LA PROBABILIDAD Y ESTADISTICA MATEMATICA","credits":7,"hours": 4,"semester":2,"order":9,"area":"mate","prereqs":["I5990"]},
    {"id":"I5995","code":"I5995","name":"LABORATORIO DE ELECTROMAGNETISMO","credits":3,"hours": 3,"semester":2,"order":10,"area":"lab","prereqs":["I5988"]},
    {"id":"I5993","code":"I5993","name":"ELECTROMAGNETISMO","credits":5,"hours": 2,"semester":2,"order":11,"area":"fis","prereqs":["I5304"]},
    {"id":"I5994","code":"I5994","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ELECTROMAGNETISMO","credits":2,"hours": 2,"semester":2,"order":12,"area":"fis","prereqs":["I5987"]},
    {"id":"I6000","code":"I6000","name":"ALGEBRA LINEAL II","credits":7,"hours": 4,"semester":2,"order":13,"area":"mate","prereqs":["I5991"]},
    {"id":"I5999","code":"I5999","name":"CALCULO DIFERENCIAL E INTEGRAL II","credits":7,"hours": 4,"semester":2,"order":14,"area":"mate","prereqs":["I5990"]},
    {"id":"SPC-II-07", "semester":2, "order":15, "kind":"spacer", "rows":1},
    {"id":"I6033","code":"I6033","name":"CLINICA TUTORIAL II","credits":2,"hours": 2,"semester":2,"order":15,"area":"metodo","prereqs":["I6032"]},

    # ===== Semestre III =====
    {"id":"I6011","code":"I6011","name":"SEMINARIO DE INVESTIGACION ","credits":3,"hours": 2,"semester":3,"order":16,"area":"metodo","prereqs":["I5989"]},
    {"id":"I5998","code":"I5998","name":"LABORATORIO DE ONDAS, FLUIDOS Y FISICA MOLECULAR ","credits":2,"hours": 2,"semester":3,"order":17,"area":"lab","prereqs":["I5988"]},
    {"id":"I5996","code":"I5996","name":"ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":5,"hours": 2,"semester":3,"order":18,"area":"fis","prereqs":["I5304"]},
    {"id":"I5997","code":"I5997","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":2,"hours": 2,"semester":3,"order":19,"area":"fis","prereqs":["I5987"]},
    {"id":"I6010","code":"I6010","name":"ECUACIONES DIFERENCIALES ORDINARIAS Y MODELACION DE SISTEMAS","credits":7,"hours": 4,"semester":3,"order":20,"area":"mate","prereqs":["I5999","I6000"]},
    {"id":"I6009","code":"I6009","name":"CALCULO AVANZADO PARA FISICA","credits":7,"hours": 4,"semester":3,"order":21,"area":"mate","prereqs":["I5999"]},
    {"id":"I6014","code":"I6014","name":"VARIABLE COMPLEJA","credits":7,"hours": 4,"semester":3,"order":22,"area":"mate","prereqs":["I5999","I6000"]},
    {"id":"I6001","code":"I6001","name":"CLINICA DE HABILIDADES BASICAS","credits":5,"hours": 4,"semester":3,"order":23,"area":"metodo","prereqs":["I6032"]},

    # ===== Semestre IV =====
    {"id":"I6037","code":"I6037","name":"TRABAJO INTEGRADOR DE CICLO DE FORMACION MODULAR BASICO","credits":20,"hours": 0,"semester":4,"order":24,"area":"extra","prereqs":["I6001"]},
    {"id":"I6004","code":"I6004","name":"LABORATORIO DE FISICA MODERNA","credits":2,"hours": 2,"semester":4,"order":25,"area":"lab","prereqs":["I5988"]},
    {"id":"I6002","code":"I6002","name":"FISICA MODERNA","credits":5,"hours": 2,"semester":4,"order":26,"area":"fis","prereqs":["I5304"]},
    {"id":"I6003","code":"I6003","name":"TALLER DE RESOLUCION DE PROBLEMAS DE FISICA MODERNA ","credits":2,"hours": 2,"semester":4,"order":27,"area":"fis","prereqs":["I5987"]},
    {"id":"I6030","code":"I6030","name":"ALGEBRA MULTILINEAL","credits":7,"hours": 4,"semester":4,"order":28,"area":"mate","prereqs":["I6010"]},
    {"id":"I6012","code":"I6012","name":"MECANICA TEORICA","credits":10,"hours": 6,"semester":4,"order":29,"area":"fis","prereqs":["I6010","I6009","I6014"]},
    {"id":"I6007","code":"I6007","name":"COMPUTO CIENTIFICO II","credits":5,"hours": 4,"semester":4,"order":30,"area":"progra","prereqs":["I5992","I6010"]},
    
    # ===== Semestre V =====
    {"id":"I6042","code":"I6042","name":"ACTIVIDADES DE FORMACION INTEGRAL","credits":16,"hours": 240,"semester":5,"order":31,"area":"extra","prereqs":[]},
    {"id":"I6006","code":"I6006","name":"LABORATORIO DE ELECTRONICA BASICA","credits":3,"hours": 3,"semester":5,"order":32,"area":"lab","prereqs":["I5993"]},
    {"id":"I6013","code":"I6013","name":"ELECTRODINAMICA","credits":10,"hours": 6,"semester":5,"order":33,"area":"fis","prereqs":["I5993"]},
    {"id":"I6018","code":"I6018","name":"TERMODINAMICA","credits":7,"hours": 4,"semester":5,"order":34,"area":"fis","prereqs":["I6030"]},
    {"id":"I6015","code":"I6015","name":"ECUACIONES DIFERENCIALES PARCIALES Y FUNCIONES ESPECIALES","credits":8,"hours": 5,"semester":5,"order":35,"area":"mate","prereqs":["I6010", "I6009"]},
    {"id":"SPC-V-06", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"SPC-V-07", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"I6034","code":"I6034","name":"CLINICA TUTORIAL III","credits":2,"hours": 2,"semester":5,"order":36,"area":"metodo","prereqs":["I6033"]},
   
    # ===== Semestre VI =====
    {"id":"SPC-VI-04", "semester":6, "order":37, "kind":"spacer", "rows":1},
    {"id":"I6016","code":"I6016","name":"LABORATORIO DE FISICA I","credits":2,"hours": 2,"semester":6,"order":37,"area":"fis","prereqs":["I6004"]},
    {"id":"I6019","code":"I6019","name":"OPTICA","credits":7,"hours": 4,"semester":6,"order":38,"area":"fis","prereqs":["I5996"]},
    {"id":"I5803","code":"I5803","name":"QUIMICA GENERAL I","credits":9,"hours": 5,"semester":6,"order":39,"area":"quim","prereqs":["I5304"]},
    {"id":"I6922","code":"I6922","name":"LABORATORIO DE QUIMICA GENERAL I","credits":3,"hours": 3,"semester":6,"order":40,"area":"quim","prereqs":["I5988"]},
    {"id":"I6020","code":"I6020","name":"FISICA RELATIVISTA","credits":7,"hours": 4,"semester":6,"order":41,"area":"fis","prereqs":["I6030"]},
    {"id":"SPC-VI-05", "semester":6, "order":42, "kind":"spacer", "rows":1},
    {"id":"I6025","code":"I6025","name":"CLINICA DE FORMACION FUNDAMENTAL","credits":5,"hours": 4,"semester":6,"order":42,"area":"metodo","prereqs":["I6001"]},

    # ===== Semestre VII =====
    {"id":"I6038","code":"I6037","name":"TRABAJO INTEGRADOR DE CICLO DE FORMACION MODULAR FUNDAMENTAL","credits":20,"hours": 0,"semester":7,"order":43,"area":"extra","prereqs":["I6025"]},
    {"id":"I6024","code":"I6024","name":"LABORATORIO DE FISICA II","credits":2,"hours": 2,"semester":7,"order":44,"area":"fis","prereqs":["I6004"]},
    {"id":"I6028","code":"I6028","name":"MECANICA DEL MEDIO CONTINUO","credits":10,"hours": 6,"semester":7,"order":45,"area":"fis","prereqs":["I6012"]},
    {"id":"OPTA1","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":7,"order":46,"area":"extra","prereqs":["I6020"]},
    {"id":"I6023","code":"I6023","name":"METODOS MATEMATICOS DE LA FISICA","credits":7,"hours": 0,"semester":7,"order":47,"area":"mate","prereqs":["I6030"]},
    {"id":"I6026","code":"I6026","name":"MECANICA CUANTICA","credits":10,"hours": 6,"semester":7,"order":48,"area":"fis","prereqs":["I6012"]},

    # ===== Semestre VIII =====
    {"id":"SPC-VIII-01", "semester":8, "order":49, "kind":"spacer", "rows":1},
    {"id":"SPC-VIII-02", "semester":8, "order":49, "kind":"spacer", "rows":1},
    {"id":"I6022","code":"I6022","name":"HISTORIA Y FILOSOFIA DE LA FISICA","credits":7,"hours": 4,"semester":8,"order":49,"area":"educ","prereqs":["I6011", "I6026", "I6020"]},
    {"id":"OPTA2","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":8,"order":50,"area":"extra","prereqs":["I6020"]},
    {"id":"I6031","code":"I6031","name":"FISICA DE MATERIA CONDENSADA ","credits":7,"hours": 4,"semester":8,"order":51,"area":"fis","prereqs":["I6023"]},
    {"id":"I6027","code":"I6027","name":"FISICA ESTADISTICA","credits":10,"hours": 6,"semester":8,"order":52,"area":"fis","prereqs":["I6026", "I6008"]},
    {"id":"SPC-VIII-07", "semester":8, "order":53, "kind":"spacer", "rows":1},
    {"id":"I6035","code":"I6035","name":"CLINICA TUTORIAL IV","credits":2,"hours": 2,"semester":8,"order":53,"area":"metodo","prereqs":["I6034"]},

    # ===== Semestre IX =====
    {"id":"SPC-IX-06", "semester":9, "order":54, "kind":"spacer", "rows":1},
    {"id":"I6029","code":"I6029","name":"LABORATORIO DE FISICA III","credits":2,"hours": 2,"semester":9,"order":54,"area":"fis","prereqs":["I6004"]},
    {"id":"I6021","code":"I6021","name":"DISEÑO Y EVALUACION DE RECURSOS EDUCATIVOS","credits":7,"hours": 4,"semester":9,"order":55,"area":"educ","prereqs":["I6020"]},
    {"id":"OPTA3","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":9,"order":56,"area":"extra","prereqs":["I6020"]},
    {"id":"SPC-IX-06", "semester":9, "order":57, "kind":"spacer", "rows":1},
    {"id":"I6040","code":"I6040","name":"CLINICA DE FORMACION ESPECIALIZANTE","credits":5,"hours": 4,"semester":9,"order":57,"area":"metodo","prereqs":["I6025"]},
    {"id":"I6017","code":"I6017","name":"SIMULACION DE PROCESOS FISICOS","credits":5,"hours": 4,"semester":9,"order":58,"area":"progra","prereqs":["I6007"]},
    {"id":"I6036","code":"I6036","name":"CLINICA TUTORIAL V","credits":2,"hours": 2,"semester":9,"order":59,"area":"metodo","prereqs":["I6035"]},

    # ==== Semestre X =====
    {"id":"I6041","code":"I6041","name":"CLINICA DE FORMACION INTER O MULTIDISCIPLINAR","credits":5,"hours": 4,"semester":10,"order":60,"area":"metodo","prereqs":["I6040"]},
    {"id":"I6039","code":"I6037","name":"TRABAJO INTEGRADOR DE CICLO DE FORMACION MODULAR ESPECIALIZANTE","credits":20,"hours": 0,"semester":10,"order":61,"area":"extra","prereqs":["I6040"]},
    {"id":"IA898","code":"IA898","name":"PRACTICAS PROFESIONALES","credits":20,"hours": 300,"semester":10,"order":62,"area":"extra","prereqs":[]},

]

per_lifi_courses = [
    # ===== Semestre I =====
    {"id":"I5989","code":"I5989","name":"METODOLOGIA EXPERIMENTAL","credits":3, "hours": 2,"semester":1,"order":1,"area":"metodo","prereqs":[]},
    {"id":"I5988","code":"I5988","name":"LABORATORIO DE MECANICA","credits":2,"hours": 2,"semester":1,"order":2,"area":"lab","prereqs":[]},
    {"id":"I5304","code":"I5304","name":"MECANICA","credits":5,"hours": 2,"semester":1,"order":3,"area":"fis","prereqs":[]},
    {"id":"I5987","code":"I5987","name":"TALLER DE RESOLUCION DE PROBLEMAS DE MECANICA","credits":2,"hours": 2,"semester":1,"order":4,"area":"fis","prereqs":[]},
    {"id":"I5991","code":"I5991","name":"ALGEBRA LINEAL I","credits":10,"hours": 6,"semester":1,"order":5,"area":"mate","prereqs":[]},
    {"id":"I5990","code":"I5990","name":"CALCULO DIFERENCIAL E INTEGRAL I","credits":10,"hours": 6,"semester":1,"order":6,"area":"mate","prereqs":[]},
    {"id":"I5992","code":"I5992","name":"COMPUTO CIENTIFICO I","credits":5,"hours": 4,"semester":1,"order":7,"area":"progra","prereqs":[]},
    {"id":"SPC-I-08", "semester":1, "order":8, "kind":"spacer", "rows":1},
    {"id":"I6032","code":"I6032","name":"CLINICIA TUTORIAL I","credits":2,"hours": 2,"semester":1,"order":8,"area":"metodo","prereqs":[]},

    # ===== Semestre II =====
    {"id":"SPC-II-01", "semester":2, "order":9, "kind":"spacer", "rows":1},
    {"id":"I5995","code":"I5995","name":"LABORATORIO DE ELECTROMAGNETISMO","credits":3,"hours": 3,"semester":2,"order":10,"area":"lab","prereqs":[]},
    {"id":"I5993","code":"I5993","name":"ELECTROMAGNETISMO","credits":5,"hours": 2,"semester":2,"order":11,"area":"fis","prereqs":[]},
    {"id":"I5994","code":"I5994","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ELECTROMAGNETISMO","credits":2,"hours": 2,"semester":2,"order":12,"area":"fis","prereqs":[]},
    {"id":"I6000","code":"I6000","name":"ALGEBRA LINEAL II","credits":7,"hours": 4,"semester":2,"order":13,"area":"mate","prereqs":[]},
    {"id":"I5999","code":"I5999","name":"CALCULO DIFERENCIAL E INTEGRAL II","credits":7,"hours": 4,"semester":2,"order":14,"area":"mate","prereqs":[]},
    {"id":"SPC-II-07", "semester":2, "order":14, "kind":"spacer", "rows":1},
    {"id":"I6008","code":"I6008","name":"TEORIA DE LA PROBABILIDAD Y ESTADISTICA MATEMATICA","credits":7,"hours": 4,"semester":2,"order":15,"area":"mate","prereqs":[]},
    {"id":"I6033","code":"I6033","name":"CLINICA TUTORIAL II","credits":2,"hours": 2,"semester":2,"order":16,"area":"metodo","prereqs":[]},

    # ===== Semestre III =====
    {"id":"SPC-III-01", "semester":3, "order":16, "kind":"spacer", "rows":1},
    {"id":"I5998","code":"I5998","name":"LABORATORIO DE ONDAS, FLUIDOS Y FISICA MOLECULAR ","credits":2,"hours": 2,"semester":3,"order":16,"area":"lab","prereqs":[]},
    {"id":"I5996","code":"I5996","name":"ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":5,"hours": 2,"semester":3,"order":17,"area":"fis","prereqs":[]},
    {"id":"I5997","code":"I5997","name":"TALLER DE RESOLUCION DE PROBLEMAS DE ONDAS, FLUIDOS Y FISICA MOLECULAR","credits":2,"hours": 2,"semester":3,"order":18,"area":"fis","prereqs":[]},
    {"id":"I6010","code":"I6010","name":"ECUACIONES DIFERENCIALES ORDINARIAS Y MODELACION DE SISTEMAS","credits":7,"hours": 4,"semester":3,"order":19,"area":"mate","prereqs":[]},
    {"id":"I6009","code":"I6009","name":"CALCULO AVANZADO PARA FISICA","credits":7,"hours": 4,"semester":3,"order":20,"area":"mate","prereqs":[]},
    {"id":"I6011","code":"I6011","name":"SEMINARIO DE INVESTIGACION ","credits":3,"hours": 2,"semester":3,"order":21,"area":"metodo","prereqs":[]},
    {"id":"I6014","code":"I6014","name":"VARIABLE COMPLEJA","credits":7,"hours": 4,"semester":3,"order":22,"area":"mate","prereqs":[]},
    {"id":"I6001","code":"I6001","name":"CLINICA DE HABILIDADES BASICAS","credits":5,"hours": 4,"semester":3,"order":23,"area":"metodo","prereqs":[]},

    # ===== Semestre IV =====
    {"id":"SPC-IV-01", "semester":4, "order":24, "kind":"spacer", "rows":1},
    {"id":"I6004","code":"I6004","name":"LABORATORIO DE FISICA MODERNA","credits":2,"hours": 2,"semester":4,"order":24,"area":"lab","prereqs":[]},
    {"id":"I6002","code":"I6002","name":"FISICA MODERNA","credits":5,"hours": 2,"semester":4,"order":25,"area":"fis","prereqs":[]},
    {"id":"I6003","code":"I6003","name":"TALLER DE RESOLUCION DE PROBLEMAS DE FISICA MODERNA ","credits":2,"hours": 2,"semester":4,"order":26,"area":"fis","prereqs":[]},
    {"id":"I6030","code":"I6030","name":"ALGEBRA MULTILINEAL","credits":7,"hours": 4,"semester":4,"order":27,"area":"mate","prereqs":[]},
    {"id":"I6012","code":"I6012","name":"MECANICA TEORICA","credits":10,"hours": 6,"semester":4,"order":28,"area":"fis","prereqs":[]},
    {"id":"I6007","code":"I6007","name":"COMPUTO CIENTIFICO II","credits":5,"hours": 4,"semester":4,"order":29,"area":"progra","prereqs":[]},
    
    # ===== Semestre V =====
    {"id":"I6006","code":"I6006","name":"LABORATORIO DE ELECTRONICA BASICA","credits":3,"hours": 3,"semester":5,"order":32,"area":"lab","prereqs":[]},
    {"id":"SPC-V-02", "semester":5, "order":33, "kind":"spacer", "rows":1},
    {"id":"I6013","code":"I6013","name":"ELECTRODINAMICA","credits":10,"hours": 6,"semester":5,"order":33,"area":"fis","prereqs":[]},
    {"id":"I6018","code":"I6018","name":"TERMODINAMICA","credits":7,"hours": 4,"semester":5,"order":34,"area":"fis","prereqs":[]},
    {"id":"I6015","code":"I6015","name":"ECUACIONES DIFERENCIALES PARCIALES Y FUNCIONES ESPECIALES","credits":8,"hours": 5,"semester":5,"order":35,"area":"mate","prereqs":[]},
    {"id":"SPC-V-06", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"SPC-V-07", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"SPC-V-08", "semester":5, "order":36, "kind":"spacer", "rows":1},
    {"id":"I6034","code":"I6034","name":"CLINICA TUTORIAL III","credits":2,"hours": 2,"semester":5,"order":36,"area":"metodo","prereqs":[]},
   
    # ===== Semestre VI =====
    {"id":"I6016","code":"I6016","name":"LABORATORIO DE FISICA I","credits":2,"hours": 2,"semester":6,"order":37,"area":"fis","prereqs":[]},
    {"id":"SPC-VI-02", "semester":6, "order":38, "kind":"spacer", "rows":1},
    {"id":"I6019","code":"I6019","name":"OPTICA","credits":7,"hours": 4,"semester":6,"order":38,"area":"fis","prereqs":[]},
    {"id":"I6020","code":"I6020","name":"FISICA RELATIVISTA","credits":7,"hours": 4,"semester":6,"order":39,"area":"fis","prereqs":[]},
    {"id":"I5803","code":"I5803","name":"QUIMICA GENERAL I","credits":9,"hours": 5,"semester":6,"order":40,"area":"quim","prereqs":[]},
    {"id":"I6922","code":"I6922","name":"LABORATORIO DE QUIMICA GENERAL I","credits":3,"hours": 3,"semester":6,"order":41,"area":"quim","prereqs":[]},
    {"id":"SPC-VI-07", "semester":6, "order":42, "kind":"spacer", "rows":1},
    {"id":"SPC-VI-08", "semester":6, "order":42, "kind":"spacer", "rows":1},
    {"id":"I6025","code":"I6025","name":"CLINICA DE FORMACION FUNDAMENTAL","credits":5,"hours": 4,"semester":6,"order":42,"area":"metodo","prereqs":[]},

    # ===== Semestre VII =====
    {"id":"I6024","code":"I6024","name":"LABORATORIO DE FISICA II","credits":2,"hours": 2,"semester":7,"order":43,"area":"fis","prereqs":[]},
    {"id":"SPC-VII-02", "semester":7, "order":44, "kind":"spacer", "rows":1},
    {"id":"SPC-VII-03", "semester":7, "order":44, "kind":"spacer", "rows":1},    
    {"id":"I6028","code":"I6028","name":"MECANICA DEL MEDIO CONTINUO","credits":10,"hours": 6,"semester":7,"order":44,"area":"fis","prereqs":[]},
    {"id":"I6026","code":"I6026","name":"MECANICA CUANTICA","credits":10,"hours": 6,"semester":7,"order":45,"area":"fis","prereqs":[]},
    {"id":"I6023","code":"I6023","name":"METODOS MATEMATICOS DE LA FISICA","credits":7,"hours": 0,"semester":7,"order":46,"area":"mate","prereqs":[]},
    {"id":"SPC-VII-07", "semester":7, "order":47, "kind":"spacer", "rows":1},    
    {"id":"OPTA1","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":7,"order":47,"area":"extra","prereqs":[]},

    # ===== Semestre VIII =====
    {"id":"SPC-VIII-01", "semester":8, "order":48, "kind":"spacer", "rows":1},
    {"id":"SPC-VIII-02", "semester":8, "order":48, "kind":"spacer", "rows":1},    
    {"id":"I6027","code":"I6027","name":"FISICA ESTADISTICA","credits":10,"hours": 6,"semester":8,"order":48,"area":"fis","prereqs":[]},
    {"id":"I6031","code":"I6031","name":"FISICA DE MATERIA CONDENSADA ","credits":7,"hours": 4,"semester":8,"order":49,"area":"fis","prereqs":[]},
    {"id":"I6022","code":"I6022","name":"HISTORIA Y FILOSOFIA DE LA FISICA","credits":7,"hours": 4,"semester":8,"order":50,"area":"educ","prereqs":[]},
    {"id":"SPC-VIII-07", "semester":8, "order":51, "kind":"spacer", "rows":1},
    {"id":"SPC-VIII-07", "semester":8, "order":51, "kind":"spacer", "rows":1},
    {"id":"OPTA2","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":8,"order":51,"area":"extra","prereqs":[]},
    {"id":"I6035","code":"I6035","name":"CLINICA TUTORIAL IV","credits":2,"hours": 2,"semester":8,"order":52,"area":"metodo","prereqs":[]},

    # ===== Semestre IX =====
    {"id":"I6029","code":"I6029","name":"LABORATORIO DE FISICA III","credits":2,"hours": 2,"semester":9,"order":53,"area":"fis","prereqs":[]},
    {"id":"SPC-IX-06", "semester":9, "order":54, "kind":"spacer", "rows":1},
    {"id":"SPC-IX-06", "semester":9, "order":54, "kind":"spacer", "rows":1},
    {"id":"I6021","code":"I6021","name":"DISEÑO Y EVALUACION DE RECURSOS EDUCATIVOS","credits":7,"hours": 4,"semester":9,"order":54,"area":"educ","prereqs":[]},
    {"id":"I6040","code":"I6040","name":"CLINICA DE FORMACION ESPECIALIZANTE","credits":5,"hours": 4,"semester":9,"order":55,"area":"metodo","prereqs":[]},
    {"id":"I6041","code":"I6041","name":"CLINICA DE FORMACION INTER O MULTIDSCIPLINAR","credits":5,"hours": 4,"semester":9,"order":56,"area":"metodo","prereqs":[]},
    {"id":"I6017","code":"I6017","name":"SIMULACION DE PROCESOS FISICOS","credits":5,"hours": 4,"semester":9,"order":57,"area":"progra","prereqs":[]},
    {"id":"OPTA3","code":"","name":"OPTATIVA","credits":7,"hours": 4,"semester":9,"order":58,"area":"extra","prereqs":[]},
    {"id":"I6036","code":"I6036","name":"CLINICA TUTORIAL V","credits":2,"hours": 2,"semester":9,"order":59,"area":"metodo","prereqs":[]}

]


base_lqfb_courses = [
    # ===== Semestre I =====
    {"id":"I6121","code":"I6121","name":"CALCULO DIFERENCIAL INTEGRAL","credits":8,"hours":10,"semester":1,"order":1,"area":"mate","prereqs":[]},
    {"id":"I6156","code":"I6156","name":"BIOETICA Y DEONTOLOGIA","credits":5,"hours":4,"semester":1,"order":2,"area":"farma","prereqs":[]},
    {"id":"I6122","code":"I6122","name":"QUIMICA GENERAL I","credits":9,"hours":5,"semester":1,"order":3,"area":"quim","prereqs":[]},
    {"id":"I6123","code":"I6123","name":"INTRODUCCION A LA FISICA","credits":7,"hours":4,"semester":1,"order":4,"area":"fis","prereqs":[]},
    {"id":"I6134","code":"I6134","name":"BASES DE BIOLOGIA CELULAR","credits":9,"hours":5,"semester":1,"order":5,"area":"farma","prereqs":[]},
    {"id":"I6157","code":"I6157","name":"METODOLOGIA DE LA INVESTIGACION","credits":2,"hours":3,"semester":1,"order":6,"area":"metodo","prereqs":[]},
    {"id":"I6159","code":"I6159","name":"SEMINARIO DE TUTORIA INICIAL I","credits":2,"hours":2,"semester":1,"order":7,"area":"metodo","prereqs":[]},

    # ===== Semestre II =====
    {"id":"I6136","code":"I6136","name":"SALUD Y SOCIEDAD","credits":7,"hours":4,"semester":2,"order":8,"area":"med","prereqs":["I6156"]},
    {"id":"I6124","code":"I6124","name":"QUIMICA ORGANICA I","credits":9,"hours":5,"semester":2,"order":9,"area":"quim","prereqs":["I6122"]},
    {"id":"I6125","code":"I6125","name":"BIOESTADISTICA","credits":7,"hours":4,"semester":2,"order":10,"area":"farma","prereqs":[]},
    {"id":"I6135","code":"I6135","name":"MORFOLOGIA","credits":8,"hours":5,"semester":2,"order":11,"area":"farma","prereqs":["I6134"]},
    {"id":"I6126","code":"I6126","name":"QUIMICA GENERAL II","credits":9,"hours":5,"semester":2,"order":12,"area":"quim","prereqs":["I6122"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA I","credits":7,"hours":3,"semester":2,"order":13,"area":"extra","prereqs":[]},
    {"id":"I6160","code":"I6160","name":"SEMINARIO DE TUTORIA INICIAL II","credits":2,"hours":2,"semester":2,"order":14,"area":"metodo","prereqs":["I6159"]},

    # ===== Semestre III =====
    {"id":"I6128","code":"I6128","name":"FISICOQUIMICA I PARA FARMACEUTICOS","credits":7,"hours":4,"semester":3,"order":15,"area":"fis","prereqs":["I6121","I6126"]},
    {"id":"I6129","code":"I6129","name":"QUIMICA ORGANICA II","credits":9,"hours":5,"semester":3,"order":16,"area":"quim","prereqs":["I6124"]},
    {"id":"I6137","code":"I6137","name":"FISIOLOGIA Y FUNDAMENTOS DE FISIO-PATOLOGIA","credits":14,"hours":7,"semester":3,"order":17,"area":"med","prereqs":["I6135"]},
    {"id":"I6127","code":"I6127","name":"QUIMICA ANALITICA I","credits":8,"hours":5,"semester":3,"order":18,"area":"quim","prereqs":["I6126"]},
    {"id":"I5874","code":"I5874","name":"DISEÑO DE EXPERIMENTOS","credits":7,"hours":3,"semester":19,"order":5,"area":"metodo","prereqs":[]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA II","credits":7,"hours":3,"semester":3,"order":20,"area":"extra","prereqs":[]},
    {"id":"I6161","code":"I6161","name":"SEMINARIO DE TUTORIA INICIAL III","credits":2,"hours":2,"semester":3,"order":21,"area":"metodo","prereqs":["I6160"]},

    # ===== Semestre IV =====
    {"id":"I6131","code":"I6131","name":"FISICOQUIMICA II PARA FARMACEUTICOS","credits":7,"hours":4,"semester":4,"order":22,"area":"","prereqs":["I6128"]},
    {"id":"I6138","code":"I6138","name":"FARMACOLOGIA I","credits":7,"hours":5,"semester":4,"order":23,"area":"","prereqs":["I6137","I6129","I6136"]},
    {"id":"I6140","code":"I6140","name":"BIOQUIMICA I","credits":7,"hours":5,"semester":4,"order":24,"area":"","prereqs":["I6129","I6137"]},
    {"id":"I6139","code":"I6139","name":"NORMATIVIDAD Y LEGISLACION SANITARIA","credits":5,"hours":2,"semester":4,"order":25,"area":"","prereqs":["I6136","I6156"]},
    {"id":"I6130","code":"I6130","name":"QUIMICA ANALITICA II","credits":8,"hours":5,"semester":4,"order":26,"area":"","prereqs":["I6127"]},
    {"id":"I6141","code":"I6141","name":"PARASITOLOGIA","credits":7,"hours":5,"semester":4,"order":27,"area":"","prereqs":[]},
    {"id":"I6162","code":"I6162","name":"SEMINARIO DE TUTORIA INTERMEDIA I","credits":2,"hours":2,"semester":4,"order":28,"area":"","prereqs":["I6161"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA II","credits":4,"hours":4,"semester":4,"order":29,"area":"","prereqs":[]},

    # ===== Semestre V =====
    {"id":"I6142","code":"I6142","name":"FARMACOLOGIA II","credits":8,"hours":4,"semester":5,"order":30,"area":"farma","prereqs":["I6138"]},
    {"id":"I6144","code":"I6144","name":"BIOQUIMICA II","credits":7,"hours":5,"semester":5,"order":31,"area":"quim","prereqs":["I6140"]},
    {"id":"I6132","code":"I6132","name":"QUIMICA ANALITICA III","credits":8,"hours":5,"semester":5,"order":32,"area":"quim","prereqs":["I6130"]},
    {"id":"I6143","code":"I6143","name":"SEMINARIO DE INVESTIGACION","credits":2,"hours":2,"semester":5,"order":33,"area":"metodo","prereqs":["I6157"]},
    {"id":"I6146","code":"I6146","name":"LABORATORIO DE PARASITOLOGIA","credits":5,"hours":4,"semester":5,"order":34,"area":"lab","prereqs":[]},
    {"id":"I6145","code":"I6145","name":"MICROBIOLOGIA","credits":9,"hours":5,"semester":5,"order":35,"area":"farma","prereqs":[]},
    {"id":"I6163","code":"I6163","name":"SEMINARIO DE TUTORIA INTERMEDIA II","credits":2,"hours":2,"semester":5,"order":36,"area":"metodo","prereqs":["I6162"]},

    # ===== Semestre VI =====
    {"id":"I6147","code":"I6147","name":"FARMACOGNOSIA","credits":4,"hours":4,"semester":6,"order":37,"area":"farma","prereqs":["I6130","I6142"]},
    {"id":"I6166","code":"I6166","name":"TECNOLOGIA FARMACEUTICA I","credits":10,"hours":10,"semester":6,"order":38,"area":"farma","prereqs":["I6132","I6142"]},
    {"id":"I6148","code":"I6148","name":"BIOFARMACIA Y FARMACOCINETICA","credits":8,"hours":4,"semester":6,"order":39,"area":"farma","prereqs":["I6131","I6142"]},
    {"id":"I6149","code":"I6149","name":"BIOLOGIA MOLECULAR Y GENETICA","credits":11,"hours":3,"semester":6,"order":40,"area":"med","prereqs":["I6144"]},
    {"id":"I6150","code":"I6150","name":"TOXICOLOGIA GENERAL","credits":7,"hours":7,"semester":6,"order":41,"area":"farma","prereqs":["I6137","I6142","I6144"]},
    {"id":"I6151","code":"I6151","name":"LABORATORIO DE MICROBIOLOGIA CLINICA","credits":10,"hours":4,"semester":6,"order":42,"area":"lab","prereqs":["I6145"]},
    {"id":"I6164","code":"I6164","name":"SEMINARIO DE TUTORIA INTERMEDIA III","credits":2,"hours":2,"semester":6,"order":43,"area":"metodo","prereqs":["I6163"]},

    # ===== Semestre VII =====
    {"id":"I6167","code":"I6167","name":"TECNOLOGIA FARMACEUTICA II","credits":7,"hours":10,"semester":7,"order":44,"area":"farma","prereqs":["I6166"]},
    {"id":"I6168","code":"I6168","name":"FARMACIA COMUNITARIA Y HOSPITALARIA","credits":4,"hours":4,"semester":7,"order":45,"area":"farma","prereqs":["I5874","I6142","I6139"]},
    {"id":"I6169","code":"I6169","name":"ANALISIS QUIMICO CLINICO","credits":9,"hours":7,"semester":7,"order":46,"area":"quim","prereqs":["I6132","I6144"]},
    {"id":"I6176","code":"I6176","name":"LABORATORIO DE BIOLOGIA MOLECULAR Y GENETICA","credits":3,"hours":3,"semester":7,"order":47,"area":"lab","prereqs":[]},
    {"id":"I6170","code":"I6170","name":"QUIMICA Y TOXICOLOGIA FORENSE","credits":7,"hours":4,"semester":7,"order":48,"area":"quim","prereqs":["I6132","I6150"]},
    {"id":"I6152","code":"I6152","name":"MICROBIOLOGIA APLICADA","credits":9,"hours":5,"semester":7,"order":49,"area":"farma","prereqs":["I6151"]},
    {"id":"I6165","code":"I6165","name":"SEMINARIO DE TUTORIA DE EGRESO","credits":2,"hours":0,"semester":7,"order":50,"area":"metodo","prereqs":["I6164"]},
    {"id":"I6182","code":"I6182","name":"PROYECTO DE QUIMICA ANALITICA Y EVALUACION TOXICOLOGICA","credits":2,"hours":51,"semester":7,"order":8,"area":"extra","prereqs":[]},

    # ===== Semestre VIII =====
    {"id":"I6173","code":"I6173","name":"SERVICIOS FARMACEUTICOS HOSPITALARIOS","credits":5,"hours":5,"semester":8,"order":52,"area":"med","prereqs":["I6168","I6148"]},
    {"id":"I6153","code":"I6153","name":"ANALISIS DE FARMACOS Y MEDICAMENTOS","credits":10,"hours":7,"semester":8,"order":53,"area":"farma","prereqs":["I6132","I6142"]},
    {"id":"I6174","code":"I6174","name":"LABORATORIO DE ANALISIS QUIMICO CLINICO","credits":7,"hours":10,"semester":8,"order":54,"area":"lab","prereqs":[]},
    {"id":"I6154","code":"I6154","name":"INMUNOLOGIA","credits":9,"hours":6,"semester":8,"order":55,"area":"med","prereqs":["I6149"]},
    {"id":"I6175","code":"I6175","name":"TOXICOLOGIA APLICADA","credits":7,"hours":4,"semester":8,"order":56,"area":"farma","prereqs":["I6150"]},
    {"id":"I6171","code":"I6171","name":"ANALISIS MICROBIOLOGICOS","credits":5,"hours":5,"semester":8,"order":57,"area":"farma","prereqs":["I6151"]},
    {"id":"I6183","code":"I6183","name":"PROYECTO DE MICROBIOLOGIA","credits":2,"hours":0,"semester":8,"order":58,"area":"extra","prereqs":[]},
    {"id":"I6181","code":"I6181","name":"PROYECTO DE BIOQUIMICA CLINICA","credits":2,"hours":0,"semester":8,"order":59,"area":"extra","prereqs":[]},

    # ===== Semestre IX =====
    {"id":"I6158","code":"I6158","name":"GERENCIA Y ADMINISTRACION","credits":5,"hours":4,"semester":9,"order":60,"area":"mate","prereqs":[]},
    {"id":"I6172","code":"I6172","name":"VALIDACION DE PROCESOS Y METODOS ANALITICOS","credits":7,"hours":5,"semester":9,"order":61,"area":"farma","prereqs":["I6132","I6139"]},
    {"id":"I6155","code":"I6155","name":"ASEGURAMIENTO DE LA CALIDAD ANALITICA","credits":7,"hours":4,"semester":9,"order":62,"area":"farma","prereqs":["I6132","I6139"]},
    {"id":"I6133","code":"I6133","name":"ANALISIS BROMATOLOGICOS","credits":5,"hours":4,"semester":9,"order":63,"area":"farma","prereqs":["I6132","I6144"]},
    {"id":"I6177","code":"I6177","name":"DESARROLLO SUSTENTABLE","credits":2,"hours":5,"semester":9,"order":64,"area":"mate","prereqs":[]},
    {"id":"I6178","code":"I6178","name":"BIOTECNOLOGIA","credits":8,"hours":5,"semester":9,"order":65,"area":"farma","prereqs":["I6176","I6152"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA III","credits":4,"hours":4,"semester":9,"order":66,"area":"extra","prereqs":[]},
    {"id":"","code":"","name":"PROYECTO MODULAR DE FARMACIA","credits":2,"hours":0,"semester":9,"order":67,"area":"extra","prereqs":[]}
]

mod_lqfb_courses = [
    # ===== Semestre I =====
    {"id":"I6121","code":"I6121","name":"CALCULO DIFERENCIAL INTEGRAL","credits":8,"hours":10,"semester":1,"order":68,"area":"","prereqs":[]},
    {"id":"I6156","code":"I6156","name":"BIOETICA Y DEONTOLOGIA","credits":5,"hours":4,"semester":1,"order":69,"area":"","prereqs":[]},
    {"id":"I6122","code":"I6122","name":"QUIMICA GENERAL I","credits":9,"hours":5,"semester":1,"order":70,"area":"","prereqs":[]},
    {"id":"I6123","code":"I6123","name":"INTRODUCCION A LA FISICA","credits":7,"hours":4,"semester":1,"order":71,"area":"","prereqs":[]},
    {"id":"I6134","code":"I6134","name":"BASES DE BIOLOGIA CELULAR","credits":9,"hours":5,"semester":1,"order":72,"area":"","prereqs":[]},
    {"id":"I6157","code":"I6157","name":"METODOLOGIA DE LA INVESTIGACION","credits":2,"hours":3,"semester":1,"order":73,"area":"","prereqs":[]},
    {"id":"I6159","code":"I6159","name":"SEMINARIO DE TUTORIA INICIAL I","credits":2,"hours":2,"semester":1,"order":74,"area":"","prereqs":[]},

    # ===== Semestre II =====
    {"id":"I6136","code":"I6136","name":"SALUD Y SOCIEDAD","credits":7,"hours":4,"semester":2,"order":75,"area":"","prereqs":["I6156"]},
    {"id":"I6124","code":"I6124","name":"QUIMICA ORGANICA I","credits":9,"hours":5,"semester":2,"order":76,"area":"","prereqs":["I6122"]},
    {"id":"I6125","code":"I6125","name":"BIOESTADISTICA","credits":7,"hours":4,"semester":2,"order":77,"area":"","prereqs":[]},
    {"id":"I6135","code":"I6135","name":"MORFOLOGIA","credits":8,"hours":5,"semester":2,"order":78,"area":"farma","prereqs":["I6134"]},
    {"id":"I6126","code":"I6126","name":"QUIMICA GENERAL II","credits":9,"hours":5,"semester":2,"order":79,"area":"","prereqs":["I6122"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA I","credits":7,"hours":3,"semester":2,"order":80,"area":"","prereqs":[]},
    {"id":"I6160","code":"I6160","name":"SEMINARIO DE TUTORIA INICIAL II","credits":2,"hours":2,"semester":2,"order":81,"area":"","prereqs":["I6159"]},

    # ===== Semestre III =====
    {"id":"I6128","code":"I6128","name":"FISICOQUIMICA I PARA FARMACEUTICOS","credits":7,"hours":4,"semester":3,"order":82,"area":"","prereqs":["I6121","I6126"]},
    {"id":"I6129","code":"I6129","name":"QUIMICA ORGANICA II","credits":9,"hours":5,"semester":3,"order":83,"area":"","prereqs":["I6124"]},
    {"id":"I6137","code":"I6137","name":"FISIOLOGIA Y FUNDAMENTOS DE FISIO-PATOLOGIA","credits":14,"hours":7,"semester":84,"order":3,"area":"","prereqs":["I6135"]},
    {"id":"I6127","code":"I6127","name":"QUIMICA ANALITICA I","credits":8,"hours":5,"semester":3,"order":85,"area":"","prereqs":["I6126"]},
    {"id":"I5874","code":"I5874","name":"DISEÑO DE EXPERIMENTOS","credits":7,"hours":3,"semester":3,"order":86,"area":"","prereqs":[]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA I","credits":7,"hours":3,"semester":3,"order":87,"area":"","prereqs":[]},
    {"id":"I6161","code":"I6161","name":"SEMINARIO DE TUTORIA INICIAL III","credits":2,"hours":2,"semester":3,"order":88,"area":"","prereqs":["I6160"]},

    # ===== Semestre IV =====
    {"id":"I6131","code":"I6131","name":"FISICOQUIMICA II PARA FARMACEUTICOS","credits":7,"hours":4,"semester":4,"order":1,"area":"","prereqs":["I6128"]},
    {"id":"I6138","code":"I6138","name":"FARMACOLOGIA I","credits":7,"hours":5,"semester":4,"order":2,"area":"","prereqs":["I6137","I6129","I6136"]},
    {"id":"I6140","code":"I6140","name":"BIOQUIMICA I","credits":7,"hours":5,"semester":4,"order":3,"area":"","prereqs":["I6129","I6137"]},
    {"id":"I6139","code":"I6139","name":"NORMATIVIDAD Y LEGISLACION SANITARIA","credits":5,"hours":2,"semester":4,"order":4,"area":"","prereqs":["I6136","I6156"]},
    {"id":"I6130","code":"I6130","name":"QUIMICA ANALITICA II","credits":8,"hours":5,"semester":4,"order":5,"area":"","prereqs":["I6127"]},
    {"id":"I6141","code":"I6141","name":"PARASITOLOGIA","credits":7,"hours":5,"semester":4,"order":6,"area":"","prereqs":[]},
    {"id":"I6162","code":"I6162","name":"SEMINARIO DE TUTORIA INTERMEDIA I","credits":2,"hours":2,"semester":4,"order":7,"area":"","prereqs":["I6161"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA II","credits":4,"hours":4,"semester":4,"order":8,"area":"","prereqs":[]},

    # ===== Semestre V =====
    {"id":"I6142","code":"I6142","name":"FARMACOLOGIA II","credits":8,"hours":4,"semester":5,"order":1,"area":"","prereqs":["I6138"]},
    {"id":"I6144","code":"I6144","name":"BIOQUIMICA II","credits":7,"hours":5,"semester":5,"order":2,"area":"","prereqs":["I6140"]},
    {"id":"I6132","code":"I6132","name":"QUIMICA ANALITICA III","credits":8,"hours":5,"semester":5,"order":3,"area":"","prereqs":["I6130"]},
    {"id":"I6143","code":"I6143","name":"SEMINARIO DE INVESTIGACION","credits":2,"hours":2,"semester":5,"order":4,"area":"","prereqs":["I6157"]},
    {"id":"I6146","code":"I6146","name":"LABORATORIO DE PARASITOLOGIA","credits":5,"hours":4,"semester":5,"order":5,"area":"","prereqs":[]},
    {"id":"I6145","code":"I6145","name":"MICROBIOLOGIA","credits":9,"hours":5,"semester":5,"order":6,"area":"","prereqs":[]},
    {"id":"I6163","code":"I6163","name":"SEMINARIO DE TUTORIA INTERMEDIA II","credits":2,"hours":2,"semester":5,"order":7,"area":"","prereqs":["I6162"]},

    # ===== Semestre VI =====
    {"id":"I6147","code":"I6147","name":"FARMACOGNOSIA","credits":4,"hours":4,"semester":6,"order":1,"area":"","prereqs":["I6130","I6142"]},
    {"id":"I6166","code":"I6166","name":"TECNOLOGIA FARMACEUTICA I","credits":10,"hours":10,"semester":6,"order":2,"area":"","prereqs":["I6132","I6142"]},
    {"id":"I6148","code":"I6148","name":"BIOFARMACIA Y FARMACOCINETICA","credits":8,"hours":4,"semester":6,"order":3,"area":"","prereqs":["I6131","I6142"]},
    {"id":"I6149","code":"I6149","name":"BIOLOGIA MOLECULAR Y GENETICA","credits":11,"hours":3,"semester":6,"order":4,"area":"","prereqs":["I6144"]},
    {"id":"I6150","code":"I6150","name":"TOXICOLOGIA GENERAL","credits":7,"hours":7,"semester":6,"order":5,"area":"","prereqs":["I6137","I6142","I6144"]},
    {"id":"I6151","code":"I6151","name":"LABORATORIO DE MICROBIOLOGIA CLINICA","credits":10,"hours":4,"semester":6,"order":6,"area":"","prereqs":["I6145"]},
    {"id":"I6164","code":"I6164","name":"SEMINARIO DE TUTORIA INTERMEDIA III","credits":2,"hours":2,"semester":6,"order":7,"area":"","prereqs":["I6163"]},

    # ===== Semestre VII =====
    {"id":"I6167","code":"I6167","name":"TECNOLOGIA FARMACEUTICA II","credits":7,"hours":10,"semester":7,"order":1,"area":"","prereqs":["I6166"]},
    {"id":"I6168","code":"I6168","name":"FARMACIA COMUNITARIA Y HOSPITALARIA","credits":4,"hours":4,"semester":7,"order":2,"area":"","prereqs":["I5874","I6142","I6139"]},
    {"id":"I6169","code":"I6169","name":"ANALISIS QUIMICO CLINICO","credits":9,"hours":7,"semester":7,"order":3,"area":"","prereqs":["I6132","I6144"]},
    {"id":"I6176","code":"I6176","name":"LABORATORIO DE BIOLOGIA MOLECULAR Y GENETICA","credits":3,"hours":3,"semester":7,"order":4,"area":"","prereqs":[]},
    {"id":"I6170","code":"I6170","name":"QUIMICA Y TOXICOLOGIA FORENSE","credits":7,"hours":4,"semester":7,"order":5,"area":"","prereqs":["I6132","I6150"]},
    {"id":"I6152","code":"I6152","name":"MICROBIOLOGIA APLICADA","credits":9,"hours":5,"semester":7,"order":6,"area":"","prereqs":["I6151"]},
    {"id":"I6165","code":"I6165","name":"SEMINARIO DE TUTORIA DE EGRESO","credits":2,"hours":0,"semester":7,"order":7,"area":"","prereqs":["I6164"]},
    {"id":"I6182","code":"I6182","name":"PROYECTO DE QUIMICA ANALITICA Y EVALUACION TOXICOLOGICA","credits":2,"hours":0,"semester":7,"order":8,"area":"","prereqs":[]},

    # ===== Semestre VIII =====
    {"id":"I6173","code":"I6173","name":"SERVICIOS FARMACEUTICOS HOSPITALARIOS","credits":5,"hours":5,"semester":8,"order":1,"area":"","prereqs":["I6168","I6148"]},
    {"id":"I6153","code":"I6153","name":"ANALISIS DE FARMACOS Y MEDICAMENTOS","credits":10,"hours":7,"semester":8,"order":2,"area":"","prereqs":["I6132","I6142"]},
    {"id":"I6174","code":"I6174","name":"LABORATORIO DE ANALISIS QUIMICO CLINICO","credits":7,"hours":10,"semester":8,"order":3,"area":"","prereqs":[]},
    {"id":"I6154","code":"I6154","name":"INMUNOLOGIA","credits":9,"hours":6,"semester":8,"order":4,"area":"","prereqs":["I6149"]},
    {"id":"I6175","code":"I6175","name":"TOXICOLOGIA APLICADA","credits":7,"hours":4,"semester":8,"order":5,"area":"","prereqs":["I6150"]},
    {"id":"I6171","code":"I6171","name":"ANALISIS MICROBIOLOGICOS","credits":5,"hours":5,"semester":8,"order":6,"area":"","prereqs":["I6151"]},
    {"id":"I6183","code":"I6183","name":"PROYECTO DE MICROBIOLOGIA","credits":2,"hours":0,"semester":8,"order":7,"area":"","prereqs":[]},
    {"id":"I6181","code":"I6181","name":"PROYECTO DE BIOQUIMICA CLINICA","credits":2,"hours":0,"semester":8,"order":8,"area":"","prereqs":[]},

    # ===== Semestre IX =====
    {"id":"I6158","code":"I6158","name":"GERENCIA Y ADMINISTRACION","credits":5,"hours":4,"semester":9,"order":1,"area":"","prereqs":[]},
    {"id":"I6172","code":"I6172","name":"VALIDACION DE PROCESOS Y METODOS ANALITICOS","credits":7,"hours":5,"semester":9,"order":2,"area":"","prereqs":["I6132","I6139"]},
    {"id":"I6155","code":"I6155","name":"ASEGURAMIENTO DE LA CALIDAD ANALITICA","credits":7,"hours":4,"semester":9,"order":3,"area":"","prereqs":["I6132","I6139"]},
    {"id":"I6133","code":"I6133","name":"ANALISIS BROMATOLOGICOS","credits":5,"hours":4,"semester":9,"order":4,"area":"","prereqs":["I6132","I6144"]},
    {"id":"I6177","code":"I6177","name":"DESARROLLO SUSTENTABLE","credits":2,"hours":5,"semester":9,"order":5,"area":"","prereqs":[]},
    {"id":"I6178","code":"I6178","name":"BIOTECNOLOGIA","credits":8,"hours":5,"semester":9,"order":6,"area":"","prereqs":["I6176","I6152"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA II","credits":4,"hours":4,"semester":9,"order":7,"area":"","prereqs":[]},
    {"id":"","code":"","name":"PROYECTO MODULAR DE FARMACIA","credits":2,"hours":0,"semester":9,"order":8,"area":"","prereqs":[]},

    # ===== Semestre X (nuevas de la tabla que no estaban) =====
    {"id":"V2455","code":"V2455","name":"ANALISIS DE PROBLEMAS GLOBALES DEL SIGLO XXI","credits":0,"hours":"","semester":10,"order":1,"area":"","prereqs":[]},

]

per_lqfb_courses = [
    # ===== Semestre I =====
    {"id":"I6121","code":"I6121","name":"CALCULO DIFERENCIAL INTEGRAL","credits":8,"hours":10,"semester":1,"order":1,"area":"","prereqs":[]},
    {"id":"I6156","code":"I6156","name":"BIOETICA Y DEONTOLOGIA","credits":5,"hours":4,"semester":1,"order":2,"area":"","prereqs":[]},
    {"id":"I6122","code":"I6122","name":"QUIMICA GENERAL I","credits":9,"hours":5,"semester":1,"order":3,"area":"","prereqs":[]},
    {"id":"I6123","code":"I6123","name":"INTRODUCCION A LA FISICA","credits":7,"hours":4,"semester":1,"order":4,"area":"","prereqs":[]},
    {"id":"I6134","code":"I6134","name":"BASES DE BIOLOGIA CELULAR","credits":9,"hours":5,"semester":1,"order":5,"area":"","prereqs":[]},
    {"id":"I6157","code":"I6157","name":"METODOLOGIA DE LA INVESTIGACION","credits":2,"hours":3,"semester":1,"order":6,"area":"","prereqs":[]},
    {"id":"I6159","code":"I6159","name":"SEMINARIO DE TUTORIA INICIAL I","credits":2,"hours":2,"semester":1,"order":7,"area":"","prereqs":[]},

    # ===== Semestre II =====
    {"id":"I6136","code":"I6136","name":"SALUD Y SOCIEDAD","credits":7,"hours":4,"semester":2,"order":1,"area":"","prereqs":["I6156"]},
    {"id":"I6124","code":"I6124","name":"QUIMICA ORGANICA I","credits":9,"hours":5,"semester":2,"order":2,"area":"","prereqs":["I6122"]},
    {"id":"I6125","code":"I6125","name":"BIOESTADISTICA","credits":7,"hours":4,"semester":2,"order":3,"area":"","prereqs":[]},
    {"id":"I6135","code":"I6135","name":"MORFOLOGIA","credits":8,"hours":5,"semester":2,"order":4,"area":"","prereqs":["I6134"]},
    {"id":"I6126","code":"I6126","name":"QUIMICA GENERAL II","credits":9,"hours":5,"semester":2,"order":5,"area":"","prereqs":["I6122"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA I","credits":7,"hours":3,"semester":2,"order":6,"area":"","prereqs":[]},
    {"id":"I6160","code":"I6160","name":"SEMINARIO DE TUTORIA INICIAL II","credits":2,"hours":2,"semester":2,"order":7,"area":"","prereqs":["I6159"]},

    # ===== Semestre III =====
    {"id":"I6128","code":"I6128","name":"FISICOQUIMICA I PARA FARMACEUTICOS","credits":7,"hours":4,"semester":3,"order":1,"area":"","prereqs":["I6121","I6126"]},
    {"id":"I6129","code":"I6129","name":"QUIMICA ORGANICA II","credits":9,"hours":5,"semester":3,"order":2,"area":"","prereqs":["I6124"]},
    {"id":"I6137","code":"I6137","name":"FISIOLOGIA Y FUNDAMENTOS DE FISIO-PATOLOGIA","credits":14,"hours":7,"semester":3,"order":3,"area":"","prereqs":["I6135"]},
    {"id":"I6127","code":"I6127","name":"QUIMICA ANALITICA I","credits":8,"hours":5,"semester":3,"order":4,"area":"","prereqs":["I6126"]},
    {"id":"I5874","code":"I5874","name":"DISEÑO DE EXPERIMENTOS","credits":7,"hours":3,"semester":3,"order":5,"area":"","prereqs":[]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA I","credits":7,"hours":3,"semester":3,"order":6,"area":"","prereqs":[]},
    {"id":"I6161","code":"I6161","name":"SEMINARIO DE TUTORIA INICIAL III","credits":2,"hours":2,"semester":3,"order":7,"area":"","prereqs":["I6160"]},

    # ===== Semestre IV =====
    {"id":"I6131","code":"I6131","name":"FISICOQUIMICA II PARA FARMACEUTICOS","credits":7,"hours":4,"semester":4,"order":1,"area":"","prereqs":["I6128"]},
    {"id":"I6138","code":"I6138","name":"FARMACOLOGIA I","credits":7,"hours":5,"semester":4,"order":2,"area":"","prereqs":["I6137","I6129","I6136"]},
    {"id":"I6140","code":"I6140","name":"BIOQUIMICA I","credits":7,"hours":5,"semester":4,"order":3,"area":"","prereqs":["I6129","I6137"]},
    {"id":"I6139","code":"I6139","name":"NORMATIVIDAD Y LEGISLACION SANITARIA","credits":5,"hours":2,"semester":4,"order":4,"area":"","prereqs":["I6136","I6156"]},
    {"id":"I6130","code":"I6130","name":"QUIMICA ANALITICA II","credits":8,"hours":5,"semester":4,"order":5,"area":"","prereqs":["I6127"]},
    {"id":"I6141","code":"I6141","name":"PARASITOLOGIA","credits":7,"hours":5,"semester":4,"order":6,"area":"","prereqs":[]},
    {"id":"I6162","code":"I6162","name":"SEMINARIO DE TUTORIA INTERMEDIA I","credits":2,"hours":2,"semester":4,"order":7,"area":"","prereqs":["I6161"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA II","credits":4,"hours":4,"semester":4,"order":8,"area":"","prereqs":[]},

    # ===== Semestre V =====
    {"id":"I6142","code":"I6142","name":"FARMACOLOGIA II","credits":8,"hours":4,"semester":5,"order":1,"area":"","prereqs":["I6138"]},
    {"id":"I6144","code":"I6144","name":"BIOQUIMICA II","credits":7,"hours":5,"semester":5,"order":2,"area":"","prereqs":["I6140"]},
    {"id":"I6132","code":"I6132","name":"QUIMICA ANALITICA III","credits":8,"hours":5,"semester":5,"order":3,"area":"","prereqs":["I6130"]},
    {"id":"I6143","code":"I6143","name":"SEMINARIO DE INVESTIGACION","credits":2,"hours":2,"semester":5,"order":4,"area":"","prereqs":["I6157"]},
    {"id":"I6146","code":"I6146","name":"LABORATORIO DE PARASITOLOGIA","credits":5,"hours":4,"semester":5,"order":5,"area":"","prereqs":[]},
    {"id":"I6145","code":"I6145","name":"MICROBIOLOGIA","credits":9,"hours":5,"semester":5,"order":6,"area":"","prereqs":[]},
    {"id":"I6163","code":"I6163","name":"SEMINARIO DE TUTORIA INTERMEDIA II","credits":2,"hours":2,"semester":5,"order":7,"area":"","prereqs":["I6162"]},

    # ===== Semestre VI =====
    {"id":"I6147","code":"I6147","name":"FARMACOGNOSIA","credits":4,"hours":4,"semester":6,"order":1,"area":"","prereqs":["I6130","I6142"]},
    {"id":"I6166","code":"I6166","name":"TECNOLOGIA FARMACEUTICA I","credits":10,"hours":10,"semester":6,"order":2,"area":"","prereqs":["I6132","I6142"]},
    {"id":"I6148","code":"I6148","name":"BIOFARMACIA Y FARMACOCINETICA","credits":8,"hours":4,"semester":6,"order":3,"area":"","prereqs":["I6131","I6142"]},
    {"id":"I6149","code":"I6149","name":"BIOLOGIA MOLECULAR Y GENETICA","credits":11,"hours":3,"semester":6,"order":4,"area":"","prereqs":["I6144"]},
    {"id":"I6150","code":"I6150","name":"TOXICOLOGIA GENERAL","credits":7,"hours":7,"semester":6,"order":5,"area":"","prereqs":["I6137","I6142","I6144"]},
    {"id":"I6151","code":"I6151","name":"LABORATORIO DE MICROBIOLOGIA CLINICA","credits":10,"hours":4,"semester":6,"order":6,"area":"","prereqs":["I6145"]},
    {"id":"I6164","code":"I6164","name":"SEMINARIO DE TUTORIA INTERMEDIA III","credits":2,"hours":2,"semester":6,"order":7,"area":"","prereqs":["I6163"]},

    # ===== Semestre VII =====
    {"id":"I6167","code":"I6167","name":"TECNOLOGIA FARMACEUTICA II","credits":7,"hours":10,"semester":7,"order":1,"area":"","prereqs":["I6166"]},
    {"id":"I6168","code":"I6168","name":"FARMACIA COMUNITARIA Y HOSPITALARIA","credits":4,"hours":4,"semester":7,"order":2,"area":"","prereqs":["I5874","I6142","I6139"]},
    {"id":"I6169","code":"I6169","name":"ANALISIS QUIMICO CLINICO","credits":9,"hours":7,"semester":7,"order":3,"area":"","prereqs":["I6132","I6144"]},
    {"id":"I6176","code":"I6176","name":"LABORATORIO DE BIOLOGIA MOLECULAR Y GENETICA","credits":3,"hours":3,"semester":7,"order":4,"area":"","prereqs":[]},
    {"id":"I6170","code":"I6170","name":"QUIMICA Y TOXICOLOGIA FORENSE","credits":7,"hours":4,"semester":7,"order":5,"area":"","prereqs":["I6132","I6150"]},
    {"id":"I6152","code":"I6152","name":"MICROBIOLOGIA APLICADA","credits":9,"hours":5,"semester":7,"order":6,"area":"","prereqs":["I6151"]},
    {"id":"I6165","code":"I6165","name":"SEMINARIO DE TUTORIA DE EGRESO","credits":2,"hours":0,"semester":7,"order":7,"area":"","prereqs":["I6164"]},
    {"id":"I6182","code":"I6182","name":"PROYECTO DE QUIMICA ANALITICA Y EVALUACION TOXICOLOGICA","credits":2,"hours":0,"semester":7,"order":8,"area":"","prereqs":[]},

    # ===== Semestre VIII =====
    {"id":"I6173","code":"I6173","name":"SERVICIOS FARMACEUTICOS HOSPITALARIOS","credits":5,"hours":5,"semester":8,"order":1,"area":"","prereqs":["I6168","I6148"]},
    {"id":"I6153","code":"I6153","name":"ANALISIS DE FARMACOS Y MEDICAMENTOS","credits":10,"hours":7,"semester":8,"order":2,"area":"","prereqs":["I6132","I6142"]},
    {"id":"I6174","code":"I6174","name":"LABORATORIO DE ANALISIS QUIMICO CLINICO","credits":7,"hours":10,"semester":8,"order":3,"area":"","prereqs":[]},
    {"id":"I6154","code":"I6154","name":"INMUNOLOGIA","credits":9,"hours":6,"semester":8,"order":4,"area":"","prereqs":["I6149"]},
    {"id":"I6175","code":"I6175","name":"TOXICOLOGIA APLICADA","credits":7,"hours":4,"semester":8,"order":5,"area":"","prereqs":["I6150"]},
    {"id":"I6171","code":"I6171","name":"ANALISIS MICROBIOLOGICOS","credits":5,"hours":5,"semester":8,"order":6,"area":"","prereqs":["I6151"]},
    {"id":"I6183","code":"I6183","name":"PROYECTO DE MICROBIOLOGIA","credits":2,"hours":0,"semester":8,"order":7,"area":"","prereqs":[]},
    {"id":"I6181","code":"I6181","name":"PROYECTO DE BIOQUIMICA CLINICA","credits":2,"hours":0,"semester":8,"order":8,"area":"","prereqs":[]},

    # ===== Semestre IX =====
    {"id":"I6158","code":"I6158","name":"GERENCIA Y ADMINISTRACION","credits":5,"hours":4,"semester":9,"order":1,"area":"","prereqs":[]},
    {"id":"I6172","code":"I6172","name":"VALIDACION DE PROCESOS Y METODOS ANALITICOS","credits":7,"hours":5,"semester":9,"order":2,"area":"","prereqs":["I6132","I6139"]},
    {"id":"I6155","code":"I6155","name":"ASEGURAMIENTO DE LA CALIDAD ANALITICA","credits":7,"hours":4,"semester":9,"order":3,"area":"","prereqs":["I6132","I6139"]},
    {"id":"I6133","code":"I6133","name":"ANALISIS BROMATOLOGICOS","credits":5,"hours":4,"semester":9,"order":4,"area":"","prereqs":["I6132","I6144"]},
    {"id":"I6177","code":"I6177","name":"DESARROLLO SUSTENTABLE","credits":2,"hours":5,"semester":9,"order":5,"area":"","prereqs":[]},
    {"id":"I6178","code":"I6178","name":"BIOTECNOLOGIA","credits":8,"hours":5,"semester":9,"order":6,"area":"","prereqs":["I6176","I6152"]},
    {"id":"","code":"","name":"OPTATIVA ABIERTA II","credits":4,"hours":4,"semester":9,"order":7,"area":"","prereqs":[]},
    {"id":"","code":"","name":"PROYECTO MODULAR DE FARMACIA","credits":2,"hours":0,"semester":9,"order":8,"area":"","prereqs":[]},

    # ===== Semestre X (nuevas de la tabla que no estaban) =====
    {"id":"V2455","code":"V2455","name":"ANALISIS DE PROBLEMAS GLOBALES DEL SIGLO XXI","credits":0,"hours":"","semester":10,"order":1,"area":"","prereqs":[]},

]

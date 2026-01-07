import re 



def minimum_value(equality):
    
    terme = []
    coefficient = []
    variable = []

    partie_droite = re.split(r'=', equality)[1].strip()
    partie_gauche = re.split(r'=', equality)[0].strip()
    details_partie_gauche = re.split(r'([+-]?\d*[a-zA-Z]+)', partie_gauche)

    for t in details_partie_gauche:
      if t != '':
        terme.append(t)

    for t in terme:
      match = re.match(r'([+-]?\d*)([a-zA-Z])', t)
      if match:
          nombre_str, var = match.groups()

          if nombre_str in ('' , '+'):
            nombre  = 1
          elif nombre_str == '-':
            nombre  = -1
          else:
            nombre = int(nombre_str)

          coefficient.append(nombre)
          variable.append(var)
            

    
    resultat = int(partie_droite)
    
    somme_lambda_carres = 0
    for l in coefficient:
        somme_lambda_carres += l**2
        

    minimum = resultat**2 / somme_lambda_carres
    
    return minimum
    
    
    pass
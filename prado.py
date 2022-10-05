###2.1.1
##Operacoes Basicas - Posicao
#Construtor

def cria_posicao(x, y):
    if type(x) != int or type (y) != int or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return (x, y)

def cria_copia_posicao(pos):
    return (pos[0], pos[1])

#Seletores
def obter_pos_x(pos):
    return pos[0]

def obter_pos_y(pos):
    return pos[1]

#Reconhecedor
def eh_posicao(arg):
    if type(arg) != tuple or len(arg) != 2 or type(arg[0]) != int or type(arg[1]) != int or arg[0] < 0 or arg[1] < 0:
        return False
    return True

#Teste
def posicoes_iguais(pos1, pos2):
    if pos1[0] == pos2[0] and pos2[1] == pos2[1]:
        return True
    return False

#Transformador
def posicao_para_str(pos):
    return f'({pos[0]}, {pos[1]})'

##Operacoes de Alto-Nivel - Posicao
#Adjacentes
def obter_posicoes_adjacentes(pos):
    res = []
    if obter_pos_y(pos) - 1 >= 0:
        res.append(cria_posicao(obter_pos_x(pos), obter_pos_y(pos) - 1))
    if obter_pos_x(pos) + 1 >= 0:
        res.append(cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos)))
    if obter_pos_y(pos) + 1 >= 0:
        res.append(cria_posicao(obter_pos_x(pos), obter_pos_y(pos) + 1))
    if obter_pos_x(pos) - 1 >= 0:
        res.append(cria_posicao(obter_pos_x(pos) - 1, obter_pos_y(pos)))
    return tuple(res)

#Ordenar
def ordenar_posicoes(posicoes):
    posicoes = list(posicoes)
    #sort x
    index = 0
    swap = True
    while swap:
        swap = False
        while index < len(posicoes) - 1:
            if obter_pos_x(posicoes[index + 1]) < obter_pos_x(posicoes[index]):
                posicoes[index + 1], posicoes[index] = posicoes[index], posicoes[index + 1]
                swap = True
            index += 1
    #Sort y
    swap = True
    index = 0
    while swap:
        swap = False
        while index < len(posicoes) - 1:
            if obter_pos_y(posicoes[index + 1]) < obter_pos_y(posicoes[index]):
                posicoes[index + 1], posicoes[index] = posicoes[index], posicoes[index + 1]
                swap = True
            index += 1
    return tuple(posicoes)

###2.1.2
##Operacoes Basicas - Animal
#Construtor
def cria_animal(especie, reproducao, alimentacao):
    if type(especie) != str or len(especie) == 0:
        raise ValueError('cria_animal: argumentos invalidos')
    elif type(reproducao) != int or reproducao <= 0:
        raise ValueError('cria_animal: argumentos invalidos')
    elif type(alimentacao) != int or alimentacao < 0:
        raise ValueError('cria_animal: argumentos invalidos')
    return {'especie': especie, 'reproducao': reproducao, 'alimentacao': alimentacao, 'idade': 0, 'fome': 0}

def cria_copia_animal(animal):
    return animal.copy()

#Seletores
def obter_especie(animal):
    return animal['especie']

def obter_freq_reproducao(animal):
    return animal['reproducao']

def obter_freq_alimentacao(animal):
    return animal['alimentacao']

def obter_idade(animal):
    return animal['idade']

def obter_fome(animal):
    return animal['fome']

#Modificadores
def aumenta_idade(animal):
    animal['idade'] += 1
    return animal

def reset_idade(animal):
    animal['idade'] = 0
    return animal

def aumenta_fome(animal):
    if animal['alimentacao'] != 0:
        animal['fome'] += 1
    return animal

def reset_fome(animal):
    if animal['alimentacao'] != 0:
        animal['fome'] = 0
    return animal

#Reconhecedor
def eh_animal(arg):
    if type(arg) != dict or len(arg) != 5:
        return False
    for atributo in ('especie', 'reproducao', 'alimentacao', 'idade', 'fome'):
        if atributo not in arg.keys():
            return False
    if type(arg['especie']) != str or len(arg['especie']) == 0:
        return False
    elif type(arg['reproducao']) != int or arg['reproducao'] <= 0:
        return False
    elif type(arg['alimentacao']) != int or arg['alimentacao'] < 0:
        return False
    elif type(arg['idade']) != int or arg['idade'] < 0:
        return False
    elif type(arg['fome']) != int or arg['fome'] < 0:
        return False
    return True

def eh_predador(arg):
    return eh_animal(arg) and arg['alimentacao'] != 0

def eh_presa(arg):
    return eh_animal(arg) and arg['alimentacao'] == 0

#Teste
def animais_iguais(animal1, animal2):
    if not eh_animal(animal1) or not eh_animal(animal2):
        return False
    return animal1 == animal2

#Transformadores
def animal_para_char(animal):
    if animal['alimentacao'] != 0:
        return animal['especie'][0].upper()
    else:
        return animal['especie'][0].lower() 

def animal_para_str(animal):
    if animal['alimentacao'] != 0:
        return f"{animal['especie']} [{animal['idade']}/{animal['reproducao']};{animal['fome']}/{animal['alimentacao']}]"
    else:
        return f"{animal['especie']} [{animal['idade']}/{animal['reproducao']}]"

##Operacoes de Alto-Nivel - Animal
#Fertil
def eh_animal_fertil(animal):
    return obter_freq_reproducao(animal) == obter_idade(animal)

#Faminto
def eh_animal_faminto(animal):
    return obter_freq_alimentacao(animal) >= obter_fome(animal)

#Reproduz
def reproduz_animal(animal):
     reset_idade(animal)
     return cria_animal(obter_especie(animal),obter_freq_reproducao(animal), obter_freq_alimentacao(animal))


###2.1.3
##Operacoes Basicas - Prado
#Construtor
def cria_prado(pos, rochedos, animais, animais_pos):
    #Validacao
    if not eh_posicao(pos) or type(rochedos) != tuple or \
    type(animais) != tuple or len(animais) == 0 or \
    type(animais_pos) != tuple or len(animais_pos) != len(animais):
        raise ValueError('cria_prado: argumentos invalidos')
    for pos_rochedo in rochedos:
        if obter_pos_x(pos_rochedo) >= obter_pos_x(pos) or obter_pos_y(pos_rochedo) >= obter_pos_y(pos):
            raise ValueError('cria_prado: argumentos invalidos')    
    for pos_animal in animais_pos:
        if obter_pos_x(pos_animal) >= obter_pos_x(pos) or obter_pos_y(pos_animal) >= obter_pos_y(pos):
            raise ValueError('cria_prado: argumentos invalidos')   
    for pos_rochedo in rochedos:
        for pos_animal in animais_pos:
            if obter_pos_x(pos_animal) == obter_pos_x(pos_rochedo) and obter_pos_y(pos_animal) == obter_pos_y(pos_rochedo):
                raise ValueError('cria_prado: argumentos invalidos') 
    #Construir
    prado = {}
    prado['info'] = {'dim': pos, 'rochedos': rochedos}
    for x in range(obter_pos_x(pos)+1):
        for y in range(obter_pos_y(pos)+1):
            if x == 0 or y == 0 or x == obter_pos_x(pos) or y == obter_pos_y(pos):
                prado[cria_posicao(x, y)] = 'montanha'
            else:
                prado[cria_posicao(x, y)] = None
    index = 0
    for animal in animais:
        prado[animais_pos[index]] = animal
        index += 1
    for rochedo in rochedos:
        prado[rochedo] = 'rochedo'

    return prado

def cria_copia_prado(prado):
    return prado.copy()

#Seletores
def obter_tamanho_x(prado):
    return obter_pos_x(prado['info']['dim']) + 1

def obter_tamanho_y(prado):
    return obter_pos_y(prado['info']['dim']) + 1

def obter_numero_predadores(prado):
    count = 0
    for pos in prado.keys():
        if eh_predador(prado[pos]):
            count += 1
    return count

def obter_numero_presas(prado):
    count = 0
    for pos in prado.keys():
        if eh_presa(prado[pos]):
            count += 1
    return count

def obter_posicao_animais(prado):
    animais = ()
    for pos in prado.keys():
        if eh_animal(prado[pos]):
            animais += (pos,)
    return ordenar_posicoes(animais)

def obter_animal(prado, pos):
    if eh_animal(prado[pos]):
        return prado[pos]

#Modificadores
def eliminar_animal(prado, pos):
    if eh_animal(prado[pos]):
        prado[pos] = None
    return prado

def mover_animal(prado, pos_in, pos_fn):
    if eh_animal(prado[pos_in]):
        prado[pos_fn], prado[pos_in] = prado[pos_in], None
    return prado

def inserir_animal(prado, animal, pos):
    prado[pos] = animal
    return prado

#Reconhecedores
def eh_prado(arg): #Um pouco incompleto!!!!!
    if type(arg) != dict or 'info' not in arg.keys() or 'dim' not in arg['info'].keys():
        return False 
    if len(arg) != ((obter_pos_x(arg['info']['dim']) + 1) * (obter_pos_y(arg['info']['dim']) + 1) + 1):
        return False
    return True

def eh_posicao_animal(prado, pos):
    return eh_animal(prado[pos])

def eh_posicao_obstaculo(prado, pos):
    return prado[pos] == 'rochedo' or prado[pos] == 'montanha'

def eh_posicao_livre(prado, pos):
    return prado[pos] == None

#Teste
def prados_iguais(prado1, prado2):
    return eh_prado(prado1) and eh_prado(prado2) and prado1 == prado2

#Transformador
def prado_para_str(prado):
    res = ''
    for y in range(obter_tamanho_y(prado)):
        line = ''
        for x in range(obter_tamanho_x(prado)):
            pos = cria_posicao(x, y)
            if (obter_pos_x(pos) == 0 and obter_pos_y(pos) == 0) or \
            (obter_pos_x(pos) == 0 and obter_pos_y(pos) == obter_tamanho_y(prado) - 1) or \
            (obter_pos_y(pos) == 0 and obter_pos_x(pos) == obter_tamanho_x(prado) - 1) or \
            (obter_pos_x(pos) == obter_tamanho_x(prado) - 1) and (obter_pos_y(pos) == obter_tamanho_y(prado) - 1):
                line += '+'
            elif obter_pos_x(pos) == 0 or obter_pos_x(pos) == obter_tamanho_x(prado) - 1:
                line += '|'
            elif obter_pos_y(pos) == 0 or obter_pos_y(pos) == obter_tamanho_y(prado) - 1:
                line += '-'
            elif eh_animal(prado[pos]):
                line += animal_para_char(prado[pos])
            elif prado[pos] == 'rochedo':
                line += '@' 
            else:
                line += '.'
        res += line + '\n'
    return res.strip()

##Operacoes Alto-Nivel - Prado
#Valor Numerico
def obter_valor_numerico(prado, pos):
    return obter_pos_x(pos) + obter_tamanho_x(prado) * obter_pos_y(pos)

#Movimento
def obter_movimento(prado, pos):
    animal = obter_animal(prado, pos)
    #Disponiveis
    disponiveis = ()
    for adjacente in obter_posicoes_adjacentes(pos):
        if eh_predador(animal) and (eh_posicao_livre(prado, adjacente) or eh_presa(obter_animal(prado, adjacente))):
            disponiveis += (adjacente,)
        elif eh_presa(animal) and eh_posicao_livre(prado, adjacente):
            disponiveis += (adjacente,)
    #Caso nenhuma posicao esteja disponivel
    if len(disponiveis) == 0:
        return pos
    #Candidatos
    candidatos = ()
    if eh_predador(animal):
        for posicao in disponiveis:
            if eh_presa(obter_animal(prado, posicao)):
                candidatos += (posicao,)
    if eh_presa(animal) or len(candidatos) == 0:
        candidatos = disponiveis
    #Sort Candidatos (12:00 Logica)
    sorted_candidatos = ()
    relogio = (cria_posicao(obter_pos_x(pos), obter_pos_y(pos)-1), \
    cria_posicao(obter_pos_x(pos)+1, obter_pos_y(pos)), \
    cria_posicao(obter_pos_x(pos), obter_pos_y(pos)+1), \
    cria_posicao(obter_pos_x(pos)-1, obter_pos_y(pos)))
    for posicao in relogio:
        if posicao in candidatos:
            sorted_candidatos += (posicao,)
    #Selecionar
    p = len(sorted_candidatos)
    N = obter_valor_numerico(prado, pos)
    selecionada = N % p
    return sorted_candidatos[selecionada]

###2.2.1
##Funcoes Adicionais
#Geracao
def geracao(prado):
    for pos_calculo in obter_posicao_animais(prado):
        animal = obter_animal(prado, pos_calculo)
        #Tempo
        if eh_predador(animal):
            animal = aumenta_fome(animal)
        animal = aumenta_idade(animal)
        #Movimento
        move = False
        pos_final = obter_movimento(prado, pos_calculo)
        prado = mover_animal(prado, pos_calculo, pos_final)
        if not animais_iguais(animal, obter_animal(prado, pos_calculo)):
            move = True  
        #Reproducao
        if obter_freq_reproducao(animal) == obter_idade(animal) and move:
            inserir_animal(prado, reproduz_animal(animal), pos_calculo)
        #Alimentacao e Morte
        if obter_fome(animal) == obter_freq_alimentacao(animal) and eh_predador(animal):
            eliminar_animal(prado, pos_final)
    return prado

#Simulacao
def simula_ecossistema(file, geracoes, verboso):
    #Criar input para geracao
    animais_data = []
    with open(file, 'r') as file:
        for pos, line in enumerate(file):
            if pos == 0:
                dim = eval(line.strip())
            elif pos == 1:
                rochedos = eval(line.strip())
            elif pos > 1:
                animais_data.append(line.strip())
        #Cria Dimensao
        dim = cria_posicao(dim[0], dim[1])
        #Cria Rochedos
        for rochedo in rochedos:
            rochedo = cria_posicao(rochedo[0], rochedo[1])
        #Cria Animais e Animais_Pos
        animais_pos = ()
        animais = ()
        for animal in animais_data:
            animal = eval(animal)
            animais_pos += (cria_posicao(animal[3][0], animal[3][1]),)
            animais += (cria_animal(animal[0], animal[1], animal[2]),)
    prado = cria_prado(dim, rochedos, animais, animais_pos)
    #Geracoes
    presas_temp = 0
    predadores_temp = 0
    for gen in range(geracoes+1):
        if obter_numero_presas(prado) != presas_temp or obter_numero_predadores(prado) != predadores_temp:
            if (not verboso and (gen == 0 or gen == geracoes)) or verboso:
                print(f'Predadores: {obter_numero_predadores(prado)} vs Presas: {obter_numero_presas(prado)} (Gen. {gen})')
                print(prado_para_str(prado))
            presas_temp = obter_numero_presas(prado)
            predadores_temp = obter_numero_predadores(prado)
        geracao(prado)
    return (obter_numero_predadores(prado), obter_numero_presas(prado))

#...
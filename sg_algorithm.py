## funcion a valorar:  f(x)=2sen(x)+cos(2x)
import random
import math
from matplotlib import pyplot as plt
from numpy import binary_repr

## variables utilizadas
Init_Population = [[0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1]]
General_population = 5 # mete la cantidad de datos iniciales que quieras y con esto tambien una parte se va a para la cruza y mutacion 
Population_size = 20
DNA_size = 6 #tamaño del genoma
N_Generations = 100 #generaciones que se establecen 
P_Mutation = 0.10 # probabilidad de que un individuo mute
P_Mutation_gen = 0.07 #probabilidad de que el genoma de un individuo mute
A = 80
B = 68
Dx = abs((B-A)/(pow(2,DNA_size)))
minx = 6
maxx = 6.9

abscisas = []
phenotype = []
all_fitnnes = []
best_Fitnnes = []
worst_Fitnnes = []
Sons = []
Mutation_P_I_C = []
mutation_Posible_gen = []
aux_abscisas = []
sumfitnnes = 0
Media = 0
media_Fitnnes = []
## Fin variables utilizadas

def definir_DA(Init_Population1):    ## esta funcion crea genes aleatorios para la cantidad_indi_ini de individuos que se espera tambien la cantidad_indi_ini de los puntos a y b ademas de la secuencia Dx
    val_X = 0
    contar = 0
    individuo = []        
    Init_Population2 = [[] for i in range(General_population)]
    for datas in range(len(Init_Population1)):            
        dato = random.randint(minx, maxx)
        otro = (bin(dato)[2:].zfill(DNA_size))        
        for item in otro:            
            Init_Population1[datas].append(int(item))            
    print(Init_Population1)    
    for item in range(DNA_size):
        val_X += pow(2,item)        
    val_X += 1
    print(val_X)    
    #A_a = random.randint(1, 100)
    #B_a = random.randint(1, 100)
    Dx_a = abs((B-A)/(val_X))    
    return Init_Population1, Dx_a

def def_Genotype():
    #print(it[0][5])
    print("Poblacion inicial \n " + str(Init_Population))
    for item in range(len(Init_Population)):## para hacer todo aleatorio con la funcion de arriba utilizar la variable it en todas las palabras que tengan Init_Population
        n = DNA_size - 1
        dna_aux = 0
        datos = 0
        for data in range(len(Init_Population[item])):
            if n != -1:
                if Init_Population[item][n] == 1:
                    datos += pow(2,dna_aux)
                dna_aux += 1
            n -= 1
        abscisas.append(datos)
    print("Genotype : " + str(abscisas))
    def_Phenotype(abscisas)

def def_Phenotype(geno):
    for item in range(len(geno)):
        phenotype.append(A + (geno[item] * Dx))
    print("Phenotype: " + str(phenotype))
    Fitness(phenotype, geno)

def Fitness(pheno, geno):
    sumfitnnes = 0
    for item in range(len(geno)):
        all_fitnnes.append((2*math.sin(phenotype[item])+ (math.cos(2*phenotype[item]))))        
        sumfitnnes += all_fitnnes[item] 
    Media = sumfitnnes / len(Init_Population)
    print("Fitnnnes: " + str(all_fitnnes))
    best_Fitnnes.append(sorted(all_fitnnes)[len(geno) - 1])
    worst_Fitnnes.append(sorted(all_fitnnes)[0])
    media_Fitnnes.append(Media)
    print("All sum fitnnes: " + str(sumfitnnes))
    print("Media: " + str(Media))
    print("Best Fitness: "+ str(sorted(all_fitnnes)[len(geno) - 1]))
    print("Worst Fitness: " + str(sorted(all_fitnnes)[0]))
    abscisas.clear()
    phenotype.clear()
    all_fitnnes.clear()

def Mutation(sons):
    #print("-------------------------------------- Mutacion: "  + " --------------------------------------")
    Mutation_P_I_C.clear()
    for item in range(len(sons)):        
        Mutation_P_I_C.append(random.random())
    #print("              Cruzas en genral: " + str(sons))
    #print("Mutacion por individuo cruzado: "+str(Mutation_P_I_C))
    for item in range(len(Mutation_P_I_C)):
        if Mutation_P_I_C[item] <= P_Mutation:
            mutation_Posible_gen.clear()
            #print("Individuo que puede mutar: "+ str(sons[item]) + " posicion del individuo: " + str(item) + " Probabilidad de mutacion: " + str(Mutation_P_I_C[item]))
            for data in range(len(sons[item])):
                mutation_Posible_gen.append(random.random())
            #print(mutation_Posible_gen)
            for pos in range(len(mutation_Posible_gen)):
                if mutation_Posible_gen[pos] <= P_Mutation_gen:
                    if sons[item][pos] == 1:
                        sons[item][pos] = 0
                    else:
                        sons[item][pos] = 1
                #print("El gen que va a mutar es: " + str(sons[item][pos]) + " la posicion del gen es: "+  str(pos) + " El valor de la mutacion es de: " + str(mutation_Posible_gen[pos]))            
    for item in range(len(sons)):## para hacer todo aleatorio con la funcion de arriba utilizar la variable it en todas las palabras que tengan Init_Population
        n = DNA_size - 1
        dna_aux = 0
        datos = 0
        for data in range(len(sons[item])):
            if n != -1:
                if sons[item][n] == 1:
                    datos += pow(2,dna_aux)
                dna_aux += 1
            n -= 1
        aux_abscisas.append(datos)
                    
    itemsMay = []
    ns = 0
    for item in aux_abscisas:
        if item < minx or item > maxx:
            itemsMay.append(sons[ns])
        ns += 1
    #print(sons)
    #print("mayores o menores al rango → " + str(itemsMay) + " \n cantidad → " + str(len(itemsMay)))
    #print('tamaño sons → ' + str(len(sons)))
    aux_abscisas.clear()
    if len(itemsMay) == len(sons):        
        crossover()        
    else:
        if len(itemsMay) != 0:
            for item in range(len(itemsMay)):                
                sons.remove(itemsMay[item])
                pass
            
    return sons

def crossover():
    Sons.clear()
    #print("-------------------------------------- Cruza: "  + " --------------------------------------")
    print("Cantidad de individuos: " + str(len(Init_Population)))
    for item in range(len(Init_Population)):
        pattern1 = random.randint(1, len(Init_Population)) - 1
        pattern2 = random.randint(1, len(Init_Population)) - 1
        if pattern1 != pattern2:
            crossover_point = random.randint(1, 4)
            Pattern1 = Init_Population[pattern1]
            Pattern2 = Init_Population[pattern2]
            #print("padre1: " + str(pattern1) + " padre2: " + str(pattern2) + " punto de cruza: " + str(crossover_point))
            if crossover_point != 0 and crossover_point != 5:
                Son1 = Pattern1[0:crossover_point] + Pattern2[crossover_point: len(Pattern2)]
                Son2 = Pattern2[0:crossover_point] + Pattern1[crossover_point : len(Pattern1)]
            else:
                Son1 = Pattern2
                Son2 = Pattern1
            #print("El padre 1: " + str(Pattern1) + " El padre 2: " + str(Pattern2))
            Sons.append(Son1)
            Sons.append(Son2)
            #print("El hijo  1: " + str(Son1) + " El hijo 2 : " + str(Son2))    
    sons_cross_mutt = Mutation(Sons)
    return sons_cross_mutt

def Selection(cross_mut, subG):
    print("         -------------------------------------- sub_Generacion: " + str(subG - .5) + " --------------------------------------")
    #print("         Datos cruzados mutados: "  + str(cross_mut) + "\n cantidad de datos: " + str(len(cross_mut)))
    #print("                 Datos iniciales: " + str(Init_Population) + "\n cantidad de datos: " + str(len(Init_Population)))
    for item in range(len(cross_mut)):
            Init_Population.append(cross_mut[item])
    #print("         Population: \n" + str(Init_Population) + " \n Size_Population: " + 
    print(" poblacion Inicial + poblacion cruzada_mutada --> " + str(len(Init_Population)))    
    for item in range(len(Init_Population)):## para hacer todo aleatorio con la funcion de arriba utilizar la variable it en todas las palabras que tengan Init_Population
        n = DNA_size - 1
        dna_aux = 0
        datos = 0
        for data in range(len(Init_Population[item])):
            if n != -1:
                if Init_Population[item][n] == 1:
                    datos += pow(2,dna_aux)
                dna_aux += 1
            n -= 1
        aux_abscisas.append(datos)
    #print("Datos de x: " + str(aux_abscisas))
    phenotype_aux = []
    for item in range(len(aux_abscisas)):
        phenotype_aux.append(A + (aux_abscisas[item] * Dx))
    #print(phenotype_aux)
    all_fitnnes_aux = []    
    for item in range(len(aux_abscisas)):
        all_fitnnes_aux.append((2*math.sin(phenotype_aux[item])+ (math.cos(2*phenotype_aux[item]))))       
    print(all_fitnnes_aux)
    order = sorted(all_fitnnes_aux)
    size = len(Init_Population) - Population_size
    #print("cantidad: " + str(size) + " datos: " + str(order))
    otro = order[0:size]
    #print(otro)
    ayuda = []
    another_one = ''
    ayuda = []
    n = len(aux_abscisas)
    for item in range(len(otro)):
        for items in range(len(all_fitnnes_aux)):
            if otro[item] == all_fitnnes_aux[items]:
                ayuda.append(items)
    #print(ayuda)
    if int(len(ayuda) % 2 ) != 0:
        #print("se metio uno " + str(ayuda[len(ayuda) - 1]) + " posicion: " +str(len(ayuda) - 1))
        ayuda.pop(len(ayuda) - 1)
    another_one = set(ayuda)
    last_one = []
    #print(another_one)
    s = 0
    for data in another_one:
        last_one.append(Init_Population[data])                    
    
    #print(Init_Population)
    #print("---------------------- " + str(last_one) + " ----------------------")    
    for data in range(len(last_one)):        
        #print("Dato a remover: " + str(last_one[data]) + " Posicion de dato: " + str(data))
        if len(Init_Population) >= Population_size + 1:
            Init_Population.remove(last_one[data - 1])            
        #print(Init_Population)
    #print(Init_Population)
    last_one.clear()
    aux_abscisas.clear()
    ayuda.clear()
    phenotype_aux.clear()
    all_fitnnes_aux.clear()
    otro.clear()

def Graphyc():
    plt.title("Fitness")
    plt.legend()
    plt.plot(best_Fitnnes, 'o-', label = " Mejores casos")
    plt.plot(worst_Fitnnes, 'o-', label = " Peores casos")
    plt.plot(media_Fitnnes, 'o-', label = "Caso promedio")        
    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.rcParams['toolbar'] = 'None'
    plt.legend()
    plt.show()

if __name__ == '__main__':
    Init_Population1 = [[] for i in range(General_population)]
    (population, dx ) = definir_DA(Init_Population1)
    Init_Population.clear()
    # A = a utiliza estas variables para hacer los puntos randoms 
    # B = b 
    Dx = dx
    Init_Population.extend(population)    
    print("posicion de A -> " + str(A) + " Posicion de B -> " + str(B) + " Datos Dx -> " + str(Dx))
    print("Poblacion inicial: "+ str(len(Init_Population)))
    print(Init_Population)
    for item in range(N_Generations):
        print("-------------------------------------- Generacion: " + str(item) + " --------------------------------------")
        (cross_mut) = crossover()            
        Selection(cross_mut, item)
        def_Genotype()
    print("-------------------------------------- Datos Fitness: "  + " --------------------------------------")
    print("             -------------------------------------- Mejores Fitness: --------------------------------------\n"+ str(best_Fitnnes))
    print("             -------------------------------------- Peores Fitness: --------------------------------------\n"+ str(worst_Fitnnes))
    print("             -------------------------------------- Media Fitness: --------------------------------------\n"+ str(media_Fitnnes))
    Graphyc()
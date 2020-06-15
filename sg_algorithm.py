## funcion a valorar:  f(x)=2sen(x)+cos(2x)
import random
import math
from matplotlib import pyplot as plt
from numpy import binary_repr
import numpy as np
import os

## variables utilizadas
Init_Population = [[0, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1]]
General_population = 8 # mete la cantidad de datos iniciales que quieras y con esto tambien una parte se va a para la cruza y mutacion 
Population_size = 20
DNA_size = 6 #tamaño del genoma
N_Generations = 50 #generaciones que se establecen 
P_Mutation = 0.10 # probabilidad de que un individuo mute
P_Mutation_gen = 0.07 #probabilidad de que el genoma de un individuo mute
A = 7
B = 8
Dx = 0
best_Fitnnes = []
worst_Fitnnes = []
aux_abscisas = []
sumfitnnes = 0
Media = 0
media_Fitnnes = []
the_best = 0
## Fin variables utilizadas

def definir_DA(Init_Population1):    ## esta funcion crea genes aleatorios para la cantidad_indi_ini de individuos que se espera tambien la cantidad_indi_ini de los puntos a y b ademas de la secuencia Dx
    val_X = 0
    contar = 0
    individuo = []            
    Init_Population2 = [[] for i in range(General_population)]
    
    for item in range(DNA_size):
        val_X += pow(2,item)        
    val_X += 1    
    Dx_a = abs((B-A)/(val_X))    

    for datas in range(len(Init_Population1)):            
        dato = random.uniform(A, B)
        Init_Population1[datas].append(round(dato,DNA_size))
    
    return Init_Population1, Dx_a, val_X

def def_Genotype():
    genotype = []
    genotipe_dec = []
    for item in Init_Population:        
        genotype.append(int(item[0]))
        genotipe_dec.append(round(item[0] - int(item[0]),DNA_size))
    print("Genotype → ", genotype, " : ",genotipe_dec)
    return genotype , genotipe_dec

def def_Phenotype():
    phenotype = []        
    for item in range(len(Init_Population)):    
        #print( A + (Init_Population[item][0] * Dx))
        phen = (A + (int(Init_Population[item][0]) * Dx)) + (Init_Population[item][0] - int(Init_Population[item][0]))
        phenotype.append(round(phen,DNA_size))        
    #print("Phenotype: ", phenotype, " : ", phenotype_dec, " : ", pru)
    print("Phenotype →  ", phenotype)
    return phenotype#, phenotype_dec, pru

def Fitness(pheno, opcion):
    
    all_fitnnes = []
    sumfitnnes = 0
    
    for item in range(len(pheno)):                    
        fit = (2*math.sin (pheno[item]) + ((math.cos(2*pheno[item]))* (math.cos(2*pheno[item])) ) ) 
        all_fitnnes.append(round(fit, DNA_size))
        if opcion == 1:
            sumfitnnes += all_fitnnes[item]
    print("Fitnnnes → ", all_fitnnes)
    if opcion == 1:                        
        Media = round(sumfitnnes / len(Init_Population), DNA_size)
        best_Fitnnes.append(sorted(all_fitnnes)[len(pheno) - 1])
        worst_Fitnnes.append(sorted(all_fitnnes)[0])
        media_Fitnnes.append(Media)
        print("All sum fitnnes: ",sumfitnnes)
        print("Media: " + str(Media))
        print("Best Fitness: ",sorted(all_fitnnes)[len(pheno) - 1])        
        print("Worst Fitness: " ,sorted(all_fitnnes)[0])
    else:
        return all_fitnnes

def Mutation(sons, Ints):
    Mutation_P_I_C = []
    mutation_Posible_gen = []
    sons_cross_mutt = [[] for i in range(len(Ints))]
    #print("-------------------------------------- Mutacion: "  + " --------------------------------------")
    #print("Cantidad de individuos cruzados → " ,len(sons))
    for item in range(len(sons)):        
        Mutation_P_I_C.append(random.random())    
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
                        sons[item][pos] = random.randint(0,9)
                        #print("Valor nuevo del gen: " ,sons[item][pos], " la posicion del gen es: "+  str(pos) + " El valor de la mutacion es de: " + str(mutation_Posible_gen[pos]))
            mutacionInt = random.random()
            #print("mutacion Int → ", mutacionInt)
            if mutacionInt <= P_Mutation_gen:
                #print("mutacion Int → ", mutacionInt, " Dato previo → ", Ints[item])
                Ints[item] = random.randint(int(A),int(B))
    #print(Ints)
    for item in range(len(Ints)):
        sons_str = ''
        for data in sons[item]:
            sons_str = sons_str + str(data)
        
        sons_cross_mutt[item].append(float(str(str(Ints[item]) + "." + sons_str)))
    return sons_cross_mutt

def crossover():
    Sons = []
    Ints = []
    #print("-------------------------------------- Cruza:  --------------------------------------")
    print("Cantidad de individuos → ", len(Init_Population))
    for item in range(len(Init_Population)*random.randint(6,7)):
        pattern1 = random.randint(1, len(Init_Population)) - 1
        pattern2 = random.randint(1, len(Init_Population)) - 1        
        if pattern1 != pattern2:
            float_helper = [[] for i in range(2)]
            n = 0        
            crossover_point = random.randint(1, DNA_size - 2)
            #print("Padre 1 → ", pattern1,":", Init_Population[pattern1], " Padre 2 → ", pattern2,":", Init_Population[pattern2], " punto de cruza → ", crossover_point)
            for data in Init_Population[pattern1], Init_Population[pattern2]:
                dot_come = False
                Ints.append(int(data[0]))
                for items in str(data[0]):
                    if dot_come == False:
                        if items == ".":                            
                            dot_come = True
                    else:
                        float_helper[n].append(items)
                n += 1
                
            Son1 = float_helper[0][0 : crossover_point] + float_helper[1][crossover_point : len(float_helper[1])]
            Son2 = float_helper[1][0 : crossover_point] + float_helper[0][crossover_point : len(float_helper[0])]
            #print("El hijo 1 → ", Son1, " El hijo 2 → ",  Son2)
            Sons.append(Son1)
            Sons.append(Son2)
            #print(float_helper)
    #print("padres int → ", Ints)
    #print("hijos float → ", Sons)
    sons_cross_mutt = Mutation(Sons, Ints)
    return sons_cross_mutt

def Selection(cross_mut, subG):
    print("         -------------------------------------- sub_Generacion: " + str(subG + .5) + " --------------------------------------")
    print("Datos cruzados mutados: "  + str(cross_mut) + "\n cantidad de datos: " + str(len(cross_mut)))    
    for item in range(len(cross_mut)):
            Init_Population.append(cross_mut[item])
    print("\nPopulation → ",Init_Population)
    print("poblacion Inicial + poblacion cruzada_mutada → ",len(Init_Population))
    if len(Init_Population) >6:        
        (pheno) = def_Phenotype()
        (fit) = Fitness(pheno, 2)
        size = len(Init_Population) - Population_size         
        print("datos →",fit ," ← fin")
        dats  = []
        other = []        
        if fit[0] < 0:
            n = 0
            for item in range(len(pheno)):                
                if n != Population_size and fit[item] < the_best :
                    print(the_best, " : ", fit[item])
                    dats.append(fit[item])
                    n += 1           
                else:
                    other.append(fit[item])
        else:
            n = 0
            for item in range(len(pheno)):                
                if n != Population_size and fit[item] > the_best :
                    print(the_best, " : ", fit[item])
                    dats.append(fit[item])
                    n += 1
                else:
                    other.append(fit[item])
        helper = []        
        print("Datos a eliminar → ", other, " Cantidad de datos → ", size)
        print("datos a conservar → ", dats, " ← fin")
        for item in range(len(other)):
            for items in range(len(fit)):
                if other[item] == fit[items]:
                    helper.append(items)
        #print(len(helper))
        #print(set(helper))
        last_one = []
        for data in set(helper):
            last_one.append(Init_Population[data])            
        #print(last_one)
        for data in range(len(last_one)):                    
            if len(Init_Population) >= Population_size + 1:
                #print("Se va a sacar → ", last_one[data], " Posicion del dato → ", data)
                Init_Population.remove(last_one[data])
        print("         ---------------------------------------------------------------------------")
        print(Init_Population)

def Graphyc():
    plt.title("Fitness")
    plt.legend()
    plt.plot(best_Fitnnes, 'o-', label = " Peores casos")
    plt.plot(worst_Fitnnes, 'o-', label = " Mejores casos")
    plt.plot(media_Fitnnes, 'o-', label = "Caso promedio")            
    plt.xlabel("Generations" )
    plt.ylabel("Fitness \n Punto Dato → " + str(A) )
    plt.rcParams['toolbar'] = 'None'
    plt.legend()
    plt.show()

if __name__ == '__main__':
    os.system("clear")
    Init_Population1 = [[] for i in range(General_population)]
    (population, dx, val ) = definir_DA(Init_Population1)
    Init_Population.clear()        
    Dx = dx
    Init_Population.extend(population)    
    print("posicion de A → ",A, " Posicion de B → ", B, " Datos Dx → ",Dx, " : " , val)
    print("Poblacion inicial: "+ str(len(Init_Population)))
    print(Init_Population)
    for item in range(N_Generations):
        print("-------------------------------------- Generacion: ", item + 1, " --------------------------------------")
        print("Individuos en la lista → ", Init_Population)
        (cross_mut) = crossover()
        Selection(cross_mut, item)
        #(geno, geno_dec) = def_Genotype()
        (pheno) = def_Phenotype()
        Fitness(pheno, 1)
        the_best = best_Fitnnes[item]
    print("-------------------------------------- Datos Fitness: "  + " --------------------------------------")
    print("             -------------------------------------- Mejores Fitness: --------------------------------------\n"+ str(best_Fitnnes))
    print("             -------------------------------------- Peores Fitness: --------------------------------------\n"+ str(worst_Fitnnes))
    print("             -------------------------------------- Media Fitness: --------------------------------------\n"+ str(media_Fitnnes))
    Graphyc()
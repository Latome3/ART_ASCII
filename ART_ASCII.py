# Converti Les images contenus dans le dossier 'IMG_ART_ASCII' en oeuvre d'art ASCII
# Installer au préalable le module opencv en executant la commande "pip install cv2"
import cv2
import os

contenaire="@#A%€&ç+ù=¤*:-_ "     #"@#A%€&ç+ù=¤*:-_ "

os.chdir("IMG_ART_ASCII")
image_list=[e for e in os.listdir() if e.endswith(".jpg") or e.endswith(".png") or e.endswith(".gif")]
os.chdir("..")

choix=-5 # 5 est choisit au hasard

while choix!=-2:
    print("\n\n================ MENU ================= ")
    print("Entrer :")
    print("Le numero de l'image à transformer ou ")
    print("-1 Pour afficher la liste des images disponibles et leurs numero")
    print("-2 pour quitter")
    try :
        choix=int(input("Votre choix:  "))
        if choix>=0 :
            if choix <len(image_list):
                save=10 # 10 est choisit au hasard
                while save!=1 and save!=0:
                    try:
                        save=int(input("\nEntrer :\n 1 Si vous voulez enregistrer le résultat\n 0 Sinon\nChoix:   "))
                        if save!=1 and save!=0:
                            print("\nVeuillez choisir entre 1 et 0")
                    except ValueError:
                        print("\nVeuillez choisir entre 1 et 0")
                if save==1:
                    print("Le résultat sera enrégistré dans le fichier ART_ASCII.txt\n\n")
                    with open("ART_ASCII.txt", "a") as fic:
                        line="\n\n\n===================================IMAGE: " + image_list[choix] + "=============================\n\n"
                        fic.write(line)
                image_path="IMG_ART_ASCII/"+image_list[choix]
                image=cv2.imread(image_path, 0)
                image=cv2.resize(image, (90, 40))
                #print(image)
                C1=0
                C2=0
                C3=0
                while C1<len(image):
                    ligne=""
                    while C2<len(image[C1]):
                            moyenne=int((image[C1][C2]/255)*(len(contenaire)-1))
                            ligne=ligne+contenaire[moyenne]
                            C2=C2+1
                    print(ligne)
                    if save==1:
                        with open("ART_ASCII.txt", "a") as fic:
                            fic.write(ligne)
                            fic.write("\n|")
                    C2=0
                    C1=C1+1
            else:
                print("\n--------------------------")
                print("Numero d'image introuvable !")
                print("--------------------------\n")
        elif choix==-1:
            numero=0
            for element in image_list:
                print(numero, ": ", element)
                numero=numero+1
        elif choix== -2:
            pass
        elif choix <-2:
            print("\n--------------------------")
            print("Numero d'image introuvable !")
            print("--------------------------\n")
    except ValueError:
        print("Veuillez Entrer un nombre entier")

    

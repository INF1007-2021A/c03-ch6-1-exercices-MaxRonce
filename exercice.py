#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

def order(values: list = None) -> list:
    liste_to_order =  []
    if values is None:
        for i in range(10):
            liste_to_order.append(input("Entrez une valeur : "))
        # TODO: demander les valeurs ici

    return sorted(liste_to_order)
     


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = [input("Mot 1 : "), input("Mot 2 : ")]
        pass
    return sorted(words[0]) == sorted(words[1]) 
    


def contains_doubles(items: list) -> bool:

    if len(items) != len(set(items)):
        return True
    else : 
        return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    averages = {}
    for key in student_grades.keys():
        averages[key] = sum(student_grades[key])/len(student_grades[key])

    for key in averages.items():
        if key[1] == max(averages.values()):
            answer = {key[0]: key[1]}
    return answer


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    answer = {}
    answer2 = {}
    for i in sentence : 
        answer[i] = sentence.count(i)

    for k in answer.keys():
        if answer[k] > 5 : 
            answer2[k] = answer[k]
    #       Retourner le tableau de lettres


    print(answer2)
    return answer


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recipe_book = {}
    name = str(input("Entrez le nom d'une recette : "))
    ingredients = str(input("Entrez les ingrédients : "))
    recipe_book[name] = ingredients
    return recipe_book


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    recette = str(input("Entrez le nom d'une recette a afficher : "))
    if recette in ingredients.keys():
        print(ingredients[recette])


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    student_grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(student_grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()

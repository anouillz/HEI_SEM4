from unidecode import unidecode

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def ajouter_lettre(mot: str) -> set[str]:
    return {
        mot[:i] + lettre + mot[i:]
        for i in range(len(mot) + 1)
        for lettre in ALPHABET
    }

def supprimer_lettre(mot: str) -> set[str]:
    return {
        mot[:i] + mot[i+1:]
        for i in range(len(mot))
    }

def substituer_lettre(mot: str) -> set[str]:
    return {
        mot[:i] + lettre + mot[i+1:]
        for i in range(len(mot))
        for lettre in ALPHABET
        if lettre != mot[i]
    }

def transposer_lettres(mot: str) -> set[str]:
    return {
        mot[:i] + mot[i+1] + mot[i] + mot[i+2:]
        for i in range(len(mot) - 1)
    }

def edits1(mot: str) -> set[str]:
    return (
        ajouter_lettre(mot)
        | supprimer_lettre(mot)
        | substituer_lettre(mot)
        | transposer_lettres(mot)
    )



def load_dictionary(filename: str) -> tuple[dict[str, int], dict[str, str]]:

    dictionnaire = {}
    index_sans_accents = {}

    with open(filename, encoding='utf-8') as f:
        next(f)  # saute l'en-tête
        for ligne in f:
            mot, freq = ligne.strip().split('\t')
            freq = int(freq)
            dictionnaire[mot] = freq

            mot_sans_accent = unidecode(mot)
            # garder le mot le plus fréquent pour chaque version sans accent
            if (mot_sans_accent not in index_sans_accents or
                freq > dictionnaire.get(index_sans_accents[mot_sans_accent], 0)):
                index_sans_accents[mot_sans_accent] = mot

    return dictionnaire, index_sans_accents



def correct_spelling(mot: str, dictionnaire: dict[str, int], index_sans_accents: dict[str, str]) -> str:
    candidats = edits1(mot)
    candidats_valides = {c for c in candidats if c in dictionnaire}

    if candidats_valides:
        return max(candidats_valides, key=lambda x: dictionnaire[x])

    # corriger sans accent
    mot_sans_acc = unidecode(mot)
    if mot_sans_acc in index_sans_accents:
        return index_sans_accents[mot_sans_acc]

    return mot


dico, dico_ac = load_dictionary("word_frequencies_200000.tsv")
print(correct_spelling("chaussetes", dico, dico_ac))     # attendu : "chaussettes"
print(correct_spelling("chausssettes", dico, dico_ac))   # attendu : "chaussettes"
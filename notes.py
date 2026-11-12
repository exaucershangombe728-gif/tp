def moyenne(notes):
    if not notes:
        raise ValueError("La liste de notes est vide")
    return round(sum(notes) / len(notes), 2)
def mention(note):
    if note >= 16:
        return "Très bien"
    if note >= 14:
        return "Bien"
    if note >= 12:
        return "Assez bien"
    if note >= 10:
        return "Passable"
        return "Ajourné"
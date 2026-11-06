def creer_contact(nom:str, telephone:str) -> dict:
    return {'nom' : nom,'telephone':telephone,'operateur' : 'INCONNU'}

def afficher_contact(contact: dict[str, str]) -> None:
    print(f"{contact['nom']} : {contact['telephone']} : {contact['operateur']}")

def valider_telephone(telephone : str) -> bool:
    pass

if __name__ == '__main__':
    # '77   100 10 10'=> '771001010'  
    # '77 de1001010' => 'pas bon'
    # '' => 'pas bon'
    # '7710015415' => 'pas bon'
    pass
    
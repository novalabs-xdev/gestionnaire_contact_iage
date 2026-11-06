from contacts import creer_contact

nom = input("Entrez le nom du contact : ")
telephone = input("Entrez le telephone du contact :")
contact = creer_contact(nom, telephone)
print(contact)
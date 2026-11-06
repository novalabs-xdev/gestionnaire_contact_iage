from contacts import creer_contact, get_valide_telephone

nom = input("Entrez le nom du contact : ")
telephone = get_valide_telephone()
contact = creer_contact(nom, telephone)
print(contact)
import string
alphabet = string.ascii_lowercase


# renvoi le decalage correspondant à une lettre de la clé
def find_decal_cle(letter):
    for n in range(len(alphabet)):
        if letter == alphabet[n]:
            return n


# renvoi un tableau qui contient le décalage associé à chaque lettre de la clé
def chiffrement_clef(cle):
    chiffrement_mdp = []
    for i in range(len(cle)):
        decal = find_decal_cle(cle[i])
        chiffrement_mdp.append(decal)
    return chiffrement_mdp


# renvoi le mot de passe chiffré
def chiffrement_vigenere(mdp, cle):
    mdp_code = ""
    decal = chiffrement_clef(cle)
    for i in range(len(mdp)):
        for n in range(len(alphabet)):
            # conserve les caractères qui ne sont pas des lettres dans le mdp
            if mdp[i] not in alphabet and n == 25:
                mdp_code += mdp[i]
            # chiffre la lettre du mdp
            elif mdp[i] == alphabet[n]:
                mdp_code += alphabet[(n + decal[i % len(decal)]) % len(alphabet)]
    return mdp_code


print(chiffrement_vigenere("hellotheworld", "hetic"))

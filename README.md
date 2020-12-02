# python-bitcoinlib-stuff
### transactionCharge.py
Ši programa suskaičiuoja pasirinktos transakcijos mokestį.
Veikimo principas:
- Perskaito įvestą transakcijos hash'ą
- Iš jos ištraukia transakciją
- Nuskaito transakcijoje turimas išeitines sumas
- Ištraukia įvestyje esančias transakcijas
- Jų išvestis prodedą prie įeitinių sumų
- Sumas atima ir išveda gautą mokestį

### hashCheck.py
Ši programa patikrina ar įvesto bloko hash'as yra teisingas
Veikimo principas:
- Perskaito įvestą bloko numerį (eilę bitcoin mazge)
- Perskaito header'io informaciją tokia tvarka: nonce (konvertuotas į hex), bits, time (konvertuotas į hex), merkleroot, previousblockhash, versionHex.
- Header'io informaciją konvertuoją į little indian formatą.
- Jį dekoduoja į binarinį formatą
- Per 2 perėjimus hash'uoja sha256 metodu
- Vėl konvertuoja į little indian formatą.
- Išveda gautą ir turėtą bloko hash'us bei juos palygina.

### Paleidimo instrukcija:
- Prisijungti prie bitcoin mazgo
- Su Python 2 pasileisti failą `python [pavadinimas].py` arba `py -2 [pavadinimas].py`.

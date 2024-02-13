sozluk = {"Bilim insanı": "Aziz Sancar", "Şair": "Mehmet Akif Ersoy", "Astronom": "Ali Kuşçu"}
meslekler = sozluk.copy()
print("Meslekler sözlüğü:", meslekler)


print("Sözlük değerleri:", list(sozluk.values()))


sozluk.clear()
print("Sözlük içeriği (içi boş):", sozluk)

sozluk["Matematikçi"] = "Cahit Arf"
print("Sözlük güncellendi:", sozluk)


if "Sanatçı" in sozluk:
    print("Sanatçı anahtarı mevcut.")
else:
    print("Sanatçı anahtarı mevcut değil.")


sozluk["Bilim insanı"] = "Canan Dağdeviren"
print("Sözlük güncellendi:", sozluk)


if "Şair" in sozluk:
    print("Şair:", sozluk["Şair"])
else:
    print("Şair anahtarı mevcut değil.")

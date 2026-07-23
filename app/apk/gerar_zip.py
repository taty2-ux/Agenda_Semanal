import zipfile

def pasta_zip():
    with zipfile.ZipFile("AppAgenda.zip", "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.write("app/apk/arquivo_apk.exe")
        z.write("app/apk/horarios.csv")
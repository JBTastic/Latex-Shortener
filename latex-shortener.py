import fitz  # PyMuPDF
import os
import re  # Für reguläre Ausdrücke

def extract_last_pages(input_pdf, output_pdf):
    # Öffnen der Original-PDF
    document = fitz.open(input_pdf)
    
    # Dictionary, um die letzte Instanz jeder Seitenzahl zu speichern
    page_numbers = {}

    # Neues Dokument für die Ausgabe erstellen
    new_document = fitz.open()

    # Durch alle Seiten iterieren
    for page_num in range(document.page_count):
        page = document.load_page(page_num)  # Seite laden
        
        # Den Text der Seite extrahieren
        page_text = page.get_text("text")
        
        # Prüfen, ob ein Slash ("/") im Text ist
        if "/" in page_text:
            matches = re.findall(r"(\d+)\s*/\s*(\d+)", page_text)  # Suche nach Mustern wie "X / Y"
            if matches:
                # Nimm das letzte gefundene Paar
                last_match = matches[-1]
                try:
                    page_num_text, total_pages = map(int, last_match)
                    page_numbers[page_num_text] = page_num
                except ValueError:
                    pass  # Falls das Match keine gültige Zahl ist, überspringen
        else:
            # Falls kein Slash vorhanden ist, füge die Seite direkt hinzu
            new_document.insert_pdf(document, from_page=page_num, to_page=page_num)

    # Seiten mit gültigen Seitenzahlen hinzufügen (nur letzte Instanz jeder Seitenzahl)
    for page_num in sorted(set(page_numbers.values())):
        page = document.load_page(page_num)
        new_document.insert_pdf(document, from_page=page_num, to_page=page_num)

    # Die neue PDF speichern
    new_document.save(output_pdf)
    print(f"Neue PDF mit den gewünschten Seiten wurde gespeichert als '{output_pdf}'")

# Den Benutzer nach dem Dateinamen fragen
input_pdf_name = str(input("Name of the input PDF: "))

# Den Pfad zur Eingabedatei im "PDFs"-Ordner erstellen
input_pdf = os.path.join("PDFs", input_pdf_name)

# Den Pfad zur Ausgabedatei im "PDFs"-Ordner erstellen (mit "no_duplicates_" Präfix)
output_pdf_name = f"no_duplicates_{input_pdf_name}"
output_pdf = os.path.join("PDFs", output_pdf_name)

# Die Funktion aufrufen, um die PDF zu verarbeiten
extract_last_pages(input_pdf, output_pdf)

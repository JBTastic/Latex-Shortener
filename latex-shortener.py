import fitz  # PyMuPDF

def extract_last_pages(input_pdf, output_pdf):
    # Öffnen der Original-PDF
    document = fitz.open(input_pdf)
    
    # Dictionary, um die letzte Instanz jeder Seitenzahl zu speichern
    page_numbers = {}

    # Durch alle Seiten iterieren
    for page_num in range(document.page_count):
        page = document.load_page(page_num)  # Seite laden
        
        # Den Text der Seite extrahieren
        page_text = page.get_text("text")
        
        # Suchen nach der Seitenzahl im Format "X/Y"
        lines = page_text.split('\n')
        for line in lines:
            if '/' in line:  # Sucht nach der Form X/Y
                try:
                    page_num_text, total_pages = map(int, line.split('/'))
                    page_numbers[page_num_text] = page_num
                except ValueError:
                    pass  # Falls die Zeile keine gültige Seitenzahl enthält, überspringen

    # Neues Dokument für die Ausgabe erstellen
    new_document = fitz.open()

    # Seiten in der Reihenfolge der letzten Instanzen hinzufügen
    for page_num in sorted(page_numbers.values()):
        page = document.load_page(page_num)
        new_document.insert_pdf(document, from_page=page_num, to_page=page_num)

    # Die neue PDF speichern
    new_document.save(output_pdf)
    print(f"Neue PDF mit den gewünschten Seiten wurde gespeichert als '{output_pdf}'")

# Beispiel: Extrahiere die letzten Instanzen jeder Seitenzahl und speichere sie in einer neuen PDF
input_pdf = str(input("Name of the input PDF: "))
output_pdf = f"no_duplicates_{input_pdf}"
extract_last_pages(input_pdf, output_pdf)

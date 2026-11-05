# matrix_rain_pdf.py

# Importación de librerías para generación de PDF y aleatoriedad -> Importing libraries for PDF generation and randomness
import fitz  # PyMuPDF
import random

# 1. Crear un documento PDF vacío en memoria y agregar una página -> Create empty PDF document in memory and add a page
pdf_document = fitz.open()
page = pdf_document.new_page(width=600, height=650)

# Dibujar fondo negro en toda la página -> Draw black background on the entire page
page.draw_rect(page.rect, color=(0, 0, 0), fill=(0, 0, 0))

# 2. Generar caracteres aleatorios simulando la lluvia de Matrix -> Generate random characters simulating Matrix rain
for _ in range(180):
    pos_x: int = random.randint(20, 580)
    pos_y: int = random.randint(50, 580)
    char: str = random.choice("01ABCXYZ")
    
    # Color en formato RGB normalizado (0.0 a 1.0) con variaciones de verde -> Normalized RGB color format (0.0 to 1.0) with green variations
    green_shade: tuple[float, float, float] = (0.1, random.uniform(0.5, 1.0), 0.2)
    
    page.insert_text((pos_x, pos_y), char, fontsize=16, color=green_shade)

# 3. Dibujar el título principal en la parte superior -> Draw main title at the top
page.insert_text((155, 40), "THE MATRIX", fontsize=28, color=(0.0, 0.8, 0.2))

# 4. Guardar el archivo PDF generado -> Save generated PDF file
output_filename: str = "matrix.pdf"
pdf_document.save(output_filename)

print(f"¡PDF generado con éxito! Archivo guardado como '{output_filename}' -> PDF created successfully! File saved as '{output_filename}'")

from translate import Translator
from docx import Document
from odf.opendocument import OpenDocumentText
from odf.text import P, Span
from odf.style import Style, TextProperties
import re
from tqdm import tqdm

def translate_document(input_txt_path, output_odt_path):
    # Configuración del traductor
    translator = Translator(from_lang="pl", to_lang="es")

    # Crear documento ODT
    doc = OpenDocumentText()

    # Estilo para la traducción (color verde)
    green_style = Style(name="GreenText", family="text")
    green_style.addElement(TextProperties(attributes={"color": "#008000"}))
    doc.styles.addElement(green_style)

    # Leer el archivo de entrada
    with open(input_txt_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Dividir el texto en frases basadas en los puntos
    sentences = re.split(r'(\.|\!|\?)', content)

    # Crear una barra de progreso
    total_sentences = len(sentences) // 2
    with tqdm(total=total_sentences, desc="Traduciendo", unit="frase") as pbar:
        # Procesar cada frase
        for i in range(0, len(sentences) - 1, 2):
            original_sentence = sentences[i].strip()
            punctuation = sentences[i + 1]
            full_sentence = original_sentence + punctuation

            if original_sentence:
                # Crear un párrafo para la frase original
                p_original = P(text=full_sentence)
                doc.text.addElement(p_original)

                # Traducir la frase
                translated_sentence = translator.translate(original_sentence)
                translation_with_format = f"({translated_sentence})"

                # Crear un párrafo para la traducción en verde
                p_translation = P()
                span_translation = Span(text=translation_with_format, stylename=green_style)
                p_translation.addElement(span_translation)
                doc.text.addElement(p_translation)

            # Actualizar la barra de progreso
            pbar.update(1)

    # Guardar el documento ODT
    doc.save(output_odt_path)

# Ruta de entrada y salida
input_txt_path = "el_brujo.txt"  # Cambiar por la ruta del archivo de entrada
output_odt_path = "el_brujo_traducido.odt"  # Cambiar por la ruta del archivo de salida

# Llamar a la función
translate_document(input_txt_path, output_odt_path)

print("Traducción completada. El archivo ODT ha sido generado.")
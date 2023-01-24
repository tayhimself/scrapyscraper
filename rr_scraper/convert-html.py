from htmldocx import HtmlToDocx
import os

# get all html files in a directory
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
new_parser = HtmlToDocx()

# create a docx file for each html file
for html_file in html_files:
    docx_file = html_file.replace('.html', '.docx')
    print(f'converting {html_file} to {docx_file}')
    new_parser.parse_html_file(html_file, docx_file)
    print(f'Created {docx_file}')

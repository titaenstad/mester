import bs4
import sys
import os

input_file = sys.argv[1]
filename = os.path.basename(input_file)

def proc_hocr(xml_file):
    lines=[]
    with open(xml_file, 'r') as data:
        txt = data.read()
        soup = bs4.BeautifulSoup(txt,'lxml')
        paras = soup.findAll("p", {"class": "ocr_par"})
        for para in paras:
            ocr_lines = para.findAll('span', {"class": "ocr_line"})
            for ocr_line in ocr_lines:
                line = ocr_line.text.replace("\n"," ").strip()
                lines.append(line)
            lines.append('')
    return lines

lines = '\n'.join(proc_hocr(input_file))
print(lines)

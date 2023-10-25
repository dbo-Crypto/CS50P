import re
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=1, align="C")
        # Performing a line break:
        self.ln(20)


def get_name():
    name = input("Name: ")
    if match_name := re.search("^\w*$", name):
        return name

def build(name):

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 30)
    pdf.cell(85, 20, "CS50 Shirtificate", center=True)
    pdf.ln(20)
    pdf.image("shirtificate.png", x=15, y=60, w=180, keep_aspect_ratio=True)
    pdf.ln(80)
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(center=True, new_y="NEXT", txt=f"{name} took CS50")
    pdf.output("shirtificate.pdf")


def main():
    name = get_name()
    build(name)

if __name__ == "__main__":
    main()
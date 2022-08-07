

from fpdf import FPDF

x = input("Name: ")

def add_image(image_path):
    pdf = FPDF(orientation="Portrait", format="A4")


    pdf.add_page()

    pdf.set_font("helvetica", size=40)
    pdf.text(x=60, y=40, txt="CS50 Shirtificate")

    pdf.image(image_path, x=0, y=60)
    pdf.set_font("helvetica", size=30)
    pdf.set_text_color(r=255, g=255, b=255)

    pdf.cell(200, 220, txt=x+" took cs50".format(image_path),  align="C")


    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    add_image('shirtificate.png')

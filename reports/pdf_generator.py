from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime


def gerar_pdf_movimentacoes(movimentacoes):
    nome_arquivo = "reports/relatorio_movimentacoes.pdf"

    pdf = canvas.Canvas(nome_arquivo, pagesize=A4)

    largura, altura = A4

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(170, altura - 50, "SAFECONTROL NR35")

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(150, altura - 80, "Relatório de Movimentações")

    pdf.setFont("Helvetica", 10)
    pdf.drawString(40, altura - 110, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    y = altura - 150

    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawString(40, y, "Data")
    pdf.drawString(100, y, "Hora")
    pdf.drawString(160, y, "Colaborador")
    pdf.drawString(300, y, "Equipamento")
    pdf.drawString(450, y, "Tipo")
    pdf.drawString(520, y, "Qtd")

    y -= 20
    pdf.setFont("Helvetica", 9)

    for mov in movimentacoes:
        data, hora, colaborador, equipamento, tipo, quantidade = mov

        pdf.drawString(40, y, str(data))
        pdf.drawString(100, y, str(hora))
        pdf.drawString(160, y, str(colaborador)[:20])
        pdf.drawString(300, y, str(equipamento)[:22])
        pdf.drawString(450, y, str(tipo))
        pdf.drawString(520, y, str(quantidade))

        y -= 18

        if y < 50:
            pdf.showPage()
            y = altura - 50
            pdf.setFont("Helvetica", 9)

    pdf.save()

    return nome_arquivo
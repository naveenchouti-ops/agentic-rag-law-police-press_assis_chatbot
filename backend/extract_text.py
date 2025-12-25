import pdfplumber
from pathlib import Path

# Input folders
DATA_DIR = Path("data")
TEXT_DIR = Path("text")

TEXT_DIR.mkdir(exist_ok=True)

PDF_FILES = {
    "law_ipc.txt": DATA_DIR / "law" / "ipc.pdf",
    "law_crpc.txt": DATA_DIR / "law" / "crpc.pdf",
    "press_pci.txt": DATA_DIR / "press" / "pci_ethics.pdf",
    "press_pib.txt": DATA_DIR / "press" / "pib_releases.pdf",
    "police_scenarios.txt": DATA_DIR / "police" / "delhi_police_scenarios_bns_bnss_bsa.pdf",
}

def extract_pdf_text(pdf_path: Path) -> str:
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                text.append(f"\n--- Page {page_num} ---\n")
                text.append(page_text)
    return "\n".join(text)

for output_file, pdf_path in PDF_FILES.items():
    print(f"Extracting: {pdf_path}")
    extracted_text = extract_pdf_text(pdf_path)

    output_path = TEXT_DIR / output_file
    output_path.write_text(extracted_text, encoding="utf-8")

    print(f"Saved → {output_path}")

print("\n✅ All PDFs converted to text successfully.")

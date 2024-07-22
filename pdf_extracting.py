import PyPDF2 as p


try:
    # Open the PDF file in read-binary mode
    with open("C:/Users/SHANU/Downloads/sample.pdf.pdf", "rb") as file:
        # Create a PDF reader object
        pd = p.PdfReader(file)

        # Get the first page of the PDF
        x = pd.pages[0]

        # Extract and print the text from the first page
        print(x.extract_text())

except FileNotFoundError:
    print("The specified file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

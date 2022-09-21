import urllib.request
import pandas as pd
import PyPDF2
from tqdm import tqdm

# Superfund Data: https://epa.maps.arcgis.com/apps/webappviewer/index.html?id=33cebcdfdd1b4c3a8b51d416956c41f1&query=Superfund_National_Priorities_List__NPL__Sites_with_Status_Information_7557,SITE_EPA_ID=%27MSD004006995%27
superfund_data = pd.read_csv("superfund_data.csv")
superfund_data["URL"] = superfund_data["Site Listing Narrative"].str.split("\"").str[1]
print(len(superfund_data))

# Grab the PDF reports for each Superfund site, convert that to text, and store both for future work.
for site_name, download_url in tqdm(zip(superfund_data["Site Name"], superfund_data["URL"])):
    try:
        print(site_name)

        # Get the PDF from the URL within the Super Fund Data
        response = urllib.request.urlopen(download_url)
        file = open(f"./npl_narrative_pdfs/{site_name.replace('/', '-')}_{download_url.split('/')[-1]}" + ".pdf", 'wb')
        file.write(response.read())
        file.close()

        # Grab the PDF from local memory in read mode
        pdfFileObj = open(f"./npl_narrative_pdfs/{site_name.replace('/', '-')}_{download_url.split('/')[-1]}" + ".pdf", 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # Grab text from the PDF and output it to a new .txt file within /npl_narrative_texts
        pdf_text = open(f"./npl_narrative_texts/{site_name.replace('/', '-')}_{download_url.split('/')[-1]}" + ".txt", 'w')
        for page_number in range(pdfReader.numPages):
            # creating a page object
            pageObj = pdfReader.getPage(page_number)

            pdf_text.write(pageObj.extractText())
            pdf_text.write("\n")

        pdf_text.close()
        pdfFileObj.close()

    except:
        print("Didn't work for", site_name)

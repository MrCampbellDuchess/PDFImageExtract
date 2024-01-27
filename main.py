import PyPDF2
import os

def imagesFromPDF():
    # request path to file
    path = input('Enter the path to the PDF file: ')

    # Open the PDF file
    pdf_file = open(path, 'rb')

    #get the PDF file name and remove the extension
    pdf_title = os.path.splitext(os.path.basename(path))[0]

    # Create a PDF reader object
    reader = PyPDF2.PdfReader(pdf_file)

    #create a folder for the output files
    if not os.path.exists(pdf_title):
        os.makedirs(pdf_title)
                
    #switch to the output folder
    os.chdir(pdf_title)
                

    # Loop through each page of the PDF
    for page_num in range(len(reader.pages)):
        
        # Get the page object
        page = reader.pages[page_num]
        
        # Get the resources dictionary
        resources = page['/Resources']
        
        # Get the XObject dictionary
        xobject = resources['/XObject'].get_object()
        
        # Loop through each key in the XObject dictionary
        for key in xobject:
            
            # Get the object
            obj = xobject[key].get_object()
            
            # Check if the object is an image
            if obj['/Subtype'] == '/Image':
                
                # Create a filename for the image
                filename = f'LondonKids_{page_num+1}.png'

                # Write the image to a file
                with open(filename, 'wb') as f:
                    f.write(obj.get_data())
                
    # Close the PDF file
    pdf_file.close()
    print(f"Done! View the images in the '{pdf_title}' folder.")

if __name__ == '__main__':
    imagesFromPDF()
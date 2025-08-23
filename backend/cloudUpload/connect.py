import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("CLOUD_API_KEY"),
    api_secret=os.getenv("CLOUD_SECRET_KEY"),
    secure=True
)

print("Cloud Name:", os.getenv("CLOUD_NAME"))
print("API Key:", os.getenv("CLOUD_API_KEY"))
print("API Secret:", os.getenv("CLOUD_SECRET_KEY"))
print("Cloudinary is configured successfully!")


fileName="fastAPI.pdf"
pdf_path = Path(__file__).parent/ f"../temp/{fileName}"

def uploadFile(filePath, folder, tag):
    print("File uploading is started")
    try:
        uploadResult=cloudinary.uploader.upload(
            str(filePath),
            folder=f"myApp/{folder}",
            resource_type="auto",
            tags=["userUpload",f"{tag}"]
        )
        print("Upload successful!")
        print(uploadResult)
        print(uploadResult.get("secure_url"))
        return 
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None
    
uploadFile(pdf_path, "pdf","pdf")
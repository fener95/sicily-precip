import gdown

# The file ID extracted from your link
file_id = '138cTjnglvnwtySmJy_XTkeKH_WEBqK1M'
# The Google Drive URL to download the file
url = f'https://drive.google.com/uc?id={file_id}'
# The name you want to save the file as
output = 'sicilyPrecip_ee_conversion.ipynb'

# Download the file
gdown.download(url, output, quiet=False)

print(f"Downloaded {output}")

from dataclasses import dataclass
import requests
import zipfile



@dataclass
class Collect:
    url: str
    path: str
    save_directory: str


    def download_files(self,chunk_size=128):
        r = requests.get(self.url, stream=True)
        with open(self.path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)


    def unzip_files(self):
        with zipfile.ZipFile(self.path, 'r') as zip_ref:
            zip_ref.extractall(self.save_directory)


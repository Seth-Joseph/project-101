import os
import dropbox

class Transfer_data():
    def __init__(self,access_token):
        self.access_token = access_token
         
    def upload_file(self,file_from,file_to):
     
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = "XuglmEAyX-4AAAAAAAAAAaJd7Qj5xV9oE-u3fHe-DsBDNN2lVH88HDPCCheHEFGr"
    transferData = TransferData(access_token)

    file_from = input("Enter file name: ")
    file_to = input("Enter the path of file to be uploaded: ") 
    transferData.upload_file(file_from, file_to)
    print("Succesfully moved files to Dropbox")
main()

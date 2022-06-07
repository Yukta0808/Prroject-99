import shutil
import time
import os

def main():
    deleted_folders = 0
    deleted_files = 0 
    path = input('Enter the path to delete: ')
    days = 30
    seconds = time.time() - (days*24*60*60)

    if (os.path.exists(path)):
        for root, folder, files in os.walk(path):
            if (seconds >= getFileFolderAge(root)):
                remove_folder(root)
                deleted_folders +=1
                break
            else:
                 for f in folder:
                     folderpath = os.path.join(root,f)
                     if seconds >= getFileFolderAge(folderpath):
                         remove_folder(folderpath)
                         deleted_folders += 1 
                 for f in files:
                     filepath = os.path.join(root,f)
                     if seconds>= getFileFolderAge(filepath):
                         remove_file(filepath)
                         deleted_files += 1
        else:
                if seconds >= getFileFolderAge(path):
                    remove_file(path)
                    deleted_files += 1 
    else:
        print("Path not found!")            
        deleted_files += 1 
    print("Total folders deleted {}".format(deleted_folders))
    print("Total files deleted {}".format(deleted_files))

def remove_file(path):
    if not os.remove(path):
        print("File removed successfully!")

    else:
       print("Unable to remove file!")

def remove_folder(path):
     if not shutil.rmtree(path):
      print("Removed successfully!")
    
     else:
      print("Unable to remove!")
      
    
def getFileFolderAge(path):
    ctime = os.stat(path).st_ctime 
    return ctime

if __name__ == '__main__':
    main()

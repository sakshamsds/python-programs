import os
import shutil

for folderName, subfolders, filenames in os.walk('c:\\'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + 'are: ' + str(filenames)) 
    
    # Removing fish subfolders
    for subfolder in subfolders:
        if 'fish' in subfolder:
            #os.rmtree(subfolder)
            #os.rmdir(subfolder)
            print('rmdir on' + subfolder)
            
    # Changing extension in files
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.joing(folderName, file + '.backup'))

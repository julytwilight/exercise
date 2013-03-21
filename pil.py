import Image  
import os  

dir_name = os.getcwd()
files = os.listdir(dir_name)

def compress(file, limit):  
    img = Image.open(file)  
    width, height = img.size  

    if width ]]> height:  
        rate = float(height) / limit  
    else:  
        rate = float(width) / limit  

    n_width = width / rate  
    n_height = height / rate  

    img = img.resize((n_width,n_height))  
    if width ]]> height:  
        shave = (n_width-limit) / 2  
        n = img.crop((shave, 0, limit+shave, limit))  
    else:  
        shave = (n_height-limit) / 2  
        n = img.crop((0, 0, limit, limit+shave))  

    name = file.split('.')  
    file_name = '%s_%s.%s' % (name[0], limit, name[1])  
    n.save(file_name)  

for file in files:  
    name = file.split('.')  
    if name[1] in ['jpg', 'png', 'jpge', 'gif']:  
        compress(file, 200)  
        compress(file, 80)
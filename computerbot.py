import os



desktop = 'C:\\Users\\Nishan\\Desktop'
disk_c = 'C:'
disk_d = 'D:'
disk_e = 'E:'




def makedir():


    mklocation = input("Where do you want to create folder sir ?").lower()
    if(mklocation == "desktop" or mklocation ==  "at desktop" or mklocation == "on desktop"):
        folder_path = desktop
    elif(mklocation == "d" or mklocation == "d drive" or mklocation == "disk d"):
        folder_path = disk_d
    else:
        print("sorry sir !! I dont have permission to create file in this location by windows")    
    namedir = input("What do I name the folder : ")
    path = os.path.join(folder_path,namedir)
    os.mkdir(path)
    print(f"Your folder named {namedir} is created")

makedir()
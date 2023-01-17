import os
import shutil
import sys
from PyQt5 import QtWidgets,QtGui

# app = QtWidgets.QApplication(sys.argv)
# windows = QtWidgets.QWidget()
# windows.resize(500,500)
# windows.move(100,100)

# windows.setWindowTitle('Title')
# # set icon
# # windows.setWindowIcon(QtGui.QIcon('icon.png'))
# windows.show()
# sys.exit(app.exec_())

while True:
    nameproject=input("Quelle est le nom de votre projet").lower()
    if len(nameproject)>0:
        break

while True:
    reactrouter=input("voulez vous utliser react router y or n").lower()
    if reactrouter=="y" or reactrouter=="n" :
        break

while True:
    reactredux=input("voulez vous utliser react redux y or n").lower()
    if reactredux=="y" or reactredux=="n" :
        break

while True:
    sass=input("voulez vous utliser Sass y or n").lower()
    if sass=="y" or sass=="n" :
        break

scss="scss"
pages="pages"
pardirprj=os.path.join(os.getcwd(),nameproject,"src")
pardirfile=os.path.join(os.getcwd(),"file")
pathscss=os.path.join(pardirprj,scss)
pathpages=os.path.join(pardirprj,pages)

if reactrouter=="y" and reactredux=="y" and sass=="y":

    os.system("npx create-react-app " + nameproject + " --template redux")
    os.makedirs(pathscss)
    os.makedirs(pathpages)

    os.chdir(nameproject)
    os.system("npm install react-router-dom")
    os.system("npm install sass")

    shutil.copy(pardirfile+"/_conf.scss",pathscss)
    shutil.copy(pardirfile+"/main.scss",pathscss)
    shutil.copy(pardirfile+"/global.scss",pathscss)
    shutil.copy(pardirfile+"/index.js",pardirprj)
    shutil.copy(pardirfile+"/App.js",pardirprj)
    shutil.copy(pardirfile+"/router.js",pardirprj+"/features")
    shutil.copy(pardirfile+"/main.js",pardirprj+"/pages")
    shutil.copy(pardirfile+"/Nopage.js",pardirprj+"/pages")
    
if  reactrouter=="y" and reactredux=="y" and sass=="n":
    os.system("npx create-react-app " + nameproject + " --template redux")
    os.makedirs(pathpages)
    os.chdir(nameproject)
    os.system("npm install react-router-dom")
    shutil.copy(pardirfile+"/index.js",pardirprj)
    shutil.copy(pardirfile+"/App.js",pardirprj)
    shutil.copy(pardirfile+"/router.js",pardirprj+"/features")
    shutil.copy(pardirfile+"/main.js",pardirprj+"/pages")
    shutil.copy(pardirfile+"/Nopage.js",pardirprj+"/pages")

if  reactrouter=="n" and reactredux=="n" and sass=="n":
    os.system("npx create-react-app " + nameproject)
    os.makedirs(pathpages)
    os.chdir(nameproject)
    shutil.copy(pardirfile+"/index.js",pardirprj)
    shutil.copy(pardirfile+"/App.js",pardirprj)
    shutil.copy(pardirfile+"/main.js",pardirprj+"/pages")
    shutil.copy(pardirfile+"/Nopage.js",pardirprj+"/pages")





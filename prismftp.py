import os
import ftplib
import zipfile

ftp = ftplib.FTP("prism.nacse.org")
ftp.login("anonymous", "khafen74@gmail.com")

ftp.cwd("monthly/ppt") #remote folder containing data (monthly precipitation data)
fnbase = "PRISM_ppt_stable_4kmM" #filename before year
fnmid = "2_" #for years before 1981
fnend = "_all_bil.zip" #filename after year and extension

savedir = "E:/konrad/Projects/usgs/prosper-nhd/data/ppt/raw" #directory to save files
os.chdir(savedir) #change local directory to save directory

startyear = 1895 #year to start downloading precipitation data
endyear = 1980 #last year to download data

for year in range(startyear, endyear+1): #loop through years
    if year > 1980:
        fnmid = "3_" #different filename for years after 1980
    ftp.cwd(str(year)) #change remote directory to download year
    fn = fnbase + fnmid + str(year) + fnend #create filename
    file = open(fn, "wb") #create and open local file to write data to
    ftp.retrbinary("RETR " + fn, file.write) #write data to local file
    file.close() #close local file
    zfile = zipfile.ZipFile(fn) #local file is zipfile, create zipfile object
    zfile.extractall() #extract zipfile contents
    zfile.close() #close zip file after extraction
    ftp.cwd("../") #move up one level in remote directory
    os.remove(fn) #delete zip file after files have been extracted
    print str(year) + " done"


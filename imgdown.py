import re
import urllib

#read the webpage link
url = raw_input("Enter the weblink : ")
page_htm = urllib.urlopen(url)
page = page_htm.read()

#regex part
patt_img=re.compile('<img[^>]*src="([^">]+)"',re.IGNORECASE)
result=re.findall(patt_img,page)

#writing to the file 
f=open("output.txt","w")
for i in result:
	f.write(url+i+"\n")
f.close()
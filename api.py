import urllib.parse
import requests

############ SEARCH QUERY URLS ############
def titletagquery(keyword):
    query="/2.2/search/advanced?order=desc&sort=votes&q=["
    query+=keyword+"]&accepted=True&title="
    query+=keyword+"&site=stackoverflow&filter=!-*jbN-o8P3E5"
    return query

def tagquery(keyword):
    query="/2.2/search/advanced?order=desc&sort=votes&q=["
    query+=keyword+"]&accepted=True&site=stackoverflow&filter=!-*jbN-o8P3E5"
    return query

def titlequery(keyword):
    query="/2.2/search/advanced?order=desc&sort=votes&accepted=True&title="
    query+=keyword+"&site=stackoverflow&filter=!-*jbN-o8P3E5"
    return query
###########################################

######### Creating HTML File ##############

class CreateHTML:

    def __init__(self,name):
        self.name=name
        self.createtemplate(self.name)

    #HTML Template (before body)
    def createtemplate(self,name):                        
        with open(name+".html","w") as f:
            f.write("""<!DOCTYPE html>
    <html>
    <head>
    <title>"""+name+"""</title>
    </head>
    <body>
    """)

    #Appending data to HTML File
    def writedata(self,title,body,ans):
        with open(self.name+".html","a") as f:
            f.write("<h1>"+title+"</h1>\n"+body+"\n\n<h1>Answer:</h1>\n"+ans+"\n<hr>\n")
            
    #Fetching Data
    def getquestion(self,keyword):
        try:
            main_api='https://api.stackexchange.com/'
            query=titletagquery(keyword)
            r=requests.get(main_api+query)
            json_object=r.json()

            #Search query preference order: title+tag -> title -> tag
            if json_object["items"]==[]:
                query=titlequery(keyword)
                r=requests.get(main_api+query)
                json_object=r.json()
                if json_object["items"]==[]:
                    query=tagquery(keyword)
                    r=requests.get(main_api+query)
                    json_object=r.json()
                    if json_object["item"]==[]:
                        raise Exception
            temp_qtitle=str(json_object["items"][0]["title"])              #0 for first question and its answer set
            temp_qbody=str(json_object["items"][0]["body"])                #body for first question
            temp_ans=str(json_object["items"][0]["answers"][0]["body"])    #first retrieved answer's body
            self.writedata(temp_qtitle,temp_qbody,temp_ans)
        except:
            print("No data could be found. Keyword: "+keyword)

    
    def addquestion(self,keyword):
        self.getquestion(keyword)

    # IMPORTANT! Closes the HTML tags including body
    def endquestion(self):
        with open(self.name+".html","a") as f:
            f.write("</body></html>")

"""
/2.2/search/advanced?order=desc&sort=votes&accepted=True&title=ACM&site=stackoverflow&filter=!-*jbN-o8P3E5
"""

from bs4 import BeautifulSoup
import urllib3,requests,time

urllib3.disable_warnings()
#disableing certifcate warnings

url="https://pareekshabhavan.uoc.ac.in/index.php/examination/notifications"


#function to fetch all notificaton
def allnotification():
    response = requests.get ( url,verify=False )
    soup = BeautifulSoup ( response.text,'lxml' )
    notifi_list = soup.find_all ( 'li',{'class' : 'notif'})
    # fetching notifications in list,class name-notiful

    try:
        for notification in notifi_list :
            noti_element = notification.find ( "a" )  # focusing "a" tag
            notification = noti_element.text
            notifi_link = noti_element["href"]
            print ( notification,"\n" )
    except:
        TimeoutError,ConnectionError

allnotification()

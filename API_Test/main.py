import requests
import time


headers={'content-type': 'application/json', 'Accept': '/', 'connection': 'keep-alive'}
payload = {"sessionID":"97850beb130ab101755038afa2e360b9"}
url = "https://a2.vmedia.ca/api/channel/recent"
list_parser = []
post_dict = []

# creating object r which will handle a session
r = requests.session()
# check head just for open session
r.head(url)
for x in range(0, 2):
    start = time.time()
    #getting response for each post
    post_dict.append(r.post(url=url, json=payload).text)
    stop = time.time()
    print(f"{round(stop-start, 5)} seconds\n")
# closing the session
r.close()

print(post_dict)
#print(r.text)
#print(type(r.text))
#print(r.status_code)





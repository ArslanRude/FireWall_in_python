import pickle
from plyer import notification
import webbrowser

model = pickle.load(open('pipe_url.pkl', 'rb'))
def classify_url(url):
    label = model.predict([url])[0]
    if label == 'good':
        return 1
    else:
        return 0
def check_url(url):
    if classify_url(url) == 0:
        print("Access to the URL is restricted due to security concerns.")
        notification.notify(
            title="Alert",
            message="Access to the URL is restricted due to security concerns",
            timeout=10
        )
    else:
        webbrowser.open(url)
import pandas as pd
from plyer import notification
def check_IP(url):
    df = pd.read_csv("Allowes_IP_ADDRESS.csv")
    isValid = pd.DataFrame(df.isin([url]).any(),dtype=int)
    ip = isValid.to_numpy().tolist()
    if ip[0][0] == 0:
        print("Access to the URL is restricted due to security concerns.")
        notification.notify(
            title="Alert",
            message="Access to the URL is restricted due to security concerns",
            timeout=5
        )
        return False
    else :
        return True
from typing import Final, List

SFH: Final[str] = "SFH"
POP_UP_WINDOW: Final[str] = "popUpWidnow"
SSL_FINAL_STATE: Final[str] = "SSLfinal_State"
REQUEST_URL: Final[str] = "Request_URL"
URL_OF_ANCHOR: Final[str] = "URL_of_Anchor"
WEB_TRAFFIC: Final[str] = "web_traffic"
URL_LENGTH: Final[str] = "URL_Length"
AGE_OF_DOMAIN: Final[str] = "age_of_domain"
HAVING_IP_ADDRESS: Final[str] = "having_IP_Address"
RESULT: Final[str] = "Result"

FEATURES: Final[List[str]] = [SFH, POP_UP_WINDOW, SSL_FINAL_STATE, REQUEST_URL, URL_OF_ANCHOR, WEB_TRAFFIC, URL_LENGTH,
                              AGE_OF_DOMAIN, HAVING_IP_ADDRESS]
CLASSES: Final[List[str]] = ["Phishing", "Suspicious", "Not Phishing"]

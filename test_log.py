import time

log = {
    "method": "Network.responseReceived",
    "params": {
        "frameId": "948569C0FD0AD2D0F076494116CB5879",
        "hasExtraInfo": True,
        "loaderId": "6F5FEC2E6E56CEC80D7483C3EBBD3550",
        "requestId": "2091.868",
        "response": {
            "alternateProtocolUsage": "unspecifiedReason",
            "connectionId": 10151,
            "connectionReused": False,
            "encodedDataLength": 274,
            "fromDiskCache": False,
            "fromPrefetchCache": False,
            "fromServiceWorker": False,
            "headers": {
                "access-control-allow-origin": "*",
                "cache-control": "max-age=86400, public",
                "content-encoding": "gzip",
                "content-type": "text/javascript",
                "cross-origin-resource-policy": "cross-origin",
                "date": "Sun, 30 Apr 2023 19:25:15 GMT",
                "etag": 'W/"63f86dec-16386"',
                "expires": "Mon, 01 May 2023 19:25:15 GMT",
                "last-modified": "Fri, 24 Feb 2023 07:57:32 GMT",
                "server": "nginx",
                "strict-transport-security": "max-age=31536000; preload;",
                "timing-allow-origin": "*",
            },
            "mimeType": "text/javascript",
            "protocol": "h2",
            "remoteIPAddress": "74.119.119.131",
            "remotePort": 443,
            "responseTime": 1682882715951.586,
            "securityDetails": {
                "certificateId": 0,
                "certificateTransparencyCompliance": "unknown",
                "cipher": "AES_128_GCM",
                "encryptedClientHello": False,
                "issuer": "DigiCert Global G2 TLS RSA SHA256 2020 CA1",
                "keyExchange": "",
                "keyExchangeGroup": "X25519",
                "protocol": "TLS 1.3",
                "sanList": ["*.criteo.net", "criteo.net"],
                "serverSignatureAlgorithm": 1027,
                "signedCertificateTimestampList": [],
                "subjectName": "*.criteo.net",
                "validFrom": 1679616000,
                "validTo": 1687132799,
            },
            "securityState": "secure",
            "status": 200,
            "statusText": "",
            "timing": {
                "connectEnd": 15.399,
                "connectStart": 0.114,
                "dnsEnd": 0.114,
                "dnsStart": 0.109,
                "proxyEnd": -1,
                "proxyStart": -1,
                "pushEnd": 0,
                "pushStart": 0,
                "receiveHeadersEnd": 28.276,
                "requestTime": 997.859127,
                "sendEnd": 15.598,
                "sendStart": 15.565,
                "sslEnd": 15.397,
                "sslStart": 6.339,
                "workerFetchStart": -1,
                "workerReady": -1,
                "workerRespondWithSettled": -1,
                "workerStart": -1,
            },
            "url": "https://static.criteo.net/js/ld/publishertag.prebid.js",
        },
        "timestamp": 997.88771,
        "type": "XHR",
    },
}
print(f"time: {log['params']['timestamp']}")
now = time.time()
print(now)
time.sleep(2)
curr = time.time()
diff = curr - now
print(diff)
print("bid" in log['params']['response']['url'])

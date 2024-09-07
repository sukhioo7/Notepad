import requests

def check_link_with_addhar(addhar_number):
    url = "https://pan-number-verification-api-using-aadhaar-number.p.rapidapi.com/api/validation/aadhaar_to_pan"

    payload = {
        "aadhaar": addhar_number,
        "consent": "y",
        "consent_text": "I hear by declare my consent agreement for fetching my information via AITAN Labs API"
    }
    headers = {
        "x-rapidapi-key": "68f0ae5d48msh22c4d73470c8443p181467jsn1a28b703a22b",
        "x-rapidapi-host": "pan-number-verification-api-using-aadhaar-number.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    text = f'''
Aadhaar Number : {data['aadhaar']}
Link Status : {data['status']}
PAN Linked : Your PAN card is linked with your addhar card.
PAN Card Number : {data['result']['pan']}
''' 
    return text

addhar_number = input("Enter your Aadhaar number: ")

result = check_link_with_addhar(addhar_number)

print(result)

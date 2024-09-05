import requests

url = "https://www2.everestgrp.com/downloadfile/EGR-2024-79-P-6633?shortCode=EverestGroup-Implica"

payload = {}
headers = {
  'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'Upgrade-Insecure-Requests': '1',
  'DNT': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'host': 'www2.everestgrp.com',
  'Cookie': '.IDSDR=71C31CE1B66AD43A7365B33F28E9D2E4EAD55D161403E4D64E91AF0C4F5BA3E23FCE8ADE65B7C78F5C8002A2786ADE0DBB10FA398181AAE82089B59C5C7FD82FFB755A4405A26D636F7DBF962BDF282C2117FEC980BF0E4DAE1B8D12A80303E7A01B5BCD5E2E17B4EA373F99D06ACD5D5F3970C6D1CFC1D04CB3B4139970CB5CEFA7DB241FEEFA72CE0C6FF89D59D9FBF73A391BCAB562ED9B01BD6E49F06441D2B8B70368D1A4A54215DABA49D10D4834232E547C74A6DEAC95346EE31F84CDB6EDDB0D0EA7DA0714990A0565C87E104FC34CAA171DBA609D86F5F904FA866C436EEC9361E9220A8350523E82CFD18AF81DC2181BDF756E7F4F067990D316AD; ASP.NET_SessionId=2zns31xmf3muwn5qqtax5fkh; ndemoSessionTracker=24e9415e-a13e-420b-b69b-3a59242af527; ndemo__RequestVerificationToken=UjNAlsQa25AkJ1RJfHe7J9_x5KqnanKMHK79N2Fgfyf_5YHb3n0kOKlK59oo2tebrW8E1VViWkyAE3YWpWqpTEMA5rSPL_12tMqEAwY7iZk1'
}

response = requests.request("GET", url, headers=headers, data=payload, allow_redirects=True)

print(response.text)
# # Check if the final response is successful
# if response.status_code == 200:
#     # Save the content of the file to disk
#     with open("downloaded_file.pdf", "wb") as f:
#         f.write(response.content)
#     print("File downloaded successfully.")
# else:
#     print(f"Failed to download file. Status code: {response.status_code}")

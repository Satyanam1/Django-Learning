import requests
from bs4 import BeautifulSoup
def message(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  text = soup.get_text()
  lines = text.strip().split('\n')
  lines = [line.strip() for line in lines if line.strip()]
  grid = {}
  max_x=0
  max_y=0
  for line in lines:
        parts = line.split()
        if len(parts) == 3:
            try:
                char = parts[0]
                x = int(parts[1])
                y = int(parts[2])
                grid[(x, y)] = char
                max_x = max(max_x, x)
                max_y = max(max_y, y)
            except ValueError:
                continue
  for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            row += grid.get((x, y), ' ')
        print(row)        
message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")
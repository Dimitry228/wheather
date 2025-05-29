# Laikapstākļu skrāpis 

## Projekta uzdevums

Šī programma automatizē laikapstākļu pārskatu iegūšanu Rīgai, izmantojot informāciju no publiski pieejamās vietnes **timeanddate.com**. Programma iegūst temperatūru, aprakstu, vēja ātrumu un mitrumu, un saglabā datus CSV failā.

## Izmantotās Python bibliotēkas

- `requests` – HTTP pieprasījuma veikšanai.
- `BeautifulSoup (bs4)` – HTML satura parsēšanai un datu nolasīšanai.
- `csv` – datu strukturētai glabāšanai CSV failā.
- `datetime` – lai reģistrētu datuma un laika zīmogu.

## Programmas darbība

Programma:
1. Apmeklē lapu https://www.timeanddate.com/weather/latvia/riga
2. Nokasa aktuālo laikapstākļu informāciju
3. Saglabā datus CSV failā `weather_log.csv`

## Papildus iespējas

- Var pielāgot skriptu citām pilsētām mainot URL.
- Ikdienas monitorings ar ieplānotiem palaišanas uzdevumiem.

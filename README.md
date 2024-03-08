# AutoScout24 Web Scraper

## Description
This repository contains a web scraping program for extracting and structuring data about cars from the AutoScout24 platform. The program uses web scraping techniques to extract information such as brand, model, fuel type, color, mileage, country of origin, year of first registration, price, and other relevant details.

## How to use
1. Installation:
    ```bash
    git clone https://github.com/utilizator/AutoScout24-WebScraper.git
    cd AutoScout24-WebScraper
    ```

2. Configuration:
    - Make sure you have installed all the dependencies mentioned in the `requirements.txt` file.
    - Replace `HEADERS` with a valid user agent for your requests.
    - Modify the `query` to match the URL of the AutoScout24 page you want to parse.

3. Running:
    ```bash
    python autoscout24.py
    ```

4. Results:
    - The extracted data will be saved in a JSON file named `autoscout.json`.

## Contributions
Contributions are welcome! If you would like to contribute to this project, please follow these steps:
1. Open an issue to discuss the proposed change.
2. Fork this repository.
3. Create a new branch (`git checkout -b feature/feature-name`).
4. Add your changes and commits (`git commit -am 'Added feature X'`).
5. Push to your branch (`git push origin feature/feature-name`).
6. Open a pull request.

# Web Scraping 

## Overview
This project is aimed at scraping data from sentimentrader website using BeautifulSoup and Selenium, two powerful Python libraries for web scraping. The scraped data is then stored in CSV format and uploaded to Google Sheets using Google Sheets API.

## Features
- **Web Scraping**: Utilizes BeautifulSoup and Selenium to extract data from websites.
- **Data Storage**: Saves the scraped data in CSV format for easy access and analysis.
- **Google Sheets Integration**: Automatically uploads the CSV files to Google Sheets via Google Sheets API.
- **Scalability**: Can be easily scaled to scrape data from multiple websites and store it in a structured format.

## Requirements
- Python 3.x
- BeautifulSoup
- Selenium
- Google Sheets API
- Google Cloud Platform Account (for setting up Google Sheets API)

## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/osman-haider/Web-Scrapping.git](https://github.com/osman-haider/Web-Scrapping.git)
   cd Web-Scrapping
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Google Sheets API:
   - Follow the instructions in the [Google Sheets API documentation](https://developers.google.com/sheets/api/quickstart/python) to enable the API for your project.
   - Download the `credentials.json` file and save it in the project directory.

4. Run the main script:
   ```bash
   python main.py
   ```

## Usage
1. Customize `main.py` with your scraping logic.
2. Run `main.py` to initiate the scraping process.
3. The scraped data will be saved in CSV files and automatically uploaded to Google Sheets.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries or suggestions, feel free to contact [osmanhaider167@gmail.com](osmanhaider167@gmail.com).

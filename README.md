# TikTok Scraper

This tool allows you to scrape TikTok videos on any topic you need. It is designed to help you gather data from TikTok for analysis, research, or any other purpose.

## Features

- Scrape TikTok videos based on specific topics or hashtags
- Extract video metadata such as views, likes, comments, and shares
- Save scraped data in a structured format for easy analysis

## Requirements

- Python 3.x
- Chrome drivers for selenium
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ramiro-marinio/tiktok_scraper.git
    cd tiktok_scraper
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. In the constants.py file, modify your batch size and target videos. Keep in mind that target videos have to be a multiple of batch size, otherwise the surplus videos will not be saved.

2. Run the scraper with the desired topic or hashtag:
    ```bash
    python main.py
    ```

3. The scraped data will be saved in JSON format. If the program reaches the target amount of videos, it will prompt you to find the folder where they are located and the files will be combined into a single one called combined.json. If you stopped the program early, you can still combine all files by running combine.py.

## Configuration

You can configure the scraper by editing the `constants.py` file. This file allows you to set parameters such as the number of videos to scrape, output format, and other options.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact me at [ramiro.marinho0@gmail.com].

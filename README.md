# Finance Investment Dataset Generator

This repository contains a Python script that generates a comprehensive and diverse dataset related to **finance investment**. The dataset includes questions and answers covering various investment strategies, asset classes, market trends, and investor performance. The script is designed to be highly customizable and expandable, allowing for detailed exploration of finance-related content.

## Features

- **Finance Investment Focus**: The script generates content related to finance investments, such as portfolio management, risk mitigation, asset allocation, and investment strategies.
- **Dynamic Dataset Generation**: The script uses templates and variables to create highly diverse entries, ensuring unique content in each generated entry.
- **Expanded Scope**: Covers a wide array of financial topics, including traditional investments, modern strategies (e.g., ESG investing, crypto arbitrage), and future trends in finance (e.g., decentralized finance).
- **Customizable Templates**: The script includes multiple templates for questions and answers, which can be easily expanded or modified to fit specific needs.
- **Supports Multiple Contexts**: Generates content that includes regional (e.g., North America, Europe) and sector-specific (e.g., technology, healthcare) dimensions to provide detailed insights into global investment practices.

## Dataset Structure

Each entry in the generated dataset includes:
- A question and answer format that discusses a finance investment topic.
- Dynamic variables for investment strategies, groups, assets, markets, regions, sectors, and performance metrics.
- A `meta` section that contains a timestamp indicating when the entry was generated.

### Example Entry

```json
{
  "content": "Question: How does value investing allow institutional investors to capitalize on opportunities in the technology sector in the stock market? Answer: Value investing helps institutional investors maximize returns by focusing on equities within the technology sector, optimizing risk and reward in the stock market.",
  "meta": {
    "time": "2023-07-15 14:23:12"
  }
}
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/finance-investment-dataset-generator.git
   cd finance-investment-dataset-generator
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install required dependencies (if any).

4. Run the script to generate the dataset:
   ```bash
   python generate_dataset.py
   ```

## Usage

1. Open the `generate_dataset.py` script to configure the dataset generation process:
   - You can modify the templates, variables, or adjust the number of entries.
   - The script generates a JSON file (`broader_finance_investment_data.json`) containing finance investment-related data.

2. To generate a dataset with 2,000 finance investment entries:
   ```bash
   python generate_dataset.py
   ```

3. The generated dataset will be saved as `broader_finance_investment_data.json`.

### Customization

The script is fully customizable. You can:
- Add new templates to the `template_data` list.
- Expand or modify the `investment_strategies`, `assets`, `markets`, `groups`, and other variables to fit your specific dataset requirements.
- Adjust the number of entries by changing the `num_entries` argument in the `generate_dataset()` function.

## File Overview

- **generate_dataset.py**: The main Python script for generating the dataset.
- **broader_finance_investment_data.json**: The generated dataset file (after running the script).
- **README.md**: This documentation file.

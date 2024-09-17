import json
import random
from datetime import datetime, timedelta

# Redesigned template data with more diverse finance investment-related questions and answers
template_data = [
    {
        "content": "Question: How does [investment_strategy] allow [group] to capitalize on opportunities in [sector] in the [market]? Answer: [investment_strategy] helps [group] maximize returns by focusing on [asset] within the [sector] sector, optimizing risk and reward in the [market] market.",
    },
    {
        "content": "Question: What impact does [project_name] have on [group]'s ability to diversify their investments in [region]? Answer: [project_name] allows [group] to diversify their portfolio in [region] by including [asset], improving [performance_metric] in the [market] market.",
    },
    {
        "content": "Question: How does [investment_strategy] help mitigate risk for [group] investing in [asset] across [region]? Answer: By using [investment_strategy], [group] can lower exposure to volatility in [asset] within [region], achieving better [performance_metric] in the [market].",
    },
    {
        "content": "Question: What advantages do [group] gain by incorporating [project_name] into their portfolio management strategy? Answer: [project_name] enables [group] to streamline their portfolio with advanced tools for [action], ensuring [performance_metric] across their holdings in [market].",
    },
    {
        "content": "Question: How is [project_name] transforming investment in [asset] for [group] within [sector]? Answer: [project_name] revolutionizes how [group] manage investments in [asset], driving [performance_metric] within the [sector] sector in [market].",
    },
    {
        "content": "Question: What are the long-term benefits of adopting [investment_strategy] in [region] for [group]? Answer: [investment_strategy] provides [group] with long-term benefits by focusing on [asset] across [region], resulting in [performance_metric] over the years in the [market] market.",
    },
    {
        "content": "Question: How is [investment_strategy] impacting sustainable investing in [sector]? Answer: [investment_strategy] supports sustainable investing in [sector] by encouraging [group] to invest in environmentally responsible [asset] with a focus on [performance_metric].",
    },
    {
        "content": "Question: How does [group] leverage [project_name] to outperform traditional [investment_strategy] in [market]? Answer: [group] uses [project_name] to enhance [performance_metric] by adopting more innovative approaches compared to traditional [investment_strategy] in [market].",
    },
    {
        "content": "Question: What role does [project_name] play in improving [group]'s [performance_metric] in [region]? Answer: [project_name] assists [group] in achieving better [performance_metric] by [action], optimizing their exposure to [asset] in [region] for greater success in [market].",
    }
]

# Expanded investment-related variables with more variety
investment_strategies = [
    "index investing", "value investing", "growth investing", "hedge fund strategies",
    "quantitative trading", "impact investing", "ESG investing", "crypto arbitrage",
    "real estate investing", "fixed income investing", "dividend growth investing"
]

project_names = [
    "InvestPro", "RiskGuard", "AlphaMax", "WealthBuilder", "QuantFund", "HedgeX", "CryptoAllocator",
    "GreenInvest", "RealEstateFund", "BondMaster", "DeFiYield"
]

groups = [
    "institutional investors", "retail investors", "pension funds", "hedge funds", "private equity firms",
    "venture capitalists", "family offices", "sovereign wealth funds", "mutual fund managers"
]

assets = [
    "equities", "bonds", "commodities", "cryptocurrencies", "real estate", "ETFs", "mutual funds",
    "derivatives", "private equity", "infrastructure", "sustainable assets", "emerging market stocks"
]

markets = [
    "stock", "bond", "commodities", "cryptocurrency", "real estate", "emerging markets", 
    "forex", "private equity", "decentralized finance"
]

performance_metrics = [
    "high returns", "low volatility", "improved liquidity", "better diversification", "enhanced capital appreciation",
    "stable income generation", "risk mitigation", "reduced fees", "long-term growth"
]

actions = [
    "optimizing asset allocation", "enhancing risk-adjusted returns", "reducing portfolio volatility", 
    "improving liquidity", "lowering transaction costs", "increasing transparency", "automating portfolio rebalancing"
]

# New variables to add broader context
regions = ["North America", "Europe", "Asia-Pacific", "Latin America", "Africa", "Global"]
sectors = ["technology", "healthcare", "financial services", "energy", "consumer goods", "industrials", "real estate"]

# Function to generate random timestamps
def generate_random_timestamp(start, end):
    return (start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))).strftime("%Y-%m-%d %H:%M:%S")

# Function to generate the finance investment-focused dataset with more diversity
def generate_dataset(num_entries):
    dataset = []
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2024, 8, 17)

    for _ in range(num_entries):
        entry_template = random.choice(template_data)
        content_variation = entry_template["content"]

        # Replacing placeholders with expanded investment-related options
        content_variation = content_variation.replace("[investment_strategy]", random.choice(investment_strategies))
        content_variation = content_variation.replace("[project_name]", random.choice(project_names))
        content_variation = content_variation.replace("[group]", random.choice(groups))
        content_variation = content_variation.replace("[asset]", random.choice(assets))
        content_variation = content_variation.replace("[market]", random.choice(markets))
        content_variation = content_variation.replace("[performance_metric]", random.choice(performance_metrics))
        content_variation = content_variation.replace("[action]", random.choice(actions))
        content_variation = content_variation.replace("[region]", random.choice(regions))
        content_variation = content_variation.replace("[sector]", random.choice(sectors))

        # Create the new entry with content and timestamp
        new_entry = {
            "content": content_variation,
            "meta": {
                "time": generate_random_timestamp(start_date, end_date)
            }
        }

        dataset.append(new_entry)

    return dataset

# Generate dataset with 2000 finance investment-related entries
dataset = generate_dataset(2000)

# Save the dataset to a JSON file
with open('broader_finance_investment_data.json', 'w') as f:
    json.dump(dataset, f, indent=2)

print("Broader finance investment dataset JSON successfully created.")

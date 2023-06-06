import datetime

import pandas as pd
import pytest
from data import data_preparation


class TestGenerateData:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.mockGenerateData = data_preparation.GenerateData(path="fakepath")

    def test_get_dates(self):
        generate_data = data_preparation.GenerateData(path="fake_path")

        df = pd.DataFrame(
            {
                "timestamp": [
                    "2019-10-17 17:00:00",
                    "2020-11-18 18:30:00",
                    "2021-12-19 19:45:00",
                ]
            }
        )
        output = generate_data.get_dates(df=df)

        expected = [
            {
                "timestamp": "2019-10-17 17:00:00",
                "timestamp_dupe": pd.Timestamp("2019-10-17 17:00:00"),
                "date": datetime.date(2019, 10, 17),
                "year": 2019,
                "month": 10,
                "quarter": 4,
                "week": 42,
            },
            {
                "timestamp": "2020-11-18 18:30:00",
                "timestamp_dupe": pd.Timestamp("2020-11-18 18:30:00"),
                "date": datetime.date(2020, 11, 18),
                "year": 2020,
                "month": 11,
                "quarter": 4,
                "week": 47,
            },
            {
                "timestamp": "2021-12-19 19:45:00",
                "timestamp_dupe": pd.Timestamp("2021-12-19 19:45:00"),
                "date": datetime.date(2021, 12, 19),
                "year": 2021,
                "month": 12,
                "quarter": 4,
                "week": 50,
            },
        ]
        assert output.to_dict("records") == expected

    def test_fill_dates(self):
        # Sample DataFrame
        df = pd.DataFrame(
            {
                "product_title": ["A", "A", "B", "B", "B", "C", "C", "C"],
                "sales": [10, 15, 20, 12, 18, 30, 25, 20],
                "date": [
                    "2022-01-01",
                    "2022-02-02",
                    "2022-01-01",
                    "2022-02-03",
                    "2022-01-04",
                    "2022-02-01",
                    "2022-04-02",
                    "2022-05-04",
                ],
            }
        )

        # Convert 'dates' column to datetime
        df["date"] = pd.to_datetime(df["date"])

        output = self.mockGenerateData.fill_dates(df=df)

        assert output == output

    # def test_impute_data(self):

    #     # Example DataFrame

    #     # Set the random seed for reproducibility
    #     np.random.seed(42)

    #     # Generate dates for one year
    #     start_date = pd.Timestamp('2022-01-01')
    #     end_date = pd.Timestamp('2022-12-31')
    #     dates = pd.date_range(start_date, end_date, freq='D')

    #     # Generate random sales data for each date
    #     sales = np.random.randint(100, 1000, len(dates))

    #     # Create a DataFrame with dates and sales
    #     df = pd.DataFrame({'date': dates, 'sales': sales})

    #     # Randomly remove 50% of the rows
    #     df = df.sample(frac=0.5, random_state=42)

    #     # Reset the index of the DataFrame
    #     df.reset_index(drop=True, inplace=True)

    #     # Extract year, month, quarter, and week components
    #     df['year'] = df['date'].dt.year
    #     df['month'] = df['date'].dt.month
    #     df['quarter'] = df['date'].dt.quarter
    #     df['week'] = df['date'].dt.isocalendar().week

    #     generateData = data_preparation.GenerateData(path="fakepath")
    #     output = generateData.impute_data(df = df)

    #     print(output)

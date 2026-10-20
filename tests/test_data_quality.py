
import unittest
import pandas as pd

class TestDataQuality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(
            "data/cleaned_retail_sales.csv"
        )

    def test_missing_values(self):
        self.assertEqual(
            self.df.isnull().sum().sum(), 0
        )

    def test_duplicate_records(self):
        self.assertEqual(
            self.df.duplicated().sum(), 0
        )

    def test_positive_sales(self):
        self.assertTrue(
            (self.df["total_sales"] > 0).all()
        )

    def test_record_count(self):
        self.assertEqual(len(self.df), 8)


if __name__ == "__main__":
    unittest.main()

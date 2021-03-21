import unittest

from anime_info_collector import InfoCollector


class TestInfoCollector(unittest.TestCase):
    def test__create_mediawiki_query_from_title(self):
        query_url = InfoCollector()._create_mediawiki_query_form_title("hoge")
        self.assertEqual(
            "https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&titles=hoge&rvprop=content&rvparse=",
            query_url,
        )


if __name__ == "__main__":
    unittest.main()
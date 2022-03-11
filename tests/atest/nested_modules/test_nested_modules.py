from pathlib import Path

from .. import Tree, Keyword, AcceptanceTest


class TestNestedModules(AcceptanceTest):
    ROOT = Path(Path(__file__).parent, "test_data")

    def test(self):
        data = self.run_sherlock()
        expected = Tree(
            name="test_data",
            res_type="Directory",
            children=[
                Tree(name="pages", res_type="Directory", children=[
                    Tree(name="pages", res_type="Library", keywords=[]),
                    Tree(name="Page1", res_type="Library", keywords=[Keyword(name="Keyword 1", used=1)]),
                    Tree(name="Page2", res_type="Library", keywords=[Keyword(name="Keyword 2", used=1), Keyword(name="Keyword 3", used=0)])
                ]),
                Tree(name="test.robot", res_type="Resource", keywords=[]),
            ],
        )
        self.should_match_tree(expected, data)

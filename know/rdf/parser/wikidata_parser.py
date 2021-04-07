# pylint: disable=no-self-use,unused-import,
import re
from rdf.parser.abstract_parser import AbstractParser, EntityType
class WikidataParser(AbstractParser):
    """parses wikidata sources"""

    def __init__(self, uri):
        super().__init__(uri)
        self.entity_id = re.search('Q[0-9]+', self.uri)
        if self.entity_id is None:
            raise Exception("Invalid Wikidata URI")

    def parse(self) -> dict:
        """call this method to start parsing"""
        return dict()
    def get_entity_type(self) -> str:
        "gets the entity type"
        return ""

    def parse_person(self) -> dict:
        """ Parses a person entity type """
        return dict()

    def parse_work_of_art(self) -> dict:
        """ Parses a work of art entity type """
        return dict()

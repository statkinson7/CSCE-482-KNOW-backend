import unittest
from rdf.parser.sparql_reader import read_sparql
from rdf.parser.wikidata_parser import WikidataParser, UnsupportedEntityTypeException
from rdf.parser.abstract_parser import EntityType


class ReadSparqlTests(unittest.TestCase):
    """ read_sparql tests """

    def test_read_replaces_0(self):
        """ test_read_replaces_0 will check that read_sparql will
            replace the $0 in the file with a test uri
        """

        # arrange
        expected = ("SELECT ?label{\n"
          "  wd:Q41513 p:P31 [ps:P31 ?instanceOf].\n"
          "  ?instanceOf rdfs:label ?label\n"
          "  FILTER((LANG(?label)) = \"en\")\n}\n")

        # act
        actual = read_sparql("get_instance.sparql", "Q41513")

        # assert
        self.assertEqual(expected, actual)

    def test_determines_book_entity_type(self):
        """Tests if the wikidata parser correctly determines book entities are books
        """
        parser = WikidataParser('https://www.wikidata.org/wiki/Q43361')
        expected = EntityType.BOOK
        actual = parser.get_entity_type()
        self.assertEqual(expected, actual)

    def test_determines_person_entity_type(self):
        """ Tests if the wikidata parser correctly determines
            person entities are type person.
        """
        parser = WikidataParser('https://www.wikidata.org/wiki/Q41513')
        expected = EntityType.PERSON
        actual = parser.get_entity_type()
        self.assertEqual(expected, actual)

    def test_throws_UnsupportedEntityTypeException_on_unsupported_entity_type(self): # pylint: disable=invalid-name
        """ Tests if the wikidata parser raises an exception
            when the entity is not a type we can parse.
        """
        parser = WikidataParser('https://www.wikidata.org/wiki/Q6928344')
        self.assertRaises(UnsupportedEntityTypeException, parser.get_entity_type)

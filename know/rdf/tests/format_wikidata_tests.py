# pylint: disable=too-many-lines
from unittest import TestCase
from rdf.parser.wikidata_formatter import (
    format_landmark,
    format_country,
    format_book,
    format_person
)

class FormatWikidataTests(TestCase):
    """ Tests the wikidata formatter functions """
    def setUp(self):
        self.maxDiff = None # pylint: disable=invalid-name

    def test_format_landmark(self):
        """ Tests format_landmark """
        # arrange
        json_input = {
            "head": {
                "vars": [
                    "name",
                    "description",
                    "territoryLocation",
                    "territoryLocationLabel",
                    "countryLocation",
                    "countryLocationLabel",
                    "inception",
                    "coordinates"
                ]
            },
            "results": {
                "bindings": [
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "tower located on the Champ de Mars in Paris, France"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Eiffel Tower"
                        },
                        "territoryLocation": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q259463"
                        },
                        "countryLocation": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q142"
                        },
                        "countryLocationLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "France"
                        },
                        "inception": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1887-01-28T00:00:00Z"
                        },
                        "coordinates": {
                            "datatype": "http://www.opengis.net/ont/geosparql#wktLiteral",
                            "type": "literal",
                            "value": "Point(2.294479 48.858296)"
                        }
                    }
                ]
            }
        }
        expected = {
            "title": "Eiffel Tower",
            "subtitle": "tower located on the Champ de Mars in Paris, France",
            "entries": {
                "Country": [
                    {
                        "value": "France",
                        "link": "http://www.wikidata.org/entity/Q142"
                    }
                ],
                "Creation Date": [
                    {
                        "value": "January 28, 1887"
                    }
                ]
            }
        }

        # act
        result = format_landmark(json_input)

        # assert
        self.assertEqual(result, expected)

    def test_format_country(self):
        """ Tests format_country """
        json_input ={
            "head": {
                "vars": [
                    "name",
                    "description",
                    "population",
                    "continentLabel",
                    "capitalLabel",
                    "areaKmSquared",
                    "headOfGov",
                    "headOfGovLabel",
                    "headOfState",
                    "headOfStateLabel"
                ]
            },
            "results": {
                "bindings": [
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "sovereign state in North Africa and Asia"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Egypt"
                        },
                        "population": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "94798827"
                        },
                        "areaKmSquared": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "1010407.87"
                        },
                        "headOfGov": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q54901515"
                        },
                        "headOfState": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q307871"
                        },
                        "continentLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Africa"
                        },
                        "capitalLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Cairo"
                        },
                        "headOfGovLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Moustafa Madbouly"
                        },
                        "headOfStateLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Abdel Fattah el-Sisi"
                        }
                    },
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "sovereign state in North Africa and Asia"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Egypt"
                        },
                        "population": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "94798827"
                        },
                        "areaKmSquared": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#decimal",
                            "type": "literal",
                            "value": "1010407.87"
                        },
                        "headOfGov": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q54901515"
                        },
                        "headOfState": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q307871"
                        },
                        "continentLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Asia"
                        },
                        "capitalLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Cairo"
                        },
                        "headOfGovLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Moustafa Madbouly"
                        },
                        "headOfStateLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Abdel Fattah el-Sisi"
                        }
                    }
                ]
            }
        }

        expected = {
            "title": "Egypt",
            "subtitle": "sovereign state in North Africa and Asia",
            "entries": {
                "Population": [
                    {
                        "value": "94,798,827"
                    },
                ],
                "Continent": [
                    {
                        "value": "Africa"
                    },
                    {
                        "value": "Asia"
                    }
                ],
                "Capital": [
                    {
                        "value": "Cairo"
                    },
                ],
                "Area": [
                    {
                        "value": "1,010,407 km sq."
                    },
                ],
                "Head of Government": [
                    {
                        "value": "Moustafa Madbouly",
                        "link": "http://www.wikidata.org/entity/Q54901515"
                    },
                ],
                "Head of State": [
                    {
                        "value": "Abdel Fattah el-Sisi",
                        "link": "http://www.wikidata.org/entity/Q307871"
                    },
                ]
            }
        }

        result = format_country(json_input)

        # assert
        self.assertEqual(result, expected)
    def test_format_person(self):
        """ Tests format_person """
        json_input = {
            "head": {
                "vars": [
                    "name",
                    "description",
                    "birthDate",
                    "deathDate",
                    "spouse",
                    "spouseLabel",
                    "nationality",
                    "nationalityLabel",
                    "occupationLabel"
                ]
            },
            "results": {
                "bindings": [
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "1st president of the United States (1732-1799)"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "George Washington"
                        },
                        "birthDate": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1732-02-22T00:00:00Z"
                        },
                        "deathDate": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1799-12-14T00:00:00Z"
                        },
                        "spouse": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q191789"
                        },
                        "nationality": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q30"
                        },
                        "spouseLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Martha Washington"
                        },
                        "nationalityLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "United States of America"
                        },
                        "occupationLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "politician"
                        }
                    },
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "1st president of the United States (1732-1799)"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "George Washington"
                        },
                        "birthDate": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1732-02-22T00:00:00Z"
                        },
                        "deathDate": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1799-12-14T00:00:00Z"
                        },
                        "spouse": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q191789"
                        },
                        "nationality": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q161885"
                        },
                        "spouseLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Martha Washington"
                        },
                        "nationalityLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Great Britain"
                        },
                        "occupationLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "politician"
                        }
                    }
                ]
            }
        }
        expected = {
            "title": "George Washington",
            "subtitle": "1st president of the United States (1732-1799)",
            "entries": {
                "Born": [
                    {
                        "value": "February 22, 1732"
                    }
                ],
                "Died": [
                    {
                        "value": "December 14, 1799"
                    }
                ],
                "Occupation": [
                    {
                        "value": "politician"
                    }
                ],
                "Nationality": [
                    {
                        "value": "United States of America",
                        "link": "http://www.wikidata.org/entity/Q30"
                    },
                    {
                        "value": "Great Britain",
                        "link": "http://www.wikidata.org/entity/Q161885"
                    }
                ],
                "Spouse": [
                    {
                        "value": "Martha Washington",
                        "link": "http://www.wikidata.org/entity/Q191789"
                    }
                ]
            }
        }
        actual = format_person(json_input)
        self.assertEqual(actual, expected)

    def test_format_book(self):
        """ Tests format_book """
        json_input = {
            "head": {
                "vars": [
                    "name",
                    "description",
                    "author",
                    "authorLabel",
                    "genreLabel",
                    "published"
                ]
            },
            "results": {
                "bindings": [
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "fantasy novel by J. K. Rowling"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Harry Potter and the Philosopher's Stone"
                        },
                        "author": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q34660"
                        },
                        "authorLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "J. K. Rowling"
                        },
                        "genreLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "adventure novel"
                        },
                        "published": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1997-06-26T00:00:00Z"
                        }
                    },
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "fantasy novel by J. K. Rowling"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Harry Potter and the Philosopher's Stone"
                        },
                        "author": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q34660"
                        },
                        "authorLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "J. K. Rowling"
                        },
                        "genreLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "young adult literature"
                        },
                        "published": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1997-06-26T00:00:00Z"
                        }
                    },
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "fantasy novel by J. K. Rowling"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Harry Potter and the Philosopher's Stone"
                        },
                        "author": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q34660"
                        },
                        "authorLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "J. K. Rowling"
                        },
                        "genreLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "speculative fiction novel"
                        },
                        "published": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1997-06-26T00:00:00Z"
                        }
                    },
                    {
                        "description": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "fantasy novel by J. K. Rowling"
                        },
                        "name": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "Harry Potter and the Philosopher's Stone"
                        },
                        "author": {
                            "type": "uri",
                            "value": "http://www.wikidata.org/entity/Q34660"
                        },
                        "authorLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "J. K. Rowling"
                        },
                        "genreLabel": {
                            "xml:lang": "en",
                            "type": "literal",
                            "value": "young adult novel"
                        },
                        "published": {
                            "datatype": "http://www.w3.org/2001/XMLSchema#dateTime",
                            "type": "literal",
                            "value": "1997-06-26T00:00:00Z"
                        }
                    }
                ]
            }
        }
        expected = {
            "title": "Harry Potter and the Philosopher's Stone",
            "subtitle": "fantasy novel by J. K. Rowling",
            "entries": {
                "Author": [
                    {
                        "value": "J. K. Rowling",
                        "link": "http://www.wikidata.org/entity/Q34660"
                    }
                ],
                "Genre": [
                    {
                        "value": "adventure novel"
                    },
                    {
                        "value": "young adult literature"
                    },
                    {
                        "value": "speculative fiction novel"
                    },
                    {
                        "value": "young adult novel"
                    }
                ],
                "Published": [
                    {
                        "value": "June 26, 1997"
                    }
                ]
            }
        }
        actual = format_book(json_input)
        self.assertEqual(actual, expected)

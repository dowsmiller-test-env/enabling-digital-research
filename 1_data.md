layout: page
title: "1. The Data"
permalink: /1_data

# 1. The Data
The data outputs of this project are intended to be used by researchers of all levels, from those with no knowledge of the underlying TEI-XML data, through to experienced users who nevertheless want to access the data in a format that enables cross-comparison.
You do not need to be able to run the processor in order to access the outputs. They can be found in the `tabular_data/output` folder, where there are two kinds:
1.	Collection: these are the data which have been extracted from the collection files, and so predominantly contain information about manuscripts and manuscript parts.
2.	Authority: these are the data which have been extracted from the authority files which accompany the collection, and so predominantly contain information about people, places, and organisations associated with the collections.

The data are presented in three formats:
1.	A single XLSX (Excel) file, containing tabs for each of the configured outputs. This is the recommended format, as the data in each tab are grouped into sections, with accompanying notes explaining the content of each column.
2.	A set of CSV files, each one corresponding to a tab in the XLSX output.
3.	A set of JSON files, each one corresponding to a tab in the XLSX output.

Details of the default contents of each tab of the Excel files (or individual CSV/JSON files) can be found below.

## Collection
### 00_overview
Each row of the output file corresponds to a manuscript unit, be that a part (`msPart`) or a whole MS (`msDesc`). The output file contains a variety of basic information about the unit in question, including details of its origin, provenance, acquisition, contents, codicology, palaeography, and binding, and a number of measurements.
### 01_records
Each row of the output file corresponds to an individual `additional` element within the collection data, and contains enhanced metadata about the object in question, as well as details of the record history, the availability of the object and any digital surrogates, and printed and digital resources associated with the object.
### 02_binding
Each row of the output file corresponds to an individual `binding` element or a `dimensions` element with `@type=“binding”`. This contains overview information about the object’s binding, as well as dating and measurement information.
### 03_measurements
Each row of the output file corresponds to an individual set of measurements for a manuscript unit, as encoded within either (or both) of `layout` and `extent` elements. This contains information about the manuscript part’s extent, as well as measurements and other details associated with rolls, fragments, leaves, columns, intercolumn widths, the written area, and ruling.
### 04_hands
Each row of the output file corresponds to an individual `handNote` element for a manuscript unit. This contains overview information about the hand in question, as well as details of any people associated with the hand, any locus information, details of dating, and palaeographic details.
### 05_contents
Each row of the output file corresponds to an individual work or part of a work contained within a manuscript unit in the collection. This contains locus and length information, alongside details of the work’s title subject, author, language, and paratext, as well as any bibliographic references associated with it in the collection file.
### 06_music
Each row of the output file corresponds to an individual description of musical notation encoded within a `musicNotation` element. This contains overview information about the notation in question, as well as locus and dimension information, and details of any people or bibliographic references associated with the notation.
### 07_decoration
Each row of the output file corresponds to an individual description of decoration encoded within a `decoNote` element. This contains overview information about the decoration in question, including its type, as well as locus and date information and details of any people, organisations, places, or bibliographic references associated with the decoration.
### 08_origins
Each row of the output file corresponds to an individual manuscript unit, and the information about its origins contained within the `origin` element (manuscript parts inherit data from their containing manuscript, should no other information be present). This contains overview information about the origin of the unit in question, as well as locus and date information, and details of any people, organisations, or bibliographic references associated with the manuscript unit’s origins.
### 09_additions
Each row of the output file corresponds to an individual description of additions to a given manuscript unit, as given within the `additions` element. This contains overview information about the addition in question, as well as locus information, and details of any people or bibliographic references associated with the addition.
### 10_provenance_acquisition	
Each row of the output file corresponds to an individual set of information given about the history of a manuscript unit, as contained within a `provenance` or `acquisition` element. This contains overview information about the historical detail in question, as well as date information, and details of any people, organisations, or places associated with the historical detail, with additional details given about former owners.
## Authority
### orgs
Each row of the output file corresponds to an organisation named within the authority file places.xml.
### persons
Each row of the output file corresponds to a person named within the authority file persons.xml.
### places
Each row of the output file corresponds to a place named within the authority file places.xml.
### works
Each row of the output file corresponds to a work named within the authority file works.xml.

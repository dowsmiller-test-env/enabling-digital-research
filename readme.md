# Tabular Data Extracted from the Medieval Manuscripts in Oxford Libraries Catalogue

This repository mirrors the [Bodleian TEI Manuscript Catalogue](https://github.com/bodleian/medieval-mss) in all aspects except for the `tabular_data` directory, which contains an experimental processor designed to extract specific data from the TEI files, and export them in tabular data to enable cross-comparison and increase accessibility.

You do not need to be able to run the processor in order to access the output data: these can be found in the `tabular_data/output` directory, and are currently being updated regularly as the catalogue develops. 

The processor is accompanied by an app which runs locally in a browser and enables users to merge files output by the processor, to suit diverse requirements for use of the data.

## Getting Started
See below for links to a user guide, which is intended to help you get started using the tabular versions of the Medieval Manuscripts in Oxford Libraries catalogue data, and to give you examples of what you can do with the data.
This guide consists of 6 different sections:

1.	The Data
2.	Worked examples using the spreadsheets
3.	Setting up the Column Merge app
4.	Worked examples using the Column Merge app
5.	Using the Processor
6.	Configuring the Processor

Before you get started, please read the following notes on the limitations on the quality and completeness of the data.

## Notes on Data Quality

The Bodleian’s Western medieval manuscript catalogues, for which this processor is primarily designed, remains a work in progress both in the encoding into TEI-XML of data which have already been recorded, and in the recording of new data. The absence of information regarding e.g. decoration or musical notation should therefore not be taken as an indication that no such features exist for a given manuscript, only that these data have not been recorded in the digital catalogues.

Similarly, many of the datapoints presented through the outputs of this processor are the work of previous generations of librarians and scholars who had cataloguing priorities and practices that are different to those of modern cataloguers. In particular, in previous cataloguing cycles, measurements have often been rounded to the nearest 5mm or quarter/eighth of an inch, and features such as decoration have been described using assessments of aesthetic and material quality (e.g. “Good border”), rather than through dispassionate descriptions of their form and contents.

Users should therefore be aware of these limitations when engaging with the outputs of this processor, whether using the default outputs or custom ones.

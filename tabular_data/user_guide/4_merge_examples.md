# 4. Worked Examples Using the Column Merge App (Intermediate)

## Example 1: Find all the IIIF manifest URIs for manuscripts containing musical notation.

Suppose you are interested in performing a digital analysis of a large corpus of musical manuscripts, and you therefore need to find those manuscripts with IIIF manifest URIs which also contain musical notation. This is not immediately possible with the default output data, since the IIIF manifest URIs are contained in 01_records, while the details of musical notation are predominantly included in 06_music. To combine the two sets of information, we can follow the steps below:

1.	With the Column Merge app running (see the steps above), navigate to http://127.0.0.1:5000/ in your web browser.
2.	Click/tap on ‘Select files’ and navigate to the `tabular_data/output/collection/csv` directory, where the CSV output files for the collection are stored.
3.	Select `01_records.csv` and `06_music.csv`, the two files we want to merge.
4.	Click/tap ‘Continue’, and wait for the files to process.
5.	On the next page (‘Select Columns to Merge’), we need to select the columns that we want to retain from each CSV file. The ‘Merge Key’ (the column used to combine the files) can stay as ‘metadata: part ID’, since this will correctly align the files based on their shared identifiers. In the left-hand column (‘01_records.csv’), tick the box labelled ‘surrogates: full iiif manifest’ to tell the app that you want to retain this column.
6.	In the right-hand column, select the columns from ‘overview: music’ through to ‘dimensions: unit’, to retain information that might be useful for a digital study of musical notation.
7.	Click/tap ‘Continue’.
8.	On the next page (‘Select Required Values’), we need to select the columns for which data must appear in a given row in order for that row to be included. Given that we’re only interested in manuscripts with a IIIF manifest file, tick ‘surrogates: full iiif manifest’ in the left-hand column.
9.	Also select ‘overview: music’ in the right-hand column, to select only those manuscripts for which details of musical notation have been included in the catalogue.
10.	Click/tap ‘Merge’.
11.	On the next page (‘Merged Data Preview’), you will see a preview of the merged table, with the merge key (in this case, the manuscript part ID) in the first column, followed by the IIIF manifests and then details of the musical notation.
12.	To download the data in either CSV or JSON format, click/tap on the appropriate button at the top of the page.

## Example 2: Find available WikiData references for people referenced as authors.

Suppose now that you are interested in connecting the data found in the MMOL catalogue about authors to other sources of linked open data, such as Wikidata, and therefore want to know their Wikidata references. This is not immediately possible with the default output data, since details of authors are predominantly included in 05_contents, while Wikidata references are stored in the ‘persons’ section of the authority output. To combine the two sets of information, we can follow the steps below:

1.	With the Column Merge app running (see the steps above), navigate to http://127.0.0.1:5000/ in your web browser.
2.	Click/tap on ‘Select files’ and navigate to the `tabular_data/output/collection/csv` directory, where the CSV output files for the collection are stored.
3.	Select `05_contents.csv`, the first of the two files that we want to merge.
4.	Click/tap on ‘Select files’ again, and navigate to the `tabular_data/output/authority/csv` directory, where the CSV output files for the authority data are stored.
5.	Select `persons.csv`, the second of the two files that we want to merge.
6.	Click/tap ‘Continue’, and wait for the files to process. `05_contents.csv` is a large file, so this may take some time.
7.	On the next page (‘Select Columns to Merge’), we need to select the columns that we want to retain from each CSV file. We want to combine the tables based on the identifiers associated with the authors, so change the ‘Merge Key’ value for `05_contents.csv` to ‘author: ID(s)’, and change the value for `persons.csv` to ‘identifiers: ID’.
8.	In the left-hand column, select ‘author: standard name(s)’, to include the author’s name.
9.	In the right-hand column, select ‘identifiers: URI (Wikidata)’ which is the Wikidata reference we want to associate with each author.
10.	Click/tap ‘Continue’.
11.	On the next page (‘Select Required Values’), we need to select the columns for which data must appear in a given row in order for that row to be included. This time, we can tick ‘Select all columns’ and ‘Exclude duplicates’, since we only want entries containing all three values, and there is no value in this case of retaining duplicate rows.
12.	Click/tap ‘Merge’.
13.	On the next page (‘Merged Data Preview’), you will see a preview of the merged table, with the merge key (in this case, the person identifier) in the first column, followed by the text associated with a given author, their name, and their Wikidata reference.
14.	To download the data in either CSV or JSON format, click/tap on the appropriate button at the top of the page.

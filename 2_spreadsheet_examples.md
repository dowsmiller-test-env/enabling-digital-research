# 2. Worked Examples using the Spreadsheets
Follow along with these worked examples to gain an idea of the sorts of research questions that the MMOL Tabular Data can help you answer.

The examples here are given for Excel for Mac version 16, and reflect the state of the tabular data at the time this guide was compiled (July 2025), so the exact process and your eventual results may differ from what you see here.

## Example 1: Cross-Comparison of Manuscript Contents

Question: What texts appear alongside the works of Catullus in the manuscripts catalogued in MMOL?

In order to answer this question, we need to narrow the data down to just those manuscripts containing the works of Catullus, so that we can look at the other authors that he appears alongside. This is relatively easy in spreadsheet format:

1.	Open ‘collection_data.xlsx’.
2.	In the ‘00_overview’ tab, navigate to the ‘contents’ section and find the ‘author(s) referenced’ column.
3.	Click/tap on the downwards facing arrow on the right hand side of the column heading, to open the Filter options.
4.	In the Search bar, enter ‘Catullus’.
5.	The only manuscripts visible should now be the relatively few containing works of Catullus.

By looking at the ‘author(s) referenced’ column, we are able to reach our conclusion. In the July 2025 version of the data, at least, Catullus’ work appears in 5 manuscripts alongside the work of Tibullus, once each alongside Ovid, Propertius, and Pseudo-Virgil, and twice on its own.

(To clear existing filters from one query to the next, go to the ‘Data’ menu, followed by ‘Clear Filters’.)

## Example 2: Quantitative Codicology

Question: Are the leaf heights of 15th-century paper manuscripts in the catalogue more standardised than those of 15th-century manuscripts on parchment? 

To answer this question, we need to narrow the data down in a more multi-dimensional way. We need to find the page heights of all the 15th-century paper manuscripts in the catalogue for which there are sufficient data, and then do the same for all the 15th-century parchment manuscripts. Here are the steps to follow:

1.	Open ‘collection_data.xlsx’.
2.	In the ‘00_overview’ tab, navigate to the ‘origin’ section and find the ‘not before’ column.
3.	Click/tap on the downwards facing arrow on the right hand side of the column heading, to open the Filter options.
4.	Since we’re only interested in the 15th century, use the number filtering options (‘Choose One’ on Mac) to select values that are greater than or equal to 1400.
5.	Navigate to the ‘not after’ column in the same section, and this time filter to select values that are less than or equal to 1500.
6.	Navigate to the ‘form’ column in the ‘codicology’ section, and open the Filter options.
7.	Untick all the options except for ‘codex’ (since we only want to look at whole manuscripts).
8.	Navigate to the ‘support’ column in the same section, and open the Filter options, selecting just ‘chart’ (=paper).
9.	Navigate to the ‘max height’ column in the ‘leaves’ section. This is the column we will use as our measurement, but you could add a column containing an average of the ‘max height’ and ‘min height’ columns if you so wished, and continue with those data.
10.	In the Filter options for this column, deselect blank cells (this is at the top of the list on Windows, and at the bottom of the list on Mac).
11.	To visualise the data, select the whole column by clicking/tapping on the column letters (‘BH’ in the July 2025 data), and then go to Excel’s ‘Insert’ tab.
12.	Selecting ‘Recommended Charts’ and then ‘Histogram’ should give you a quick and easy visualisation of the distribution of the leaf heights.
13.	Rename this chart as ‘15th-Century Paper MSS Leaf Heights’ or similar, and save a screenshot of the chart (since Excel updates charts as you change the Filter settings).
14.	We now have our data for paper manuscripts. To get the same for parchment manuscripts, simply leave the other Filter options unchanged and navigate back to the ‘support’ column in the ‘codicology’ section, and replace ‘chart’ with ‘perg’ (=parchment).
15.	Return to the ‘max height’ column in the ‘leaves’ section, and repeat steps 11–13 to produce the second chart.

By comparing the charts, we can therefore answer our question. The leaf heights of 15th-century parchment manuscripts in the MMOL catalogue appear roughly in line with a normal distribution, suggesting that their values coalesce around an average, but that this is not part of a standardised process. The paper manuscripts, meanwhile, appear to fit into two main categories of page height, suggesting certain standard paper sizes are common in the collection.

(To clear existing filters from one query to the next, go to the ‘Data’ menu, followed by ‘Clear Filters’.)

## Example 3: Quantitative Palaeography

Question: What are the 10 most common script types found in manuscripts catalogued in MMOL?

To answer this question, we need to produce counts of manuscripts according to their script type, using Excel’s Pivot Table function. Here are the steps to follow:

1.	Open ‘collection_data.xlsx’.
2.	In the ‘04_hands’ column, select all the data by going to Edit > Select All, or by pressing Command/Control + A.
3.	In the ‘Insert’ tab, select ‘Pivot Table’, and press ‘OK’.
4.	A new worksheet should appear containing a blank pivot table. In the ‘Field Name’ section of the ‘PivotTable Fields’ menu that should have appeared on the right, select ‘shelfmark’ and ‘script’.
5.	Drag ‘shelfmark’ from the ‘Rows’ into the ‘Values’ column, to gain a count of the manuscripts containing each script type.
6.	On the pivot table itself, click/tap on the downwards facing arrow on the right hand side of the ‘Row Labels’ column heading, to open the Filter options.
7.	In the Filter options, deselect blank cells (this is at the top of the list on Windows, and at the bottom of the list on Mac).
8.	Also in the Filter options, select ‘Count of shelfmark’ in the ‘Sort by:’ dropdown list, and then click ‘Descending’, to ensure that the most frequent scripts appear at the top of the list.
9.	To visualise the data, select any cell in the pivot table and then go to Excel’s ‘Insert’ tab. Selecting a 2D pie chart will allow you to show the data as the proportion of a whole, excluding the more unusual or highly specified script types.

By looking at this pie chart and at the pivot table, we can say that, with just over a quarter of examples, Northern Textualis is the most common script type given in the collection (as defined by Albert Derolez (2003), The Palaeography of Gothic Manuscript Books from the Twelfth to the Early Sixteenth Century). However, the limited volume of data available in the catalogue (1,997 entries as of July 2025) means that we must be cautious about drawing too many conclusions from these data about the whole catalogue.

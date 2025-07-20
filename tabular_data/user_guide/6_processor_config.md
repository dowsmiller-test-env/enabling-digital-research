# 6. Configuring the Processor (Advanced)

If you wish to customise the configuration files for your own purposes, you can do so by modifying the CSV files in the ‘config’ directory. This section of the guide contains information on the process of extraction, as well as what information is expected for both the ‘collection’ and the ‘authority’ configuration files.

## Processing Principles

Any .xml file found in the root directory of the repository will be treated as authority files, and will be assumed to contain information on entities named in the collection files, linked using UIDs. Any XML file found in the collection directory or its sub-directories will be treated as a file containing data about an individual manuscript unit.

All configuration files will be processed in alphabetical order by filename, and this is also the order in which the output tabs will appear in the output XLSX files. If you wish to modify this order, include numbers at the beginning of your config filenames.

Authority files will be processed before collection files, to ensure that the data required for any authority lookups have already been extracted.

## Authority Configuration Files

Any CSV file found in the tabular_data/config/authority directory will be treated as configuration files for authority output files.

For details of what the default configuration files contain, see the earlier section of the user guide.

Individual rows in the .csv configuration file will correspond to individual columns in the output file. All authority configuration files must begin with a column containing a unique identifier, in order for authority lookups to be possible.

In order for the data extraction to be successful, each .csv configuration file must have the following columns:

### section

A top-level heading to group different output columns together. Consecutive output columns with the same section heading will be grouped into a single section within the XLSX output. This field is optional, but advised.

### heading

A heading for the output column, within the previously designated section.	

### auth_file

The authority input file (without suffix) from which the data should be extracted.

### xpath

The XPath query that should be used to extract the data for the present output column. Every XPath query in a given authority file must return exactly the same number of values as any other, else the code will fail. `string()` and `string-join()` are good ways of forcing multiple (or zero-length) values to be returned as a single value. XPath up to and including version 3.0 is supported, with the exception of FLOWR loops and conditional (e.g. if/else) statements.

### separator

The string separator that should be used when the XPath returns multiple values but the code expects only one. The default values are as below, which can be modified or expanded in _global_config.py:
*	“default” (returns “; ” – this will also be used if a given separator field is empty or unrecognised)
*	“comma”
*	“semi-colon”
*	“space”
*	“empty” (no separator)

### format
The desired format of the data returned in the current column. The default values are as below. On the expectation that the input data may not always consistently meet the requirements of a given data format (not least the fact that Excel struggles with dates before 1900), data values which fail to strictly adhere to the chosen data format will usually be silently formatted as text.
*	“text” (formats as string)
*	“number” (formats as double)
*	“date” (formats as date if before 1950, else date-like string)
*	“boolean” (true/false)
*	“percentage” (formats decimal as percentage, rounded to two decimal places)

### comment

An optional comment explaining the output of the XPath query, which (if present) will be included as a note attached to the relevant column heading in the XLSX output file.

The authority configuration files result in output files in CSV and JSON format of the same name, as well as a combined XLSX file with tabs corresponding to each configuration file. These files are stored in the `tabular_data/output/authority` directory.

## Collection Configuration Files

Any CSV file found in the tabular_data/config/collection directory will be treated as configuration files for collection output files.

For details of what the default configuration files contain, see the earlier section of the user guide.

By default, all output files are configured to begin with columns containing comparable metadata such as shelfmark and the name of the collection file, to allow cross-comparison.

Individual rows in the .csv configuration file will correspond to individual columns in the output file. In order for the data extraction to be successful, each .csv configuration file must have the following columns:

### section

A top-level heading to group different output columns together. Consecutive output columns with the same section heading will be grouped into a single section within the .xlsx output. This field is optional, but advised.

### heading

A heading for the output column, within the previously designated section.	

### xpath

The XPath query that should be used to extract the data for the present output column. Every XPath query in a given authority file must return exactly the same number of values as any other, else the code will fail. `string()` and `string-join()` are good ways of forcing multiple (or zero-length) values to be returned as a single value. XPath up to and including version 3.0 is supported, with the exception of FLOWR loops and conditional (e.g. if/else) statements. If you wish to perform an ‘authority lookup’ and extract data from one of the authority output files, then this query must result in an identifier that corresponds with the identifier given in the first column of the relevant authority output file.

### auth_file

The name of the authority output file from which the data should be extracted, if you are performing an authority lookup. Else this can be left blank.

### auth_section

The top-level heading in the authority output file within which the desired lookup column can be found, if you are performing an authority lookup. This can be left blank if no authority lookup is being performed, or if the authority file has no section headings.

### auth_heading

The heading in the authority output file of the desired lookup column. This can be left blank if no authority lookup is being performed.

### separator

The string separator that should be used when the XPath returns multiple values but the code expects only one. The default values are as below, which can be modified or expanded in _global_config.py:
*	“default” (returns “; ” – this will also be used if a given separator field is empty or unrecognised)
*	“comma”
*	“semi-colon”
*	“space”
*	“empty” (no separator)

### format

The desired format of the data returned in the current column. The default values are as below. On the expectation that the input data may not always consistently meet the requirements of a given data format (not least the fact that Excel struggles with dates before 1900), data values which fail to strictly adhere to the chosen data format will usually be silently formatted as text.
*	“text” (formats as string)
*	“number” (formats as double)
*	“date” (formats as date if before 1950, else date-like string)
*	“boolean” (true/false)
*	“percentage” (formats decimal as percentage, rounded to two decimal places)

### comment

An optional comment explaining the output of the XPath query, which (if present) will be included as a note attached to the relevant column heading in the XLSX output file.

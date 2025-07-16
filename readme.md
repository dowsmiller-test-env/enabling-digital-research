## Tabular Data Extracted from the Medieval Manuscripts in Oxford Libraries Catalogue

This repository mirrors the [Bodleian TEI Manuscript Catalogue](https://github.com/bodleian/medieval-mss) in all aspects except for the `tabular_data` directory, which contains an experimental processor designed to extract specific data from the TEI files, and export them in tabular data to enable cross-comparison and increase accessibility.

You do not need to be able to run the processor in order to access the output data: these can be found in the `tabular_data/output` directory, and are currently being updated regularly as the catalogue develops. 

The processor is accompanied by an app which runs locally in a browser and enables users to merge files output by the processor, to suit diverse requirements for use of the data.

For information on how to run the processor and the app on your own system, see `processor_setup_instructions.txt` and `column_merge_setup_instructions.txt` in the `tabular_data` directory. For details of how to customise the processor to suit your requirements, see the `_read_me.txt` file in the `tabular_data/config` directory.

A full user guide is in preparation, and should be released soon.

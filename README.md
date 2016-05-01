##Tagging Engine 1.0.2
01 May 2016

###Description
A simple Tagging Engine in Python which takes a user-specified file and
returns the most common word, as well as listing the n-most common words
(where n is user-defined).

###Applications
Useful for highlighting top n words in a blog post (to create tags), or
reviewing the relevance of articles, web pages, etc. to a particular topic.

###Some problems to be ironed out:
* Program currently takes a text file with punctuation marks already stripped out, punctuation marks and other non-alpha characters currently returned as unique words;
* Words appearing both singular and plural currently returned as two unique words;
* Need to add error handling on user input of n (order).

###Further improvements to be made:
* User to specify whether Python/coding reserved words to be counted or excluded. Excluded words list for Python reserved words - when I tried (putting them in either single- or double-quotes) it returned a syntax error;
* Add ability to handle files with punctuation marks by stripping them out before splitting and counting words (at user request);
* Add ability to handle plurals and singulars as one word  (at user request);
* Add error-handling on user inpout of n (order);
* Add ability to handle file paths (file in location other than working directory);
* Add ability to save outputs to file (user to sepcify: restricted counts, full counts, or both).

###Future developments planned:
* Allow user to specify whether uploading simple text or html. If html, the program can use html tags (title, headers (h1, h2, etc.), strong or italic html tags to weight importance of text (either as words or phrases) more highly than normal, untagged/unformatted text. This will help make the program more useful if being used, for example, to auto-tag a Wordpress blog post;
* Review the text in pairs and/or triplets to identify significant phrases. User prompted to check/confirm if phrase is a significant phrase. User able to modify/overwrite significant phrase as required before appending to a list;
* The user can be prompted for a file path and filename where the significant phrases list can be saved. This can then be reloaded when using the program multiple times on multiple web pages/articles/etc;
* The same functionality can be used to test titles and headers for significant phrases.

This functionality will be useful for accelerated learning, and for rapid searching/reviewing of many web sites/pages/articles.

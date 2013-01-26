mklists
=======

Refreshes folders of plain-text lists in sync with your evolving rules

This will be a completely new reimplementation of the script previously known
as shuffle (1994), shawkle (2006), shawkle.py (2011), originally planned as a
project to incrementally improve shawkle.py under various names (listmunger,
puralista, ascilist).  

A frozen, stable, copy of shawkle is included in this project, for reference,
under the name shawkle-20130102.py, along with shawkle-alt-20130102.py, an 
alternative algorithm for a key part of the script.

How to use mklists quickly:
----------

Add mklists as an environment variable.

    $ alias mkdir='python /absolute/path/to/mklists.py'

Change to the directory for list making.

    $ cd /change/to/your/lists/folder

Run mklists

    $ mklists

Wish list:
----------

* Unit tests (most of the code is about testing data integrity anyway) - will start with these
* Configuration files in YAML
* Default configuration file generated when program first run
* Per-directory configuration not just of rules, but of all options (over-rideable with command-line switches)
* Object-oriented design (overkill?)
* Display process information at various levels of verbosity, or optionally write out event log
* Python distribution package
* Running mklists for the first time will generate a default configuration file, .mklistsrc

Tag line - which one conveys the idea best?
-------------------------------------------

* Tweaks folders of plain-text lists as you edit your evolving rules
* Rearranges folders of plain-text lists according to your evolving rules
* Refreshes folders of plain-text lists to match your evolving rules
* Synchs folders of plain-text lists to match your evolving rules
* Tweaks folders of plain-text lists in synch with evolving content rules

2012-12-26. First posted.
2013-01-20. Add test data, frozen reference copy of 

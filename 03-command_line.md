# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > `grep` Search a file for lines matching a regular expression.  
`cat` Write contents of a file to standard output.  
`find` Find files using file name.  
`diff` Compare two files for differences.  
`chmod` Change permissions for file or directory.  
`head` Prints first few lines of a file.  
`tail` Prints last 10 lines of a file.  
`touch` creates a new file with the argument name.  
`echo` Print string passed as an arg.  
`history` Previous commands.  

---

###Q2.  List Files in Unix   

What do the following commands do:    

> > `ls` Lists contents of directory.  
`ls -a` Includes hidden files starting with '.'  
`ls -l` Long format, shows file permissions.  
`ls -lh` Long human-readable format, with file size.  
`ls -lah` Long human readable format, hidden files.  
`ls -t` Sort by modified time/date, newest first.  
`ls -Glp` Long format, with '/' for directories, highlight directories.  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -R` List subdirectories as well.  
`ls -1` Displays list in a column (one entry per line).  
`ls -u` Displays by the file access time.  
`ls -g` Long format without owner name.  
`ls -o` long format without group name.  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs` is a shortcut to avoid using loops to run a command on a series of files.  
Example:  
`$ for i in *.txt; do [action] $i; done`  
is equivalent to  
`$ ls *.txt | xargs -i [action] {}`

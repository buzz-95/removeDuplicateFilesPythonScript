# removeDuplicateFilesPythonScript
This was just written with the purpose of removing Duplicate songs in multiple directories. One can use it for a variety of files by the way. <strong>Note that</strong> two files with the same name but different file contents ARE considered as the same file. Have fun. Contact 'darshanbari123@gmail.com' for any doubts or error reports. Thank you.<br>
The use is as follows: python3 py_repeat_songs_remover.py /path/to/directory <br>
Example: python3 py_repeat_songs_remover.py /home/silver_buzz/directory/ <br>
<pre><font color="#55FF55"><b>silver_buzz@PC</b></font>:<font color="#5555FF"><b>~</b></font>$ tree directory/
<font color="#5555FF"><b>directory/</b></font>
├── <font color="#5555FF"><b>anotherDirectory</b></font>
│   ├── a.txt
│   ├── b.txt
│   └── c.txt
├── a.txt
└── <font color="#5555FF"><b>whatAnotherDirectory</b></font>
    ├── b.txt
    └── d.txt

2 directories, 6 files
<font color="#55FF55"><b>silver_buzz@PC</b></font>:<font color="#5555FF"><b>~</b></font>$ python3 py_repeat_songs_remover.py /home/silver_buzz/directory/
Deleting /home/silver_buzz/directory/anotherDirectory/a.txt
Deleting /home/silver_buzz/directory/whatAnotherDirectory/b.txt
<font color="#55FF55"><b>silver_buzz@PC</b></font>:<font color="#5555FF"><b>~</b></font>$ tree directory/
<font color="#5555FF"><b>directory/</b></font>
├── <font color="#5555FF"><b>anotherDirectory</b></font>
│   ├── b.txt
│   └── c.txt
├── a.txt
└── <font color="#5555FF"><b>whatAnotherDirectory</b></font>
    └── d.txt

2 directories, 4 files
<font color="#55FF55"><b>silver_buzz@PC</b></font>:<font color="#5555FF"><b>~</b></font>$ 
</pre>
Hope you understood.

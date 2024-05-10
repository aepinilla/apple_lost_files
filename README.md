# Instructions

1. Get list of files in the directories you want to compare. Run once per directory.

   `ls -R <directory_path> > <file_name>.txt`
   
   For example:

   `ls -R /Users/aepinilla/Documents > local_documents.txt`
   `ls -R /Users/aepinilla/Documents > icloud_archive.txt`

2. Place the files inside the data folder.

3. Edit main.py with the path to the files generated with the terminal:

   `icloud_archive_path = "data/icloud-archive-13:04:2024.txt"`

   `local_documents_path = "data/local-documents-13:04:2024.txt"`

4. Run the script:

   `python main.py`

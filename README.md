# Book-Mark-Widget

#### Lightweight workflow helper tool to keep track of projects, locations and materials 

## App Layout

<img width="475" alt="bookmark" src="https://user-images.githubusercontent.com/74392848/123342456-d0df6000-d51d-11eb-997e-b96ffb357220.png">

</br>

My start to a simple yet helpful widget design to improve workflow and organization when it comes to personally managing your local development process.
Meant to be a quick and easy way to neatly store and grab useful info.
It's main purpose is to aid in keeping track of which projects you are working on from day to day and their specific details.
What you named them, which directory, filepath, what articles or documents are you pairing with them, 
what valuable snippets have you come across while probing the internet? This is all part of procedure and it can get rather messy, 
so the widget gives you a fast UI to a nice consolidated place to store and compartmentalize all these goodies.  
Run the widget to access any of these details when you need them. Makes picking up where you left off more manageable. 
Instead of juggling multiple current tasks in your head and keeping a mental roladex of all the things you
closed, opened, named, read, when and where you left them :thinking:(this could get tiring..) 
Why not automate this balancing act? 







## In Action -

## Save Button:

Fill in the text fields to make an entry in the Book Mark Widget. Saves the date and time along with the entry.

<img width="1010" alt="keepmainapp" src="https://user-images.githubusercontent.com/74392848/123342318-85c54d00-d51d-11eb-9e7d-1364be014d36.png">

## Set it and forget it!

</br>




## Urls Button:

Project names with links to associated reference materials.

<img width="1226" alt="keepurls" src="https://user-images.githubusercontent.com/74392848/123342509-e5bbf380-d51d-11eb-9c53-002a98eb42c9.png">

</br>

## Paste Box Button:

Spare place to jot down notes, copy/paste any useful info for safe keeping and future access.

<img width="899" alt="keeppastebox" src="https://user-images.githubusercontent.com/74392848/123342581-fec4a480-d51d-11eb-9986-31979b2faea8.png">

</br>

## Show List Button:

Simplify keeping track of the details. View all of your recently saved items.


<img width="1189" alt="keeplist" src="https://user-images.githubusercontent.com/74392848/123342614-1439ce80-d51e-11eb-80b3-51d48a843e6b.png">

</br>

## Find Button:

Search for individual project names in your recent work load. Get it's info!

<img width="966" alt="keepfindspot" src="https://user-images.githubusercontent.com/74392848/123342638-2156bd80-d51e-11eb-8674-aa9acbd6160a.png">

</br>

To run this app: 
Clone or download the zip file and open.

From terminal:

```
$ cd path/to/Book-Mark-Widget-master
```

start and activate virtual env to install packages

```
$ python3 -m venv venv
```


```
$ source venv/bin/activate
```

```
$ pip install -r requirements.txt
```

and run to start widget

```
$ python3 main.py
```

When program is run and entry is saved it will automatically generate 3 files within the Book-Mark-Widget directory.
* A 'marks.json' file where the main list is saved. (will be opened with your default text editor) 
* A 'urls.txt' file containing a list of (project names, urls) tuples.
* And a 'paste_box.txt' file that will open with the widget where you can manually add or delete it's contents.

There is only 2 packages to be installed, just for additional widget/buttons styles for mac os.
If you don't need these packages, comment them out. (You may have to modify some of the color names(?))
The other packages imported are built ins and tkinter should still accept the same commands.


















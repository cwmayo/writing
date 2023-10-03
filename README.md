# Writing
Works by Mayo's Creative Writing Students

Live website: [cwmayo.github.io/writing](https://cwmayo.github.io/writing/)

# How to create file
1. Make sure you are signed into your github account
2. Click the period key to enter the online editor
3. Create your .txt file by hovering over the sidebar on the left and pressing the new file button
4. Make sure your file is in the docs folder (If not, it won't properly deploy to the website)
5. Click on the branch icon on the side. You should see a list of the files you changed and a green "commit and push" button
6. Enter a commit message, which can be something simple like the name of your work
7. Click the "commit and push button" and your changes will be reflected in the website
8. It may take a couple minutes for the website to update, but your changes will deploy as quickly as they are processed

# Using YAML
At the top of your txt file, you may optionally put some modifiers that will change the display of the page.

```
---
author: your name
title: work title
keywords:
    - test
    - poem
    - best poem
---
```
These are the special keywords that will change elememts on the page. Author and title will change the author and title sections at the top of the page. Keywords will help provide words that will bring the work up when searched for. Author and title will also be included in the search keywords.

```
---
title: a title
author: your name
type: work type (poem, short story, etc.) 
keywords:
    - Some keyword
    - Another
text-style:
    - font-size: 20px
    - color: blue
---
```
The title, author, and type keywords are ones that you should put in every file. This will help to differentiate between different works as well as make the website more readable. Keywords are optional, but should be included if I ever decide to make a search feature for the website.

text-style will change the [CSS](https://www.w3schools.com/css/) of the 'p' tags. Changing the values there will change how the work text is displayed. You can read about it, or look here for some helpful ones.

```
font-size: 20px (Will change the font size to a 20 point font)

color: red (Will change the font color to whatever color specified)

text-indent: 20px (Will indent the first paragraph by 20 pixels, but you can also use % e.g. 3% would indent by 3 percent of the page width)

text-align: center (Will center the text, useful for poems)


```

Not everything has to be specified, default values will be entered for anything lacking in the YAML. Make sure that if you use the YAML, you include <b>both</b> the beginning '---' and end '---' or your file may be parsed incorrectly.

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
color: blue
font-size: 30px
---
```
These are a couple of examples of changing the display of the text itself. Color will change the color of the text, and font size will change the display font-size (px standing for pixels). There are other ones as well, but these serve for basic functionality. More functionality can also be provided in the future.

An example of a file could be...
```
---
author: name
color: purple
---

This is the purple text
```
Not everything has to be specified, default values will be entered for anything lacking in the YAML. Make sure that if you use the YAML, you include both the beginning '---' and end '---' or your file may be parsed incorrectly.

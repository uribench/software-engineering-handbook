# Guides Policy and Conventions

The contents of the `Guides` folder describe practical steps on performing a task. The style used 
for the guides is less restricting than the style of the [topics][1]. For instance, unlike with 
topics, a guide may be opinionated.

The contents of the `Guides` folder have to be organized **all** in one level of sub-folders (no 
deeper than that). The name of the sub-folders should be meaningful and hint on the common subject
that is grouping several underlying guides. Unlike with `Topics` sub-folders, here the names of the 
sub-folders are not used to generate titles. They are used only in the path of the reference links.

Inside each sub-folder, there is no particular entry point. Each one of the included guides may be 
referred directly from the handbook navigation tree or other guides, but not from topics.

In order to keep the guides pages short, with roughly no more than 100 lines, a guide can span over
multiple separate guides under the same subject sub-folder. Each guide should start with H1 title. 
The title of each guide should be the same as the name of the guide file.

Guides may refer to other guides, inside or outside of their group, and also to topics. Note that
when referring from a guide to a topic, the reference has to be to the topic's sub-folder and not to 
the respective `index.md` file or any other topic file. Referencing a folder will automatically 
render the underlying `index.md` that is converted automatically to `index.html` on the Handbook 
site (e.g., hosted as GitHUb pages). Note that the GitHub repository does not render the `index.md` 
automatically when its hosting folder is referred. Instead, the content of the referred folder is 
displayed as a list of links.

---

[1]: /Topics/README

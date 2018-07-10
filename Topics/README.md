# Topics Policy and Conventions

The contents of the `Topics` folder have to describe specific topics in an **opinion neutral** way 
(Wikepedia style). It **should not** include guides on how to perform a task (these belong to the
[guides][1] under the `Guides` folder).

The contents of the `Topics` folder have to be organized **all** in one level of sub-folders (no 
deeper than that). The name of the sub-folders should carry the title of the topic.

Inside each sub-folder, there should be an `index.md` file. This file will be the entry point of 
that topic. The title of the `index.md` file should be similar to the name of the hosting sub-folder.

In order to keep the topics pages short, with roughly no more than 100 lines, external Markdown 
files can be placed next to the respective `index.md` file under the same parent sub-folder. 

These satellite files should be referred only from the `index.md` file. They should start with H1 
title. Only the `index.md` file may be referred directly from the handbook navigation tree or guides.

Topics other than those in `index.md` should not refer back to their main `index.md`. Topics also 
should not refer to guides.

---

[1]: /Guides/README


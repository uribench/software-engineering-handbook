# Software Engineering Handbook


The contents of this repository is used to dynamically build the [Software Engineering Handbook][1] 
site. 

The main two data elements in this repository are:

- **Authored content** that is accessible to the end user from the handbook navigation tree 
- **Configuration data files** to construct the handbook navigation tree

All the authored content is placed under the `Guides/` and `Topics/` directories.
All the configuration files are placed under the `config/` directory. 
The resulting handbook navigation tree, which is created dynamically using the above two main data 
elements, is placed under the `Handbook/` directory.

On the differences between the contents of `Guides/` and `Topics/` see their respective README files.

Contributors are invited to propose additions and improvements to any of these two elements.

# Structure of the Repository

```
software-engineering-handbook/
├──.git/                                        local Git repository. created automatically
├──_index/                                      created automatically by madness for the search engine
├──config/                                      main folder for configuration files
|  ├──metadata/                                 metadata for the template file of navigation index.md files
|  |  ├──<metadata-configuration-yml-files>     metdata files with optional contents expected by the template
|  |  └──README.md                              metdata files description for contributors
|  ├──navigation/                               main navigation configuration folder for the handbook tree
|  |  ├──<navigation-configuration-yml-files>   handbook tree navigation configuration files starting from root.yml
|  |  └──README.md                              navigation configuration file description for contributors
|  └──templates/                                main folder for templates
|     └──index-template.j2                      Jinja2 template file for navigation index.md files
├──Guides/                                      root of the contributed custom topics
|  ├──<guides-subjects>/                        one or more folders for grouping subjects of related guides
|  |  └──<guides-markdown-files>                markdown files related to the parent guide subject
|  ├──index.md                                  "Internal Folder" message when rendered by GitHub pages
|  └──README.md                                 policy and conventions for use on GitHub repository
├──Handbook/                                    volatile handbook navigation tree. created automatically
|  ├──<first-level-handbook-subject>/           zero or more children folders for the hosting folder
|  |  ├──<second-level-handbook-subjects>/      zero or more children folders for the hosting folder
|  |  └──index.md                               current level index file with next level navigation links
|  └──index.md                                  root level index file with next level navigation links
├──images/                                      common media resources folder
├──Topics/                                      root of the contributed custom topics
|  ├──<topics-subjects>/                        one or more folders for grouping subjects of related topics
|  |  └──<topic-subject-index-markdown-file>    main index.md file for the parent topic subject
|  |  └──<guides-markdown-files>                sub-topics markdown files for the parent topic subject
|  ├──index.md                                  "Internal Folder" message when rendered by GitHub pages
|  └──README.md                                 policy and conventions for use on GitHub repository
├──.gitignore                                   list of files and directory to exclude from the Git repository
├──.madness.yml                                 default options and arguments for madness
├──_config.yml                                  configuration for GitHub (e.g., exclude files from MD to HTML)
├──CNAME                                        canonical name record for the domain to be used by GitHub pages
├──CODE_OF_CONDUCT.md
├──CONTRIBUTING.md
├──index.md                                     get priority over README.md on GitHub pages (becomes index.html)
├──LICENSE.md
├──README.md                                    becomes index.html on GitHub pages when index.md is absent
└──TOC.md                                       automatically generated from scanning the Handbook tree
```

# Key Concepts and Principles

The `Handbook/` directory hierarchy represents an instance of a handbook, which is created 
automatically based on the `*.yml` configuration files in config/navigation/ directory. The starting
point for the navigation tree configuration is the `root.yml` file.

See the `config/navigation/` [README][2] file for more information on the structure of the navigation 
configuration files.

The idea is to isolate the actual content of the handbook, given under `Guides/` and `Topics/` 
directories, from the navigation experience. This makes a robust and easily maintained repository, 
which supports relatively easy changes to the handbook structure and the navigation experiences.

The Handbook tree hierarchy includes directories and index.md files. All the directories under
the `Handbook/` directory have capitalized names with spaces ('Humanized' style), which represent 
the exact names of the Software Engineering Handbook chapters and sections.

We distinguish between **intermediate Handbook directories** (i.e., directories having one or more 
child directories) and **terminal Handbook directories** (i.e., directories having no child 
directories).

Each 'intermediate Handbook directory' contains an `index.md` file that includes, among other 
optional parts, a contents list pointing to the child directories of the hosting directory (i.e., 
next level of the Handbook directory hierarchy).

Each 'terminal Handbook directory' also contains an `index.md` file pointing to one or more guides or 
topics that are relevant to the hosting directory (i.e., in the context of the entire navigation 
path leading from the Handbook root to the hosting directory).

See the `config/metadata/` [README][3] file for more information on the structure of the navigation 
`index.md` files and on how they are composed automatically using metadata and Jinja2 template.

The entire content of the `Handbook/` directory (i.e., directory hierarchy and all the index.md files)
is automatically generated and maintained by the automation scripts in the [tools repository][4],
based on the configuration files under the `config/` directory.

### Note on the use of README.md and index.md files

`REAME.md` files are intended for *contributors* and are rendered by default as `index.html` by 
**GitHub repository** site.

However, `index.md` files are intended for the *end users* visiting the 
[Software Engineering Handbook][1] site. These files get priority by **GitHub pages** over 
neighboring `README.md` files when translating them to `index.html` files. GitHub pages is responsible 
for translating all the Markdown files in the repository and exporting them as static html files to 
a standalone web site.

---

[1]: http://software-engineering-handbook.com/
[2]: /config/navigation/README.md
[3]: /config/metadata/README.md
[4]: https://github.com/uribench/software-engineering-handbook-tools


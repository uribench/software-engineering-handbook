# Software Engineering Handbook

The contents of this repository is used to dynamically build the [Software Engineering Handbook][1] 
site. 

The main two data elements in this repository are:

- **Authored content** that is accessible to the end user from the handbook navigation tree 
- **Configuration data files** to construct the handbook navigation tree

Contributors are invited to propose additions and improvements to any of these 
two elements following the [contributing guidelines](about/CONTRIBUTING.md).

## Structure of the Repository

### Main Directories

```
software-engineering-handbook/
├──config/                                      main directory for the configuration files
├──Guides/                                      root of the authored contents for guides
├──Topics/                                      root of the authored contents for topics
└──Handbook/                                    handbook navigation tree. created automatically
```

All the authored content is placed under the [`Guides`](Guides) and [`Topics`](Topics) directories.
All the configuration files are placed under the [`config`](config) directory. 
The resulting handbook navigation tree, which is created dynamically using the authored content and 
configuration files, is placed under the [`Handbook`](Handbook) directory.

On the differences between the contents of `Guides` and `Topics` see their respective README files.

### Comprehensive Structure

```
software-engineering-handbook/
├──about/                                       directory for contribution instructions
├──config/                                      main directory for the configuration files
|  ├──metadata/                                 metadata for the template file of navigation index.md files
|  |  ├──<metadata-configuration-yml-files>     metadata files with optional contents expected by the template
|  |  └──README.md                              metadata files description for contributors
|  ├──navigation/                               main navigation configuration folder for the handbook tree
|  |  ├──<navigation-configuration-yml-files>   handbook tree navigation configuration files starting from root.yml
|  |  └──README.md                              navigation configuration file description for contributors
|  └──templates/                                main folder for templates
|     └──index-template.j2                      Jinja2 template file for navigation index.md files
├──Guides/                                      root of the authored contents for guides
|  ├──<guides-subjects>/                        one or more folders for grouping subjects of related guides
|  |  └──<guides-markdown-files>                markdown files related to the parent guide subject
|  ├──index.md                                  "Internal Folder" message when rendered by GitHub Pages
|  └──README.md                                 policy and conventions for use on GitHub repository
├──Handbook/                                    handbook navigation tree. created automatically
|  ├──<first-level-handbook-subject>/           zero or more children folders for the hosting folder
|  |  ├──<second-level-handbook-subjects>/      zero or more children folders for the hosting folder
|  |  └──index.md                               current level index file with next level navigation links
|  └──index.md                                  root level index file with next level navigation links
├──images/                                      common media resources folder
├──Topics/                                      root of the authored contents for topics
|  ├──<topics-subjects>/                        one or more folders for grouping subjects of related topics
|  |  └──<topic-subject-index-markdown-file>    main index.md file for the parent topic subject
|  |  └──<guides-markdown-files>                sub-topics markdown files for the parent topic subject
|  ├──index.md                                  "Internal Folder" message when rendered by GitHub Pages
|  └──README.md                                 policy and conventions for use on GitHub repository
├──.madness.yml                                 default options and arguments for madness
├──_config.yml                                  Jekyll configuration
├──CNAME                                        canonical name record for the domain to be used by GitHub Pages
├──index.md                                     gets priority over README.md on GitHub Pages
└──README.md                                    this README file for contributors
```

## Key Concepts and Principles

The `Handbook` directory hierarchy represents an instance of a handbook, which is created 
automatically based on the `*.yml` configuration files in `config/navigation` directory. The starting
point for the navigation tree configuration is the [`root.yml`](config/navigation/root.yml) file.

See the `config/navigation` [README][2] file for more information on the structure of the navigation 
configuration files.

The idea is to isolate the actual content of the handbook, given under `Guides` and `Topics` 
directories, from the navigation experience. This makes a robust and easily maintained repository, 
which supports relatively easy changes to the handbook structure and the navigation experiences.

The Handbook tree hierarchy includes directories and index.md files. All the directories under
the `Handbook` directory have capitalized names with spaces ('Humanized' style), which represent 
the exact names of the Software Engineering Handbook chapters and sections.

All the directories of the Handbook tree have each an `index.md` file that is generated automatically
when the Handbook tree is built. The `index.md` files include, among other optional parts, a 
contents list pointing to the children directories of the hosting directory (i.e., next level of the 
Handbook tree hierarchy). They also include optional references to guides and topics that are 
relevant to the handbook subject represented by the hosting directory.

See the `config/metadata` [README][3] file for more information on the structure of the navigation 
`index.md` files and on how they are composed automatically using metadata and Jinja2 template.

The entire content of the `Handbook` directory (i.e., directory hierarchy and all the index.md files)
is automatically generated and maintained by the automation scripts in the [tools repository][4],
based on the configuration files under the `config` directory.

### Note on the use of README.md and index.md files

`README.md` files are intended for *contributors*, while `index.md` files are intended for the 
*end users* visiting the [Software Engineering Handbook][1] site. 

**GitHub repository** renders the `README.md` files by default. However, the `index.md` files get 
priority by [**GitHub Pages**][5] over neighboring `README.md` files.

---

[1]: http://software-engineering-handbook.com/
[2]: /config/navigation/README.md
[3]: /config/metadata/README.md
[4]: https://github.com/uribench/software-engineering-handbook-tools
[5]: https://pages.github.com/


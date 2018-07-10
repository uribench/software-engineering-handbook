# Metadata Configuration Files

The optional metadata configuration files are used to compose the `index.md` files for each directory
in the navigation tree. The composition of the `index.md` files is done using Jinja2 template engine
with a custom [template file](/config/templates/index-template.j2).

All the metadata configuration files are placed directly under `/config/metadata` directory without 
additional grouping directories.

There are two types of index.md files:
- Non-leaf index files - hosted by non-leaf directories
- Leaf index files - hosted by tree leaf directories

From the engine generating the above mentioned index.md files, there is no difference between the
two types.

## Anatomy of Index Files

Index files are composed of the following parts:
- Title - mandatory. taken from the navigation configuration (e.g., root.yml).
- Introduction - optional. taken from metadata.
- Contents - mandatory. exists only in non-leaf index files. taken from the navigation configuration.
- Guides - optional. taken from metadata.
- Topics - optional. taken from metadata.

### Title

The name of the hosting directory. A mandatory part. It is taken automatically from the navigation 
tree configuration file and not from metadata.

### Introduction

Free text providing an introduction to the subject of the hosting directory. An optional part. 
Markdown is allowed in the introduction. It will be included in the respective `index.md` file as-is.
It is provided by a metadata file associated with the hosting directory.

YAML item type: dictionary
Key: intro
Value: text with optional Markdown syntax

Example:

```yml
intro: |
  Vagrant is an open source wrapper around a Virtual Machine provider, such as Oracle's 
  VirtualBox. It makes it easy to create and run a Virtual Machine (VM) from the command line.
```

### Contents

List of the next navigation level. Equal to the names of the children directories of the hosting 
directory (siblings of the index file). It is taken automatically from the navigation tree 
configuration file and not from metadata. A mandatory part that exists only in non-leaf index files.

### Guides

List of references to guides relevant to the subject of the hosting directory. An optional part. 
It is provided by a metadata file associated with the hosting directory.

YAML item type: dictionary
Key: guides
Value: list of links relative to the `/Guides` directory

Example:

```yml
guides:
  - Vagrant/Vagrant Overview
  - Vagrant/Vagrant Installation
  - Vagrant/Getting Started with Vagrant
  - Vagrant/Known Issues
```

Notes: 
1. The guides under the `/Guides` directory are grouped under one-level of grouping directories. 
   In the above example, the grouping directory is `Vagrant`.
   See ['Guides Policy and Conventions'][1] for details.
2. The links should be without leading or trailing `'/'`
3. No Markdown syntax is allowed

### Topics

List of references to topics relevant to the subject of the hosting directory. An optional part. 
It is provided by a metadata file associated with the hosting directory.

YAML item type: dictionary
Key: topics
Value: list of links relative to the `/Topics` directory

Example:

```yml
topics:
  - SSH Protocol
```

Restrictions: 
1. The guides under the `/Topics` directory are grouped under one-level of grouping directories.
   See ['Topics Policy and Conventions'][2] for details.
2. The links should be without leading or trailing `'/'`
3. No Markdown syntax is allowed

## Metadata File Naming Principles

Metadata files are associated 1-1 with directories in the navigation tree.
By default, their name is a "slagified" version of the 'Humanized' (i.e., title case with spaces)
name of the associated directory as defined by the navigation tree configuration file (e.g., root.yml)

For instance, a directory called `Vagrant and VirtualBox` will be associated by default with an 
optional metadata file called `vagrant-and-virtualbox.yml`

The optional argument `@id=<unique-id-value>` of any node in the navigation tree configuration file 
can be used to specify a custom id of the associated navigation node. When used, the respective 
metadata filename will be `<unique-id-value>.yml`  

## Metadata File Example

The following example is taken from `/config/metadata/vagrant-and-virtualbox.yml`.

```yml
intro: |
  Vagrant is an open source wrapper around a Virtual Machine provider, such as Oracle's 
  VirtualBox. It makes it easy to create and run a Virtual Machine (VM) from the command line.

guides:
  - Vagrant/Vagrant Overview
  - Vagrant/Vagrant Installation
  - Vagrant/Getting Started with Vagrant
  - Vagrant/Known Issues
```

---

[1]: /Guides/README
[2]: /Topics/README


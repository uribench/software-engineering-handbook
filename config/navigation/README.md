# Navigation Configuration Files

## Main Navigation Configuration File

The entry point of the navigation configuration is the `root.yml`.

It describes a nested data structure representing the navigation tree.

Following is a simple example of `root.yml`:

```yml
- Root:
  - L1
  - L2:
    - L2.1
    - L2.2
  - L3:
    - L3.1
    - L3.2:
      - L3.2.1
    - L3.3:
      - L3.3.1
      - L3.3.2
```

After loading the above YAML file into Python the data structure is as follows:

```python
{'Root': ['L1', {'L2': ['L2.1', 'L2.2']}, {'L3': ['L3.1', {'L3.2': ['L3.2.1']}, {'L3.3': ['L3.3.1', 'L3.3.2']}]}]}
```

Typically, the top most tree is represented by a one-item dictionary, in which:

- the 'key' is a string (root name followed by optional arguments)
- the 'value' is a list of root's children trees

In this example, the root name is 'Root' and its child trees ('forest') represented by the following 
list:

```python
['L1', {'L2': ['L2.1', 'L2.2']}, {'L3': ['L3.1', {'L3.2': ['L3.2.1']}, {'L3.3': ['L3.3.1', 'L3.3.2']}]}]
```

In general, a tree (or a sub-tree) from a given path onward can be represented by one of the 
following two possibilities:
        1. one-item dictionary representing a 'non-leaf directory' (having children):
            - the 'key' is a string (root name followed by optional arguments)
            - the 'value' is a list of root's children trees
        2. string representing a 'leaf directory' (having no children):
            - root name followed by optional arguments

If for instance we look at 'L3' as the root of the following sub-tree:

```python
{'L3': ['L3.1', {'L3.2': ['L3.2.1']}, {'L3.3': ['L3.3.1', 'L3.3.2']}]}
```
We can see the the child trees of 'L3' are:

```python
['L3.1', {'L3.2': ['L3.2.1']}, {'L3.3': ['L3.3.1', 'L3.3.2']}]
```

The sub-tree rooted by 'L3.3' is represented by:

```python
{'L3.3': ['L3.3.1', 'L3.3.2']}
```

and its children are a simple list:

```python
['L3.3.1', 'L3.3.2']
```

Nevertheless, 'L1' for instance, is one of the sub-trees of 'Root'. It is a simple string because
it is a leaf-directory with no children.

## Navigation Node Arguments

A navigation node including a directory name ('Humanized' style) followed by optional space 
separated arguments as tags, in any order, having each the following syntax:
[<tag-marker><key>[=<value>]]
        
where,
    <tag-marker> is @
    key is one of the following keywords:
        id          its value is a unique 'slag' string representing the node
        include     its value is a name of an external navigation file to be included
        stop        a flag indicating not to create a link for the node (i.e., forcing a stub)

Tags examples:

1. @stop
2. @include
3. @include=development
4. @id
5. @id=vagrant-and-virtualbox
6. @id=vagrant-and-virtualbox @stop
7. @stop @include=include-file
8. @id=vagrant-and-virtualbox @include=include-file @stop

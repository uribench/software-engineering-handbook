# Navigation Configuration Files

Following is a simple example of `root.yml`:

```yml
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
navigation = ['L1', {'L2': ['L2.1', 'L2.2']}, {'L3': ['L3.1', {'L3.2': ['L3.2.1']}, {'L3.3': ['L3.3.1', 'L3.3.2']}]}]
```

In this example, `navigation` is a list of 3 items (i.e., `'L1'` is a string, `'L2'` and `'L3'` are
one-item `dictionary` each).

The `key` of the one-item `dictionary` is a `string`, the `value` repeats the 
overall pattern of `navigation` recursively.

The term `nextLevels` of a node at any level refers to the recursive pattern of `navigation`.  
For instance, the `nextLevels` of `'L3'` is the following nested data structure:

```python
['L3.1', {'L3.2': ['L3.2.1']}, {'L3.3': ['L3.3.1', 'L3.3.2']}]
```

The term `children` of a node at any level refers to the immediate children of that node.
For instance, the children of `'L3'` are:

```python
['L3.1', 'L3.2', 'L3.3']
```
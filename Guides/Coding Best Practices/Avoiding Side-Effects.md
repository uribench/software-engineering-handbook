# Avoid Side-Effects When Mutating a Common Object

This brief article addresses a problem that is hard to identify with common tests that are not targeted to identify mutation side-effects. The subject is presented here as a coding challenge with the following sections:

- [Challenge](#challenge)
- [Solution Summary](#solution-summary)
- [Problem Definition](#problem-definition)
- [Possible Solutions](#possible-solutions)

## Challenge

Can you correct the code in `decoder_faulty.js`?

Visit [this online repl][3] to interact with the faulty code and minimally modify it to pass all the given tests.

## Solution Summary

The solution is to replace the following lines of `decoder_faulty.js`:

```javascript
  let _words = words;
  let _keys = keys;
```

with the following lines:

```javascript
  // Arrays are passed by reference. Use local clones to keep them unchanged.
  let _words = words.slice();
  let _keys = keys.slice();
```

## Problem Definition

Objects (not simple primitive types), such as arrays, are passed by reference to functions in JavaScript.

When a function uses mutating operations on received objects, such as shift() and splice(), it may cause side-effects. Others attempting to use the original object may not be aware of such changes.

Example:

Let's say we have a function called `decode()` that receives an array, and it uses `shift()` operation on that array.

After the first call to that function the array is changed by that function. Consecutive calls to the same function, or other functions, with the same parameters will be affected by the mutations of the passed parameters done by the preceding call.

This may affect tests for instance, when that passed array is attempted to be used as-is multiple times.

## Possible Solutions

Following are two possible solutions:

1. [Reload the imported mutable module](#reload-the-module)
2. [Create a local clone of the passed mutable object](#create-a-local-clone)

Note:

In ES6, variables created by `let` are mutable, while variables created by `const` are immutable. It may be tempting to use that as a solution to the above problem. However, if a constant refers to an object, it will always refer to that object, but the object itself can still be changed (if it is mutable). In other words, the reference (i.e., the address) may be protected from mutability by the 'const' keyword, but the target object remains mutable.

### Reload the Module

If the array in the above example is required (imported), it still will not help getting a fresh copy after it was modified by the function in the above example. This is because [modules are cached after the first time they are loaded][1]. The respective cache has to be explicitly deleted in order to get a fresh copy of the imported module, such as in the following example:

```javascript
  let secret_module = '../src/secrets/secret_1'

  delete require.cache[require.resolve(secret_module)]
  var secret = require(secret_module);

```

### Create a Local Clone

A more general solution is to work on a local clone of the passed object in the receiving function. There are [several ways][2] to clone an array. One simple approach is using `slice()` method as follows:

```javascript
  let _arr = arr.slice();
```

The `slice` method is for slicing part of the array. It is non-destructive since it will return some part of the target array without changing the original. When the `slice` method is called without specifying the start and end of the requested sliced array, or if only the start is specified by 0, then the whole array will be sliced. Meaning, a full copy of the original array will be returned.

---

[1]: https://stackoverflow.com/questions/9210542/node-js-require-cache-possible-to-invalidate
[2]: https://stackoverflow.com/questions/7486085/copy-array-by-value
[3]: https://repl.it/@handbook/crack-the-code-bothell

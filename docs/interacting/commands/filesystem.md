# Filesystem Commands

Available commands:

- [filesystem.open](#open)
- [filesystem.exists](#exists)
- [filesystem.list](#list)
- [filesystem.mkdir](#mkdir)
- [filesystem.remove](#remove)
- [filesystem.move](#move)
- [filesystem.chmod](#chmod)
- [filesystem.chown](#chown)
- [filesystem.read](#read)
- [filesystem.write](#write)
- [filesystem.close](#close)
- [filesystem.upload](#upload)
- [filesystem.download](#download)
- [filesystem.upload_file](#upload_file)
- [filesystem.download_file](#download_file)


<a id="open"></a>
## filesystem.open

Opens a file on the node.

Arguments:
```javascript
{
  'file': {file},
  'mode': {mode},
  'perm': {perm}
}
```

Values:
- **file**: File path to open
- **mode**: One of the following modes:
  - 'r' read only
  - 'w' write only (truncate)
  - '+' read/write
  - 'x' create if not exist
  - 'a' append


<a id="exists"></a>
## filesystem.exists

Check if path exists.

Arguments:
```javascript
{
  'path': {path}
}
```


<a id="list"></a>
## filesystem.list

List all entries in a given directory.

Arguments:
```javascript
{
  'path': {path}
}
```


<a id="mkdir"></a>
## filesystem.mkdir

Creates a new directory, functions as `mkdir -p path`.

Arguments:
```javascript
{
  'path': {path}
}
```


<a id="remove"></a>
## filesystem.remove

Removes a path (recursively).

Arguments:
```javascript
{
  'path': {path}
}
```


<a id="move"></a>
## filesystem.move

Move a path to destination.

Arguments:
```javascript
{
  'path': {path},
  'destination': destination
}
```


<a id="chmod"></a>
## filesystem.chmod

Changes permission of a file or directory.

Arguments:
```javascript
{
  'path': {path},
  'mode': {mode},
  'recursive': {recursive}
}
```

<a id="chown"></a>
## filesystem.chown

Changes the owner of a file or directory.

Arguments:
```javascript
{
  'path': {path},
  'user': {username},
  'group': {group},
  'recursive': {recursive}
}
```


<a id="read"></a>
## filesystem.read

Reads a block from the given file descriptor.

Arguments:
```javascript
{
  'fd': {fd}
}
```


<a id="write"></a>
## filesystem.write

Writes a block of bytes to an open file descriptor (that is open with one of the writing modes).

Arguments:
```javascript
{
  'fd': {fd},
  'bytes': {bytes}
}
```


<a id="close"></a>
## filesystem.close

Closes a file.

Arguments:
```javascript
{
  'fd': {fd}
}
```


<a id="upload"></a>
## filesystem.upload

Uploads a file.

Arguments:
```javascript
{
  'remote': {remote},
  'reader': {reader},
}
```

<a id="download"></a>
## filesystem.download

Downloads a file.

Arguments:
```javascript
{
  'remote': {remote},
  'writer': {writer},
}
```


<a id="upload_file"></a>
## filesystem.upload_file

Uploads a file.

Arguments:
```javascript
{
  'remote': {remote},
  'local': {local},
}
```


<a id="download_file"></a>
## filesystem.download_file

Downloads a file.

Arguments:
```javascript
{
  'remote': {remote},
  'local': {local},
}
```

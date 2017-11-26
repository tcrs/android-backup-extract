# Extract a `tar` from an `adb backup` file

Backup file goes into stdin, tar file comes out on stdout.

## Limitations

 - Does not support encrypted backups (pull requests welcome!)
 - Does not support uncompressed backups (not sure how to create these?)

## Examples

To view the contents of a backup

```
./extract.py < backup | tar -tv
```

To extract all files from a backup

```
./extract.py < backup | tar -x
```

# Further info

[Details of backup file structure](https://android.stackexchange.com/questions/23357/is-there-a-way-to-look-inside-and-modify-an-adb-backup-created-file)
[Further Details](https://nelenkov.blogspot.co.uk/2012/06/unpacking-android-backups.html) - could be used as a reference to implement backup decryption

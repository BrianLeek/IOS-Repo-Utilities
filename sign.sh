#!/bin/bash
gpg --list-secret-keys
while true; do
	read -p 'Key ID: ' keyid
if [[ "$keyid"  != "" ]]
then
	echo $keyid
	break
fi
done

gpg -abs -u $keyid -o Release.gpg Release
gpg -abs -u $keyid --clearsign -o InRelease Release

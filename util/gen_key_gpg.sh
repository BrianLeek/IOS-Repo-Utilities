#!/bin/bash
gpg --list-secret-keys
while true; do
	read -p 'Key ID: ' keyid
if [[ "$keyid"  != "" ]]
then
	echo "Creating key.gpg with $keyid ..."
	break
fi
done

gpg --export $keyid -o key.gpg
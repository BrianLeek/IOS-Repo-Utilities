#!/bin/bash
gpg --list-secret-keys
echo ""
echo "Please enter your key ID again, this step will create a key.gpg file."
while true; do
	read -p 'Key ID: ' keyid
if [[ "$keyid"  != "" ]]
then
	echo "Creating key.gpg with $keyid ..."
	break
fi
done

mkdir -p "keyring"
mkdir -p "keyring/DEBIAN/"
mkdir -p "keyring/etc/apt/trusted.gpg.d/"

gpg --export $keyid > keyring/etc/apt/trusted.gpg.d/key.gpg

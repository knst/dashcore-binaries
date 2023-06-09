
cd $VERSION

mkdir debug
mv debug *debug*

mkdir unsigned
mv unsigned *unsigned*

sha256sum * > SHA256SUMS
for f in dashcore-*; do gpg --detach-sign --armour $f; done
gpg --clear-sign SHA256SUMS
rm SHA256SUMS

cd debug
sha256sum * > SHA256SUMS
for f in dashcore*; do gpg --detach-sign --armour $f; done
gpg --clear-sign SHA256SUMS
rm SHA256SUMS

cd ../unsigned

sha256sum * > SHA256SUMS
for f in dashcore*; do gpg --detach-sign --armour $f; done
gpg --clear-sign SHA256SUMS
rm SHA256SUMS

cd ..

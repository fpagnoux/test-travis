version=`cat ./version`
git tag $version
git push --tags
echo "Releasing"

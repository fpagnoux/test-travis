version=`python setup.py --version`
eval "$(ssh-agent -s)" #start the ssh agent
chmod 400 ./id_travis-tests
ssh-add ./id_travis-tests
git remote set-url origin git@github.com:fpagnoux/test-travis.git
git tag $version
git push --tags

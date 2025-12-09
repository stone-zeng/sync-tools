REPO=$1
REPO_NAME=$(basename "$REPO" .git)

# Clone or update the mirrored repository
if [ -d "$REPO_NAME.git" ]; then
    cd "$REPO_NAME.git"
    git remote update
    cd ..
else
    git clone --mirror "https://github.com/$REPO.git"
fi

# Remove pull request refs to reduce size
cd $REPO_NAME.git
git for-each-ref --format="%(refname)" refs/pull | xargs -r -n1 git update-ref -d
cd ..

tar czf $REPO_NAME.tar.gz $REPO_NAME.git

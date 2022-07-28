#!/bin/bash

TAG=1.5-whiner

git tag -d $TAG
git push --delete origin $TAG
git tag $TAG
git push origin $TAG


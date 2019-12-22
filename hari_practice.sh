#! /usr/bin/sh

echo "executing the commands to configure the GIT confirguration..."
pwd

cd Desktop

#This will close the December folder from git server. (Make sure your ssh key is already added to your github)
# to add a ssh key ($ ssh-keygen -t rsa -b 4096 -C "your_email@example.com" > cat ~/.ssh/id_rsa.pub > copy/paste the key to your Github)
git clone git@github.com:ExtracIT/December.git

cd December

#Configuring user info for GIT push
git config --global user.name hellohari
git config --global user.email gtm.harry83@gmail.com

# If the existing GIT fork configuration needs to remove to add new
git remote rm origin
git remote rm upstream


#Adding Fork (This will take place after clone the 
git remote add upstream git@github.com:ExtracIT/December.git
git remote add origin git@github.com:hellohari/December.git
git remote -v


#just to check the origin repo
git origin

echo "GIT confirguration done!"

echo "bye!"



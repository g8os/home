import re
import os
import requests
import subprocess
import tempfile

"""

Docifier
--------

  - Documentation analyer
  - Check for self-reference with absolute path
  - Check for rawgit.com reference
  - Able to download full organizations code
  - Only depends on 'requests'
  - Check the __main__ part to see how it works

  - Organizations are a list of github organizations
  - Rootdir is the directory where all the repos will
    be cloned

  - Note: repositories are cloned using ssh, please make
          sur your ssh keys are well available

"""

class Docifier():
    def __init__(self, organizations, rootdir):
        self.organizations = organizations
        self.rootdir = rootdir
        self._notice = {}

        if not os.path.isdir(self.rootdir):
            os.mkdir(self.rootdir)

    # load list of all repositories found on all organizations
    def repositories(self):
        repos = []

        for organisation in self.organizations:
            items = requests.get("https://api.github.com/users/%s/repos" % organisation)
            for item in items.json():
                repos.append(item['full_name'])

        return repos

    # clone a repository to the current path
    def clone(self, repository):
        try:
            proc = subprocess.Popen(["git", "clone", "--depth=1", "git@github.com:%s" % repository], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            for input in proc.stdout:
                # print(input.decode('utf-8'))
                pass

        except subprocess.CalledProcessError as e:
            for input in proc.stderr:
                print(input.decode('utf-8'))

            os.exit(1)

    def notice(self, filename, line, issue):
        if filename not in self._notice:
            print("[-]   %s" % filename)
            self._notice[filename] = 0

        # new issue found on this file
        self._notice[filename] += 1

        print("[-]     line %d: %s" % (line, issue))

        return self._notice[filename]

    # process a markdown file for consistency
    # this function returns True if the file is consistant
    #               returns False if modifications are made
    def process(self, filename, repository):
        with open(filename, "r") as f:
            contents = f.read().split("\n")

        issues = 0
        current = 1

        for line in contents:
            if "https://github.com/%s" % repository in line:
                if "git clone https://" in line or "git+https" in line:
                    issues = self.notice(filename, current, "absolute self-reference (possible fake-positive)")
                else:
                    issues = self.notice(filename, current, "absolute self-reference")

            if "rawgit.com/" in line:
                issues = self.notice(filename, current, "rawgit.com reference")

            current += 1

        return issues

    # analyze a repository to find markdown file to fix
    def analyze(self, repository, root):
        path = os.path.join(root, repository)
        edited = False

        for root, dirs, files in os.walk(path):
            for filename in files:
                # skipping not Markdown file
                if not filename.endswith('.md'):
                    continue

                # processing this file
                fullpath = os.path.join(root, filename)
                issues = self.process(fullpath, repository)

                if issues > 0:
                    print("[-]   == %d issues found" % issues)

    # run the whole check on all repositories found
    # on all organizations set
    def check(self):
        # loading repositories list
        repos = self.repositories()

        print("[+] analyzing %d repositories" % len(repos))
        print("[+] working directory: %s" % self.rootdir)

        # saving current working directory
        cwdbefore = os.getcwd()

        # cloning each repository to a unique destination
        for repo in repos:
            dirname = os.path.dirname(repo)
            reporoot = os.path.join(self.rootdir, dirname)

            # ensure organisation name directory exists
            if not os.path.isdir(reporoot):
                os.mkdir(reporoot)

            print("[+] cloning: %s" % repo)
            os.chdir(reporoot)
            self.clone(repo)

        # restoring current directory
        os.chdir(cwdbefore)

        for repo in repos:
            print("[+] analyzing: %s" % repo)
            self.analyze(repo, self.rootdir)

if __name__ == '__main__':
    doc = Docifier(["zero-os"], "/tmp/gitfix")
    doc.check()

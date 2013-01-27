#-*- coding: utf-8 -*-
from contextlib import nested

from fabric.api import *
from fabric.contrib.console import confirm
from fabric.utils import abort

env.user = 'thoredan'
env.hosts = ['danielsen.net']

env.root = '/home/' + env.user + '/src'
env.repo = env.root + '/frodes_blog'
env.branch = 'master'

def deploy(branch=None):
    """Lanser gitt branch eller master som standard."""
    to_deploy = env.branch if branch is None else branch
    if not confirm("Er du sikker på at du vil lansere branch '%s' til '%s'?" %
            (to_deploy, env.host), default=False):
        abort("Lansering kansellert.")
    pull(to_deploy)

def pull(branch):
    """Henter HEAD fra git repo."""
    with nested(cd(env.repo), show('stdout')):
        run("git pull")
        # TODO: Upgrade Git on server for the -B flag to work
        # run("git checkout -B %s origin/%s" % (branch, branch))
        run("git submodule init")
        run("git submodule update")

import unittest
import time
import timeout_decorator
from relation import *
from functional_dependency import *
from bcnf import ImplementMe

def main():
    relations = RelationSet({Relation({'a','b','c'})})
    fds = FDSet({FunctionalDependency({'a'}, {'b','c'})})
    ImplementMe.DecompositionSteps(relations, fds)


main()
from .linked_list import LinkedList
import pytest

def test_linked_list_class():
    assert LinkedList

def test_linked_list_instance():
    assert LinkedList('foo')

def test_linked_list_add_one():
    ll = LinkedList()
    ll.add('apples')
    assert ll.head.value == 'apples'

def test_linked_list_add_two():
    ll = LinkedList()
    ll.add('apples')
    ll.add('bananas')
    assert ll.head.value == 'apples'
    assert ll.head.nxt.value == 'bananas'


def test_linked_list_iteration():
    ll = LinkedList()
    ll.add('apples')
    ll.add('bananas')

    items = []
    for item in ll:
        items.append(item)

    assert items == ['apples','bananas']

def test_linked_list_conversion ():
    ll = LinkedList()
    ll.add('apples')
    ll.add('bananas')

    items = list(ll)

    assert items == ['apples','bananas']

def test_linked_list_expressesion():
    ll = LinkedList()
    ll.add('apples')
    ll.add('bananas')

    cap_fruits = [f.upper() for f in ll]

    assert cap_fruits == ['APPLES','BANANAS']

def test_linked_list_filter():
    letters = LinkedList()
    letters.add('a')
    letters.add('b')
    letters.add('c')
    letters.add('d')
    letters.add('e')
    letters.add('f')
    letters.add('g')

    vowels = 'aeiou'
    
    consonants = [char for char in letters if char not in vowels]

    assert consonants == ['b','c','d','f','g']

    

def test_add_operator():
    animals = LinkedList()

    animals += 'giraffe'

    assert list(animals) == ['giraffe']

def test_concat():
    montagues = LinkedList(['Romeo','Benvolio'])

    capulets = LinkedList(['Juliet','Tybalt'])

    tutti = montagues + capulets

    assert len(list(tutti)) == 4

    assert len(list(montagues)) == 2

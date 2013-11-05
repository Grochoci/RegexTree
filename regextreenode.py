"""
# Copyright 2013 Nick Cheng, Brian Harrington, Danny Heap, 2013
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""


class RegexTreeNode:
    """A Regex Tree node"""
    def __init__(self: 'RegexTreeNode', symbol: str,
                 children: list) -> None:
        """A new RegexTreeNode with regex symbol and subtrees children.
        REQ: symbol must be one of "0", "1", "e", "|", ".", "*"

        >>> print(RegexTreeNode("0", []))
        RegexTreeNode('0', [])
        >>> print(RegexTreeNode("1", []))
        RegexTreeNode('1', [])
        """
        self.symbol = symbol
        self.children = children[:]

    def __repr__(self: 'RegexTreeNode') -> str:
        """Return a string representing the regextree node.
        """
        return ('RegexTreeNode(' + repr(self.symbol) + ', ' +
                repr(self.children) + ')')


class UnaryNode(RegexTreeNode):
    """RegexTreeNode with a single child, for now used only for star nodes."""
    def __init__(self: 'RegexTreeNode', symbol: str,
                 child: 'RegexTreeNode') -> None:
        """A new UnaryNode with regex symbol and (only) child"""
        RegexTreeNode.__init__(self, symbol, [child])

    def __repr__(self: 'UnaryNode') -> str:
        """Return representation of this UnaryNode"""
        return ('UnaryNode(' + repr(self.symbol) +
                ', ' + repr(self.children[0]) + ')')


class BinaryNode(RegexTreeNode):
    """RegexTreeNode with two children.  For now, it's only used for bar
    and dot nodes.
    """
    def __init__(self: 'BinaryNode', symbol: str,
                 left: 'RegexTreeNode', right: 'RegexTreeNode') -> None:
        """A new BinaryNode with regex symbol and left and right children.
        """
        RegexTreeNode.__init__(self, symbol, [left, right])

    def __repr__(self: 'BinaryNode') -> str:
        """Return a representation of this BinaryNode"""
        return ('BinaryNode(' + repr(self.symbol) + ', ' +
                repr(self.children[0]) + ', ' +
                repr(self.children[1]) + ')')


class StarNode(UnaryNode):
    """A UnaryNode for a star ("*")

    >>> rtn0 = RegexTreeNode("0", [])
    >>> rtn1 = RegexTreeNode("1", [])
    >>> rtdot = DotNode(rtn1, rtn1)
    >>> rtbar = BarNode(rtn0, rtdot)
    >>> print(StarNode(rtbar))
    StarNode(BarNode(RegexTreeNode('0', []), DotNode(RegexTreeNode('1', []), \
    RegexTreeNode('1', []))))
"""
    def __init__(self: 'UnaryNode', child: 'RegexTreeNode') -> None:
        """New StarNode with (only) child"""
        UnaryNode.__init__(self, '*', child)

    def __repr__(self: 'StarNode') -> str:
        """Return a string representation of this StarNode"""
        return 'StarNode(' + repr(self.children[0]) + ')'


class BarNode(BinaryNode):
    """Binary node for a bar ('|')"""
    def __init__(self: 'BinaryNode', left: 'RegexTreeNode',
                 right: 'RegexTreeNode') -> None:
        BinaryNode.__init__(self, "|", left, right)

    def __repr__(self: 'BarNode') -> str:
        """Return string representation of this Node"""
        return ('BarNode(' + repr(self.children[0]) + ', ' +
                repr(self.children[1]) + ')')


class DotNode(BinaryNode):
    """BinaryNode for a dot ('.')

    >>> rtn0 = RegexTreeNode("0", [])
    >>> rtn1 = RegexTreeNode("1", [])
    >>> rtdot = DotNode(rtn1, rtn1)
    >>> print(BarNode(rtn0, rtdot))
    BarNode(RegexTreeNode('0', []), DotNode(RegexTreeNode('1', []), \
    RegexTreeNode('1', [])))
    """
    def __init__(self: 'DotNode', left: 'RegexTreeNode',
                 right: 'RegexTreeNode') -> None:
        """New DotNode with left and right children

        >>> rtn0 = RegexTreeNode("0", [])
        >>> rtn1 = RegexTreeNode("1", [])
        >>> print(DotNode(rtn1, rtn1))
        DotNode(RegexTreeNode('1', []), RegexTreeNode('1', []))
        """
        BinaryNode.__init__(self, ".", left, right)

    def __repr__(self: 'DotNode') -> str:
        """String represenation of this DotNode"""
        return ('DotNode(' + repr(self.children[0]) +
                ', ' + repr(self.children[1]) + ')')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
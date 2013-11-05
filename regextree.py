"""
# Copyright 2013 Nick Cheng, Brian Harrington, Danny Heap, Paul 
# Grochocinski 2013
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


from regextreenode import RegexTreeNode, UnaryNode, \
    BinaryNode, DotNode, BarNode, StarNode


class Stack:
    
    def __init__(self):
        self._data = []
    
    def pop(self):
        if self.is_empty():
            return Exception
        else:
            return self._data.pop()
    
    def is_empty(self):
        return self._data == []
    
    def push(self, item):
        self._data.append(item) 
        
        
class RegexTree:
    """A Regex Tree"""
    def __init__(self: 'RegexTree', regex: str) -> None:
        """Req: regex must be valid regular expression."""
        # this is where parsing of regex into tree happens
        stack = Stack()
        for char in regex:
            if (char == "0") or (char == "1") or (char == "e"):
                cur_char = RegexTreeNode(char, [])
            elif char == ")":
                exp3 = stack.pop()
                exp2 = stack.pop()
                exp1 = stack.pop()
                stack.pop()
                if exp2 == "|":
                    cur_char = BarNode(exp1, exp3)
                elif exp2 == ".":
                    cur_char = DotNode(exp1, exp3)
            elif char == "*":
                exp = stack.pop()
                cur_char = StarNode(exp)
            else:
                cur_char = char
            stack.push(cur_char) 
        self.root = stack.pop()
        
        
def regex_match(r: 'RegexTree', s: str):
    """ Returns True iff s matches Regex Tree r."""
    
    try:
        r.root
    except AttributeError:
        pass
    else:
        r = r.root
        
    if r.symbol in ("0", "1", "e"):
        if r.symbol == "e":
            if s == "":
                return True
        elif r.symbol == s:
            return True
    elif r.symbol == "|":
        r1 = r.children[0]
        r2 = r.children[1]
        
        if regex_match(r1, s) or regex_match(r2, s):
            return True
    elif r.symbol == ".":
        r1 = r.children[0]
        r2 = r.children[1]

        for idx in range(len(s) + 1):
            s1 = s[:idx]
            s2 = s[idx:]
            
            if regex_match(r1, s1) and regex_match(r2, s2):
                return True
    elif r.symbol == "*":
        if s == "":
            return True     
        
        for idx in range(len(s) + 1):
            s1 = s[:idx]
            s2 = s[idx:]
            
            if regex_match(r.children[0], s1) and regex_match(r, s2):
                return True

    return False